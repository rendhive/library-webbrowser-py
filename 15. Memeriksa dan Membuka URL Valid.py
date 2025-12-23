import re

url_to_check = 'https://www.validurl.com'

# Cek validitas URL
if re.match(r'https?://.*', url_to_check):
    webbrowser.open(url_to_check)
    print("URL valid telah dibuka.")
else:
    print("URL tidak valid.")
# Fungsi: Memeriksa apakah URL sesuai dengan pola dan kemudian membukanya jika valid.
# Kondisi: Ketika Anda perlu memastikan URL yang akan dibuka adalah valid.
