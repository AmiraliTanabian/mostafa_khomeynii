# dictinory 
# dict : json 
# first_user = { 
#     # Key    # Value
#    "name":"Ali" , 
#     "age" : 16, 
#     'id': 3655,
# }
# key : immutable
# value : all types
# print(first_user.keys())
# print(first_user.values())


# دیکشنری تو در تو 
info = {
    "name":"Amirali",
    "langs" : {
        "front": "js", 
        "backend":"python"
    }
}

# print(info["langs"]["front"])

print(dict.fromkeys(["name", "lname", "langs"]))