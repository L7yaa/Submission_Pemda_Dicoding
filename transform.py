import pandas as pd
import unittest

def transform_data(data):
    print(f"📊 Jumlah data awal: {len(data)}")

    for record in data:
        if "Price" in record:
            price_in_usd = record["Price"].replace("$", "").replace(",", "") if isinstance(record["Price"], str) else "0"
            try:
                price_in_usd = float(price_in_usd)
                record["Price"] = price_in_usd * 16000  # Konversi ke Rupiah
            except ValueError:
                record["Price"] = None
        else:
            record["Price"] = None

        if "Colors" not in record:
            record["Colors"] = "0"
        if "Size" not in record:
            record["Size"] = "Unknown Size"
        if "Gender" not in record:
            record["Gender"] = "Unknown Gender"
        if "Title" not in record:
            record["Title"] = "Unknown Product"
        if "Rating" not in record:
            record["Rating"] = "No Rating"

    df = pd.DataFrame(data)
    print(f"📄 DataFrame dibuat: {df.shape[0]} baris, {df.shape[1]} kolom")

    if "Title" not in df.columns:
        raise KeyError("'Title' column is missing in the scraped data")

    # Bersihkan kolom Rating untuk hanya mengambil angka
    df["Rating"] = df["Rating"].str.replace("Rating:  ⭐", "", regex=True).str.extract(r'(\d+\.\d+)').astype(float)

    # Bersihkan kolom Gender untuk menghapus "Gender: "
    df["Gender"] = df["Gender"].str.replace("Gender: ", "", regex=True)

    # Pastikan kolom Colors hanya berisi angka dan hapus ".0"
    df["Colors"] = df["Colors"].str.extract(r'(\d+)').astype(int)

    # Bersihkan kolom Size untuk menghapus teks "Size: "
    df["Size"] = df["Size"].str.replace("Size: ", "", regex=True)

    # Menambahkan timestamp
    df["Timestamp"] = pd.to_datetime("now").strftime("%Y-%m-%d %H:%M:%S")

    # Hapus kolom yang semua isinya NaN (tidak hapus baris!)
    df.dropna(axis=1, how='all', inplace=True)

    # Hapus baris yang memiliki nilai invalid atau kosong
    df = df[df["Title"] != "Unknown Product"]
    df = df[df["Rating"].notna()]
    df = df[df["Price"].notna()]
    df = df[df["Colors"].notna()]

    # Hapus baris yang mengandung nilai NaN
    df.dropna(inplace=True)

    print(f"✅ Transformasi selesai: {df.shape[0]} baris, {df.shape[1]} kolom")
    

    return df
