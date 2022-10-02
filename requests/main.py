import requests

data_petstore = {
  "id": 10,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

response = requests.post("https://petstore.swagger.io/v2/pet", json = data_petstore) #Add a new pet to the store
print(response.text)

data_petstore = {
  "id": 10,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "scooby_doo",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

response = requests.put("https://petstore.swagger.io/v2/pet", json = data_petstore) #Update an existing pet
print(response.text)


{
  "id": 10,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "scooby_doo",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response = requests.get("https://petstore.swagger.io/v2/pet/10", json = data_petstore) #Find Pet by ID
print(response.text)