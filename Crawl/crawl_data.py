import requests
import mysql.connector
root_url = 'http://ooo_api_container:8000'
def callApi(data):
    url = root_url + '/insert_data'
    for i in data:
        for item in i['data']['data']:
            new_data = {
                "id": item['id'],
                "name": item['name'],
                "image": "https://cdn11.dienmaycholon.vn/filewebdmclnew/DMCL21/Picture//Apro/Apro_product_" + item['id'] + "/" + item['picture'] + ".png.webp",
                "saleprice": item['saleprice'],
                "discount": item['discount']
            }
            response = requests.post(url, json=new_data)
            if response.status_code == 200:
                print("Data inserted successfully!")
            else:
                print("Failed to insert data:", response.text)

# def getApi():
#     url = root_url + '/get_all_data'
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         for item in data:
#             print(item)
#     else:
#         print("Failed to get data:", response.text)

def crawl(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        return None
    
# getApi()
def main():
    ids = [3, 8, 10, 13, 18, 24, 26]
    # ids = [3, 8, 10, 13, 18, 24, 26, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 42, 43, 48, 53, 55, 69, 70, 71, 72, 73, 74, 75, 76, 77, 80, 81, 82, 83, 85, 86, 87, 88, 89, 103, 109, 113, 114, 117, 118, 123, 126]
    data = []
    
    for id in ids:
        url = f"https://dienmaycholon.vn/api/product/cate?page=1&id={id}&offset=40"
        result = crawl(url)
        if result:
            data.append(result)
        else:
            print(f"Data for ID {id} could not be retrieved or was empty.")

    callApi(data)

if __name__ == "__main__":
    main()