from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import UserInfoForm
from .models import Client
import telebot
from trimmer.settings import BOT_API_KEY
from django.contrib import messages

# Create your views here.
bot = telebot.TeleBot(BOT_API_KEY)

def main(request):
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            client = Client.objects.create(name=name, phone_number=phone_number)
            requested_time = client.request_time.strftime("%m/%d/%Y, %H:%M:%S")
            bot.send_message(chat_id=366321052, 
                text=f"Mijoz ismi: {client.name}\nTelefon raqami: {client.phone_number}\nBuyurtma vaqti: {requested_time}")
            message = 'Buyurtma muvaffaqiyatli bo\'ldi. Tez orada operatorimiz siz bilan bo\'g\'lanadi!'
            
            messages.success(request, 'Buyurtma muvaffaqiyatli bo\'ldi. Tez orada operatorimiz siz bilan bo\'g\'lanadi!')
            return redirect('main')
        else:
            message = "Telefon raqam noto'g'ri kiritilgan. Iltimos, tekshirib qaytadan kiriting!"
            messages.error(request, message)
            return redirect('main')
    return render(request, "main/index.html", context={"form":UserInfoForm()})

