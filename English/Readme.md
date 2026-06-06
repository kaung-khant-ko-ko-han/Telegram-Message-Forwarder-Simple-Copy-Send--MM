```markdown
# Telegram Message Forwarder (Simple Copy & Send)

This is a minimal Python script that forwards **all** new messages from a source chat (group or channel) to a destination chat (group or channel) using the Telethon library.

## Requirements

- Python 3.7+
- Telegram API ID and API Hash (get them from https://my.telegram.org/apps)

## Installation

```bash
pip install telethon
```

## Script (`forwarder.py`)

```python
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
```

## How to Use

1. Replace `API_ID`, `API_HASH`, and `PHONE_NUMBER` with your own credentials.
2. Replace `SOURCE_CHAT_ID` and `DEST_CHAT_ID` with the actual chat IDs.
   - To find chat IDs, you can use `client.get_dialogs()` or use the `@username` if the chat has a public username.
3. Run the script:
   ```bash
   python forwarder.py
   ```
4. The script will prompt for a verification code (sent to your Telegram) on first run.
5. It will then continuously forward every new message from the source to the destination.

## Notes

- The script only forwards **new messages** that arrive while it is running.
- To forward old/historical messages, you would need to iterate through `client.get_messages()` manually.
- If the source chat is a **channel**, your account must be an administrator or at least have access to view messages.
- For private groups/channels, your account must be a member.

## Stopping the Script

Press `Ctrl + C` in the terminal to stop the forwarder.

## License

This script is provided under the MIT License.
