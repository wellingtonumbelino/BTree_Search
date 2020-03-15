# definindo um nó
class Node:
    def __init__(self, key=None, right=None, left=None):
        self.key = key
        self.right = right
        self.left = left

    def __str__(self):
        return str(self.key)


class Tree:  # definindo uma ávore
    def __init__(self):
        self.root = Node()
        self.root = None

    def insert(self, value):  # inserindo valores na Btree
        new = Node(value, None, None)  # criando um novo nó
        if self.root == None:
            self.root = new
        else:  # se a raiz já existir
            treeRoot = self.root
            while True:
                previous = treeRoot  # anterior recebe o valor atual
                if value <= treeRoot.key:  # ir para a esquerda
                    treeRoot = treeRoot.left
                    if treeRoot == None:
                        previous.left = new  # criando um novo nó se esq for nulo
                        return
                # fim da condição para a esquerda
                else:  # ir para direita
                    treeRoot = treeRoot.right
                    if treeRoot == None:
                        previous.right = new  # criando um novo nó se dir for nulo
                        return
                # fim da condição para a direita

    def inOrder(self, treeRoot):  # printando em ordem
        if treeRoot == None:  # se root for nulo, retorne
            return
        self.inOrder(treeRoot.left)  # chama a recurssão para a esquerda
        print(treeRoot.key, end=" ")
        self.inOrder(treeRoot.right)  # chama a recurssão para a direita

    def preOrder(self, treeRoot):
        if treeRoot == None:  # se root for nulo, retorne
            return
        print(treeRoot.key, end=" ")
        self.preOrder(treeRoot.left)  # chama a recurssão para a esquerda
        self.preOrder(treeRoot.right)  # chama a recurssão para a direita

    def posOrder(self, treeRoot):
        if treeRoot == None:  # se root for nulo, retorne
            return
        self.posOrder(treeRoot.left)  # chama a recurssão para a esquerda
        self.posOrder(treeRoot.right)  # chama a recurssão para a direita
        print(treeRoot.key, end=" ")

    def walk(self):  # percorre a árvore printando os nós na recurssão
        print("\nExibindo em ordem: ", end="")
        self.inOrder(self.root)
        print("\nExibinto em pré-ordem: ", end="")
        self.preOrder(self.root)
        print("\nExibinto em pos-ordem: ", end="")
        self.posOrder(self.root)

    def find(self, key):
        if self.root == None:  # caso a arvore esteja vazia
            return None
        treeRoot = self.root  # inicia busca pela raiz
        while treeRoot.key != key:
            if treeRoot == None:
                return None
            if key < treeRoot.key:  # caminha para esquerda
                treeRoot = treeRoot.left
            else:  # caminha para direita
                treeRoot = treeRoot.right
        return treeRoot  # retorna a folha encontrada

    def nodeSuccessor(self, erase):
        fatherSuccessor = erase
        successor = erase
        treeRoot = erase.right  # vai para a subarvore a direita

        while treeRoot != None:
            fatherSuccessor = successor
            successor = treeRoot
            treeRoot = treeRoot.left  # caminha para a esquerda

        if successor != erase.right:
            fatherSuccessor.left = successor.right
        return successor

    def remove(self, value):
        if self.root == None:
            return False
        treeRoot = self.root
        father = self.root
        son_left = True  # assumo que existe um filho a esquerda
        # buscar o valor
        while treeRoot.key != value:
            father = treeRoot
            if treeRoot == None:
                return False
            if value < treeRoot.key:  # caminhando para esquerda
                treeRoot = treeRoot.left
                son_left = True  # se existir filho a esquerda
            else:  # caminhando para direita
                treeRoot = treeRoot.right
                son_left = False  # se não existir filho a esquerda
        # fim do while
        # se não possui nenhum filho é uma folha, eline-o
        if treeRoot.left == None and treeRoot.right == None:
            if treeRoot == self.root:
                self.root = None  # se for a raiz
            else:
                if son_left:
                    father.left = None  # se o filho a ser removido for esq
                else:
                    father.right = None  # se o filho a ser removido for dir
        elif treeRoot.right == None:  # se for pai e não possuir filho a dir
            if treeRoot == self.root:
                self.root = treeRoot.left
            else:
                if son_left:
                    father.left = treeRoot.left  # se for filho a esq de pai
                else:
                    father.right = treeRoot.left  # se for filho a dir de pai
        elif treeRoot.left == None:  # se for pai e não possuir filho a esq
            if treeRoot == self.root:
                self.root = treeRoot.right
            else:
                if son_left:
                    father.left = treeRoot.right  # se for filho a esq de pai
                else:
                    father.right = treeRoot.right  # se for filho a dir de pai
        else:
            successor = self.nodeSuccessor(treeRoot)
            if treeRoot == self.root:
                self.root = successor  # se for raiz
            else:
                if son_left:
                    father.left = successor  # se for filho a esq de pai
                else:
                    father.right = successor  # se for filho a dir de pai
                successor.left = treeRoot.left  # acertando o ponteiro a esquerda
        return True
#### fim da classe ####


btree = Tree()
print("Vamos brincar com Árvores :)")
print("- 1 - Inserir")
print("- 2 - Mostrar")
print("- 3 - Buscar um valor")
print("- 4 - Remover")
print("- 5 - Sair")

op = 0
while(True):
    op = int(input("\nDigite um valor para o menu: "))
    if op == 1:
        value = int(input("Digite um valor -> "))
        btree.insert(value)
    elif op == 2:
        btree.walk()
    elif op == 3:
        value = int(input("Digite um valor -> "))
        if btree.find(value) != None:
            print("\nAchei!")
        else:
            print("\nNenhum valor encontrado")
    elif op == 4:
        value = int(input("\nDigite um valor: "))
        if btree.remove(value):
            print("\nApaguei")
        else:
            print("\nNão achei :(")
    elif op == 5:
        break
