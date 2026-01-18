import csv

CSV_PATH = "files/created_users.csv"
def get_users_from_csv():

    user_list = []
    with open(CSV_PATH) as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None) 
        for row in reader:
            user_list.append(row)
    
    return user_list