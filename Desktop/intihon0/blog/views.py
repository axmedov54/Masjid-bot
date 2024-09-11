from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import Post,Contact,Category



def category_post(request, slug):
    object_list = Post.objects.filter(category__slug = slug)
    cat = Category.objects.get(slug=slug)
    page = request.GET.get('page')
  
    return render(request, 'post_list.html', {'posts':object_list,'cat':cat})





def HomePage(request):
    Posts = Post.objects.all()
    return render (request,'index.html',{'posts':Posts})


def contactPage(request):
    contact=Contact()
    if request.method == 'POST':
       contact.username=request.POST.get('name')
       contact.email=request.POST.get('email')
       contact.message=request.POST.get('message')
       contact.save()
       print('Contact Saqlandi')
       return render (request,'contact.html')




def PostDatail(request,id=id):
    Posts = Post.objects.get(id=id)
    return render(request,'post_detail.html',{"post":Posts})



def SignupPage(request):

    if request.method == 'POST':
      username = request.POST.get('YourName')
      useremail = request.POST.get('YourEmail')
      password = request.POST.get('Password')
      password2 = request.POST.get('Password2')
      if password==password2:
          password= request.POST.get('Password')
          user=User.objects.create_user(username=username,email=useremail,password=password)
          login(request, user)
          return redirect('home')     
    return render (request,'singnup.html')

def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('YourName')
        password = request.POST.get('Passwordl')
        user= authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
        return redirect('home')

    return render(request,'login.html')


def LogoutUser(request):
    logout(request)
    return redirect('home')


def AboutPage(requeset):
    return render (requeset,'about.html')



# from django.shortcuts import render
# from django.http import HttpResponse
# import requests

# def send_to_telegram(request):
#     if request.method == "POST":
#         quantity = request.POST.get('quantity')
#         price = request.POST.get('price')
#         product_name = request.POST.get('product_name')

#         # Telegramga yuborish uchun API URL va token
#         # bot_token = 'YOUR_BOT_TOKEN'
#         chat_id = '-4510294630'
#         message = f"Mahsulot: {product_name}\nSoni: {quantity} dona\nNarxi: {price} so'm"

#         # Telegram API orqali yuborish
#         # url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
#         data = {'chat_id': chat_id, 'text': message}

#         response = requests.post(data=data)

#         if response.status_code == 200:
#             return HttpResponse("Xabar yuborildi!")
#         else:
#             return HttpResponse("Xabar yuborishda xatolik yuz berdi.")

#     return HttpResponse("Noto'g'ri so'rov turi.")