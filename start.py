from pyrogram import Client, filters
import random
import json
import os

plugins = dict(root="plugins")

app = Client(
	"my_account",
	api_id = "", #вставьте сюда api_id
	api_hash = "" #сюда api_hash
	plugins = plugins
	)

app.run()
