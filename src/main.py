from discord.ext import commands
from src.utils import get_key_from_json, load_cogs
import src.serverconfig


class Chan(commands.Bot):

    def __init__(self, prefix):
        super().__init__(command_prefix=prefix)

    async def on_ready(self):
        src.serverconfig.check_server_json(self)  # Check if each servers where the bot is, have a json config file
        load_cogs(self, subdir='commands')  # Loading all commands
        load_cogs(self, subdir='commands/social')  # Loading all social commands
        load_cogs(self, subdir='commands/mod')  # Loading all moderation commands
        print(f"Logged as {self.user}, active in {len(self.guilds)} server(s) with a total amount of {len([user for user in self.users if not user.bot])} user(s).")


if __name__ == '__main__':
    client = Chan(prefix='%')
    # Middleware
    client.remove_command('help')
    client.run(get_key_from_json("TOKEN"))
