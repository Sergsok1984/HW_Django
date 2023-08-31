from django.http import HttpResponse
import logging
from functools import wraps

logger = logging.getLogger(__name__)


def get_log(func):
    @wraps(func)
    def wrapper(request):
        res = func(request)
        view_name = func.__name__
        client_ip = get_client_ip(request)
        logger.info(f'Page "{view_name}" from ip = {client_ip}')
        return res

    return wrapper


@get_log
def index(request):
    html_text = "<h1>Главная страница.</h1>" \
                "<h2>Меня зовут Соколов Сергей.</h2>" \
                "<h2>Мне 39 лет.</h2>"
    return HttpResponse(html_text)


@get_log
def about(request):
    html_text = f"<h1>Обо мне.</h1>" \
                f"<h2>Я изучаю язык программирования Python.</h2>" \
                f"<h2>В настоящее время осваиваю Фреймворк Django.</h2>"
    return HttpResponse(html_text)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
