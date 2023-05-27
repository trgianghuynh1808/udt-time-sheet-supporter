from config import *
from googleapiclient.discovery import build

def getSheetValues(credentials):
    service = build('sheets', 'v4', credentials=credentials)
    # Call the Sheets API
    sheet = service.spreadsheets()
    sheetValues = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()

    return sheetValues

def readSheet(sheetValues):
    return sheetValues.get('values', [])
