import csv

date_set = []
for i in range(100):
    curr_year = 1913 + i
    date_set.append(curr_year + "-09-01")


def passes_filter(row):
    # Filter criteria:

    if row['Country'] != 'United States':
        return False
    elif row['dt'] in date_set:
        return False
    else:
        return True


# import and run passes_filter
data = []
header = []

# switch out the input .csv file
with open('GlobalLandTemperaturesByState.csv', 'r') as f:
    reader = csv.DictReader(f)

    header = reader.fieldnames
    for row in reader:
        if passes_filter(row):

            data.append(row)

# name the output file
with open('States1913and2013.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
