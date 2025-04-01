from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# def send_email(subject, to, context, template_name):
#     try:
#         html_message = render_to_string(template_name, context)
#         plain_message = strip_tags(html_message)
#         from_email = settings.EMAIL_HOST_USER


def send_test_email():
    subject = 'تست ارسال ایمیل'
    message = 'این یک ایمیل تستی از جنگو است.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['abdollahi003@gmail.com']  # آدرس ایمیل گیرنده

    send_mail(subject, message, from_email, recipient_list)
    print("ایمیل ارسال شد!")


def send_custom_email(subject, from_email, to, html_page, email_active_code):
    context = {'email_active_code': email_active_code}
    html_content = render_to_string(html_page, context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_email, to)
    email.attach_alternative(html_content, "text/html")
    email.send()

