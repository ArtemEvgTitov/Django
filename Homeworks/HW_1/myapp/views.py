import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Visit Index page')
    html = """
        <h1>Добро пожаловать на мой сайт!</h1>
        <p>Это главная страница.</p>
        """
    return HttpResponse(html)


def about(request):
    logger.info('Visit About page')
    html = """
        <h1>Обо мне</h1>
        <p>Привет, меня зовут Артём, и это мой первый Django-сайт!</p>
        """
    return HttpResponse(html)
