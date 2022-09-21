def clean_word(word):
    if len(word) == 1:
        return word

    if word[0] == word[1]:
        return clean_word(word[1:])
    else:
        return word[0] + clean_word(word[1:])


n = int(input())
word = input()
my_list = list(clean_word(word))
print("YES" if my_list[0] == "S" and len(my_list) % 2 == 0 else "NO")
