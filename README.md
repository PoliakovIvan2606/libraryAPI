ДОБРО ПОЖАЛОВАТЬ НА МОЙ РЕПОЗИТОРИЙ ПОД НАЗВАНИЕМ libraryAPI!!!

ЗАПУСК ПРОЕКТА:
1) У вас должен быть установлен docker. Затем скопируйте проект с репозитория.
2) Зайдите в папку libraryAPI
3) Соберите docker-compose, команадой "docker-compose build"
4) И запустите проект командой "docker-compose up"

ИНСТРУКЦИЯ ПО ИСПОЛЬЗОВАНИЮ API:
1) post запрос на url book/api/v1/users/ авторизирует пользователя.
Запрос:
{
    "email": "poliakov1256iv@mail.ru",
    "username": "PoliakovIvan",
    "passwowrd": "BdFy1324."
}
2) post запрос на url book/api/v1/token/login/ аунтетификацирует пользователя
Запрос:
{
    "username": "PoliakovIvan",
    "password": "BdFy13324."
}
В результате прийдёт токен, который надо будет вставлять в Headers с ключём Authorization
Пример:
"Authorization": "Token ec455be6c8ce482a4ddc4dcad8c751dfb5b37ae1"
3) post запрос на url book/api/v1/logout/ с зоголовком Authorization делает выход пользователя с сайта
4) get запрос на url book/api/v1/list/ с заголовком Authorization выводит весь список книг
5) get запрос на url book/api/v1/<int:pk> с заголовком Authorization получает книгу
6) post запрос на url book/api/v1/create/ с заголовком Authorization создаёт книгу
Запрос:
{
    "name": "oleg",
    "author": "ponarin",
    "year": 2014,
    "ISBN": "978-5-44-610923-4"
}
7) PUT запрос на url book/api/v1/<int:pk> с заголовком Authorization изменяет книгу
pk - id книги в которой лежит книга
Запрос:
{
    "name": "ivan",
    "author": "poliakov",
    "year": 2014,
    "ISBN": "978-5-44-610923-4"
}
8) delete запрос на url book/api/v1/<int:pk> с заголовком Authorization удаляет книгу