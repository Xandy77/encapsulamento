# classe 
class Pessoa:
    def __init__(self, nome, idade, email):
        self.__nome = nome  # public # nome, idade e email são atributos
        self.__idade = idade # protected
        self.__email = email # private: só consigo ter acesso na propria classe mas não na sub-classe

    # metodos de acesso
    '''def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade
    
    def set_idade(self, idade):
        self.__idade = idade

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email'''
    
    # método get nome
    @property
    def nome(self):
        return self.__nome
    
    # método set nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def nome(self, idade):
        self.__idade = idade

    @property
    def email(self):
        return self.__email
    
    @idade.setter
    def email(self, email):
        self.__email = email

    
    
