class Email():
    def __init__(self, Nome, Email, server):
        self.Nome = nome
        self.Email = Email
        self.server = servidor
    def pegar_Servidor(self):
        print(f"Seu servidor é: {self.server}")

nome = "Felipe"

minha_conta = Email("Felipe", "Felipe@gmail.com", "@Gmail.com")

minha_conta.pegar_Servidor()