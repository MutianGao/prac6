class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __repr__(self):
        return f"{self.name}, {self.typing} Typing,Reflection={self.reflection},First appeared in {self.year}"

    def check_dynamic(self):
        return self.typing == "Dynamic"


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages = [ruby, python, visual_basic]
    print(python)
    print("The dynamically typed languages are:")
    for language in languages:
        if language.check_dynamic():
            print(language.name)


if __name__ == "__main__":
    main()
