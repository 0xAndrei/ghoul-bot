import discord
from discord.ext import commands
from datetime import datetime
from discord import Spotify



class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='userinfo', aliases=["ui"])
    async def userinfo(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.message.author
        author = ctx.message.author
        created_at = str(user.created_at.timestamp())
        created_at = created_at.split(".")

        joined_at = str(user.joined_at.timestamp())
        joined_at = joined_at.split(".")
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])

        embed = discord.Embed(
            title=f"{user.name} | User Info",
            description=f"Information about {user.name}\n\n> **Name:** {user.name}\n> **Discriminator:** {user.discriminator}\n> **Registered:** <t:{created_at[0]}:R>\n> **Joined:** <t:{joined_at[0]}:R>\n> **Roles [{len(user.roles)-1}]:** {role_string}\n\u200b\n",
            color=0x000000
        )
        embed.set_thumbnail(url=user.avatar)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
        embed.timestamp = datetime.utcnow()
        embed.set_footer(text=f"command ran by {ctx.message.author}", icon_url=author.avatar)

        await ctx.send(embed=embed)

    @commands.command(name="serverinfo", aliases=["si"])
    async def serverinfo(self, ctx):
        guild = ctx.message.guild
        author = ctx.message.author
        created_at = str(guild.created_at.timestamp())
        created_at = created_at.split(".")


        embed = discord.Embed(
            title=f"{guild.name} | Server Info",
            description=f"Information about {guild.name}\n\n **General Information**\n> **Name:** {guild.name}\n> **Owner:** <@{guild.owner.id}>\n> **Created:** <t:{created_at[0]}:R>\n> **Members:** {guild.member_count}\n> **Roles:** {len(guild.roles)}\n\n**Channel Information**\n> **Text Channels:** {len(guild.text_channels)}\n> **Voice Channels:** {len(guild.voice_channels)}\n> **Categories:** {len(guild.categories)}\n\n**Boost Info**\n> **Boost Level:** {guild.premium_tier}\n> **Boosters:** {guild.premium_subscription_count}\n\u200b",
            color=0x000000
        )
        embed.set_thumbnail(url=guild.icon)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
        embed.timestamp = datetime.utcnow()
        embed.set_footer(text=f"command ran by {ctx.message.author}", icon_url=author.avatar)
        embed.set_image(url=guild.banner)
        await ctx.send(embed=embed)


    @commands.command(name="avatar", aliases=["pfp", "av"])
    async def avatar(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.message.author

        embed = discord.Embed(
            title=f"{user.name} | Avatar",
            color=0x000000
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
        embed.timestamp = datetime.utcnow()
        embed.set_image(url=user.avatar)
        embed.set_footer(text=f"command ran by {ctx.message.author}", icon_url=ctx.message.author.avatar)
        await ctx.send(embed=embed)

    @commands.command(name="spotify", aliases=["cs", "currentsong"])
    @commands.guild_only()
    async def spotify(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.message.author
        
        if user.activities:
            for activity in user.activities:
                if isinstance(activity, Spotify):
                    embed = discord.Embed(
                    title = f"{user.name} |  Spotify",
                    description = f"Listening to **{activity.title}**\n\n> **Artist:** {activity.artist}\n> **Title:** {activity.title}\n> **Album:** {activity.album}\n\u200b",
                    color = 0x000000,
                    url=activity.track_url
                    )
                    embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
                    embed.timestamp = datetime.utcnow()
                    embed.set_thumbnail(url=activity.album_cover_url)
                    embed.set_footer(text=f"command ran by {ctx.message.author}", icon_url=ctx.message.author.avatar)
                    await ctx.send(embed=embed)

    @commands.command(name="info")
    async def test(self, ctx):
        embed = discord.Embed(
            title="Info | Ghoul",
            description=f"""```
\t  _ /     / \t
\t (//)()(/(  \t
\t_/          \t ```\n\n> **Developer:** andrei#1337\n> **Language:** Python\n> **Commands:** 5\n> **[Invite](https://ghoul.cx)**\n\u200b""",
            color=0x000000,
            url="https://ghoul.cx"
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
        embed.set_thumbnail(url=self.bot.user.avatar)
        embed.set_footer(text=f"command ran by {ctx.message.author}", icon_url=ctx.message.author.avatar)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Info(bot))