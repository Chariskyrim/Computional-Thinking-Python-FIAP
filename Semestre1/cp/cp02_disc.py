"""
Assuntos envolvidos:
• Estruturas de decisão
• Estruturas de Repetição
• Criação de Subalgoritmos: Função e procedimento
Requisitos:
• Desenvolva as telas das rotinas semelhantes às telas sugeridas.
• Desenvolva ao menos um subalgoritmos para resolver cada rotina.
• Caso seja utilizado algum recurso da linguagem que não foi apresentado perderá os pontos
da questão.
Checkpoint:
Considere um menu com as seguintes opções:
0 - SAIR
1 - Número intermediário
2 - Ordem crescente
3 - Tabuada
4 - Nota válida
Escolha: _

Se o usuário digitar valores diferentes dos existentes no menu, exibir a mensagem “Opção
inválida!” e voltará ao menu.
Este menu será executado até que a pessoa digite 0 (SAIR) para finalizar o programa.
Ao finalizar o programa, apresentar quantas vezes cada rotina foi executada e a sua
respectiva porcentagem.
A tela final deve ser colocada no else do laço e deverá ter a aparência:
Rotina 1 - 3 vezes - 30%
Rotina 2 - 2 vezes - 20%
Rotina 3 - 2 vezes - 20%
Rotina 4 - 3 vezes - 30%
Imagem 2 - Tela sugerida da apresentação final do programa
Seguem as características e o funcionamento de cada rotina:

Rotina 1:
O usuário digitará 3 valores floats no programa principal.
Crie uma função que receba 3 valores por parâmetro e retorne o de valor
intermediário (meio), por exemplo, se forem passados os números 5, 8, 2 o número
5 será o retornado para no programa principal ser exibido na tela:
Digite o 1.o número: 5
Digite o 2.o número: 8
Digite o 3.o número: 2
Número intermediário: 5
Caso dois ou mais números sejam repetidos, exibir o intermediário será um deles.

Rotina 2:
O usuário digitará 3 valores floats no programa principal.
Crie um procedimento que receba 3 valores por parâmetro e exiba-os em ordem
crescente:
Digite o 1.o número: 5
Digite o 2.o número: 8
Digite o 3.o número: 2
Ordem crescente: 2, 5 e 8

Rotina 3:
O usuário digitará um valor int no programa principal.
Crie um procedimento que receba um parâmetro referente ao número da tabuada e
exiba a tabuada o formato do Ensino Fundamental:
Digite a tabuada: 3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
Independentemente da tabuada, ela será multiplicada até o número 10.

Rotina 4:
O usuário digitará um valor float no programa principal.

Crie uma função que receba um parâmetro referente a nota e retorne True caso a
nota seja válida (entre 0 e 10 inclusive) ou retorne False caso a nota não seja válida:
Digite uma nota: 33
A nota 33 é inválida
Repare que a função retorna um dado bool (lógico: True ou False). A partir deste
dado, o programa principal o tratará e gerará a mensagem adequada (sugerida na
tela).
"""