
class AcessibilityException:
     
    def __init__(self, tag_error: str, type_error: str):
        self.tag_error = tag_error
        self.type_error = type_error
      
    def display_tag_error(self):
        print(self.tag_error)

    def display_type_error(self):
        print(self.type_error)
    
    def set_type_error(self, type_error: str):
        self.type_error = type_error

    def set_tag_error(self, tag_error: str):
        self.tag_error = tag_error