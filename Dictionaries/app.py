#use dictionaries in situations where you have to store information in key value pairs
#name : 'Robbin'
#email: 'ronbbin.hood@email.com'

customer = {
    "name":'Robbin Hood',
    "age":30,
    "is_verified":True
}

print(customer["name"])
#print(customer["Something"]) this will give error as we dont have this something key in the dictionary hence use get method
print(customer.get("birthdate"))
print(customer.get("age"))
print(customer.get("birthdate","Jan 1 1980"))

customer["name"] = "Jack Smith"
print(customer["name"])

customer["is_graduate"] = True

print(customer)
