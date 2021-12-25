import pandas as pd
import numpy as np
from datetime import datetime, date
from dateutil import relativedelta



def age_cal(dob):
     today = date.today()
     dob = datetime.strptime(dob, '%d-%m-%Y').date()
     diff = relativedelta.relativedelta(today, dob)
     years = diff.years 
     months = diff.months 
     days = diff.days
     return years, months, days
