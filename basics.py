# Caesar Cipher walk through:
#
# Write a program that can encode and decode, using the Caesar Cipher method.
# https://en.wikipedia.org/wiki/Caesar_cipher

# Basically we encode a string by changing its position be a certain value
# and decode it by moving back by that value.

# For example: "my house" adjusted by 1, will be "nz ipvtf"

# Plan for the program:
# A: Encoding:
# 1. Convert the letters to numbers
# 2. Add a adjustment value to the number
# 3. Turn the number back into text.

# B: Decoding
# 1. Convert the letters to numbers
# 2. Minus a adjustment value to the number
# 3. Turn the number back into text.

text_to_be_encoded = "In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence."

# print(ord('a'))
# print(ord('n'))
# print(ord(' '))
# print(ord('c'))


def encoder(text_to_be_encoded, adjustment):

    encoded_numbers = []

    for character in text_to_be_encoded:
        # while testing/building explain the modulo quickly, with UTF-8 having 256 characters
        encoded_numbers.append((ord(character) + adjustment) % 256)

    encoded_text_list = []

    for number in encoded_numbers:
        encoded_text_list.append(chr(number))

    encoded_text = ''.join(encoded_text_list)

    return encoded_text


def decoder(text_to_decode, adjustment):
    adjustment = -adjustment
    return encoder(text_to_decode, adjustment)


encoded_text = "Jo!dszquphsbqiz-!b!Dbftbs!djqifs-!bmtp!lopxo!bt!Dbftbs(t!djqifs-!uif!tijgu!djqifs-!Dbftbs(t!dpef!ps!Dbftbs!tijgu-!jt!pof!pg!uif!tjnqmftu!boe!nptu!xjefmz!lopxo!fodszqujpo!ufdiojrvft/!Ju!jt!b!uzqf!pg!tvctujuvujpo!djqifs!jo!xijdi!fbdi!mfuufs!jo!uif!qmbjoufyu!jt!sfqmbdfe!cz!b!mfuufs!tpnf!gjyfe!ovncfs!pg!qptjujpot!epxo!uif!bmqibcfu/!Gps!fybnqmf-!xjui!b!mfgu!tijgu!pg!4-!E!xpvme!cf!sfqmbdfe!cz!B-!F!xpvme!cfdpnf!C-!boe!tp!po/!Uif!nfuipe!jt!obnfe!bgufs!Kvmjvt!Dbftbs-!xip!vtfe!ju!jo!ijt!qsjwbuf!dpssftqpoefodf/"
print(decoder(encoded_text, 1))

# letters = ["a", "b", "c", "d", "e", "f", "g"]
# adjusted_letters = []
# adjustment = 3
# for index in range(0, len(letters)):
#     adjusted_letters.append(letters[(index + adjustment) % len(letters)])

# print(adjusted_letters)
