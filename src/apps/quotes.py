import random

from fastapi import Request
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
router = APIRouter()


quotes = [
    {
        "text": "Что разум человека может постигнуть и во что он может поверить, того он способен достичь",
        "author": "Наполеон Хилл, журналист и писатель",
    },
    {
        "text": "Стремитесь не к успеху, а к ценностям, которые он дает",
        "author": "Альберт Эйнштейн",
    },
    {
        "text": "Своим успехом я обязана тому, что никогда не оправдывалась и не принимала оправданий от других",
        "author": "Флоренс Найтингейл",
    },
    {
        "text": "Сложнее всего начать действовать, все остальное зависит только от упорства",
        "author": "Амелия Эрхарт",
    },
    {
        "text": "Надо любить жизнь больше, чем смысл жизни",
        "author": "Федор Достоевский",
    },
    {
        "text": "Логика может привести Вас от пункта А к пункту Б, а воображение — куда угодно.",
        "author": "Альберт Эйнштейн",
    },
    {
        "text": "Через 20 лет вы будете больше разочарованы теми вещами, которые вы не делали, чем теми, которые вы сделали. Так отчальте от тихой пристани. Почувствуйте попутный ветер в вашем парусе. Двигайтесь вперед, действуйте, открывайте!",
        "author": "Марк Твен",
    },
    {
        "text": "Начинать всегда стоит с того, что сеет сомнения",
        "author": "Борис Стругацкий",
    },
    {
        "text": "Настоящая ответственность бывает только личной",
        "author": "Фазиль Искандер",
    },
    {
        "text": "80% успеха - это появиться в нужном месте в нужное время",
        "author": "Вуди Аллен",
    },
]


def get_random_quote(quotes):
    return random.choice(quotes)


@router.get("/")
def home_quote(request: Request):
    quote = get_random_quote(quotes)

    return templates.TemplateResponse(
        "examples/index.html",
        {
            "request": request,
            "quote": quote,
        },
    )


@router.get("/quote")
def randome_quote(request: Request):
    quote = get_random_quote(quotes)

    return templates.TemplateResponse(
        "examples/quotes/index.html",
        {
            "request": request,
            "quote": quote,
        },
    )
