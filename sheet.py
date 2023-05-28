from config import *
from googleapiclient.discovery import build

class SheetService:
    def __init__(self, credentials):
        service = build('sheets', 'v4', credentials=credentials)
        sheet = service.spreadsheets()
        sheet_values = sheet.values()
        self.sheet_values = sheet_values

    def readSheet(self):
        result = self.sheet_values.get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        return result.get('values', [])

    def writeSheet(self, range, body_data):
        return self.sheet_values.update(spreadsheetId=SPREADSHEET_ID, range=range, valueInputOption="USER_ENTERED", body={"values": body_data}).execute()
