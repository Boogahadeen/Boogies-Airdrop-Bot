import discord
from discord.ext import commands

# --- Discord ---
DISCORD_TOKEN=your_discord_bot_token_here
CHANNEL_ID=1420087598382321677

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# --- Airdrop definitions ---
airdrops = [
    {
        "name": "Prison Island",
        "embed": {
            "content": "",
            "tts": False,
            "embeds": [
                {
                    "description": "<@&1252738767182102590>\n🚨**AIRDROP INBOUND NEXT RESET**🚨\n\n"
                                   "*A CDF MI8 Helicopter has crashed at Prison Island*\n"
                                   "**LOCATION: 2608.36 / 1295.48**\n\n"
                                   "**‼️High-Tier Loot‼️**\n"
                                   "**⚠️PvP is expected – proceed with caution⚠️**\n\n"
                                   "*Survivors, gear up and move fast – the wreck won’t stay for long.*",
                    "image": {"url": "https://cdn.discordapp.com/attachments/1252738767660257347/1405688550921605260/DayZ_Screenshot_2025.08.14_-_18.47.41.16.png"},
                    "thumbnail": {"url": "https://cdn.discordapp.com/attachments/1252738767660257347/1405688001140494386/BoogieNightsPVP_ICON.png"},
                    "fields": []
                }
            ]
        }
    },
    {
        "name": "VMC",
        "embed": {
            "content": "",
            "tts": False,
            "embeds": [
                {
                    "description": "<@&1252738767182102590>\n🚨**AIRDROP INBOUND NEXT RESET**🚨\n\n"
                                   "*A CDF cargo plane has crashed at **Veresnik Military Base*** \n"
                                   "**Coordinates: 4557.24 / 8354.58**\n\n"
                                   "**‼️High-Tier Loot‼️**\n"
                                   "**⚠️PvP is expected – proceed with caution⚠️**\n\n"
                                   "*Survivors, gear up and move fast – the wreck won’t stay for long.*",
                    "image": {"url": "https://cdn.discordapp.com/attachments/1252738767660257347/1405687646893903882/DayZ_Screenshot_2025.08.14_-_18.49.04.84.png"},
                    "thumbnail": {"url": "https://cdn.discordapp.com/attachments/1252738767660257347/1405688001140494386/BoogieNightsPVP_ICON.png"},
                    "fields": []
                }
            ]
        }
    },
    {
        "name": "NEAF",
        "embed": {
            "content": "",
            "tts": False,
            "embeds": [
                {
                    "description": "<@&1252738767182102590>\n🚨**AIRDROP INBOUND NEXT RESET**🚨\n\n"
                                   "*A CDF cargo plane has crashed near North East Airfield!*\n"
                                   "**Coordinates: 12313.63 / 12461.35**\n\n"
                                   "‼️High-Tier Loot ‼️\n⚠️PvP is expected – proceed with caution⚠️\n\n"
                                   "Survivors, gear up and move fast – the wreck won’t stay for long.",
                    "image": {"url": "https://message.style/cdn/images/84a53470971f6d8241a15dcf5196d80570857355f9c594a8ac48605d563cd29a.png"},
                    "thumbnail": {"url": "https://media.discordapp.net/attachments/1086103333527355462/1241843987325780039/IMG_6362.png"},
                    "fields": []
                }
            ]
        }
    },
    {
        "name": "NWAF",
        "embed": {
            "content": "",
            "tts": False,
            "embeds": [
                {
                    "description": "<@&1252738767182102590>\n🚨**AIRDROP INBOUND NEXT RESET**🚨\n\n"
                                   "*A CDF cargo plane has crashed near North West Airfield!*\n"
                                   "**Coordinates: 4323.12 / 10671.90**\n\n"
                                   "**‼️High-Tier Loot‼️**\n"
                                   "**⚠️PvP is expected – proceed with caution⚠️**\n\n"
                                   "*Survivors, gear up and move fast – the wreck won’t stay for long.*",
                    "image": {"url": "https://message.style/cdn/images/84a53470971f6d8241a15dcf5196d80570857355f9c594a8ac48605d563cd29a.png"},
                    "thumbnail": {"url": "https://media.discordapp.net/attachments/1086103333527355462/1241843987325780039/IMG_6362.png"},
                    "fields": []
                }
            ]
        }
    }
]

# --- Bot events ---
@bot.event
async def on_ready():
    print(f"✅ {bot.user} is online!")

# --- Helper to trigger airdrop ---
async def trigger_airdrop(ctx, number):
    # delete the command message
    try:
        await ctx.message.delete()
    except Exception as e:
        print(f"Could not delete command message: {e}")

    ad = airdrops[number - 1]
    inject_airdrop(ad.get("spawner_entry"))

    try:
        channel = await bot.fetch_channel(CHANNEL_ID)

        embeds_to_send = []
        for e in ad["embed"]["embeds"]:
            embed = discord.Embed(description=e.get("description", ""))
            if "image" in e:
                embed.set_image(url=e["image"]["url"])
            if "thumbnail" in e:
                embed.set_thumbnail(url=e["thumbnail"]["url"])
            if "fields" in e:
                for f in e["fields"]:
                    embed.add_field(
                        name=f.get("name", "\u200b"),
                        value=f.get("value", "\u200b"),
                        inline=f.get("inline", True)
                    )
            embeds_to_send.append(embed)

        # just send the embed, no extra "activated" message
        await channel.send(
            content=ad["embed"]["content"],
            embeds=embeds_to_send,
            tts=ad["embed"]["tts"]
        )

    except Exception:
        pass  # Completely silent on failure

# --- Individual commands ---
@bot.command()
async def airdrop1(ctx): await trigger_airdrop(ctx, 1)

@bot.command()
async def airdrop2(ctx): await trigger_airdrop(ctx, 2)

@bot.command()
async def airdrop3(ctx): await trigger_airdrop(ctx, 3)

@bot.command()
async def airdrop4(ctx): await trigger_airdrop(ctx, 4)

# --- Run bot ---
bot.run(TOKEN)
