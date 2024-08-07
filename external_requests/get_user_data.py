from tools.treatment_data import create_csv_file, filter_user_data, save_etl_data
from tools.file_management import create_file
import pandas as pd
import requests
import config, datetime

def get_daily_user_data():
    try:
        now = datetime.datetime.now()
        today = now.strftime("%Y%m%d")

        url_site = config.RESTAPI_URL

        users_request = requests.get(url=url_site)

        users_request_json = users_request.json()

        users_data = users_request_json["users"]

        create_file(users_request_json, 'data', 'json')
        df = pd.json_normalize((users_request_json['users']))
        df.to_csv(f'users-data/etl_{today}.csv')

        users_by_gender, users_by_age, users_by_city, users_by_so = filter_user_data(users_data)
        summary_id = create_csv_file(users_data, users_by_gender, users_by_age, users_by_city, users_by_so)
        save_etl_data(users_data, summary_id)
        return True
    except Exception as e:
        print(e)