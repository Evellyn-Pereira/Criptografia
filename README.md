# Criptografia

Cifrar documentos com textos e decifrar em Python.



# Projeto do Programa
 
O projeto foi desenvolvido com a intenção de Cifrar documentos com textos e decifrar em Python.
O objetivo é tornar um arquivo de texto incompreensível utilizando a cifra de César. Adaptei o programa para cifrar letras em letras, de modo que após o Z maiúsculo tenhamos o A maiúsculo e após o z minúsculo, tenhamos o a minúsculo. Além disso, os espaços, pontuações e demais caracteres foram preservados, de modo que apenas as letras fossem cifradas. 
Para saber um valor numérico de um caracter, utilizei a função ord(). Com esta função, as letras maiúsculas estão entre ord(‘A’) e ord(‘Z’), enquanto as minúsculas, entre ord(‘a’) e ord(‘z’). Logo, se um caracter estiver fora de um desses dois intervalos, ele não é uma letra e não deve ser cifrado. 
As letras maiúsculas foram cifradas em letras maiúsculas, assim como as letras minúsculas foram cifradas em letras minúsculas. Os demais caracteres, incluindo letras acentuadas, foram mantidos inalterados. 
O processo de descriptografia é quase idêntico ao processo de criptografia com a única diferença sendo o na parte de substituição 




# Tutorial


Crie um arquivo chamado “mensagem.txt”

Crie um arquivo chamado “criptodoc.py”. 
Digite o código do Programa.

No sistema Windows utilize o aplicativo powershell. Portanto, na utilização entre o sistema Mac OS ou Linux use o Terminal. 
Diante do terminal Linux, digite “python3 criptodoc.py” . Desse modo, irá aparecer uma mensagem, e vai criar dois arquivos chamados msg_cifrada.txt e msg_decifrada.txt

# Interface gráfica de Criptografia 

crie um arquivo chamado "Interface.py" e digite o código.
