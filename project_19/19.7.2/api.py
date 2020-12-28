import json
import requests

from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends1.herokuapp.com/"

    def post_new_pet_simple(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
        """Method posts new pet data on the server (except photo), returns request status and added data results"""

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def get_api_key(self, email: str, password: str) -> json:
        """Method requests API authentication key with valid data provided"""

        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_all_pets(self, auth_key: json, filter: str = "") -> json:
        """Method sends requests and returns list of filtered pets in JSON. Currently there are two filters
        available: 'my_pets' - to get the list of own listed pets, or '' - to get the list of all users pets"""

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_new_pet(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo: str) -> json:
        """Method posts new pet data on the server, returns request status and added data results"""

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def post_photo_of_own_pet(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
        """Method uploads the photo of the existing pet"""

        headers = {'auth_key': auth_key['key']}
        data = MultipartEncoder(
            fields={'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'images/jpeg')}
        )

        res = requests.post(self.base_url + '/api/pets/set_photo/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def delete_pet(self, auth_key: json, pet_id: str) -> json:
        """Method sends request to delete pet as per the given ID, returns status request and result in JSON.
        Currently there is a bug, the result is empty, although the status is 200"""

        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def put_pet_info(self, auth_key: json, pet_id: str, name: str,
                        animal_type: str, age: int) -> json:
        """Method sends requests to update pet data as per the given ID, returns  request status and result
        in JSON with updated pet data"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
