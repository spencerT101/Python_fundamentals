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

lowest_lotto = sorted(users["Erik"]["lottery_numbers"])[0]
print(lowest_lotto)

# - SORTED function sorts data numerically or alphabetically.
# - lotto numbers will be in numerical order 
#  - index of [0] is added out side of brackets to get first number in list.

# 6. Return an array of Avril's lottery numbers that are even

lottery_numbers = users["Erik"]["lottery_numbers"] #variable 
even_numbers = []                                  # create list
for number in lottery_numbers:                     # create & define FOR loop to go through lottery_numbers list.
  if number % 2 == 0:                              # if statement to extract even numbers
     even_numbers.append(number)             # append even (number) to list

print(even_numbers)
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers

users["Erik"]["lottery_numbers"].append(7)

lotto_append = users["Erik"]["lottery_numbers"]

print(lotto_append)

# 8. Change Erik's hometown to Edinburgh

new_home = users["Erik"]["home_town"] = "Edinburgh"
print(new_home)

# 9. Add a pet dog to Erik called "Fluffy"

# use {} to append to dictionary.

users["Erik"]["pets"].append({"name": "Fluffy","species": "dog"})

new_pet_name = users["Erik"]["pets"][4]

print(new_pet_name)



# 10. Add another person to the users dictionary

# write new object with KEY to add to dictionary.

users["Craig"]= {
    "twitter": "craigster",
    "lottery_numbers": [9, 33, 6, 40, 22, 18],
    "home_town": "Royston",
    "pets": [
      {
        "name": "Guiness",
        "species": "dog"
      }
    ]
}


print(users["Craig"])
