from datetime import date
import os


## Refresh Pivot Table

import win32com.client as win32

xlapp = win32.DispatchEx('Excel.Application')
xlapp.DisplayAlerts = False
xlapp.Visible = True

xlbook = xlapp.Workbooks.Open(r'\\fs-dev\public dev\ApplicationInfrastructure\dev\bi_dev8200\Eilon\extract to excel\pvt.xlsx')

# Refresh all pivot tables
xlbook.RefreshAll()

xlbook.Save()
xlbook.Close()
xlapp.Quit()

# Make sure Excel completely closes
del xlbook
del xlapp

