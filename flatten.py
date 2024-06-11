from test import validate

inputs = [{
        "name": "John",
        "age": 30,
        "address": {
          "street": "123 Main St",
          "city": "New York",
          "country": {
            "name": "USA",
            "code": "US"
          }
        },
        "hobbies": ["reading", "traveling"],
        "married": True
      },
      {
        "company": "Acme Inc.",
        "employees": [
          {
            "name": "Alice",
            "role": "Developer",
            "skills": ["JavaScript", "Python"]
          },
          {
            "name": "Bob",
            "role": "Manager",
            "team": {
              "name": "Engineering",
              "size": 10
            }
          }
        ],
        "location": {
          "city": "San Francisco",
          "country": "USA"
        }
      },
      {
        "products": [
          {
            "name": "iPhone",
            "price": 999.99,
            "specs": {
              "color": "Black",
              "storage": "128GB"
            }
          },
          {
            "name": "iPad",
            "price": 799.99,
            "specs": {
              "color": "Silver",
              "storage": "256GB"
            },
            "accessories": ["Apple Pencil", "Smart Keyboard"]
          }
        ],
        "customer": {
          "name": "Emily",
          "email": "emily@example.com"
        }
      }]

def format_preface(preface, value):
   if preface == "":
      return value
   else:
      return preface + "." + value

def flatten(input):
    result = dict({})
    def recurse(preface, obj):
       for x, y in obj.items():
          if (type(y) is list):
              for i, item in enumerate(y):
                if type(item) is dict:
                   recurse(format_preface(preface, x + "." + str(i)), item)
                else:
                   result[format_preface(preface, x + "." + str(i))] = item
          elif (type(y) is dict):
             recurse(format_preface(preface, x), y)
          else:
             result[format_preface(preface, x)] = y

    recurse("", input)
    return result



outputs = [{
        "name": "John",
        "age": 30,
        "address.street": "123 Main St",
        "address.city": "New York",
        "address.country.name": "USA",
        "address.country.code": "US",
        "hobbies.0": "reading",
        "hobbies.1": "traveling",
        "married": True
      },
      {
        "company": "Acme Inc.",
        "employees.0.name": "Alice",
        "employees.0.role": "Developer",
        "employees.0.skills.0": "JavaScript",
        "employees.0.skills.1": "Python",
        "employees.1.name": "Bob",
        "employees.1.role": "Manager",
        "employees.1.team.name": "Engineering",
        "employees.1.team.size": 10,
        "location.city": "San Francisco",
        "location.country": "USA"
      },
      {
        "products.0.name": "iPhone",
        "products.0.price": 999.99,
        "products.0.specs.color": "Black",
        "products.0.specs.storage": "128GB",
        "products.1.name": "iPad",
        "products.1.price": 799.99,
        "products.1.specs.color": "Silver",
        "products.1.specs.storage": "256GB",
        "products.1.accessories.0": "Apple Pencil",
        "products.1.accessories.1": "Smart Keyboard",
        "customer.name": "Emily",
        "customer.email": "emily@example.com"
      }]



validate(flatten, inputs, outputs)