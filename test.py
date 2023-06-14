def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"
    '''
    pass


message = "TIMHYZ_ANOE_O_NA_PDN_G_JOI__"
shift = 7
column_num = 0
index = 0
acc=""
    
for letter in message:
    if (index * shift) - ((len(message)-1) * column_num) < len(message):
        formula = (index * shift) - ((len(message)-1) * column_num)
        new_letter = message[formula]
        index+=1
        acc+=new_letter
    else:
        column_num +=1
        formula = (index * shift) - ((len(message)-1) * column_num)
        new_letter = message[formula]
        index+=1
        acc+=new_letter
        
print(acc)

    #in cipher, this was used to identify the nth letter that will replace the letter in the current index
    #how might we use the same formula (without changing it) so that we can revert the placement?
''' 
    what is happening: after using the formula, the current index is replaced by the letter in the nth position
    hence, the letter in the current index is actually the nth letter in the actual message
    so what I need to do is find a way to replace the nth letter with the letter in the current index
    but what happens to the letter in the current index? 
        current plan: RETAIN UNTIL CHANGED
    something about subtracting ???'''
