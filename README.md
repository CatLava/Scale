# Purpose:
The goal of this script is to pull data that describes an image analysis. The analysis is then spot checked by this script for any anomalies to be reported on.
The script is a test on 8 samples, however, it should maintain consistency up to 250K samples.

## Run:
Simply run the main.py script in the same folder as all other scripts. Note, csv must be created prior to running.
Be sure to fill out all necessary information in parameters before going executing.
Script uses Python 3.8, it has not been heavily tested in other situations

### libraries:
request, csv

## Requirements:
This script is making API requests to ScaleAI endpoints, in order to make requests, a valid API key is required