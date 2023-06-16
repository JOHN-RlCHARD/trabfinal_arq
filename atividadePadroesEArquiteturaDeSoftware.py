class Livro:
    def __init__(self, titulo: str, autor: str, ano_publicacao: int):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Biblioteca().adicionar_livro(self)

    def obter_titulo(self):
        return self.titulo

    def obter_autor(self):
        return self.autor

    def obter_ano_publicacao(self):
        return self.ano_publicacao

    def esta_disponivel(self):
        return self.disponivel

    def definir_disponibilidade(self, status: bool):
        self.disponivel = status


class Usuario:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email
        self.livros_emprestados = []
        Biblioteca().adicionar_usuario(self)

    def obter_nome(self):
        return self.nome

    def obter_email(self):
        return self.email
    
    def obter_livros_emprestados(self):
        return self.livros_emprestados

    def emprestar_livro(self, livro: Livro):
        self.livros_emprestados.append(livro)

    def devolver_livro(self, livro: Livro):
        self.livros_emprestados.remove(livro)


class Biblioteca:

    _instancia = None
    ## SUBSTITUICAO DO INIT PELO NEW, PARA SER USADA COMO SINGETON
    def __new__(cls):
        if not cls._instancia:
            cls._instancia = super(Biblioteca, cls).__new__(cls)
            cls._instancia.livros = []
            cls._instancia.usuarios = []
        return cls._instancia

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)
        print(f"Livro '{livro.obter_titulo()}' adicionado à biblioteca.")

    def remover_livro(self, livro: Livro):
        if livro in self.livros:
            self.livros.remove(livro)
            print(f"Livro '{livro.obter_titulo()}' removido da biblioteca.")
        else:
            print(f"Livro '{livro.obter_titulo()}' não está na biblioteca.")

    def buscar_livro(self, titulo: str):
        for livro in self.livros:
            if livro.obter_titulo() == titulo:
                return livro
        return None
    
    def emprestar_livro(self, livro: Livro, usuario: Usuario):
        if livro.esta_disponivel():
            livro.definir_disponibilidade(False)
            usuario.emprestar_livro(livro)
            print(f"Livro '{livro.obter_titulo()}' emprestado a '{usuario.obter_nome()}'")
        else:
            print(f"Livro '{livro.obter_titulo()} nao esta disponivel")

    def devolver_livro(self, livro: Livro, usuario: Usuario):
        if livro in usuario.obter_livros_emprestados():
            livro.definir_disponibilidade(True)
            usuario.devolver_livro(livro)
            print(f"Livro '{livro.obter_titulo()}' devolvido por '{usuario.obter_nome()}'")
            return
        print(f"Livro '{livro.obter_titulo()}' nao esta com '{usuario.obter_nome}'")

    def adicionar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)
        print(f"Usuário '{usuario.obter_nome()}' adicionado à biblioteca.")

    def remover_usuario(self, usuario: Usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
            print(f"Usuário '{usuario.obter_nome()}' removido da biblioteca.")
        else:
            print(f"Usuário '{usuario.obter_nome()}' não está registrado na biblioteca.")

    def buscar_usuario(self, nome: str):
        for usuario in self.usuarios:
            if usuario.obter_nome() == nome:
                return usuario
        return None


# Exemplo de uso do código:

# Criação da biblioteca
biblioteca = Biblioteca()

# Criação de alguns livros
livro1 = Livro("Python para Iniciantes", "John Smith", 2018)
livro2 = Livro("Python Avançado", "Jane Doe", 2020)

# Criação de usuários
usuario1 = Usuario("Alice", "alice@example.com")
usuario2 = Usuario("Bob", "bob@example.com")

# Empréstimo de livro
biblioteca.emprestar_livro(livro1, usuario1)

# Tentativa de empréstimo de livro indisponível
biblioteca.emprestar_livro(livro1, usuario2)

# Devolução de livro
biblioteca.devolver_livro(livro1, usuario1)

# Remoção de livro
biblioteca.remover_livro(livro2)

# Remoção de usuário
biblioteca.remover_usuario(usuario2)

# Busca de livro e usuário
livro_encontrado = biblioteca.buscar_livro("Python para Iniciantes")
usuario_encontrado = biblioteca.buscar_usuario("Alice")

# Exemplo de uso dos métodos de acesso
if livro_encontrado:
    print(livro_encontrado.obter_titulo())
if usuario_encontrado:
    print(usuario_encontrado.obter_nome())
