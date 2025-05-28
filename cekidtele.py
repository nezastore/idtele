from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters
import random

# Daftar kutipan inspiratif
QUOTES = [
    "Jangan pernah menyerah, karena kegagalan adalah awal dari kesuksesan.",
    "Kesuksesan adalah hasil dari persiapan, kerja keras, dan belajar dari kegagalan.",
    "Hidup adalah 10% apa yang terjadi pada kita dan 90% bagaimana kita meresponnya.",
    "Jadilah perubahan yang ingin kamu lihat di dunia.",
    "Keberanian bukanlah ketiadaan rasa takut, tapi kemampuan untuk mengatasi rasa takut.",
    "Setiap hari adalah kesempatan baru untuk menjadi lebih baik.",
    "Impian tidak akan menjadi kenyataan tanpa kerja keras dan ketekunan."
]

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("CEKID", callback_data='cekid')],
        [InlineKeyboardButton("QUOTE", callback_data='quote')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "👋 Halo! Silakan pilih menu di bawah ini:",
        reply_markup=reply_markup
    )

def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'cekid':
        user = query.from_user
        message = (
            f"🆔 *Informasi Akun Telegram Kamu:*\n\n"
            f"👤 Nama Lengkap: {user.first_name} {user.last_name or ''}\n"
            f"🔖 Username: @{user.username if user.username else 'Tidak ada username'}\n"
            f"🆔 ID Akun: `{user.id}`"
        )
        query.edit_message_text(text=message, parse_mode=ParseMode.MARKDOWN)

    elif query.data == 'quote':
        quote = random.choice(QUOTES)
        message = f"💡 *Kutipan Inspiratif:*\n\n_{quote}_"
        query.edit_message_text(text=message, parse_mode=ParseMode.MARKDOWN)

def main():
    # Ganti dengan token bot Telegram Anda
    TELEGRAM_BOT_TOKEN = "8063311159:AAHnKuZkk2AkU2AUSsSlIXxGVcccjB5h0uA"

    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button_handler))

    print("Bot berjalan... Tekan Ctrl+C untuk berhenti.")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
