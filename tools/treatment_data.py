from tools.file_management import create_file, create_file_by_string
from database.database_connection import db_session
from database.models import Summary, ETL
def filter_user_data(users_data):
    users_by_gender = {}
    users_by_age = {
        "0-10": {},
        "11-20": {},
        "21-30": {},
        "31-40": {},
        "41-50": {},
        "51-60": {},
        "61-70": {},
        "71-80": {},
        "81-90": {},
        "91+": {}
    }
    users_by_city = {}
    users_by_so = {}
    for user in users_data:
        users_by_gender.setdefault(user["gender"], []).append(user)
        
        gender = user["gender"]

        users_by_city.setdefault(user["address"]["city"], {})
        users_by_city[user["address"]["city"]].setdefault(gender, []).append(user)
        
        if "Macintosh" in user["userAgent"]:
            users_by_so.setdefault("Apple", []).append(user)
        elif "Windows" in user["userAgent"]:
            users_by_so.setdefault("Windows", []).append(user)
        elif "Linux" in user["userAgent"]:
            users_by_so.setdefault("Linux", []).append(user)


        if 0 <= user["age"] <= 10:
            users_by_age["0-10"].setdefault(gender, []).append(user)
        elif 11 <= user["age"] <= 20:
            users_by_age["11-20"].setdefault(gender, []).append(user)
        elif 21 <= user["age"] <= 30:
            users_by_age["21-30"].setdefault(gender, []).append(user)
        elif 31 <= user["age"] <= 40:
            users_by_age["31-40"].setdefault(gender, []).append(user)
        elif 41 <= user["age"] <= 50:
            users_by_age["41-50"].setdefault(gender, []).append(user)
        elif 51 <= user["age"] <= 60:
            users_by_age["51-60"].setdefault(gender, []).append(user)
        elif 61 <= user["age"] <= 70:
            users_by_age["61-70"].setdefault(gender, []).append(user)
        elif 71 <= user["age"] <= 80:
            users_by_age["71-80"].setdefault(gender, []).append(user)
        elif 81 <= user["age"] <= 90:
            users_by_age["81-90"].setdefault(gender, []).append(user)
        elif user["age"] <= 91:
            users_by_age["91+"].setdefault(gender, []).append(user)
    
    return users_by_gender, users_by_age, users_by_city, users_by_so




def create_csv_file(users_data, users_by_gender, users_by_age, users_by_city, users_by_so):
    genders = []
    csv_data = f"registre, {len(users_data)} \n"
    csv_data += 'gender,total\n'
    for gender, users in users_by_gender.items():
        csv_data += f"{gender},{len(users)}\n"
        genders.append(gender)
    csv_data +="\n"

    csv_data +=  f"age,{','.join(genders)}\n"
    for age, users in users_by_age.items():
        csv_data += f"{age}"
        for gender in genders:
            csv_data += f",{ len(users[gender]) if gender in users else '' }"
        csv_data += "\n"

    csv_data += "\n"
    csv_data +=  f"City,{','.join(genders)}\n"
    for city, users in users_by_city.items():
        csv_data += f"{city}"
        for gender in genders:
            csv_data += f",{ len(users[gender]) if gender in users else '' }"
        csv_data += "\n"

    csv_data += "\n"
    csv_data += 'SO,total\n'
    for so, users in users_by_so.items():
        csv_data += f"{so},{len(users)}\n"

    create_file_by_string(csv_data, 'summary', 'csv')
    s = Summary(csv_data)
    db_session.add(s)
    db_session.commit()

    return s.summary_id


def save_etl_data(etl_data,summary_id):
    for etl in etl_data:
        e = ETL(summary_id, 
                etl['id'],
                etl['firstName'],
                etl['lastName'],
                etl['maidenName'],
                etl['age'],
                etl['gender'],
                etl['email'],
                etl['phone'],
                etl['username'],
                etl['password'],
                etl['birthDate'],
                etl['image'],
                etl['bloodGroup'],
                etl['height'],
                etl['weight'],
                etl['eyeColor'],
                etl['ip'],
                etl['macAddress'],
                etl['university'],
                etl['ein'],
                etl['ssn'],
                etl['userAgent'],
                etl['role'],
                etl['hair']['color'],
                etl['hair']['type'],
                etl['address']['address'],
                etl['address']['city'],
                etl['address']['state'],
                etl['address']['stateCode'],
                etl['address']['postalCode'],
                etl['address']['coordinates']['lat'],
                etl['address']['coordinates']['lng'],
                etl['address']['country'],
                etl['bank']['cardExpire'],
                etl['bank']['cardNumber'],
                etl['bank']['cardType'],
                etl['bank']['currency'],
                etl['bank']['iban'],
                etl['company']['department'],
                etl['company']['name'],
                etl['company']['title'],
                etl['company']['address']['address'],
                etl['company']['address']['city'],
                etl['company']['address']['state'],
                etl['company']['address']['stateCode'],
                etl['company']['address']['postalCode'],
                etl['company']['address']['coordinates']['lat'],
                etl['company']['address']['coordinates']['lng'],
                etl['company']['address']['country'],
                etl['crypto']['coin'],
                etl['crypto']['wallet'],
                etl['crypto']['network']
            )
        db_session.add(e)
        db_session.commit()
        
    return True