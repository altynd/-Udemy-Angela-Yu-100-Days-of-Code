#
# def prime_cheker(number):
#     n=0
#     for i in range(2, number):
#         if number % i  ==0:
#             n=n+1
#     if n==0:
#         print("it is a prime number")
#     else:
#         print("it is not a prime number")
#
#
# n = int(input("Chek this number:"))
# prime_cheker(number=n)




alphabet = ["q","w","e","r","t","y","u","i","o",
            "p","a","s","d","f","g","h","j","k",
            "l","z","x","c","v","b","n","m",
            "q","w","e","r","t","y","u","i","o",
            "p","a","s","d","f","g","h","j","k",
            "l","z","x","c","v","b","n","m"]

char_time =""

while True:
    new_message = ""
    message = input("Type your message")
    code = input("decode or encode")
    key = int(input("Type key"))
    char_time = ""
    if code == "encode":
        for char in message:
            for char_alpha in range(len(alphabet)):
                if char == alphabet[char_alpha] and char != char_time:
                    char_time = char
                    new_char = alphabet[char_alpha+key]
                    new_message += new_char

    if code == "decode":
        for char in message:
            for char_alpha in range(len(alphabet)):
                if char == alphabet[char_alpha] and char != char_time:
                    char_time = char
                    new_char = alphabet[char_alpha-key]
                    new_message += new_char
    print(new_message)
