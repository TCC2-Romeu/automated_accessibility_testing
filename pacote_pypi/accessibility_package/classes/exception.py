
class AcessibilityException:
     
    # numero de linha
    # trocar a nomenclatura fragmento do html onde apareceu o erro
    # error message
    def __init__(self, code_fragment_error: str, error_message: str):
        self.code_fragment_error = code_fragment_error
        self.error_message = error_message

    def __str__(self):
        # retornar uma string
        # caso eu de print no error printar o erro e a mensagem
        pass
    

 
    
    # retirar os metodos, o python não precisa de get/set 
