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
        "Ketik /id untuk melihat detail akunmu.\n"
        "Ketik /cek @username untuk melihat detail akun Telegram orang lain."
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

def cek_command(update: Update, context: CallbackContext) -> None:
    # Pastikan ada argumen username
    if not context.args:
        update.message.reply_text("⚠️ Mohon sertakan username setelah perintah /cek, contoh: /cek @username")
        return

    username = context.args[0]
    if not username.startswith("@"):
        update.message.reply_text("⚠️ Username harus diawali dengan '@', contoh: /cek @username")
        return

    # Hapus '@' untuk pencarian
    username_clean = username[1:]

    try:
        # Gunakan metode get_chat untuk mendapatkan info user berdasarkan username
        user_chat = update.effective_chat.bot.get_chat(username_clean)

        # Ambil data user
        user_id = user_chat.id
        first_name = user_chat.first_name or ""
        last_name = user_chat.last_name or ""
        username_resp = f"@{user_chat.username}" if user_chat.username else "Tidak ada username"

        # Tanggal pembuatan akun (tidak tersedia)
        creation_date = get_account_creation_date(user_id)

        message = (
            f"🔍 *Informasi Akun Telegram untuk {username_resp}:*\n\n"
            f"👤 Nama Lengkap: {first_name} {last_name}\n"
            f"🔖 Username: {username_resp}\n"
            f"🆔 ID Akun: `{user_id}`\n"
            f"📅 Tanggal Pembuatan Akun: {creation_date}\n\n"
            "ℹ️ Informasi ini didapatkan dari Telegram API."
        )
        update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)

    except Exception as e:
        # Jika username tidak ditemukan atau error lain
        update.message.reply_text(f"❌ Gagal mendapatkan informasi untuk {username}. Pastikan username benar dan bot memiliki akses.")

def main():
    # Ganti 'YOUR_BOT_TOKEN' dengan token bot Telegram Anda
    updater = Updater("8063311159:AAHnKuZkk2AkU2AUSsSlIXxGVcccjB5h0uA", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("id", id_command))
    dispatcher.add_handler(CommandHandler("cek", cek_command))

    print("Bot berjalan... Tekan Ctrl+C untuk berhenti.")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
