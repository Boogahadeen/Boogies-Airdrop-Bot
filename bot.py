import discord
from discord.ext import commands

# --- Discord ---
TOKEN = "Discord_Token"
CHANNEL_ID = Channel_ID  # Discord channel ID for airdrops

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# --- Airdrop definitions ---
airdrops = [
    {
        "name": "Prison Island",# --- 1 ---
        "embed": {
            "content": "",
            "tts": False,
            "embeds": [
                {
                    "description": "🚨**AIRDROP INBOUND NEXT RESET**🚨\n\n"
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
        "name": "VMC",# --- 2 ---
        "embed": {
            "content": "",
            "tts": False,
            "embeds": [
                {
                    "description": "🚨**AIRDROP INBOUND NEXT RESET**🚨\n\n"
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
        "name": "NEAF",# --- 3 ---
        "embed": {
            "content": "",
            "tts": False,
            "embeds": [
                {
                    "description": "🚨**AIRDROP INBOUND NEXT RESET**🚨\n\n"
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
        "name": "NWAF",# --- 4 ---
        "embed": {
            "content": "",
            "tts": False,
            "embeds": [
                {
                    "description": "🚨**AIRDROP INBOUND NEXT RESET**🚨\n\n"
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
    },
    {
        "name": "Zelengorsk",# --- 5 ---
        "embed": {
            "content": "",
            "tts": False,
            "embeds": [
                {
                    "description": "🚨**AIRDROP INBOUND NEXT RESET**🚨\n\n"
                                   "*A CDF cargo plane has crashed near Zelengorsk!*\n"
                                   "**Coordinates: 2410.65 / 5447.91**\n\n"
                                   "**‼️High-Tier Loot‼️**\n"
                                   "**⚠️PvP is expected – proceed with caution⚠️**\n\n"
                                   "*Survivors, gear up and move fast – the wreck won’t stay for long.*",
                    "image": {"url": "https://message.style/cdn/images/560ce048490486615970d21bc77ec6967431590de3b0e4b0e53b1355b13fa48b.png"},
                    "thumbnail": {"url": "https://media.discordapp.net/attachments/1086103333527355462/1241843987325780039/IMG_6362.png"},
                    "fields": []
                }
            ]
        }
    },
    {
        "name": "Stary Sobor",# --- 6 ---
        "embed": {
            "content": "",
            "tts": False,
            "embeds": [
                {
                    "description": "🚨**AIRDROP INBOUND NEXT RESET**🚨\n\n"
                                   "*A CDF cargo plane has crashed near Stary Sobor!*\n"
                                   "**Coordinates: 6404.86 / 7768.93**\n\n"
                                   "**‼️High-Tier Loot‼️**\n"
                                   "**⚠️PvP is expected – proceed with caution⚠️**\n\n"
                                   "*Survivors, gear up and move fast – the wreck won’t stay for long.*",
                    "image": {"url": "https://message.style/cdn/images/bacbd109fbc751fd559dc432ff2a72fb279e0655c08928378423dda60b4032af.png"},
                    "thumbnail": {"url": "https://media.discordapp.net/attachments/1086103333527355462/1241843987325780039/IMG_6362.png"},
                    "fields": []
                }
            ]
        }
    },
    {
        "name": "Balota",# --- 7 ---
        "embed": {
            "content": "",
            "tts": False,
            "embeds": [
                {
                    "description": "🚨**AIRDROP INBOUND NEXT RESET**🚨\n\n"
                                   "*A CDF cargo plane has crashed near Balota!*\n"
                                   "**Coordinates: 5139.50 / 2327.05**\n\n"
                                   "**‼️High-Tier Loot‼️**\n"
                                   "**⚠️PvP is expected – proceed with caution⚠️**\n\n"
                                   "*Survivors, gear up and move fast – the wreck won’t stay for long.*",
                    "image": {"url": "https://message.style/cdn/images/19ceeb3c9508b5975fca5770fa5dc23410aae64d1cba45506ffe247b0b445f35.png"},
                    "thumbnail": {"url": "https://media.discordapp.net/attachments/1086103333527355462/1241843987325780039/IMG_6362.png"},
                    "fields": []
                }
            ]
        }
    },
    {
        "name": "Krona Castle",# --- 8 ---
        "embed": {
            "content": "",
            "tts": False,
            "embeds": [
                {
                    "description": "🚨**AIRDROP INBOUND NEXT RESET**🚨\n\n"
                                   "*A CDF cargo plane has crashed near Krona!*\n"
                                   "**Coordinates: 1454.84 / 9224.33**\n\n"
                                   "**‼️High-Tier Loot‼️**\n"
                                   "**⚠️PvP is expected – proceed with caution⚠️**\n\n"
                                   "*Survivors, gear up and move fast – the wreck won’t stay for long.*",
                    "image": {"url": "https://message.style/cdn/images/59b7cd4e0bba23d95462f181ab7321f07f2fdddf1f8e1cf9c6997cbfc1f58944.png"},
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
    try:
        await ctx.message.delete()
    except Exception as e:
        print(f"Could not delete command message: {e}")

    ad = airdrops[number - 1]

    # Only call if spawner_entry exists
    spawner_entry = ad.get("spawner_entry")
    if spawner_entry:
        inject_airdrop(spawner_entry)

    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        print("❌ Channel not found!")
        return

    embeds_to_send = []
    for e in ad["embed"]["embeds"]:
        embed = discord.Embed(description=e.get("description", ""))
        if "image" in e:
            embed.set_image(url=e["image"]["url"])
        if "thumbnail" in e:
            embed.set_thumbnail(url=e["thumbnail"]["url"])
        for f in e.get("fields", []):
            embed.add_field(
                name=f.get("name", "\u200b"),
                value=f.get("value", "\u200b"),
                inline=f.get("inline", True)
            )
        embeds_to_send.append(embed)

    try:
        await channel.send(
            content=ad["embed"]["content"],
            embeds=embeds_to_send,
            tts=ad["embed"]["tts"]
        )
    except Exception as e:
        print(f"❌ Failed to send embed: {e}")

# --- Individual commands ---
@bot.command()
async def airdrop1(ctx): await trigger_airdrop(ctx, 1)

@bot.command()
async def airdrop2(ctx): await trigger_airdrop(ctx, 2)

@bot.command()
async def airdrop3(ctx): await trigger_airdrop(ctx, 3)

@bot.command()
async def airdrop4(ctx): await trigger_airdrop(ctx, 4)

@bot.command()
async def airdrop5(ctx): await trigger_airdrop(ctx, 5)

@bot.command()
async def airdrop6(ctx): await trigger_airdrop(ctx, 6)

@bot.command()
async def airdrop7(ctx): await trigger_airdrop(ctx, 7)

@bot.command()
async def airdrop8(ctx): await trigger_airdrop(ctx, 8)

@bot.command()
async def airdrop9(ctx): await trigger_airdrop(ctx, 9)

@bot.command()
async def airdrop10(ctx): await trigger_airdrop(ctx, 10)

# --- Run bot ---
bot.run(TOKEN)
