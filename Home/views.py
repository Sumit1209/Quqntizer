from django.shortcuts import render,HttpResponse,redirect
from Home.models import Contact,Home1, Product,Product2,Product3
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def home(request):
    abc=Home1.objects.all()
    pro= Product.objects.all()
    forpaginator=Paginator(pro,4)
    pageNumber=request.GET.get('page')
    pro_final=forpaginator.get_page(pageNumber)
    totalPage=pro_final.paginator.num_pages
    
    
    context={
           'def':abc,
           'pros':pro_final,
           'totalPageList':[n+1 for n in range(totalPage)]
    } 
    return render(request,"home.html",context)

def about(request):
        return render(request,"about.html")

def contact(request):
        if request.method =="POST":
               name=request.POST['name']
               email=request.POST['email']
               phone=request.POST['phone']
               discription =request.POST['discription']
               if len(name)<1 or len(email) <3 or len(phone) < 4 :
                      messages.error(request,"Oops......plz recheck details")
               else:
                      getDetails= Contact (name=name,email=email,phone=phone,discription=discription,time_taken= datetime.today())
                      messages.success(request,"Thank you for response")
                      getDetails.save()
        
        return render(request,"contact.html")

def services(request):
    
    pro1= Product.objects.all()
    forpaginator1=Paginator(pro1,4)
    pageNumber1=request.GET.get('page')
    pro_final1=forpaginator1.get_page(pageNumber1)
    totalPage1=pro_final1.paginator.num_pages
    
    pro2= Product2.objects.all()
    forpaginator2=Paginator(pro2,4)
    pageNumber2=request.GET.get('page')
    pro_final2=forpaginator2.get_page(pageNumber2)
    totalPage2=pro_final2.paginator.num_pages

    pro3= Product3.objects.all()
    forpaginator3=Paginator(pro3,4)
    pageNumber3=request.GET.get('page')
    pro_final3=forpaginator3.get_page(pageNumber3)
    totalPage3=pro_final3.paginator.num_pages
    

    
    context={
           'pros1':pro_final1,
           'totalPageList1':[n+1 for n in range(totalPage1)],
           'pros2':pro_final2,
           'totalPageList2':[n+1 for n in range(totalPage2)],
            'pros3':pro_final3,
           'totalPageList3':[n+1 for n in range(totalPage3)]
    } 
    
    return render(request,"services.html",context)


def feedback(request):
        return render(request,"feedback.html")


def search(request):
        if request.method =='GET':
               nameName=request.GET.get('nameName')
       
      
        stu=Product.objects.all()
        stu2=Product2.objects.all()

        if nameName :
            stu=stu.filter(Q( label__icontains=nameName) | Q(price__icontains=nameName) | Q(Text__icontains=nameName))
        elif nameName :
            stu2=stu2.filter(Q( label__icontains=nameName) | Q(price__icontains=nameName) | Q(Text__icontains=nameName))
        elif nameName :
            stu3=stu3.filter(Q( label__icontains=nameName) | Q(price__icontains=nameName) | Q(Text__icontains=nameName))
        if len(stu)==0 :
            messages.error(request,'Oops......plz search again')
        
        
        
            
        context={
            'stu':stu,
           
            

            'nameName':nameName 
        }
        return render(request,"search.html",context)

def Detailpage(request,ilabel):
        pro1= Product.objects.get(label=ilabel)
      

        con={
            "pro11":pro1  

        }
        
        return render(request,"detail.html",con)
def Detailpage2(request,ilabel):
        
        pro2= Product2.objects.get(label=ilabel)
       

        con={
            
            "pro12":pro2 ,  
            

        }
        
        return render(request,"detail2.html",con)
def Detailpage3(request,ilabel):
       
        pro3= Product3.objects.get(label=ilabel)

        con={
            
            "pro13":pro3  

        }
        
        return render(request,"detail3.html",con)
        

