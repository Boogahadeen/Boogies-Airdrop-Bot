<img width="512" height="512" alt="3339d0db-0ce6-4737-b46a-ea5c90f54bb1" src="https://github.com/user-attachments/assets/3713485d-fb53-4b7b-aa87-b2e6c4c611be" />


A Discord bot that posts scheduled / manual DayZ airdrop announcement embeds.  
Originally built to automate event announcements and (optionally) inject custom spawner entries into a DayZ server's `cfggameplay.json`. This repo contains the Discord-only version (no Nitrado logic) for safe sharing.

## Features
- Four preconfigured airdrop embeds (Prison Island, VMC, NEAF, NWAF).
- Commands: `!airdrop1`, `!airdrop2`, `!airdrop3`, `!airdrop4` — deletes the invoking command message and posts the embed to a designated channel.
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
