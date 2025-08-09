#Praticando Métodos de Classe e Estático
class Usuario:
    contador = 0

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        Usuario.contador += 1
    
    @classmethod
    def contador_usuarios(cls):
        return cls.contador
    
    @classmethod
    def criar_a_partir_de_string(cls, texto):
        nome, email = texto.split(",")
        return cls(nome.strip(), email.strip())
    
    def validar_email(self):
        return "@" in self.email

user1 = Usuario("Alessandra", "alessandra@gmail.com")
print(user1.nome, user1.email)
print(user1.validar_email())
user2 = Usuario.criar_a_partir_de_string("Rayane, rayanegmail.com")
print(user2.nome, user2.email)
print(user2.validar_email())