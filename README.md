# examples-htmx

## Установка

клонировать репозиторий и перейти в каталог:
`git clone git@github.com:YuriyGrinev/example-htmx.git && cd example-htmx`

### Requires

- python3
- [pdm](https://pdm.fming.dev/latest/)

### Запустить проект

Установить через pdm все продакш зависимости:

```sh
pdm install --prod
```

Перейти в каталог src и запустить проект:

```sh
cd src
pdm run uvicorn main:app --reload --host 0.0.0.0
```


## Использование HTMX

### О HTMX

htmx - JS-библиотека, которая позволяет получать доступ к современным функциям браузера, не используя при этом написание функций непосредственно на JavaScript

Для использования HTMX необходимо [скачать](https://unpkg.com/htmx.org/dist/htmx.min.js) подключить библиотеку в основной шаблон:

```html
<script src="/path/to/htmx.min.js"></script>
```

или подключить, используя загрузку через CDN:

```html
<script src="https://unpkg.com/htmx.org@1.9.6" integrity="sha384-FhXw7b6AlE/jyjlZH5iHa/tTe9EpJ1Y55RjcgPbjeWMskSxZt1v9qkxLJWNJaGni" crossorigin="anonymous"></script>
```

### Простой пример

```html
<style>
  #quote.htmx-added {
    opacity: 0;
  }
  #quote {
    opacity: 1;
    transition: opacity 1s ease-out;
  }
</style>
<div
    id="quote"
    hx-get="/quote"
    hx-trigger="click, every 5s"
    hx-swap="outerHTML settle:1s"
    hx-target="#quote">
    {{ quote.text }}
</div>
```

Разберем код, представленный выше. Представим, что нам нужно обновлять какой-то блок контента (например известные цитаты известных людей) на странице автоматически и/или по клику на него мышкой.
`hx-get="/quote"` - позволяет выполнить GET-запрос на указанный URL
`hx-trigger="click, every 5s"` - указывает триггер, на который будет реагировать этот элемент. Здесь реакция на клик мышкой и автоматическая активация каждые 5 секунд
`hx-swap="outerHTML settle:1s"` - описывает стратегию замены. outerHTML заменяет весь целевой элемент возвращенным содержимым. Дополнительно мы можем управлять анимаций замены, описывая дополнительные CSS
`hx-target="#quote"` - указывает на id целевого элемета для замены
