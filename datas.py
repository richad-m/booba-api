import gspread
import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


try:
    os.environ['USER'] == 'richad'
    sheet_id = os.environ.get("sheet_id")
    gsheet_credentials = {
        "type": os.environ.get("type"),
        "project_id": os.environ.get("project_id"),
        "private_key_id": os.environ.get("private_key_id"),
        "private_key": os.environ.get('private_key'),
        "client_email": os.environ.get("client_email"),
        "client_id": os.environ.get("client_id"),
        "auth_uri": os.environ.get("auth_uri"),
        "token_uri": os.environ.get("token_uri"),
        "auth_provider_x509_cert_url": os.environ.get("auth_provider_x509_cert_url"),
        "client_x509_cert_url": os.environ.get("client_x509_cert_url"),
    }
except KeyError:
    print('Je suis en production')
    sheet_id = os.environ.get('sheet_id')
    gsheet_credentials = os.environ.get('gsheet_credentials')


def fetch_datas():
    print(os.environ.get('private_key'))
    print(type(gsheet_credentials))
    # Fetches data from my google_sheet
    # Get your crendentials in google developers portal
    gc = gspread.service_account_from_dict(gsheet_credentials)
    # Get your sheet ID directly from the URL of the spreadsheet
    sh = gc.open_by_key(sheet_id)
    database = sh.sheet1
    return database.get_all_records()
