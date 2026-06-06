# Telegram-Message-Forwarder-Simple-Copy-Send--MM


# Telegram မက်ဆေ့ချ် မိတ္တူပို့ခြင်း (ရိုးရှင်းသော ကူးယူပို့ဆောင်ခြင်း)

ဤသည်မှာ Telethon library ကိုသုံးပြီး အရင်းအမြစ် chat (အုပ်စု သို့မဟုတ် ချန်နယ်) မှ လက်ခံမည့် chat (အုပ်စု သို့မဟုတ် ချန်နယ်) သို့ **မက်ဆေ့ချ်အသစ်များအားလုံးကို** ပြန်လည်ပို့ဆောင်ပေးသည့် အနည်းဆုံး Python script ဖြစ်သည်။

## လိုအပ်ချက်များ

- Python 3.7+
- Telegram API ID နှင့် API Hash (https://my.telegram.org/apps မှ ရယူပါ)

## တပ်ဆင်ခြင်း

```bash
pip install telethon

```markdown
# Telegram မက်ဆေ့ချ် မိတ္တူပို့ခြင်း (ရိုးရှင်းသော ကူးယူပို့ဆောင်ခြင်း)

ဤသည်မှာ Telethon library ကိုသုံးပြီး အရင်းအမြစ် chat (အုပ်စု သို့မဟုတ် ချန်နယ်) မှ လက်ခံမည့် chat (အုပ်စု သို့မဟုတ် ချန်နယ်) သို့ **မက်ဆေ့ချ်အသစ်များအားလုံးကို** ပြန်လည်ပို့ဆောင်ပေးသည့် အနည်းဆုံး Python script ဖြစ်သည်။

## လိုအပ်ချက်များ

- Python 3.7+
- Telegram API ID နှင့် API Hash (https://my.telegram.org/apps မှ ရယူပါ)

## တပ်ဆင်ခြင်း

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

## အသုံးပြုပုံ

1. `API_ID`, `API_HASH` နှင့် `PHONE_NUMBER` တို့ကို သင့်ကိုယ်ပိုင် အထောက်အထားများဖြင့် အစားထိုးပါ။
2. `SOURCE_CHAT_ID` နှင့် `DEST_CHAT_ID` တို့ကို အမှန်တကယ် chat ID များဖြင့် အစားထိုးပါ။
   - Chat ID များကိုရှာရန် `client.get_dialogs()` ကိုသုံးနိုင်သည် သို့မဟုတ် chat တွင် အများသုံး username ရှိပါက `@username` ကိုလည်း သုံးနိုင်သည်။
3. Script ကို run ပါ
   ```bash
   python forwarder.py
   ```
4. ပထမဆုံး run ချိန်တွင် သင့်အကောင့်သို့ ပို့သော verification code ကို ထည့်သွင်းရန် တောင်းဆိုလိမ့်မည်။
5. ထို့နောက် အရင်းအမြစ် chat မှ မက်ဆေ့ချ်အသစ်တိုင်းကို လက်ခံမည့် chat သို့ အဆက်မပြတ် ပြန်လည်ပို့ဆောင်ပေးလိမ့်မည်။

## မှတ်စုများ

- Script သည် ၎င်းလည်ပတ်နေစဉ်အတွင်း **ရောက်ရှိလာသော မက်ဆေ့ချ်အသစ်များကိုသာ** ပြန်ပို့ပေးသည်။
- သမိုင်းဝင် မက်ဆေ့ချ်ဟောင်းများကို ပြန်ပို့လိုပါက `client.get_messages()` ကို ကိုယ်တိုင် loop ပတ်၍ လုပ်ဆောင်ရမည်။
- အရင်းအမြစ် chat သည် **ချန်နယ်** ဖြစ်ပါက သင့်အကောင့်သည် အက်ဒမင် သို့မဟုတ် မက်ဆေ့ချ်များကို ကြည့်ရှုခွင့် ရှိရမည်။
- သီးသန့် အုပ်စု/ချန်နယ်များအတွက် သင့်အကောင့်သည် အဖွဲ့ဝင်တစ်ဦး ဖြစ်ရမည်။

## Script ရပ်တန့်ရန်

Terminal တွင် `Ctrl + C` ကို နှိပ်ပါ။

## လိုင်စင်

ဤ script ကို MIT လိုင်စင်အောက်တွင် ရရှိနိုင်ပါသည်။
```
