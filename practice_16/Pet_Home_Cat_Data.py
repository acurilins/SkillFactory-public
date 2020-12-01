import urllib.request, json

with urllib.request.urlopen\
        (
        "http://130.193.37.179/api/pet/?page=1&page_size=6&species__name=%D0%BA%D0%BE%D1%88%D0%BA%D0%B0"
        ) as url:
    data = json.loads(url.read().decode())
    # print(data)
    print(data.get('results'))
