from django.shortcuts import render

from .producer import send_message


# Create your views here.
def message_view(request):

    message = "Hello"
    send_message(message)
    context = {"message": message}
    return render(request, "device/message.html", context=context)
