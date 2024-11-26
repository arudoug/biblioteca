# Trabalho Prático de POO em Python
# Vence 2 de dezembro de 2024 às 23:59
# Instruções
# Objetivo do Trabalho

# O objetivo deste trabalho é aplicar os quatro pilares da Programação Orientada a Objetos (Encapsulamento, Abstração, Herança e Polimorfismo) no desenvolvimento de um sistema para gerenciamento de uma biblioteca virtual. Esse sistema deverá permitir o cadastro de livros, usuários e realizar operações como empréstimos e devoluções de livros.

# Descrição do Cenário
# Você foi contratado para desenvolver o sistema de uma biblioteca virtual que possui as seguintes funcionalidades:

# Gerenciar o cadastro de livros (título, autor, ano de publicação, status de disponibilidade).
# Gerenciar o cadastro de usuários (nome, idade, número de matrícula).
# Realizar operações de empréstimos e devoluções.
# Exibir relatórios simples, como:
# Livros disponíveis.
# Usuários que possuem livros emprestados.
# Este sistema será dividido em classes, respeitando os conceitos de POO.
# Dicas para o Desenvolvimento:
# Planejamento:

# Identifique as classes: Pessoa, UsuarioComum, Administrador, ItemBiblioteca, Livro.
# Aplique os 4 pilares da POO: Encapsulamento, Abstração, Herança, e Polimorfismo.
# Criação das Classes:

# Classe base Pessoa (abstrata): métodos e atributos gerais.
# Subclasses UsuarioComum e Administrador: comportamentos específicos (como empréstimos e cadastro de livros).
# Classe base ItemBiblioteca (abstrata): atributos de itens como titulo, autor.
# Subclasse Livro: implemente métodos específicos.
# Funcionalidades:

# Cadastro de livros e usuários.
# Controle de empréstimos (máximo de 3 livros por usuário).
# Relatórios: livros disponíveis e usuários com livros emprestados.
# Entrega:

# Suba o código no GitHub e envie o link.
# Deixe o projeto publico no GitHub.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) < 3 and livro.disponivel:
            self.livros_emprestados.append(livro)
            livro.disponivel = False

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.disponivel = True


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_livros_disponiveis(self):
        for livro in self.livros:
            if livro.disponivel:
                print(f'{livro.titulo} - {livro.autor}')

    def listar_usuarios_com_livros(self):
        for usuario in self.usuarios:
            if usuario.livros_emprestados:
                livros = ", ".join([livro.titulo for livro in usuario.livros_emprestados])
                print(f'{usuario.nome} ({usuario.matricula}): {livros}')
                
                
    
biblioteca = Biblioteca()


livro1 = Livro("1984", "George Orwell")
livro2 = Livro("Dom Quixote", "Miguel de Cervantes")
livro3 = Livro("A Revolução dos Bichos", "George Orwell")
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)


usuario1 = UsuarioComum("João", 25, "12345")
usuario2 = UsuarioComum("Maria", 30, "67890")
biblioteca.cadastrar_usuario(usuario1)
biblioteca.cadastrar_usuario(usuario2)


usuario1.emprestar_livro(livro1)
usuario2.emprestar_livro(livro2)


print("\nLivros disponíveis:")
biblioteca.listar_livros_disponiveis()

print("\nUsuários com livros emprestados:")
biblioteca.listar_usuarios_com_livros()


usuario1.devolver_livro(livro1)


print("\nLivros disponíveis após devolução:")
biblioteca.listar_livros_disponiveis()

print("\nUsuários com livros emprestados após devolução:")
biblioteca.listar_usuarios_com_livros()

