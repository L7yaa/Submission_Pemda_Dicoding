import pandas as pd

def transform_data(data):
    for record in data:
        price_in_usd = record["Price"].replace("$", "").replace(",", "") if isinstance(record["Price"], str) else "0"
        
        try:

            price_in_usd = float(price_in_usd)
            record["Price"] = price_in_usd * 16000  
        except ValueError:
            record["Price"] = None  

    df = pd.DataFrame(data)

    df = df[df["Title"] != "Unknown Product"]  
    df = df.dropna(subset=["Title", "Price", "Rating"]) 
    df = df.drop_duplicates()  

    df["Colors"] = df["Colors"].str.extract(r'(\d+)').astype(float)  


    df["Size"] = df["Size"].str.replace("Size: ", "", regex=True)

    df["Size"] = df["Size"].astype(str)
    df["Gender"] = df["Gender"].astype(str)

    df["Timestamp"] = pd.to_datetime("now").strftime("%Y-%m-%d %H:%M:%S")

    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

    df = df.dropna(subset=['Price'])

    return df
