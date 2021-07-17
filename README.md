# py-runner_questionnaire

Интерпретатор анкет который использует json-подобный синтаксис для набора вопросов и возможных ответов.

## Структура json файла беседы

Структура вопроса:

```json
{
  'var': "имя_переменной",
  'question': "текст вопроса",
  'answer': {
    'type': тип_ответа,
    'list_answer': список_возможных_ответов
  }
}

```

где

* **тип_ответа** — обязательный параметр, тип ответа для проверки при вводе, может быть один из следующих:
    * int - целое число
    * float - число с плавающей точкой
    * string - строка
    * list - список возможных ответов

* **список_возможных_ответов** — необязательный параметр, список возможных ответов в виде списка и который выводится для
  того чтобы пользователю сообщить что есть для ответа только этот
