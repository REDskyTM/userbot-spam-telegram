# userbot-spam-telegram

## 1. Получение api_id и api_hash
###### Переходим на сайт https://my.telegram.org/apps далее авторизируемся при помощи номера и вводим код подтверждения,
###### пишем App title, Shorname
###### Пример: App Title - Lucky, Shortname - Lucky4ka
###### Выше вы увидите api_id и api_hash именно он нам и нужен.

## 3. Что делать с api_id и api_hash?
###### Откройте start.py и найдите
```py
app = Client(
	"my_account",
	api_id = "", #Сюда добавьте ваш api_id должно быть так api_id = "ваш айди", с хешем так же
	api_hash = ""
	)
```

## 3. Запуск кода и дальнейшие действия
###### При первом запуске код потребует ваш номер телефона
```
Welcome to Pyrogram (version 1.3.0)
Pyrogram is free software and comes with ABSOLUTELY NO WARRANTY. Licensed
under the terms of the GNU Lesser General Public License v3 or later (LGPLv3+).

Enter phone number or bot token: +78005553535
```
###### После ввода номера код спросит верны ли данные? Напишите Y и нажмите клавишу ввод, enter
###### Далее вам придёт код подтверждения от Telegram который вы вводите в код и всё получаете рабочего бота на вашем аккауте

## Проверить бота на спам легко, введите команду ```.spam ИВАШЕСООБЩЕНИЕ```
