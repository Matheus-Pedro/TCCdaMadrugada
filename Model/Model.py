class Usuario:
    def __init__(self, cod_usuario, nome, email, senha):
        self.cod_usuario = cod_usuario
        self.nome = nome
        self.email = email
        self.senha = senha

    def __str__(self):
        return f'Código = {self.cod_usuario}\nNome: {self.nome}\nEmail = {self.email}\nSenha = {self.senha}'


class Universidade:
    def __init__(self, cod_universidade, nome, descricao, localizacao):
        self.cod_universidade = cod_universidade
        self.nome = nome
        self.descricao = descricao
        self.localizacao = localizacao

    def __str__(self):
        return f'Código = {self.cod_universidade}\nNome = {self.nome}\nDescrição = {self.descricao}\nLocalização = {self.localizacao}'


class Imagens_Universidade:
    def __init__(self, cod_imagem, dados_imagem, cod_universidade):
        self.cod_imagem = cod_imagem
        self.dados_imagem = dados_imagem
        self.cod_universidade = cod_universidade