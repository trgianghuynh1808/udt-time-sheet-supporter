from __future__ import print_function

from googleapiclient.errors import HttpError
from authentication import googleSheetConnect
from sheet import *


def main():
    credentials = googleSheetConnect()
    sheet_service = SheetService(credentials)

    try:
        sheet_data = sheet_service.readSheet(range="timesheet!A2:G2")
        # response = sheet_service.writeSheet(range="timesheet!G2", body_data=[["x"]])

        # print("response", response)

        if not sheet_data:
            print('No data found.')
            return
        print("test values",sheet_data)
    except HttpError as error:
        print(error)

if __name__ == '__main__':
    main()
