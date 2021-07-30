import datetime
import time
import requests
import csv

csv_path = "File_Input.csv"
file_out = "File_Output.txt"
with open(csv_path, "r") as f_obj:
    reader = csv.reader(f_obj)
    for row in reader:
        try:
            response = requests.post('https://statusnpd.nalog.ru/api/v1/tracker/taxpayer_status',
                                     json={"inn": row[0].split(";")[1],
                                           "requestDate": str(datetime.datetime.utcnow())[0:10]})

            json_response = response.json()
			
            if (list(json_response.keys()))[0] == 'status':
                data = [row[0].split(";")[0], json_response['status']]
            else:
                data = [row[0].split(";")[0], "server error"]

            print(str(data[0]) + ' ' + str(data[1]))

            with open(file_out, "a") as f_out:
                f_out.write(str(data[0]) + ' ' + str(data[1]) + '\n')

        except Exception:
            print(str(row[0].split(";")[0]) + ' ' + "our error")

            with open(file_out, "a") as f_out:
                f_out.write(str(row[0].split(";")[0]) + ' ' + "our error" + '\n')

        time.sleep(31)

input("Enter any key for quit ... ")

