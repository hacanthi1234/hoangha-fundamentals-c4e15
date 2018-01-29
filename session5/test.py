# person = ["tuan anh", 22, 2, "Hanoi", "Moc chau", 5, 4, 'Maria', "Ping Pong"]


#
# person = {}
# print(person)
#
# person = {
#     #key : value
#     "name": "Tuan Anh"
# }
#
# print(person)

person = {
    "name": "Tuan Anh",
    "age": 22,
    "sex": "male"
}

for key in person:
    print(key, person[key])#nó chỉ quan tâm đến key

person["projects"] = 5 #auto thêm code

# print( person["age"] )

# if "age" in persons:
#     print( person["age"] )
