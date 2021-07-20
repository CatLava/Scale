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

FILE = 'output.csv'

# This decorater allows callable requests to URL
@Get_Frame
def get_caller():
    return

image_data = get_caller(URL, TOKEN, PARAMS)['docs']

output = []

sum = 0

for task in image_data:
    current = [sum]
    #print(task.keys())
    current.append(task['task_id'])
    occlusion_check(task, current)
    time_check(task, current)
    background_NA_check(task, current)
    file_update(FILE, current)
    print(current)
    output.append(current)
    sum +=1







