class Person:
    def __init__(self, name, surname, sentence):
        self.__name = name
        self.__surname = surname
        self.__sentence = sentence

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_sentence(self):
        return self.__sentence

    def set_sentence(self, sentence):
        self.__sentence = sentence

