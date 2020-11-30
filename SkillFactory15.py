# myFile = open('lb.txt')
# print(myFile.read())

# myFile = open('lb.txt')
# for line in myFile:
#     print(line)

# myFile = open('namefile.txt', 'w')
# myFile.write('tttt')
# print('itsjusr', file=myFile)
#
# with open('lb.txt') as myFile:
#     for line in myFile:
#         print(line)

# import json
#
# with open('json_test.json', encoding='utf8') as f:
#     strfile = f.read()
#     templates = json.loads(strfile)
#
# print(templates)
# print(type(templates))

# import json
#
# template = {
#
# 	"firstname":"Иван",
# 	"lastname":"Иванов",
# 	"isAlive":True,
# 	"age":32,
# 	"address":{
# 		"streetAddress":"Нейбута 32",
# 		"city":"Владивосток",
# 		"state":"",
# 		"postalcode":""
# 	},
# 	"phonenumbers":[
# 		{
# 			"type":"mob",
# 			"number":"050-5977840"
# 		},
# 		{
# 			"type":"office",
# 			"number":"06-5984600"
# 		}
# 	],
# 	"children":[
#
# 	],
# 	"spouse":None
# }
#
#
# with open('json_test.json', 'w', encoding='utf8') as f:
#     json.dump(template, f, ensure_ascii=False, indent=4)
#
# with open('json_test.json', encoding='utf8') as f:
#     print(f.read())


import json

with open('json_example_QAP.json', encoding='utf8') as f:
    templates = json.load(f)

def CheckInt(item):
    return isinstance(item, int)

def CheckStr(item):
    return isinstance(item, str)

def CheckBool(item):
    return isinstance(item, bool)

def CheckUrl(item):
    if isinstance(item,str):
        return item.startswith('http://') or item.startswith('https://')
    else:
        return False

def CheckStrValue(item, val):
    if isinstance(item, str):
        return item in val
    else:
        return False

def ErrorLog(item, value, string):
    Error.append({item: f'{value}, {string}'})

listOfItems = {'timestamp': 'int', 'item_price': 'int', 'referer': 'url', 'location': 'url',
               'item_url': 'url', 'remoteHost': 'str', 'partyID': 'str', 'sessionId': 'str', 'pageViewId': 'str',
               'item_Id': 'str', 'basket_price': 'str', 'userAgentName': 'str', 'eventType': 'val',
               'detectedDuplicate': 'bool', 'detectedCorruption': 'bool', 'firstInSession': 'bool'}

Error = []
for items in templates:
    for item in items:
        if item in listOfItems:
            if listOfItems[item] == 'int':
                if not CheckInt(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listOfItems[item]}')
            elif listOfItems[item] == 'str':
                if not CheckStr(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listOfItems[item]}')
            elif listOfItems[item] == 'bool':
                if not CheckBool(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listOfItems[item]}')
            elif listOfItems[item] == 'url':
                if not CheckUrl(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listOfItems[item]}')
            elif listOfItems[item] == 'val':
                if not CheckStrValue(items[item], ['itemBuyEvent', 'itemsViewEvent']):
                    ErrorLog(item, items[item], 'ожидали значение itemBuyEvent или itemViewEvent')
            else:
                ErrorLog(item, items[item], 'неожиданное значение')

if Error == []:
    print('Pass')
else:
    print('Fail')
    print(Error)

