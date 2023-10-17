print('Bem_vindo(a) a Loja')
valor_produto = float(input('Entre com o valor desejado: '))
qtd_produto = int(input('Entre com a quantidade desejada:'))
desconto_produto = 0
# Testar em cima da variavel da quantidade
if qtd_produto <= 9:# outra opção de execução if qtd_produto>= 10:
  desconto_produto = 0.00
elif 10 <= qtd_produto < 100: # outras opções if(qtd_produto >= 10) and (qtd_produto < 100):
  desconto_produto = 0.05 #5% = 0.05 || 100% = 1.00
elif 100<= qtd_produto < 999: #if(qtd_produto>= 100) and (qtd_produto <999):
  desconto_produto = 0.10 #10% = 0.10 || 100% = 1.00
else:
  desconto_produto = 0.15 #15% = 0.15

total_sem_desconto = valor_produto * qtd_produto
print('O valor total Sem desconto é de: R$ {:.2f}'.format(total_sem_desconto))
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto
print('O valor total Com desconto é de: R$ {:.2f}'.format(total_com_desconto))