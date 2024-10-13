Data = [
    {"Name": "Naruto", "size": 1000, "Rating":"Grade A"},
    {"Name": "Bleach", "size": 500, "Rating":"Grade C"},
    {"Name": "Hunter x Hunter", "size": 2000, "Rating":"Grade A+"}
]

extracted_data = {item['Name']: item['size'] for item in Data}

print(extracted_data)