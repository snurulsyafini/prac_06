"""CP1404/CP5632 Practical - ProgrammingLanguage class."""


class ProgrammingLanguage:
    """Display information about programming language"""

    def __init__(self, name, typing, reflection, year):
        """Create ProgrammingLanguage"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string format of ProgrammingLanguage"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        """Find out if typing is Dynamic/Static"""
        return self.typing == "Dynamic"

    # def test_run():
    #     """Conduct test on ProgrammingLanguage"""
    #     ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    #     python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    #     visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    #
    #     languages = [ruby, python, visual_basic]
    #     print(python)
    #
    #     print("The dynamically typed languages are:")
    #     for language in languages:
    #         if language.is_dynamic():
    #             print(language.name)

    # if __name__ == "__main__":
    #     test_run()
