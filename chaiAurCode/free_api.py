import requests

def fetch_random_freeapi():
    print("Please wait......")
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    data = response.json()

    if data:
        for val in data:
            print(f"userId: {val['id']}")
            print(f"username: {val['username']}")
            print(f"name: {val['name']}")
            print(f"phone: {val['phone']}")
            print(f"address: {val['address']['city']}")
            print("*"*50)
    else:
        raise Exception("Faild to fetch")
    # print(data)

fetch_random_freeapi()