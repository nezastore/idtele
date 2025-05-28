from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

# Fungsi untuk format tanggal pembuatan akun (Telegram API tidak menyediakan tanggal ini)
def get_account_creation_date(user_id: int) -> str:
    # Telegram tidak menyediakan tanggal pembuatan akun secara resmi melalui API.
    # Sebagai alternatif, kita bisa memberikan info bahwa data ini tidak tersedia.
    return "❓ Tidak tersedia melalui API Telegram"

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    message = (
        f"👋 Hai, *{user.first_name}*!\n\n"
        "Saya adalah bot yang bisa membantu kamu melihat informasi akun Telegram-mu.\n"
        "Ketik /id untuk melihat detail akunmu."
    )
    update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)

def id_command(update: Update, context: CallbackContext) -> None:
    user = update.effective_user

    # Ambil data user
    user_id = user.id
    first_name = user.first_name or ""
    last_name = user.last_name or ""
    username = f"@{user.username}" if user.username else "Tidak ada username"

    # Tanggal pembuatan akun (tidak tersedia, jadi pakai fungsi placeholder)
    creation_date = get_account_creation_date(user_id)

    message = (
        f"🆔 *Informasi Akun Telegram Kamu:*\n\n"
        f"👤 Nama Lengkap: {first_name} {last_name}\n"
        f"🔖 Username: {username}\n"
        f"🆔 ID Akun: `{user_id}`\n"
        f"📅 Tanggal Pembuatan Akun: {creation_date}\n\n"
        "Terima kasih sudah menggunakan bot ini! 😊"
    )
    update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)

def main():
    # Ganti 'YOUR_BOT_TOKEN' dengan token bot Telegram Anda
    updater = Updater("8063311159:AAHnKuZkk2AkU2AUSsSlIXxGVcccjB5h0uA", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("id", id_command))

    print("Bot berjalan... Tekan Ctrl+C untuk berhenti.")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
