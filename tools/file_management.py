import json
import datetime

def create_file(users_data_json, prefix, extension):
    now = datetime.datetime.now()

    today = now.strftime("%Y%m%d")
    with open(f'users-data/{prefix}_{today}.{extension}', 'w') as outfile:
        json.dump(users_data_json, outfile)

    return True

def create_file_by_string(users_data_str, prefix, extension):
    now = datetime.datetime.now()

    today = now.strftime("%Y%m%d")
    with open(f'users-data/{prefix}_{today}.{extension}', 'w') as outfile:
        outfile.write(users_data_str)

    return True