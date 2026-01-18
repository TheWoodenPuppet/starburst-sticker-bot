Here is a professional, comprehensive `README.md` for your project. I have included a special **"Maintenance"** section that documents the complex APK extraction and merging workflow we just established, so you don't forget it in the future.

---

# 🌲 Forest Sticker Bot

A Telegram bot designed for **Forest App** communities. It automatically detects Forest room links and replies with a specific sticker corresponding to the tree being planted.

It supports **14+ languages** (English, Arabic, Chinese, Japanese, etc.) and handles spam protection, scheduled messages, and dynamic sticker management.

## ✨ Features

* **Auto-Reply:** Detects tree names in messages *only* if they contain a valid `forestapp.cc` room link.
* **Multilingual Support:** Recognizes tree names in every language supported by the Forest App (extracted directly from the APK).
* **Anti-Spam:**
* **Cooldown:** Ignores repeated triggers from the same user for 5 seconds.
* **Logic:** Ignores general conversation (e.g., "I like white rice") unless a link is present.


* **Scheduled Messages:** Sends recurring daily reminders (e.g., "Bed 'o clock", "Drink Water") to specific groups.
* **Admin Tools:** Add new stickers directly from Telegram using `/addsticker` and export the database with `/export`.
* **Keep-Alive:** Includes a lightweight Flask server to keep the bot running on cloud platforms (Render, Replit, etc.).

## 🛠️ Installation & Setup

### 1. Prerequisites

* Python 3.9+
* A Telegram Bot Token (from [@BotFather](https://t.me/BotFather))

### 2. Install Dependencies

```bash
pip install python-telegram-bot flask pytz pandas

```

### 3. Configuration

Set your environment variables (or hardcode them in `config.py` for local testing):

* `BOT_TOKEN`: Your Telegram Bot API Token.

### 4. The Database (`stickers.csv`)

The bot relies on a `stickers.csv` file acting as the database.
**Format:** `trigger_word, sticker_file_id`

```csv
cedar, CAACAg...
white rose, CAACAg...
الوردة البيضاء, CAACAg...

```

## 🚀 Usage

### Running the Bot

```bash
python bot.py

```

### User Commands

Just paste a Forest Link!

> **User:** Join me! [https://forestapp.cc/join-room?token=xyz](https://www.google.com/search?q=https://forestapp.cc/join-room%3Ftoken%3Dxyz) I am planting a Cedar.
> **Bot:** *[Sends Cedar Sticker]*

### Admin Commands

*(Only accessible to IDs listed in `BOT_ADMIN_IDS`)*

* `/addsticker` - Starts a conversation to add a new trigger/sticker pair to the database.
* `/export` - Sends the current `stickers.csv` file to the admin.

## 🔄 Maintenance: Adding New Trees

When Forest releases a new update (e.g., new trees), follow this workflow to update the bot's vocabulary.

### Step 1: Extract New Names

1. Download the new **Forest APK**.
2. Decompile it using `apktool`.
3. Place `extract_master_list.py` in the decompiled `res` folder.
4. Run the script to generate `forest_master_list.csv`.

### Step 2: Update Sticker IDs

1. Send the new tree stickers to the bot (or @idstickerbot) to get their **File IDs**.
2. Open your current `stickers.csv` (from GitHub or `/export`).
3. Add the **English name only** at the bottom:
```csv
new tree name, CAACAg...[New_ID]

```



### Step 3: Merge Languages

1. Place `forest_master_list.csv`, `stickers.csv`, and `merge_langs.py` in the same folder.
2. Run the merge script:
```bash
python merge_langs.py

```


3. This generates `stickers_final.csv` containing the new tree in all 14 languages.
4. Rename it to `stickers.csv` and redeploy the bot.

## ⚠️ Known Localization Notes

### The "White Birch" Conflict (Arabic)

The Forest App contains a translation error where **White Birch** is named `الوردة البيضاء` ("The White Rose"), which is identical to the name for **White Rose**.

* **Behavior:** If an Arabic user plants a White Birch, the bot may send the White Rose sticker because the text triggers are identical.
* **Fix:** The CSV prioritizes the exact match or the first entry found. This is a known limitation of the app's data, not the bot.

### "Bear's Paw" Quotes

Some trees in the APK (like "Bear's Paw") are stored with literal quote marks (`"Bear's Paw"`). The `merge_langs.py` script automatically strips these so users don't have to type quotes.

## 📄 License

[Your License Choice]