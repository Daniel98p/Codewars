def clip_text(text, text_lenght):
    if len(text) < text_lenght:
        return text
    return text[:text_lenght]


def invert(text):
    return text[::-1]


if __name__ == '__main__':
    my_text_lenght = int(input('Podaj długość przycięcia tekstu: '))
    my_text = 'Ala ma kota'
    print(clip_text(my_text, my_text_lenght))
