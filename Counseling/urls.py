"""
URL configuration for Counseling project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CounsellingApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index),
    path("commonpage",views.commonpage),
    path("login",views.Login),
    path("Registration",views.Registration),
    path("CounsilorRegistration",views.CounsilorRegistration),
     path("Userhome",views.Userhome),
       path("Reques",views.Reques),
         path("userprofile",views.userprofile),
    path("CounsilerHome",views.CounsilerHome),
       path("Counsilerprofile",views.Counsilerprofile),
         path("preparequestion",views.preparequestion),
          path("Chatuser",views.Chatuser),
          path("SearchCounsiler",views.SearchCounsiler),
           path("moreaboutcounsiler",views.moreaboutcounsiler),
           path("Questionaries",views.Questionaries),
            path("BookCounsiler",views.BookCounsiler),
               path("Chatcounsiler",views.Chatcounsiler),
                path("viewbooking",views.viewbooking),
                  path("AdminviewCounsiler",views.AdminviewCounsiler),
                path("adminmoreaboutcounsiler",views.adminmoreaboutcounsiler),
                  path("AdminHome",views.AdminHome),
 path("AdminviewUser",views.AdminviewUser),
  path("AutorityMessage",views.AutorityMessage),
 path("viewAutorityMessage",views.viewAutorityMessage),
 path("takeaction",views.takeaction),
 path("viewhistory",views.viewhistory),
 path("paymentForm",views.paymentForm), 
  path("ApproveCounsiler",views.ApproveCounsiler), 
  path("Aboutus",views.Aboutus), 
  path("Contactus",views.Contactus), 
  path("AdHome",views.AdHome), 
  path("CHome",views.CHome), 
   path("AdminviewnonupprovedCounsiler",views.AdminviewnonupprovedCounsiler),
   path("viewpaymentForm",views.viewpaymentForm), 
  path("feedback",views.feedbacks), 
  path("viewfeedback",views.viewfeedback), 
]
