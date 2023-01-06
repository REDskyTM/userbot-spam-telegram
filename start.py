from pyrogram import Client, filters
import random
import json

app = Client(
	"my_account",
	api_id = "", #вставьте сюда api_id
	api_hash = "" #сюда api_hash
	)

app.run()
