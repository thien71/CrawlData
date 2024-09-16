from django.shortcuts import render
from django.http import HttpResponse
import requests
import random

# Create your views here.
# def get_product_data(id):
#     url = f"https://dienmaycholon.vn/api/product/cate?page=1&id={id}&offset=40&"
#     headers = {
#         'User-Agent': 'My App/1.0',
#         'Accept': 'application/json',
#     }

#     try:
#         response = requests.get(url, headers=headers, timeout=10)
#         if response.status_code == 200:
#             data = response.json()
#         else:
#             data = None
#     except requests.exceptions.Timeout:
#         print("Request timed out")
#         data = None
#     except requests.exceptions.RequestException as e:
#         print("Error:", e)
#         data = None

#     return data

# def home(request):
#     product_ids = [3,8,13,18,24,26,32,39,42,69]
#     # product_ids = [3, 8, 10, 13, 18, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 42, 43, 48, 53, 55, 65, 69, 70, 71, 72, 73, 74, 75, 76, 77, 80, 81, 82, 83, 85, 86, 87, 88, 89, 103, 109, 113, 114, 117, 118, 123, 126]

#     data = [get_product_data(id) for id in product_ids]

#     context = {
#         'data': data
#     }

#     return render(request, 'app/home.html', context)



def crawl(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        return None
    
# getApi()
# def main(request):
#     if request.method == 'POST':
#         search_input = request.POST.get('searchInput', '')
#         if search_input:
#             url = f'http://localhost:7000/search/?search_input={search_input}'
#             products_data = crawl(url)
#         else:
#             url = 'http://localhost:7000/get_all_data'
#             products_data = crawl(url)

#         if products_data:
#             random.shuffle(products_data)
#             products_data = products_data[:40]
#         else:
#             products_data = []

#         products = [{
#             'id': item[0],
#             'name': item[1],
#             'image': item[2],
#             'saleprice': item[3],
#             'discount': item[4]
#         } for item in products_data]

#         context = {
#             'products': products
#         }
#         return render(request, 'app/home.html', context)

#     return render(request, 'app/home.html')


def main(request):
    products_data = []
    try:
        search_input = request.GET.get('searchInput', '')  # Lấy tham số tìm kiếm từ request
        print("Thiện"+ search_input)
        if search_input: 
            url = f'http://localhost:7777/search/?search_input={search_input}'
            products_data = crawl(url)
        else:
            url = 'http://localhost:7777/get_all_data'
            products_data = crawl(url)

            if products_data:
                random.shuffle(products_data)
                products_data = products_data[:40]
            else:
                products_data = []
    except requests.exceptions.RequestException as e:
        print(e) 
        products_data = []

    if not products_data:
        products_data = []


    products = [{
        'id': item[0],
        'name': item[1],
        'image': item[2],
        'saleprice': item[3],
        'discount': item[4]
    } for item in products_data]

    context = {
        'products': products,
        'searchInput': search_input
    }
    return render(request, 'app/home.html', context)



    # ids = [3, 8, 13, 18, 24, 26, 32, 39, 42, 69]
    # data = []
    
    # for id in ids:
    #     url = f"https://dienmaycholon.vn/api/product/cate?page=1&id={id}&offset=40"
    #     result = crawl(url)
    #     if result:
    #         data.append(result)
    #     else:
    #         print(f"Data for ID {id} could not be retrieved or was empty.")

    # # callApi(data)
    # print(data)
    # context = {
    #     'data': data
    # }
    # return render(request, 'app/home.html', context)
