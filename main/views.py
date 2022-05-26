from django.shortcuts import render
from .forms import UserInfoForm
from .models import Client
import telebot
from trimmer.settings import BOT_API_KEY

# Create your views here.
bot = telebot.TeleBot(BOT_API_KEY)

def main(request):
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            client = Client.objects.create(name=name, phone_number=phone_number)
            client.save()
            bot.send_message(chat_id=366321052, 
                text=f"Mijoz ismi: {client.name}\nTelefon raqami: {client.phone_number}\nBuyurtma vaqti: {client.request_time}")
            
        else:
            error_message = "Insert correct type of phone number"

    return render(request, "main/index.html", context={"form":UserInfoForm})

# bot.in