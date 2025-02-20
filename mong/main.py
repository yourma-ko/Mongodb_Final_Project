import requests
import json
url = "https://walmart-data.p.rapidapi.com/search"
headers = {
    "x-rapidapi-host": "walmart-data.p.rapidapi.com",
    "x-rapidapi-key": "14b2ba5617msh42ddf51b2e7ce18p1f1143jsnf3549a34559c"  
}
query_params = {
    "q": "laptop",
    "page": 3
}

try:
    response = requests.get(url, headers=headers, params=query_params)
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))
        filename = "search_results_laptop_page_1.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Search results successfully saved to '{filename}'")
    else:
        print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
        print("Response:", response.text)

except Exception as e:
    print(f"An error occurred: {e}")
