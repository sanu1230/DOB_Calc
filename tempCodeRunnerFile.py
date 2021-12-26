import pandas as pd
import numpy as np
from datetime import datetime, date
from dateutil import relativedelta


today = date.today()
dob = '15-01-1982'
dob = datetime.strptime(dob, '%d-%m-%Y')
print(dob.date())
print(today)


