import pandas as pd
import sqlite3

# Part 1: Storing CTA data in a SQLite database called cta.db

def DataToDatabase(filename, dbname):
  data = pd.read_csv("CTA-Ridership-L-Station-Entries-Daily-Totals.csv", names = ['station_id', 'stationname', 'date', 'daytype', 'rides'], skiprows = [0])

  conn = sqlite3.connect("cta.db")
  cur = conn.cursor()

  cur.execute("CREATE TABLE daily_ridership_counts (station_id int, stationname text, date text, daytype text, rides int)")

  for i in range(len(data)):
   a = int(data['station_id'][i])
   b = data['stationname'][i]
   c = data['date'][i]
   d = data['daytype'][i]
   e = int(data['rides'][i])
   sql = "INSERT INTO daily_ridership_counts (station_id, stationname, date, daytype, rides) VALUES (:station_id, :stationname, :date, :daytype, :rides)"
   cur.execute(sql, {"station_id":a, "stationname":b, "date":c, "daytype":d, "rides":e})

  conn.commit()
  conn.close()

  # The database containing the data is 38.9 MB.

# Part 2: Calculating the average number of rides, for all months, for the UIC-Halsted station

def avg_num_rides_months():
  conn = sqlite3.connect("cta.db")
  cur = conn.cursor()
  sql = "SELECT date, rides FROM daily_ridership_counts WHERE station_id = 40350"
  date_and_rides_columns = cur.execute(sql)
  all_date_and_rides = date_and_rides_columns.fetchall()

  jan_rides = []
  for row in all_date_and_rides:
    if row[0][0:2] == "01": # accessing the months
      jan_rides.append(row[1]) # appending the rides
  jan_avg = sum(jan_rides)/len(jan_rides)
  print("January :", jan_avg)

  feb_rides = []
  for row in all_date_and_rides:
    if row[0][0:2] == "02":
      feb_rides.append(row[1])
  feb_avg = sum(feb_rides)/len(feb_rides)
  print("February :", feb_avg)

  mar_rides = []
  for row in all_date_and_rides:
    if row[0][0:2] == "03":
      mar_rides.append(row[1])
  mar_avg = sum(mar_rides)/len(mar_rides)
  print("March :", mar_avg)

  apr_rides = []
  for row in all_date_and_rides:
    if row[0][0:2] == "04":
      apr_rides.append(row[1])
  apr_avg = sum(apr_rides)/len(apr_rides)
  print("April :", apr_avg)

  may_rides = []
  for row in all_date_and_rides:
    if row[0][0:2] == "05":
      may_rides.append(row[1])
  may_avg = sum(may_rides)/len(may_rides)
  print("May :", may_avg)

  june_rides = []
  for row in all_date_and_rides:
    if row[0][0:2] == "06":
      june_rides.append(row[1])
  june_avg = sum(june_rides)/len(june_rides)
  print("June :", june_avg)

  july_rides = []
  for row in all_date_and_rides:
    if row[0][0:2] == "07":
      july_rides.append(row[1])
  july_avg = sum(july_rides)/len(july_rides)
  print("July :", july_avg)

  aug_rides = []
  for row in all_date_and_rides:
    if row[0][0:2] == "08":
      aug_rides.append(row[1])
  aug_avg = sum(aug_rides)/len(aug_rides)
  print("August :", aug_avg)

  sept_rides = []
  for row in all_date_and_rides:
    if row[0][0:2] == "09":
      sept_rides.append(row[1])
  sept_avg = sum(sept_rides)/len(sept_rides)
  print("September :", sept_avg)

  oct_rides = []
  for row in all_date_and_rides:
    if row[0][0:2] == "10":
      oct_rides.append(row[1])
  oct_avg = sum(oct_rides)/len(oct_rides)
  print("October :", oct_avg)

  nov_rides = []
  for row in all_date_and_rides:
    if row[0][0:2] == "11":
      nov_rides.append(row[1])
  nov_avg = sum(nov_rides)/len(nov_rides)
  print("November :", nov_avg)

  dec_rides = []
  for row in all_date_and_rides:
    if row[0][0:2] == "12":
      dec_rides.append(row[1])
  dec_avg = sum(dec_rides)/len(dec_rides)
  print("December :", dec_avg)

  conn.commit()
  conn.close()

  # OUTPUT

  # Average number of rides for all months at UIC-Halsted

  # January : 3907.7758913412563
  # February : 4955.733208955224
  # March : 4375.134125636672
  # April : 4863.619298245614
  # May : 2899.1358234295417
  # June : 2919.5263157894738
  # July : 2877.663701067616
  # August : 3518.5681003584227
  # September : 5675.288888888889
  # October : 5931.137992831541
  # November : 5104.498148148148
  # December : 2920.8888888888887

# Part 3: Finding the busiest station in the CTA system

def busiest_station():
  conn = sqlite3.connect("cta.db")
  cur = conn.cursor()

  sql = "SELECT stationname, SUM(rides) FROM daily_ridership_counts GROUP BY stationname ORDER BY SUM(rides) DESC" # orders the sum of rides in descending order, so that we may easily access it later on
  data = cur.execute(sql)
  all_data = data.fetchall()
  print("Busiest station: ", all_data[0][0]) # prints the busiest station
  print("Total ridership count: ", all_data[0][1]) # prints the total ridership count

  conn.commit()
  conn.close()

  # OUTPUT

  # Busiest station in the CTA system
  # Busiest station:  Clark/Lake
  # Total ridership count:  94799999

#DataToDatabase('CTA-Ridership-L-Station-Entries-Daily-Totals.csv', 'cta.db') # the table is only created once, so we don't have to re-execute this function
print("\n*****")
print("Average number of rides for all months at UIC-Halsted\n")
avg_num_rides_months()
print("\n*****")
print("Busiest station in the CTA system\n")
busiest_station()
