import requests
from bs4 import BeautifulSoup

def fetch_product_data(page_number):
    try:
        # Tentukan URL berdasarkan nomor halaman
        if page_number == 1:
            url = "https://fashion-studio.dicoding.dev"
        else:
            url = f"https://fashion-studio.dicoding.dev/page{page_number}"

        print(f"📥 Mengakses halaman: {url}")

        # Lakukan permintaan HTTP ke URL
        response = requests.get(url)
        response.raise_for_status()

        # Parsing konten HTML dengan BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        data_produk = []

        # Cari semua elemen dengan class "collection-card"
        cards = soup.find_all("div", class_="collection-card")

        print(f"✅ Halaman {page_number}: {len(cards)} produk ditemukan")

        for card in cards:
            # Ekstrak informasi produk dari elemen yang sesuai
            title_elem = card.find("h3", class_="product-title")
            price_elem = card.find("div", class_="price-container")
            rating_elem = card.find("p", string=lambda t: t and 'Rating' in t)
            colors_elem = card.find("p", string=lambda t: t and 'Colors' in t)
            size_elem = card.find("p", string=lambda t: t and 'Size' in t)
            gender_elem = card.find("p", string=lambda t: t and 'Gender' in t)

            produk = {
                "Title": title_elem.text.strip() if title_elem else "",
                "Price": price_elem.text.strip() if price_elem else "",
                "Rating": rating_elem.text.strip() if rating_elem else "",
                "Colors": colors_elem.text.strip() if colors_elem else "",
                "Size": size_elem.text.strip() if size_elem else "",
                "Gender": gender_elem.text.strip() if gender_elem else ""
            }

            data_produk.append(produk)

        return data_produk

    except requests.exceptions.RequestException as e:
        raise Exception(f"❌ Gagal mengakses halaman produk: {str(e)}")
