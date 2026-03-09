import json



# -------------------------------

# Task 1 — Build a JSON Structure

# -------------------------------



# Create Python dictionary

user_profile = {

  "name": "Reshma",

  "age": 23,

  "email": "reshma@example.com",

  "is_active": True,

  "skills": ["Python", "SQL", "JSON"]

}



# Convert to JSON string with indentation

json_data = json.dumps(user_profile, indent=4)



print("Task 1 Output:")

print(json_data)





# -------------------------------

# Task 2 — Parse an API Response

# -------------------------------



api_response = '{"status": "success", "data": {"user_id": 101, "username": "alex99", "score": 87.5}}'



# Convert JSON string to Python dictionary

parsed_data = json.loads(api_response)



username = parsed_data["data"]["username"]

score = parsed_data["data"]["score"]



print("\nTask 2 Output:")

print("Username:", username)

print("Score:", score)

print(f"User {username} scored {score} points")





# -------------------------------

# Task 3 — Handle Nested JSON

# -------------------------------



nested_json = '''

{

 "name": "Priya",

 "address": {

  "city": "Bengaluru",

  "state": "Karnataka",

  "zip": "560001"

 }

}

'''



# Convert JSON string to dictionary

user_data = json.loads(nested_json)



city = user_data["address"]["city"]

zip_code = user_data["address"]["zip"]



print("\nTask 3 Output:")

print("City:", city)

print("Zip Code:", zip_code)



# Add new key

user_data["address"]["country"] = "India"



# Convert back to JSON

updated_json = json.dumps(user_data, indent=4)



print("\nUpdated JSON:")

print(updated_json)