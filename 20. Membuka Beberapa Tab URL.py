websites = ['https://www.reddit.com', 'https://www.stackoverflow.com']

for website in websites:
    webbrowser.open_new_tab(website)

print("Semua situs telah dibuka dalam tab baru.")
# Fungsi: Membuka beberapa URL di tab baru secara otomatis.
# Kondisi: Ketika Anda ingin mengunjungi beberapa situs web tanpa menutup tab yang ada.
