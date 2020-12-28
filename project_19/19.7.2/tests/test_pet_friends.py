from api import PetFriends
from settings import valid_email, valid_password
from settings import invalid_email, invalid_password, invalid_auth_key  # PEP 328 ;)))
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """Test to receive authentication key with valid e-mail and password"""
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    """Test to receive the list of all pets with valid data """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_all_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='плоскомордый', animal_type='собакин',
                                     age='2', pet_photo='images/pass.jpg'):
    """Test to add new pet with valid data"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    """Test to delete own pet"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_all_pets(auth_key, "my_pets")
    if len(my_pets['pets']) == 0:
        pf.post_new_pet(auth_key, "Суперкот", "кот", "3", "images/perfect_smile.jpg")
        _, my_pets = pf.get_list_of_all_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_all_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Афонасий', animal_type='Лемур', age=3):
    """Test to update own pet info"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_all_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.put_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There are no pets posted, yet")


"""19.7.2"""


# 1
def test_successful_delete_other_pet():
    """Test to delete someone's pet"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, all_pets = pf.get_list_of_all_pets(auth_key, "")
    pet_id = all_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    assert status == 200
    assert pet_id not in all_pets.values()


# 2
def test_successful_update_other_pet_info(name='Извиняйте', animal_type='Теста ради', age=33):
    """Test to update someone's pet info"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, all_pets = pf.get_list_of_all_pets(auth_key, "")
    status, result = pf.put_pet_info(auth_key, all_pets['pets'][0]['id'], name, animal_type, age)
    assert status == 200
    assert result['name'] == name


# 3
def test_add_new_pet_with_valid_data_and_age_in_words_simple(name='Ева', animal_type='Мопс',
                                     age='Девять'):
    """Test to add new pet with valid data and age written in letters instead of numbers"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name


# 4
def test_add_new_pet_with_valid_data_long_values(name='супердлинноеимя '*70, animal_type='собакин',
                                     age='2', pet_photo='images/pass.jpg'):
    """Test to add new pet with valid data and very long name"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


# 5
def test_add_new_pet_with_valid_data_empty_values_with_photo(name='', animal_type='',
                                     age='', pet_photo='images/perfect_smile.jpg'):
    """Test to add new pet with empty values, with photo"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


# 6
def test_add_new_pet_with_valid_data_empty_values_without_photo(name='', animal_type='',
                                     age='', pet_photo=''):
    """Test to add new pet with empty values, without photo"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


# 7
def test_add_new_pet_with_valid_data_photo_bmp(name='угрюмый', animal_type='котейка',
                                     age='2', pet_photo='images/cat_bmp.bmp'):
    """Test to add new pet with valid data and unacceptable photo file format - .bmp"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


# 8
def test_add_new_pet_with_valid_data_photo_gif(name='тест', animal_type='тест',
                                     age='2', pet_photo='images/cat.gif'):
    """Test to add new pet with valid data and unacceptable photo file format - .gif"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


# 9
def test_get_api_key_for_invalid_user(email=invalid_email, password=invalid_password):
    """Test to receive authentication key with invalid e-mail and password"""
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' in result


# 10
def test_get_all_pets_with_invalid_key(filter=''):
    """Test to receive the list of all pets with invalid data """

    auth_key = invalid_auth_key
    status, result = pf.get_list_of_all_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0