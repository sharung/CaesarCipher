from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']


def ceasar(start, nama_revers, huruf):

    new_text = ""

    if start == "decode":
        huruf *= -1

    for latter in nama_revers:
        if latter in alphabet:
            position = alphabet.index(latter)
            new_latter = position + huruf
            new_text += alphabet[new_latter]
        else:
            new_text += latter

    print(new_text)

print(logo)

game = True
while game:

    direction = input("encode / decode ? ")
    text = input("text : ")
    shift = int(input("shift number : "))

# def encode(nama, huruf):
#     new_text = ""
#     for latter in nama:
#         position = alphabet.index(latter)
#         new_latter = position + huruf
#         # mengisi dengan index alphabet
#         new_text = new_text + alphabet[new_latter]
#     print(new_text)

# def decode(nama_revers, huruf):
#     new_text = ""
#     for latter in nama_revers:
#         position = alphabet.index(latter)
#         new_latter = position - huruf
#         new_text += alphabet[new_latter]
#     print(new_text)

# def ceasar(direction, nama_revers, huruf):
#     if direction == "encode":
#         encode(nama_revers, huruf)
#     elif direction == "decode":
#         decode(nama_revers, huruf)

    ceasar(start=direction, nama_revers=text, huruf=shift)

    text = input("You want try again? ").lower()

    if text == "yes":
        game = True
    elif text == "no":
        game = False
    else:
        game = False
        print("Wrong input")
