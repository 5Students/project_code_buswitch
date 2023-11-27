import datetime
from dateutil.relativedelta import relativedelta
d = datetime.datetime.now()
d = d - relativedelta(days=5)
print(d.strftime('%Y%m%d'))
