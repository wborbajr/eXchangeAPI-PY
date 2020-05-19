# from pymongo import MongoClient


# def mongoConnect():
#     conn = MongoClient("mongodb://localhost:27017/lab")
#     return conn


# conn = mongoConnect()

# items = conn.items

# for item in items:
#     print(f"Collection -> {item}")


from pymongo import MongoClient
from random import randint

# Step 1: Connect to MongoDB - Note: Change connection string as needed
MONGO_HOST = "127.0.0.1"
MONGO_PORT = "27017"
MONGO_DB = "lab"
MONGO_USER = "lab"
MONGO_PASS = "lab"

uri = "mongodb://{}:{}@{}:{}/{}".format(
    MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, MONGO_DB
)
conn = MongoClient(uri)
db = conn.lab

# Step 2: Create sample data
names = [
    "Kitchen",
    "Animal",
    "State",
    "Tastey",
    "Big",
    "City",
    "Fish",
    "Pizza",
    "Goat",
    "Salty",
    "Sandwich",
    "Lazy",
    "Fun",
]
company_type = ["LLC", "Inc", "Company", "Corporation"]
company_cuisine = [
    "Pizza",
    "Bar Food",
    "Fast Food",
    "Italian",
    "Mexican",
    "American",
    "Sushi Bar",
    "Vegetarian",
]
for x in range(1, 10000):
    business = {
        "name": names[randint(0, (len(names) - 1))]
        + " "
        + names[randint(0, (len(names) - 1))]
        + " "
        + company_type[randint(0, (len(company_type) - 1))],
        "rating": randint(1, 5),
        "cuisine": company_cuisine[randint(0, (len(company_cuisine) - 1))],
    }
    # Step 3: Insert business object directly into MongoDB via isnert_one
    result = db.reviews.insert_one(business)
    db.items.insert_one(business)
    # Step 4: Print to the console the ObjectID of the new document
    # print("Created {0} of 500 as {1}".format(x, result.inserted_id))
# Step 5: Tell us that you are done
print("finished creating 500 business reviews")
