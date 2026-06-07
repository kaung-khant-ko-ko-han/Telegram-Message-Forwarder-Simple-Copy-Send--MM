import asyncio
from telethon import TelegramClient, events

# ---------- CONFIGURATION ----------
API_ID = 1234567          # Your API ID
API_HASH = 'your_api_hash_here'
PHONE_NUMBER = '+1234567890'   # Your phone number (with country code)

SOURCE_CHAT_ID = -1001234567890   # Source chat ID (group/channel)
DEST_CHAT_ID = -1009876543210     # Destination chat ID
# -----------------------------------

client = TelegramClient('session', API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHAT_ID))
async def forward_message(event):
    # Copy the message to the destination chat
    await client.send_message(DEST_CHAT_ID, event.message.text or "Media message (no text)")
    # Optional: also forward media
    if event.message.media:
        await client.send_file(DEST_CHAT_ID, event.message.media, caption=event.message.text)

async def main():
    await client.start(PHONE_NUMBER)
    print("Forwarder is running... (Press Ctrl+C to stop)")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())