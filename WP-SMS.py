import pywhatkit
import sys

# telefon numarası, mesaj ve gönderilecek zamanı al
phone_number = sys.argv[1]
message = sys.argv[2]
send_time = sys.argv[3]

# tarih ve saat bilgilerini ayrıştır
year, month, day, hour, minute = map(int, send_time.split())

# mesajı gönder
pywhatkit.sendwhatmsg(phone_number, message, hour, minute, day, month, year)
