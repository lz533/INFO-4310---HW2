import csv

date_set = []
for i in range(101):
    curr_year = str(1913 + i)
    date_set.append(curr_year + "-09-01")


def passes_filter(row):
    # Filter criteria:

    if row['Country'] != 'United States':  # keep US states and cities
        return False
    elif row['dt'] not in date_set:  # keep entries from 1913 to 2013
        return False
    elif len(row['Latitude']) < 2 or len(row['Longitude']) < 2:
        return False
    elif len(row['AverageTemperature']) < 1:
        return False
    else:
        return True


# import and run passes_filter
data = []
header = []

# switch out the input .csv file
with open('GlobalLandTemperaturesByCity.csv', 'r') as f:
    reader = csv.DictReader(f)

    header = reader.fieldnames
    for row in reader:
        if passes_filter(row):
            row['Longitude'] = row['Longitude'][:-1]
            row['Latitude'] = row['Latitude'][:-1]
            data.append(row)

# name the output file
with open('processed_city_1913_2012.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
    print('processed')
