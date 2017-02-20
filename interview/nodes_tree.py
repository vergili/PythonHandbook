def parse_word(s):
    new_string = ""
    reverse_string = ""
    convert_to_uppercase = True

    for i in range(len(s)):
        if s[i].isspace():
            if i > 0:
                if not s[i - 1].isspace():
                    if not convert_to_uppercase:
                        new_string += reverse_string
                        reverse_string = ""
                    convert_to_uppercase = not convert_to_uppercase
            new_string += s[i]
        else:
             if convert_to_uppercase:
                 new_string += s[i].upper()
             else:
                 reverse_string = s[i] + reverse_string
    new_string += reverse_string
    return new_string


print(parse_word("This is a  test String!!"))


