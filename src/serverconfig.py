import os
import json
from datetime import date
from discord.ext import commands
from pymongo import MongoClient
from src.utils import get_key_from_json

client = MongoClient(
    f'mongodb+srv://{get_key_from_json("db_username")}:{get_key_from_json("db_password")}@root.zfrgv.gcp.mongodb.net/{get_key_from_json("db_name")}?retryWrites=true&w=majority')
database = client["database_root"]
server_col = database["collection_root"]


def is_guild_registered(guild_id) -> bool:
    return server_col.find({"guild_id": guild_id}).count() > 0


# Checking if the server has it's json file
def check_server_json(bot_instance: commands.Bot):
    for guild in bot_instance.guilds:
        if not is_guild_registered(guild.id):
            server_col.insert_one({"guild_id":          guild.id,
                                   "guild_prefix":      "%",
                                   "log_channel":       "False",
                                   "role_join":         "False",
                                   "log_channel_id":    "N/A",
                                   "role_join_id":      "N/A",
                                   "music_channel":     "False",
                                   "music_channel_id":  "N/A",
                                   "private_channel":   "False",
                                   "private_channel_id": "N/A",
                                   "xp_system":         "False",
                                   "xp_channel_id":     "N/A",
                                   "lang":              "en"})
            print(f"[os] {guild.id}({guild.name}) config file has been created | {date.today()}")