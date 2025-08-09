class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw): #só precisa escrever o __init__ se quiser fazer algo a mais além do que Animal já faz
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw) #assim todo argumento novo será passado automaticamente
        self.cor_bico = cor_bico

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __str__(self):
        return "Ornitorrinco"

print(Ornitorrinco.mro())

gato = Gato(nro_patas=4,cor_pelo="branco")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="preto", cor_bico="roxo")
print(ornitorrinco)