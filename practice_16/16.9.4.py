from PetsHome import Volunteer

vol1 = Volunteer("Иван Петров", "г.Москва", '"наставник"')
vol2 = Volunteer("Константин Багданов", "г.Москва", '"ассистент"')
vol3 = Volunteer("Евгений Федоров", "г.Екатеринбург", '"ветеринар"')

print(vol1.getName(), ",", vol1.getCity(), ",", "статус", vol1.getStatus())
print(vol2.getName(), ",", vol2.getCity(), ",", "статус", vol2.getStatus())
print(vol3.getName(), ",", vol3.getCity(), ",", "статус", vol3.getStatus())
