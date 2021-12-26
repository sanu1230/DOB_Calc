import pandas as pd
import numpy as np
from datetime import datetime, date
from dateutil import relativedelta

# dob = '15-01-1982'

def age_cal(dob):
     today = datetime.now()
     dob = datetime.strptime(dob, '%d-%m-%Y')
     diff = relativedelta.relativedelta(today, dob)
     years = diff.years 
     months = diff.months 
     days = diff.days
     hours = diff.hours
     minutes = diff.minutes
     seconds = diff.seconds
     microsec = diff.microseconds
     diff1 = (today - dob).days
     totalhrs = diff1 * 24
     totalmin = totalhrs * 60
     totalsec = totalmin * 60
     
     return years, months, days, hours, minutes, seconds, microsec, diff1, totalhrs, totalmin, totalsec

# age_cal(dob)