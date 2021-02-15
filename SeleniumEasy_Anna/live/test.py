def get_palindrome (string):
    last_ind = len(string)

    max_palindrome=""


    for i in range(0,len(string)+1):
        new_string_from_end=string[i:last_ind]
        rev_string=new_string_from_end[::-1]
        print('end', new_string_from_end)
        if new_string_from_end==rev_string and len(new_string_from_end)>len(max_palindrome):
            max_palindrome=new_string_from_end
        new_string_from_start=string[0:last_ind-i]
        rev_string_2 = new_string_from_start[::-1]
        print('start', new_string_from_start)
        if new_string_from_start == rev_string_2 and len(new_string_from_start)>len(max_palindrome):
            max_palindrome = new_string_from_start
    return (max_palindrome)


print(get_palindrome ('tet123'))