import json

urls_to_open = ['https://www.microsoft.com', 'https://www.oracle.com']
with open('urls.json', 'w') as f:
    json.dump(urls_to_open, f)

with open('urls.json', 'r') as f:
    urls = json.load(f)

for url in urls:
    webbrowser.open_new_tab(url)

print("URL dari berkas JSON telah dibuka.")
# Fungsi: Menyimpan dan kemudian membuka URL dari berkas JSON.
# Kondisi: Ketika Anda ingin mengelola dan memanfaatkan daftar URL yang tersimpan.

