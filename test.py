def caesar_cipher(message, shift):
    '''Caesar Cipher.
    10 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    acc = ""
    for letter in message:
        if letter == " ":
            acc+=" "
        else:
            letter_num = ord(letter) - ord('A') + (shift % 26)
            if letter_num <= 26:
                new_word = chr(letter_num + ord('A'))
                acc += new_word
            else:
                new_word = chr(letter_num + ord('A') - (25 * shift//26))
                acc += new_word
    return(acc)

print(caesar_cipher("ABCDE HDJD", 1))