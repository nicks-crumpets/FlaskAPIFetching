import requests

url = "https://api.themoviedb.org/3/account/22548726"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMmFjYTk3MWVjYzMwZWY4YTBjYzE0ZDhlMTg5NWFiOCIsIm5iZiI6MTc2NTU1MDA4OC4xMiwic3ViIjoiNjkzYzI4MDgxZTE2MTA4NDE0ZTBiYmMzIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.CcEUnUcjshDCQBLxbU4IkrFgcg6iZoewICpmat4q9dw"
}

response = requests.get(url, headers=headers)

print(response.text)