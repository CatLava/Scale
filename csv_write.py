# This file needs significant improvement
# Must have file created prior to executing
import csv



def file_update(file, data):
    with open(file, 'a+', newline='') as csv_update:
        filewrite = csv.writer(csv_update, delimiter=',')
        filewrite.writerow(data)
    return


