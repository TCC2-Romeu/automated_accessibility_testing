class AcessibilityException:
    def __init__(
        self,
        type_exception: str,
        code_fragment_error: str,
        error_message: str,
        line: int,
        column: int,
    ):
        self.type_exception = type_exception
        self.code_fragment_error = code_fragment_error
        self.error_message = error_message
        self.line = line
        self.column = column

    def __repr__(self):

        if self.line == "" and self.column == "":
            return "\n{}: {}\n{}\n".format(
                self.type_exception, self.error_message, self.code_fragment_error
            )
        else:
            return "\n{}: Line {} Column {}: {}\n{}\n".format(
                self.type_exception,
                self.line,
                self.column,
                self.error_message,
                self.code_fragment_error,
            )
