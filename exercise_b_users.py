users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

twit_hand = users["Jonathan"]["twitter"]
print (twit_hand)

# 2. Get Erik's hometown

home_town = users["Erik"]["home_town"]
print(home_town)

# 3. Get the array of Erik's lottery numbers

lotto_num = users["Erik"]["lottery_numbers"]
print(lotto_num)

# 4. Get the species of Avril's pet Monty

pet_species = users["Avril"]["pets"][0]["species"]
print(pet_species)

# 5. Get the smallest of Erik's lottery numbers

smallest_num = users["Erik"]["lottery_numbers"][2]
print(smallest_num)

# 6. Return an array of Avril's lottery numbers that are even


# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers

users["Erik"]["lottery_numbers"].append(7)
print(users["Erik"]["lottery_numbers"])

# 8. Change Erik's hometown to Edinburgh

new_home = users["Erik"]["home_town"] = "Edinburgh"
print(new_home)

# 9. Add a pet dog to Erik called "Fluffy"

# new_pet_name = users["Erik"]["pets"]
#new_pet_species = users["Erik"]["pets"]["species"] = "dog"

print["Erik"]["pets"]

print(users["Erik"]["pets"])

# 10. Add another person to the users dictionary


