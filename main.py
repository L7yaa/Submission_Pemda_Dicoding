from utils.extract import fetch_product_data
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_google_sheets
import unittest

def start_scraper():
    produk_terkumpul = []

    for idx in range(1, 51):
        isFirst = False

        if idx == 1:
            isFirst = True
            base = "https://fashion-studio.dicoding.dev"
        else:
            base = f"https://fashion-studio.dicoding.dev/page{idx}"

        print(f"\n🔍 Mengakses: {base}")

        try:
            hasil = fetch_product_data(idx)
            if hasil:
                produk_terkumpul.extend(hasil)
                print(f"✅ {len(hasil)} produk diambil dari halaman {idx}")
            else:
                print(f"⚠️ Tidak ada data pada halaman {idx}")
        except Exception as e:
            print(f"❌ Gagal mengambil data dari halaman {idx}: {e}")

    if not produk_terkumpul:
        print("\n❌ Tidak ada data yang berhasil dikumpulkan.")
        return

    print("\n🔧 Transformasi data...")
    hasil_bersih = transform_data(produk_terkumpul)

    print("💾 Menyimpan ke CSV...")
    save_to_csv(hasil_bersih, path="data_produk.csv")

    print("☁️ Upload ke Google Sheets...")
    save_to_google_sheets(
        hasil_bersih,
        spreadsheet_id="1jLugs_w3XT2mPz7iuCz2E2DzPxNjV2t6Gym2CsyKr3Q",
        worksheet_name="Sheet1"   
    )
    

    print("\n🎉✅ Scraping selesai!")

if __name__ == "__main__":
    start_scraper()
