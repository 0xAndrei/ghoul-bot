import discord
from discord.ext import commands
from datetime import datetime
from discord import Spotify
from datetime import datetime

from discord.ext.commands import has_permissions, MissingPermissions


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ban", aliases=["b"])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, target: discord.Member, *, reason="N/A"):
        if not target:
            embed = discord.Embed(
                title="Error | Ban",
                description="> You forgot to mention someone!",
                color=0x000000
            )
            embed.set_author(name=self.bot.user.name,
                             icon_url=self.bot.user.avatar)
            embed.set_footer(
                text=f"command ran by {ctx.message.author}", icon_url=ctx.message.author.avatar)
            embed.timestamp = datetime.utcnow()

            await ctx.send(embed=embed)

        embed = discord.Embed(
            title=f"Banned {target.name} | Ghoul",
            description=f"\u200b\n> Successfully banned **{target.name}**\n> Banned by **{ctx.message.author.name}**\n> Reason: **{reason}**\n\u200b",
            color=0x000000
        )
        embed.timestamp = datetime.utcnow()
        embed.set_author(name=self.bot.user.name,
                         icon_url=self.bot.user.avatar)
        embed.set_footer(
            text=f"command ran by {ctx.message.author}", icon_url=ctx.message.author.avatar)
        await ctx.send(embed=embed)
        await target.ban(reason=reason)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Error | Ban",
                description="> You cant ban people!",
                color=0x000000
            )
            embed.set_author(name=self.bot.user.name,
                             icon_url=self.bot.user.avatar)
            embed.set_footer(
                text=f"command ran by {ctx.message.author}", icon_url=ctx.message.author.avatar)
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)

    @commands.command(name="kick", aliases=["k"])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, target: discord.Member, *, reason="N/A"):
        if not target:
            embed = discord.Embed(
                title="Error | Kick",
                description="> You forgot to mention someone!",
                color=0x000000
            )
            embed.set_author(name=self.bot.user.name,
                             icon_url=self.bot.user.avatar)
            embed.set_footer(
                text=f"command ran by {ctx.message.author}", icon_url=ctx.message.author.avatar)
            embed.timestamp = datetime.utcnow()

            await ctx.send(embed=embed)

        embed = discord.Embed(
            title=f"Kicked {target.name} | Ghoul",
            description=f"\u200b\n> Successfully kicked **{target.name}**\n> Kicked by **{ctx.message.author.name}**\n> Reason: **{reason}**\n\u200b",
            color=0x000000
        )
        embed.timestamp = datetime.utcnow()
        embed.set_author(name=self.bot.user.name,
                         icon_url=self.bot.user.avatar)
        embed.set_footer(
            text=f"command ran by {ctx.message.author}", icon_url=ctx.message.author.avatar)
        await ctx.send(embed=embed)
        await target.ban(reason=reason)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Error | Kick",
                description="> You cant kick people!",
                color=0x000000
            )
            embed.set_author(name=self.bot.user.name,
                             icon_url=self.bot.user.avatar)
            embed.set_footer(
                text=f"command ran by {ctx.message.author}", icon_url=ctx.message.author.avatar)
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)

    @commands.command(name="clear", aliases=["c", "purge", "p"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=None):
        if not amount:
            embed = discord.Embed(
                title=f"Success | Clear",
                description=f"> 🧹 cleared 50 messages",
                color=0x000000
            )
            embed.timestamp = datetime.utcnow()
            embed.set_author(name=self.bot.user.name,
                             icon_url=self.bot.user.avatar)
            embed.set_footer(
                text=f"command ran by {ctx.message.author}", icon_url=ctx.message.author.avatar)
            await ctx.channel.purge(limit=50)

            await ctx.send(embed=embed)
        else:
            try:
                int(amount)
            except:
                embed = discord.Embed(
                    title="Error | Clear",
                    description="> Enter a valid number",
                    color=0x000000
                )
                embed.set_author(name=self.bot.user.name,
                                 icon_url=self.bot.user.avatar)
                embed.set_footer(
                    text=f"command ran by {ctx.message.author}", icon_url=ctx.message.author.avatar)
                embed.timestamp = datetime.utcnow()
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title=f"Success | Clear",
                    description=f"> 🧹 cleared {amount} messages",
                    color=0x000000
                )
                embed.timestamp = datetime.utcnow()
                embed.set_author(name=self.bot.user.name,
                                 icon_url=self.bot.user.avatar)
                embed.set_footer(
                    text=f"command ran by {ctx.message.author}", icon_url=ctx.message.author.avatar)
                await ctx.channel.purge(limit=int(amount))

                await ctx.send(embed=embed)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Error | Clear",
                description="> You cant clear messages!",
                color=0x000000
            )
            embed.set_author(name=self.bot.user.name,
                             icon_url=self.bot.user.avatar)
            embed.set_footer(
                text=f"command ran by {ctx.message.author}", icon_url=ctx.message.author.avatar)
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)
            
async def setup(bot):
    await bot.add_cog(Mod(bot))
