def get_words_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    chars = {}
    for char in text:
        chars[char.lower()] = chars.get(char.lower(), 0) + 1
    return chars


def get_sorted_char_count(chars_dict):
    return [
        {"char": char, "num": count}
        for char, count in sorted(
            chars_dict.items(), key=lambda item: item[1], reverse=True
        )
    ]
