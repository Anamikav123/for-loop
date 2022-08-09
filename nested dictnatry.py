nested_dictionary = {
    "one":
        {
            "name": "saji",
            "age": 30,
            "city": "new york"
        },
    "two":
        {"name": "sree",
         "age": 50,
         "city": "mzhd",
         },
    "three":
        {"name": "bobby",
         "age": 20,
         "city": "york",

         }
}
print(nested_dictionary)
print("---------------------------------------------")
print(nested_dictionary["three"]["name"])
print(nested_dictionary["two"]["name"])
print(nested_dictionary["one"]["age"])

