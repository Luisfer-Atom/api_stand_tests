import sender_stand_request
import data


# Prueba 1. Creación de un nuevo usuario o usuaria
# El parámetro "firstName" contiene dos caracteres

def test_create_user_2_letter_in_first_name_get_success_response():
    # La versión actualizada del cuerpo de solicitud que contiene el nombre "Aa" se guarda en la variable "user_body"
    user_body = get_user_body("Aa")
    # El resultado de la solicitud relevante se guarda en la variable "user_response"
    user_response = sender_stand_request.post_new_user(user_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != ""

    # El resultado de la solicitud de recepción de datos de la tabla "user_model" se guarda en la variable "users_table_response"
    users_table_response = sender_stand_request.get_users_table()
    # El string que debe estar en el cuerpo de la respuesta para recibir datos de la tabla "users" se ve así
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    # Comprueba si el usuario o usuaria existe y es único/a
    assert users_table_response.text.count(str_user) == 1

    # Función de prueba positiva
    def positive_assert(first_name):
        # El cuerpo de la solicitud actualizada se guarda en la variable user_body
        user_body = get_user_body(first_name)
        # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable user_response
        user_response = sender_stand_request.post_new_user(user_body)

        # Comprueba si el código de estado es 201
        assert user_response.status_code == 201
        # Comprueba que el campo authToken está en la respuesta y contiene un valor
        assert user_response.json()["authToken"] != ""

        # El resultado de la solicitud de recepción de datos de la tabla "user_model" se guarda en la variable "users_table_response"
        users_table_response = sender_stand_request.get_users_table()

        # String que debe estar en el cuerpo de respuesta
        str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
                   + user_body["address"] + ",,," + user_response.json()["authToken"]

        # Comprueba si el usuario o usuaria existe y es único/a
        assert users_table_response.text.count(str_user) == 1

    # Prueba 1. Creación de un nuevo usuario o usuaria
    # El parámetro "firstName" contiene dos caracteres
    def test_create_user_2_letter_in_first_name_get_success_response():
        positive_assert("Aa")



