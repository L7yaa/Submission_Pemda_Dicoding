import os
import pandas as pd
import gspread  # ✅ tambahkan ini
from google.oauth2.service_account import Credentials
from gspread_dataframe import set_with_dataframe

def save_to_csv(df, path):
    df.to_csv(path, index=False)
    print(f"✅ Data disimpan ke CSV: {path}")

def save_to_google_sheets(df, spreadsheet_id, worksheet_name="Sheet1"):
    SERVICE_ACCOUNT_FILE = './google-sheets-api.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    try:
        creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        client = gspread.authorize(creds)
        sheet = client.open_by_key(spreadsheet_id).worksheet(worksheet_name)
        set_with_dataframe(sheet, df)
        print("✅ Berhasil menambahkan data!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")