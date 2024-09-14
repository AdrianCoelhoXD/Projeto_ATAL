from datetime import datetime

# Classe para os nós da lista ligada
class Node:
    def __init__(self, livro):
        self.livro = livro
        self.next = None  # Referência para o próximo nó

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Data de Publicação: {self.ano_publicacao}"

class Biblioteca:
    def __init__(self):
        self.head = None  # Cabeça da lista (primeiro nó)

    # Adicionar livro na lista ligada (no final)
    def adicionar_livro(self, livro):
        novo_node = Node(livro)
        if self.head is None:
            self.head = novo_node  # A lista estava vazia, agora o novo livro é o primeiro
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = novo_node  # Adiciona o livro no final da lista
        print(f"Livro '{livro.titulo}' adicionado com sucesso!")

    # Remover livro da lista ligada por título
    def remover_livro(self, titulo):
        current = self.head
        previous = None
        while current:
            if current.livro.titulo.lower() == titulo.lower():
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                print(f"Livro '{titulo}' removido com sucesso!")
                return
            previous = current
            current = current.next
        print(f"Livro '{titulo}' não encontrado no acervo.")

    # Listar todos os livros da lista ligada
    def listar_livros(self):
        if self.head is None:
            print("Nenhum livro no acervo.")
        else:
            current = self.head
            while current:
                print(current.livro)  # O método __str__ da classe Livro será chamado aqui
                current = current.next

    # Ordenar por título (usando Bubble Sort na lista ligada)
    def ordenar_por_titulo(self):
        if self.head is None:
            print("Nenhum livro para ordenar.")
            return
        
        trocado = True
        while trocado:
            trocado = False
            current = self.head
            while current.next:
                if current.livro.titulo > current.next.livro.titulo:
                    # Usar temp_livro para trocar os valores
                    temp_livro = current.livro
                    current.livro = current.next.livro
                    current.next.livro = temp_livro
                    trocado = True
                current = current.next

    # Ordenar por autor (usando Bubble Sort na lista ligada)
    def ordenar_por_autor(self):
        if self.head is None:
            print("Nenhum livro para ordenar.")
            return

        trocado = True
        while trocado:
            trocado = False
            current = self.head
            while current.next:
                if current.livro.autor > current.next.livro.autor:
                    temp_livro = current.livro
                    current.livro = current.next.livro
                    current.next.livro = temp_livro
                    trocado = True
                current = current.next
        print("Acervo ordenado por autor.")

    # Buscar livro por título
    def buscar_por_titulo(self, titulo):
        current = self.head
        while current:
            if current.livro.titulo.lower() == titulo.lower():
                return current.livro
            current = current.next
        return None

# Interface de linha de comando para testar as funcionalidades
def interface():
    biblioteca = Biblioteca()
    while True:
        print("\nOpções:")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Ordenar por Título")
        print("4. Ordenar por Autor")
        print("5. Buscar por Título")
        print("6. Remover Livro")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            data_publicacao = input("Data de Publicação (DD/MM/AAAA): ")
            biblioteca.adicionar_livro(Livro(titulo, autor, data_publicacao))

        elif opcao == '2':
            biblioteca.listar_livros()

        elif opcao == '3':
            biblioteca.ordenar_por_titulo()

        elif opcao == '4':
            biblioteca.ordenar_por_autor()

        elif opcao == '5':
            titulo = input("Digite o título do livro: ")
            livro = biblioteca.buscar_por_titulo(titulo)
            if livro:
                print(f"Livro encontrado: {livro}")
            else:
                print("Livro não encontrado.")

        elif opcao == '6':
            titulo = input("Digite o título do livro a ser removido: ")
            biblioteca.remover_livro(titulo)

        elif opcao == '7':
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    interface()