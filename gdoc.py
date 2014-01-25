#!/usr/bin/python

import sys
import time
import datetime
import gspread

# ===========================================================================
# Google Account Details
# ===========================================================================

# Account details for google docs
email       = 'youe email address here
password    = 'password here'
spreadsheet = 'Data'

# ===========================================================================
# Example Code
# ===========================================================================


# Login with your Google account
try:
  gc = gspread.login(email, password)
except:
  print "Unable to log in.  Check your email address/password"
  sys.exit()

# Open a worksheet from your spreadsheet using the filename
try:
  worksheet = gc.open(spreadsheet).sheet1
  # Alternatively, open a spreadsheet using the spreadsheet's key
  # worksheet = gc.open_by_key('0BmgG6nO_6dprdS1MN3d3MkdPa142WFRrdnRRUWl1UFE')
except:
  print "Unable to open the spreadsheet.  Check your filename: %s" % spreadsheet
  sys.exit()

#weight martin 91.3
dim1 = sys.argv[1]
dim2 = sys.argv[2]
value = sys.argv[3]

# Append the data in the spreadsheet, including a timestamp
try:
    values = [datetime.datetime.now(), value, dim1, dim2 ]
    worksheet.append_row(values)
except:
    print "Unable to append data.  Check your connection?"
    sys.exit()

