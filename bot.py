import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Token Bot
TOKEN = "8224359305:AAFOhs1kQFtjIAJ6ZT_LnVKJfKuYeFQqUls"
ADMIN_ID = 6666021576  # ID Telegram kakak

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Menu Start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("➕ Buat Akun", callback_data="buat_akun")],
        [InlineKeyboardButton("👥 Cek User Aktif", callback_data="cek_user")],
        [InlineKeyboardButton("💸 Top Up Saldo", callback_data="topup")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Selamat Datang Di Petarukan Store kak ☺\n\nSilahkan pilih menu di bawah 👇",
        reply_markup=reply_markup
    )

# Callback Menu
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "buat_akun":
        await query.edit_message_text(
            "📌 Pembuatan Akun\n\n"
            "- Request Nama\n"
            "- Masa Aktif\n"
            "- Atur Kuota\n"
            "- Limit IP"
        )

    elif query.data == "cek_user":
        await query.edit_message_text("👥 User Aktif Saat Ini:\n- VMESS: 67\n- TROJAN: 1\n- SSH: 3")

    elif query.data == "topup":
        await query.edit_message_text(
            "💸 Top Up Saldo\n\n"
            "Silahkan Transfer Ke Dana: *085643838017*\n"
            "Nominal: *Rp 45,000*\n\n"
            "Setelah transfer, tunggu konfirmasi admin."
        )

# Main
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()

if __name__ == "__main__":
    main()
