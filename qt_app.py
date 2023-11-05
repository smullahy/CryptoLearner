import sys
from PySide6 import QtCore, QtWidgets, QtGui

import Encoding_scheme
from Encoding_scheme import *


if __name__ == "__main__":
    global encrypted_msg
    global encode
    app = QtWidgets.QApplication(sys.argv)
    welcome_page = QtWidgets.QWidget()
    welcome_page.setWindowTitle('Cryptography App')
    welcome_page.setStyleSheet('background-color: lightblue;')
    welcome_page.setGeometry(100, 100, 400, 200)
    welcome_layout = QtWidgets.QVBoxLayout()

    instruction_page = QtWidgets.QWidget()
    instruction_page.setWindowTitle('Cryptography App')
    instruction_page.setStyleSheet('background-color: lightblue;')
    instruction_page.setGeometry(100, 100, 400, 200)
    instruction_layout = QtWidgets.QVBoxLayout()

    sender_page = QtWidgets.QWidget()
    sender_page.setWindowTitle('Cryptography App')
    sender_page.setStyleSheet('background-color: lightblue;')
    sender_page.setGeometry(100, 100, 400, 200)
    sender_layout = QtWidgets.QVBoxLayout()

    receiver_page = QtWidgets.QWidget()
    receiver_page.setWindowTitle('Cryptography App')
    receiver_page.setStyleSheet('background-color: lightblue;')
    receiver_page.setGeometry(100, 100, 400, 200)
    receiver_layout = QtWidgets.QVBoxLayout()

    header_font = QtGui.QFont()
    header_font.setFamily('Times New Roman')
    header_font.setPointSize(48)
    header_font.setWeight(QtGui.QFont.Bold)

    body_font = QtGui.QFont()
    body_font.setFamily('Times New Roman')
    body_font.setPointSize(24)

    welcome_title = QtWidgets.QLabel('Here is the Welcome Page!', welcome_page)
    welcome_layout.addWidget(welcome_title)
    welcome_title.setFont(header_font)
    welcome_title.setAlignment(QtCore.Qt.AlignCenter)

    getting_started_button = QtWidgets.QPushButton('Click me to get started!', welcome_page)
    welcome_layout.addWidget(getting_started_button)
    welcome_page.setLayout(welcome_layout)

    instruction_title = QtWidgets.QLabel('How the App Functions:', instruction_page)
    instruction_title.setAlignment(QtCore.Qt.AlignCenter)
    instruction_title.setFont(header_font)
    instruction1 = QtWidgets.QLabel('You and a friend Bob use the Diffe-Hellman key exchance to share a secret key x.', instruction_page)
    instruction1.setFont(body_font)
    instruction2 = QtWidgets.QLabel('Using this secret key, you can encrpyt a secret message to send to Bob!', instruction_page)
    instruction2.setFont(body_font)
    instruction3 = QtWidgets.QLabel('Enter the message that you would like to send to bob below:', instruction_page)
    instruction3.setFont(body_font)
    # label2.move(150,50)
    # instruction_text_edit = QtWidgets.QTextEdit(window2)
    # label2.setAlignment(QtCore.Qt.AlignCenter)

    instruction_layout.addWidget(instruction_title)
    instruction_layout.addWidget(instruction1)
    instruction_layout.addWidget(instruction2)
    instruction_layout.addWidget(instruction3)

    user_input_line_edit = QtWidgets.QLineEdit(instruction_page)
    instruction_layout.addWidget(user_input_line_edit)
    process_button = QtWidgets.QPushButton('Dive into Cryptology', instruction_page)
    instruction_layout.addWidget(process_button)



    def on_getting_started_click():
        welcome_page.hide()
        instruction_page.show()

    def on_process_click():
        global encrypted_msg
        global encode
        instruction_page.hide()
        sender_title = QtWidgets.QLabel('Message Encryption:')
        sender_title.setAlignment(QtCore.Qt.AlignCenter)
        sender_title.setFont(header_font)
        sender_layout.addWidget(sender_title)
        msg_label = QtWidgets.QLabel(' ', sender_page)
        sender_layout.addWidget(msg_label)

        user_input = user_input_line_edit.text()
        msg_label.setText(f'You entered: {user_input}')
        msg_label.setFont(body_font)
        print(f'User entered: {user_input}')
        encode = Encoding_scheme.EncodingScheme()

        ascii_text = encode.convert_to_ascii(str(user_input))
        explanation1 = QtWidgets.QLabel(f'Step 1: We convert the user input to ASCII value.', sender_page)
        explanation1.setFont(body_font)

        explanation2 = QtWidgets.QLabel(f'Converted ASCII Value: {ascii_text}', sender_page)
        explanation2.setFont(body_font)

        explanation3 = QtWidgets.QLabel(f'Step 2: We convert the ASCII values to our cipher text using Elgamal. Elgamal '
                                        f'is an asymmetric encryption technique that uses different keys for the'
                                        f' encryption and decryption, exploiting the difficulty of solving discrete '
                                        f'logarithms to ensure secure communication.', sender_page)
        explanation3.setFont(body_font)
        explanation3.setWordWrap(True)
        encrypted_msg = encode.encrypt_el_gamal(ascii_text)
        encrypted = QtWidgets.QLabel(f'Cipher Text: {encrypted_msg}', sender_page)
        print(f'Encrypted Message: {encrypted_msg}')
        encrypted.setFont(body_font)
        encrypted.setWordWrap(True)


        sender_layout.addWidget(explanation1)
        sender_layout.addWidget(explanation2)
        sender_layout.addWidget(explanation3)
        sender_layout.addWidget(encrypted)

        receiver_button = QtWidgets.QPushButton("Move to Receiver's Side", sender_page)
        receiver_button.clicked.connect(on_receiver_click)
        sender_layout.addWidget(receiver_button)
        sender_page.setLayout(sender_layout)
        sender_page.show()

    def on_receiver_click():
        global encrypted_msg
        sender_page.hide()
        receiver_page.show()
        receiver_title = QtWidgets.QLabel('Message Decryption:')
        receiver_title.setAlignment(QtCore.Qt.AlignCenter)
        receiver_title.setFont(header_font)
        receiver_layout.addWidget(receiver_title)
        print("Bob received this:", encrypted_msg)
        explanation4 = QtWidgets.QLabel('This is the cipher text that bob received:', receiver_page)
        explanation4.setFont(body_font)
        explanation4.setWordWrap(True)
        receiver_layout.addWidget(explanation4)
        explanation5 = QtWidgets.QLabel(str(encrypted_msg), receiver_page)
        explanation5.setFont(body_font)
        explanation5.setWordWrap(True)
        receiver_layout.addWidget(explanation5)
        explanation6 = QtWidgets.QLabel("Step 3: The cipher text is decrypted into ASCII", receiver_page)
        explanation6.setFont(body_font)
        explanation6.setWordWrap(True)
        receiver_layout.addWidget(explanation6)
        decrypt_ascii_text = encode.decrypt_el_gamal(encrypted_msg)
        explanation7 = QtWidgets.QLabel(f"Reconverted ASCII Text: {decrypt_ascii_text}", receiver_page)
        explanation7.setFont(body_font)
        explanation7.setWordWrap(True)
        receiver_layout.addWidget(explanation7)
        explanation8 = QtWidgets.QLabel("Step 4: The ASCII is converted back to human readable texts", receiver_page)
        explanation8.setFont(body_font)
        explanation8.setWordWrap(True)
        receiver_layout.addWidget(explanation8)
        regular_text = encode.convert_to_string(decrypt_ascii_text)
        explanation9 = QtWidgets.QLabel(f"Reconverted ASCII Text: {regular_text}", receiver_page)
        explanation9.setFont(body_font)
        explanation9.setWordWrap(True)
        receiver_layout.addWidget(explanation9)
        explanation10 = QtWidgets.QLabel("Bob knows that "
                                         "the message is genuine due to the attached digital signature. RSA digital"
                                         " signatues ensure authenticity through a provided verification key", receiver_page)
        explanation10.setFont(body_font)
        explanation10.setWordWrap(True)
        receiver_layout.addWidget(explanation10)
        goback_welcome_button = QtWidgets.QPushButton("Go Back to Welcome Page", receiver_page)
        goback_welcome_button.clicked.connect(on_goback_click)
        receiver_layout.addWidget(goback_welcome_button)
        receiver_page.setLayout(receiver_layout)

    def on_goback_click():
        receiver_page.hide()
        welcome_page.show()


    getting_started_button.clicked.connect(on_getting_started_click)
    process_button.clicked.connect(on_process_click)

    instruction_page.setLayout(instruction_layout)

    welcome_page.show()

    sys.exit(app.exec())
