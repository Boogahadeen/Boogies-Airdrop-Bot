<img width="1536" height="512" alt="a1f2b331-55ed-4ad2-adf3-7fbb2c02acd5" src="https://github.com/user-attachments/assets/5f743688-b659-4859-993f-e180f9d49977" />


A Discord bot that posts scheduled / manual DayZ airdrop announcement embeds.  

## Features
- Eight preconfigured airdrop embeds you can change the names to whatever you want(Prison Island, VMC, NEAF, NWAF, etc).
- Commands: `!airdrop1`, `!airdrop2`, `!airdrop3`, `!airdrop4`, `!airdrop5`, `!airdrop6`, `!airdrop7`, `!airdrop8` deletes the invoking command message and posts the embed to a designated channel.
- Silent operation (no confirmation messages) for clean chat.
- Modular embed definitions so you can add more events easily.

## Demo
(Insert a short GIF or screenshot of the bot posting an embed)

## Files
- `bot.py` — main bot code (Discord commands + embed definitions)
- `README.md` — this file
- `.gitignore` — recommended git ignore
- `docs/` — (optional) screenshots, demo video, config examples

## Getting started

### Requirements
- Python 3.10+ (tested on 3.11/3.13)
- `discord.py` library

### Install
```bash
py -m pip install -U discord.py
