import requests
from datetime import datetime

USERNAME = "kenjidev"
TOKEN = ""
GRAPH_ID = "graph1"
FMT_DATE = "%Y%m%d"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

pixela_endpoint = "https://pixe.la/v1/users"
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.status_code)
# print(response.text)


graph_config = {
    "id": GRAPH_ID,
    "name": "Food spending",
    "unit": "yen",
    "type": "int",
    "color": "kuro",
}

my_headers = {
    "X-USER-TOKEN": TOKEN
}
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=my_headers)
# print(response.status_code)
# print(response.text)


# Today
today = datetime.now()
today_fmt = today.strftime(FMT_DATE)

post_today_date = {
    "date": today_fmt,
    "quantity": "3200",
}

pixel_create_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
def create_pixel():
    what_date = input("Create pixel for today?[y]es/[n]no/[e]xit: ")
    match what_date.lower():
        case "y" | "yes":
            response = requests.post(url=pixel_create_endpoint, json=post_today_date, headers=my_headers)
            print(response.status_code)
            print(response.text)
        case "n" | "no":
            specify_date = input("Specify a date[yyyymmdd]: ")
            quantity = input("Specify quantity: ")
            post_specified_date = {
                "date": specify_date,
                "quantity": str(quantity),
            }
            response = requests.post(url=pixel_create_endpoint, json=post_specified_date, headers=my_headers)
            print(response.status_code)
            print(response.text)
        case "e" | "exit":
            exit
            
        case _:
            print(f"Something went wrong..")


def update_pixel():
    what_date = input("Update pixel for today?[y]es/[n]o/[e]xit: ")
    match what_date.lower():
        case "y" | "yes":
            pixel_update_endpoint = f"{pixel_create_endpoint}/{today_fmt}"
            quantity = input("Specify quantity: ")
            update_config = {
                "quantity": quantity,
            }
            response = requests.put(url=pixel_update_endpoint, json=update_config, headers=my_headers)
            print(response.status_code)
            print(response.text)
        case "n" | "no":
            specify_date = input("Specify a date[yyyymmdd]: ")
            pixel_update_endpoint = f"{pixel_create_endpoint}/{specify_date}"
            quantity = input("Specify quantity: ")
            update_config = {
                "quantity": quantity,
            }
            response = requests.put(url=pixel_create_endpoint, json=update_config, headers=my_headers)
            print(response.status_code)
            print(response.text)
        case "e" | "exit":
            exit
            
        case _:
            print(f"Something went wrong..")


def delete_pixel():
    what_date = input("Delete pixel for today?[y]es/[n]o/[e]xit: ")
    match what_date.lower():
        case "y" | "yes":
            pixel_delete_endpoint = f"{pixel_create_endpoint}/{today_fmt}"
            response = requests.delete(url=pixel_delete_endpoint, headers=my_headers)
            print(response.status_code)
            print(response.text)
        case "n" | "no":
            specify_date = input("Specify a date[yyyymmdd]: ")
            pixel_delete_endpoint = f"{pixel_create_endpoint}/{specify_date}"
            response = requests.delete(url=pixel_delete_endpoint, headers=my_headers)
            print(response.status_code)
            print(response.text)
        case "e" | "exit":
            exit
        
        case _:
            print(f"Something went wrong..")
            

choose = input("'[c]reate' to create pixel, '[u]pdate' to update pixel, '[d]elete/[d]el' to delete pixel, [e]xit to exit: ")
match choose.lower():
    case "c" | "create":
        create_pixel()
    case "u" | "update":
        update_pixel()
    case "d" | "delete" | "del":
        delete_pixel()
    case "e" | "exit":
        exit

     
