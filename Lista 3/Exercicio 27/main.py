'''
27. Simule uma pilha usando append e pop. Mostre a pilha a cada opera¸c˜ao.
'''
import func

pilha = []

alternativa = func.mensagem_lista_vazia()

if alternativa == 1:
    item = func.adicionar()
    pilha.append(item)
    print
    print(f"PIlha: {pilha}")
elif alternativa == 2:
    if not pilha:
        print("Não há nada na pilha para remover!")
    else:
        print("item removido da pilha")
        pilha.pop()
        print()
        print(f"Pilha: {pilha}")
    
