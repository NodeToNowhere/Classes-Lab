class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort

    def talk(self):
        return str("I can talk!")

    def say_favourite_language(self, language):  # favorite... damn you america
        return str("I love " + language)

    # remember indents of methods!!
