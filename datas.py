import gspread
import secrets_key


def fetch_datas():
  # Fetches data from my google_sheet
    # Get your crendentials in google developers portal
    gsheet_credentials = secrets_key.gsheet_credentials
    gc = gspread.service_account_from_dict(gsheet_credentials)
    # Get your sheet ID directly from the URL of the spreadsheet
    sh = gc.open_by_key(secrets_key.sheet_id)
    database = sh.sheet1
    return database.get_all_records()
