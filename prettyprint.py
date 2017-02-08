def pretty_print(dictionary, indent):
    for key in dictionary:
        if isinstance(dictionary[key], dict):
            print(indent, key, ": ")
            pretty_print(dictionary[key], indent + indent)
        else:
            print(indent, key, ": ", dictionary[key])


o1 = {
        "a": 1,
        "b": 2
     }
o2 = {
        "a": 1,
        "b": 2,
        "c": {
                "name": "Bruce Wayne",
                "occupation": "Hero"
            },
        "d": 4
    }
o3 = {
        "a": 1,
        "b": 2,
        "c":{
            "name": "Bruce Wayne",
             "occupation": "Hero",
              "friends": {
                            "spiderman": {
                                            "name": "Peter Parker"
                                        },
                            "superman": {
                                            "name": "Clark Kent"
                                        }
                        }
            },
        "d": 4
    }

indent = "  "

print("o1 pretty print")
pretty_print(o1, indent)
print()

print("o2 pretty print")
pretty_print(o2, indent)
print()

print("o3 pretty print")
pretty_print(o3, indent)
print()
