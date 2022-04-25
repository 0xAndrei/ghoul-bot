import discord, os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.environ.get("TOKEN")


class Ghoul(commands.Bot):
  def __init__(self):
    intents=discord.Intents.all()
    super().__init__(command_prefix=".", case_insensitive=True, intents=intents)
    super().remove_command("help")
  async def setup_hook(self):
      for file in os.listdir("./cogs"):
        if file.endswith(".py"):
          extension = file[:-3]
          try:
            await self.load_extension(f"cogs.{extension}")
            print(f"[+] {extension}")
          except Exception as e:
            exception = f"{type(e).__name__} > {e}"
            print(f"[-] {extension}\n{exception}")

  async def close(self):
    await super().close()

  async def on_ready(self):
    await super().change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="lonestar"))
    print(f"""            
      _ /     / 
     (//)()(/(  
    _/      

{super().user.name} | {super().user.id}\n\tOnline
    """)



bot = Ghoul()

bot.run(TOKEN)



