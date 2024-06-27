from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.db.models import Q
from .models import *
# Create your views here.
def index(request):
    return render(request,"CommonHome.html")
def commonpage(request):
    return render(request,"CommonPage.html")
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('t1')
        password = request.POST.get('t2')
        request.session["uname"] =username
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.userType =="user":
                # login(request,user)
                messages.info(request,"Login successfull")
                return redirect('/Userhome')
            if user.userType =="counsiler":
                # login(request,user)
                messages.info(request,"Login successfull")
                return redirect('/CHome')
            if user.userType =="Admin":
                # login(request,user)
                messages.info(request,"Login successfull")
                return redirect('/AdHome')
        else:
            messages.info(request,"invalid username or password")
            messages.error(request,'Invalid Credentials')
    return render(request,"Login.html")
def Registration(request):
    if request.POST:
        name=request.POST["t1"]
        email=request.POST["t2"]
        mobile=request.POST["t3"]
        address=request.POST["t4"]
        dob=request.POST["t5"]
        image=request.FILES["t6"]
        gender=request.POST["t7"]
        password=request.POST["t8"]
        if not CustomUser.objects.filter(username=email).exists():
            login=CustomUser.objects.create_user(username=email,password=password,userType='user',viewpassword=password)
            login.save()
            reg=Userregistration.objects.create(user=login,name=name,email=email,phone=mobile,address=address,dob=dob,img=image)
            reg.save()
            messages.info(request,"user Added successfuly ")
        else:
            messages.info(request,"user already added")
    return render(request,"Registration.html")
def CounsilorRegistration(request):
    if request.POST:
        name=request.POST["t1"]
        email=request.POST["t2"]
        mobile=request.POST["t3"]
        address=request.POST["t4"]
        dob=request.POST["t5"]
        image=request.FILES["t6"]
        gender=request.POST["t7"]
        video=request.FILES["t66"]
        aboutme=request.POST["t67"]
        password=request.POST["t9"]
        desig=request.POST["t8"]
        if not CustomUser.objects.filter(username=email).exists():
            login=CustomUser.objects.create_user(username=email,password=password,userType='counsiler',viewpassword=password,is_active=0)
            login.save()
            reg=Counsilerregistration.objects.create(user=login,name=name,email=email,phone=mobile,address=address,dob=dob,img=image,desig=desig,video=video,aboutme=aboutme)
            reg.save()
            messages.info(request,"Counselor Added successfuly waiting for Admin approval")
        else:
            messages.info(request,"Counselor already added")
    return render(request,"Counsilerregistration.html")
def Userhome(request):
    return render(request,"Userhome.html")
def Reques(request):
    if request.POST:
        uname=request.session["uname"]
        user=CustomUser.objects.get(username=uname)
        requ=request.POST["t1"]
        type=request.POST["t2"]
        gender=request.POST["t3"]

        req=Requestuser.objects.create(user=user,requests=requ,status=type,gender=gender)
        req.save()

    return render(request,"Request.html")
def userprofile(request):
    uname=request.session["uname"]
    data=Userregistration.objects.get(email=uname)
    if request.POST:
        name=request.POST["t1"]
        email=request.POST["t2"]
        mobile=request.POST["t3"]
        address=request.POST["t4"]
        dob=request.POST["t5"]
        data=Userregistration.objects.get(email=uname)
        
        data.name=name
        # data.email=email
        data.phone=mobile
        data.address=address
        data.dob=dob
        data.save()

    return render(request,"userprofile.html",{"data":data})
def CounsilerHome(request):
    uname=request.session["uname"]
    img=Counsilerregistration.objects.get(email=uname)
    return render(request,"CounsilerHome.html",{"uname":uname,"img":img.img})
def Aboutus(request):
    return render(request,"Aboutus.html",)
def Contactus(request):
    return render(request,"Contactus.html",)
def AdminHome(request):
    return render(request,"AdminHome.html",)
def Counsilerprofile(request):
    uname=request.session["uname"]
    img=Counsilerregistration.objects.get(email=uname)
    data=Counsilerregistration.objects.get(email=uname)
    if request.POST:
        name=request.POST["t1"]
        email=request.POST["t2"]
        mobile=request.POST["t3"]
        address=request.POST["t4"]
        dob=request.POST["t5"]
        video=request.FILES["t66"]
        data=Counsilerregistration.objects.get(email=uname)
        
        data.name=name
        # data.email=email
        data.phone=mobile
        data.address=address
        data.dob=dob
        data.video=video
        data.save()
    return render(request,"Counsilerprofile.html",{"data":data,"img":img.img})
def preparequestion(request):
    uname=request.session["uname"]
    img=Counsilerregistration.objects.get(email=uname)
    if request.POST:
        question=request.POST["t1"]
        answer1=request.POST["t2"]
        answer2=request.POST["t3"]
        answer3=request.POST["t4"]
        answer4=request.POST["t5"]
        answer=request.POST["t6"]
        quest=Question.objects.create(question=question,answer1=answer1,answer2=answer2,answer3=answer3,answer4=answer4,answer=answer)
        quest.save()
    return render(request,"question.html",{"img":img.img})
def Chatuser(request):
    to=""
    chat=""
    data=Counsilerregistration.objects.all()
    if request.GET:
        to=request.GET["to"]
    if request.POST:
        to=to
        message=request.POST["t2"]
        file=request.FILES["t3"]
        typ=file.content_type
        uname=request.session["uname"]
        obj=Message.objects.create(frm=uname,to=to,message=message,filetype=typ,file=file)
        obj.save()
        chat=Message.objects.filter(frm=uname)
    return render(request,"Chatuser.html",{"data":data,"to":to,"chat":chat})
def Chatcounsiler(request):
    uname=request.session["uname"]
    img=Counsilerregistration.objects.get(email=uname)
    to=""
    chat=""
    data=Userregistration.objects.all()
    if request.GET:
        to=request.GET["to"]
    if request.POST:
        to=to
        message=request.POST["t2"]
        if request.FILES["t3"]:
            file=request.FILES["t3"]
            typ=file.content_type
        else:
            file=""
            typ=""
        uname=request.session["uname"]
        obj=Message.objects.create(frm=uname,to=to,message=message,filetype=typ,file=file)
        obj.save()
        chat=Message.objects.filter(frm=uname)
    return render(request,"Chatcounsiler.html",{"data":data,"to":to,"chat":chat,"img":img.img})
def SearchCounsiler(request):
    data=Counsilerregistration.objects.all()
    if request.POST:
        name=request.POST["name"]
        data=Counsilerregistration.objects.filter(Q(desig__contains=name))
    return render(request,"SearchCounsiler.html",{"data":data})
def AdHome(request):
   
    cntuser=Userregistration.objects.filter().count()
    countcoun=Counsilerregistration.objects.filter().count()
    
    return render(request,"AdHome.html",{"user":cntuser,"coun":countcoun})
def CHome(request):
    uname=request.session["uname"]
    
    img=Counsilerregistration.objects.get(email=uname)
    cntuser=Message.objects.filter(to=uname).count()
    countcoun=Booking.objects.filter(councelr__email=uname).count()
    return render(request,"CHome.html",{"user":cntuser,"coun":countcoun,"img":img.img})
def AdminviewCounsiler(request):
    data=Counsilerregistration.objects.all()
    return render(request,"AdminviewCounsiler.html",{"data":data})
def AdminviewnonupprovedCounsiler(request):
    data=Counsilerregistration.objects.filter(Q(user__is_active=0))
    return render(request,"AdminviewnonupprovedCounsiler.html",{"data":data})
def AdminviewUser(request):
    data=Userregistration.objects.all()
    return render(request,"AdminviewUser.html",{"data":data})
def adminmoreaboutcounsiler(request):
    id=request.GET["id"]
    data=Counsilerregistration.objects.get(id=id)
    return render(request,"adminmoreaboutcounsiler.html",{"data":data})
def moreaboutcounsiler(request):
    id=request.GET["id"]
    data=Counsilerregistration.objects.get(id=id)
    return render(request,"moreaboutcounsiler.html",{"data":data})
def Questionaries(request):
    # data=""
    # print(request.session["qno"])
    # if  request.session["qno"] :
    #     print("##########################")
    #     request.session["qno"]=1
    #     data=Question.objects.get(id=request.session["qno"])
    #     print(request.session["qno"])
    #     return render(request,"Questionaries.html",{"data":data})
    
    # if request.POST:
    #     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    #     ans=request.POST["answer"]
    #     if(ans==data.answer):
    #         request.session["count"]=int(request.session["count"])+1
    #         request.session["qno"]=int(request.session["qno"])+1
    #         data=Question.objects.get(id=request.session["qno"])
    #         return render(request,"Questionaries.html",{"data":data})
    #     print(request.session["qno"])

    # exam = Question.objects.get(pk=exam_id)
    questions = Question.objects.all()
    uname=request.session["uname"]
    if 'sub' in request.POST:
        usr=CustomUser.objects.get(username=uname)
        score = 0
        for question in questions:
            selected_option = request.POST.get(f'question_{question.pk}')
            print(selected_option)
            # if selected_option == question.answer:
            score += 1
            obj=Answeruser.objects.create(user=usr,question=question.question,answer=question.answer)
            obj.save()
            print(score)
            return redirect("/SearchCounsiler")
    if 'skip' in request.POST:

        return redirect("/SearchCounsiler")
    return render(request,"Questionaries.html",{"questions":questions})
def BookCounsiler(request):
    import datetime

    x = str(datetime.datetime.now())
    x=x[0:10]
    print(x)
    if request.POST:
        uname=request.session["uname"]
        counsilerid=request.GET["id"]
        req=request.POST["t1"]
        typ=request.POST["t2"]
        date=request.POST["t3"]
        
        usr=Userregistration.objects.get(email=uname)
        con=Counsilerregistration.objects.get(id=counsilerid)
        obj=Booking.objects.create(councelr=con,usr=usr,request=req,typ=typ,bookingdate=date,status='booked')
        obj.save()
        request.session["amt"]=500
        print(counsilerid)
        return redirect('/paymentForm?id='+counsilerid)
    return render(request,"BookCounsiler.html",{"x":str(x)})
def viewbooking(request):
    uname=request.session["uname"]
    img=Counsilerregistration.objects.get(email=uname)
    data=Booking.objects.filter(Q(councelr__email=uname))
    return render(request,"ViewBooking.html",{"data":data,"img":img.img})
def ApproveCounsiler(request):
    try:
        uname=request.GET["id"]
        uid=Counsilerregistration.objects.get(id=uname)
        data=CustomUser.objects.get(id=uid.user_id)
        data.is_active=1
        data.save()
    except:
        msg=""
    return redirect('/AdminviewCounsiler')
def viewhistory(request):
    id=request.GET["id"]
    print(id)
    # email=Userregistration.objects.get(id=id)
    data=Answeruser.objects.filter(Q(user__username=id))
    return render(request,"viewhistory.html",{"data":data})
def AutorityMessage(request):
    data=Authmessage.objects.filter(Q(usr__email=request.session["uname"]))
    if request.POST:
        uname=request.session["uname"]
        usr=Userregistration.objects.get(email=uname)
        message=request.POST.get("t1")
        fil=request.FILES["t2"]
        obj=Authmessage.objects.create(usr=usr,messages=message,video=fil,status='request')
        obj.save()
    return render(request,"AutorityMessage.html",{"data":data})
def viewAutorityMessage(request):
    data=Authmessage.objects.all()
    
    return render(request,"ViewCriticalmessage.html",{"data":data})
def takeaction(request):
    id=request.GET["id"]
    Authmessage.objects.filter(id=id).update(status='Take Action')
    return redirect('/viewAutorityMessage')
def paymentForm(request):
    amt=request.session["amt"]
    if request.POST:
        uname=request.session["uname"]
        con=request.GET["id"]
        usr=Userregistration.objects.get(email=uname)
        cons=Counsilerregistration.objects.get(id=con)
        obj=payment.objects.create(usr=usr,con=cons,amount=amt)
        obj.save()
        messages.info(request,"Payment successfully")
    return render(request,"paymentForm.html",{"amt":amt})

def viewpaymentForm(request):
    data=payment.objects.all()
    
    return render(request,"viewpaymentForm.html",{"data":data})
def feedbacks(request):
    if request.POST:
        uname=request.session["uname"]
        feed=request.POST["t1"]
        usr=Userregistration.objects.get(email=uname)
        obj=feedback.objects.create(usr=usr,feedbackss=feed)
        obj.save()
    
    return render(request,"feedback.html")
def viewfeedback(request):
    data=feedback.objects.all()
    
    return render(request,"viewfeedback.html",{"data":data})