##############################################################################
# Console Output
##############################################################################

class Console:
    """
    Class for formatting console output.
    """

    bold = "\033[1m"
    reset = "\033[0m"
    red = "\033[31m"

    def red_string(self, msg):
        """
        Formats the given string in red.
        """
        return self.red + msg + self.reset

    def bold_string(self, msg):
        """
        Formats the given string in bold.
        """
        return self.bold + msg + self.reset


if __name__ == "__main__":
    c = Console()
    print(c.red_string("This is red text."))
    print(c.bold_string("This is bold text."))
