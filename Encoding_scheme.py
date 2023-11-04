def convert_to_ascii(message):
    ascii_list = []
    for char in message:
        ascii_list.append(ord(char))
    return ascii_list


def convert_to_string(ascii_list):
    message = ""
    for int_char in ascii_list:
        message += chr(int_char)
    return message


def encrypt_el_gamel(message):
    pass