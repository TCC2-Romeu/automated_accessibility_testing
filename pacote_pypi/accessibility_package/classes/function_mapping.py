
class FunctionMapping:
     
    def __init__(self, function_name: str, description: str, enable: bool):
        self.function_name = function_name
        self.description = description
        self.enable = enable
      
    def display_function_name(self):
        print(self.function_name)

    def display_function_description(self):
        print(self.description)

    def display_enable(self):
        print(self.enable)

    def get_function_name(self):
        return self.function_name

    def get_is_enable(self):
        return self.enable

    def set_function_name(self, function_name: str):
        self.function_name = function_name

    def set_function_description(self, description: str):
        self.description = description

    def set_enable(self, enable: bool):
        self.enable = enable

    