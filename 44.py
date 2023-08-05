import datetime

y, m, d=tuple(map(int, input().split()))
print("%02d/%02d/%04d"%(m, d, y))

date = datetime.date(y, m, d)

next_day = date + datetime.timedelta(days=1)

next_day_formatted = next_day.strftime("%m/%d/%Y")

print(next_day_formatted)
