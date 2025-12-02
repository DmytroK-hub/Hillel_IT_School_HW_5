import string

text = input("Введіть рядок: ")

def make_hashtag(text):
    clean = ""
    for ch in text:
        if ch not in string.punctuation:
            clean += ch

    words = clean.split()
    result = "#" + "".join(word.capitalize() for word in words)

    if len(result) > 140:
        result = result[:140]

    return result

print(make_hashtag(text))
