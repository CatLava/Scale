#!/usr/bin/env python3
from scale_rq import Get_Frame
from checkers import occlusion_check, time_check, background_NA_check
from csv_write import file_update


# enter your scale token
TOKEN = ''

# Enter project url in this case
# This will also pull any valid GET request URL
URL = 'https://api.scale.com/v1/tasks'

# Optional field; params to filter for batches
PARAMS =  {"status":"completed", "project":"Traffic Sign Detection"}

# File must be created before running
FILE = 'output.csv'

# This decorater allows callable requests to URL
@Get_Frame
def get_caller():
    return


if __name__ == "__main__":
    # Calling all the data to iterate over
    image_data = get_caller(URL, TOKEN, PARAMS)['docs']

    # will append a row count to the file
    sum = 0

    for task in image_data:
        # current is a list that is appended to csv file
        current = [sum]

        # Add task ID to row
        current.append(task['task_id'])

        # Check occlusion levels
        occlusion_check(task, current)

        # Check if time is reasonable
        time_check(task, current)

        # Backgrgound color within spec
        background_NA_check(task, current)

        # write to file
        file_update(FILE, current)

        sum +=1







