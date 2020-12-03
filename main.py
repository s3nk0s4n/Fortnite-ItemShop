import requests


items_type = ['daily', 'featured', 'specialFeatured']
items_type_n = ['Daily:', 'Featured:', 'Special:']
bundle_type = ['image', 'name']
request = requests.get('https://fortnite-api.com/v2/shop/br').json()

for i in range(3):
    entries_v = len(request['data'][items_type[i]]['entries'])
    print(items_type_n[i], end='\n----------\n')
    for i_1 in range(entries_v):
        items_v = len(request['data'][items_type[i]]['entries'][i_1]['items'])
        try:
            for i_4 in range(2):
                print(bundle_type[i_4] + ':', request['data'][items_type[i]]['entries'][i_1]['bundle'][bundle_type[i_4]])
        except:
            for i_4 in range(2):
                print(bundle_type[i_4] + ': None')
        for i_2 in range(items_v):
            print(str(i_2) + ':', request['data'][items_type[i]]['entries'][i_1]['items'][i_2]['name'])
            print('rarity:', request['data'][items_type[i]]['entries'][i_1]['items'][i_2]['rarity']['displayValue'])
            try:
                print('showcase:', 'https://www.youtube.com/embed/' + request['data'][items_type[i]]['entries'][i_1]['items'][i_2]['showcaseVideo'])
            except:
                print('showcase: None')
            print('icon:', request['data'][items_type[i]]['entries'][i_1]['items'][i_2]['images']['icon'])
        print('price:', request['data'][items_type[i]]['entries'][i_1]['finalPrice'])
        print()

input()