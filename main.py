def valor_pagamento (valor_prestacao,dias_atraso):
    valor_final = valor_prestacao + (valor_prestacao*0.03) + (valor_prestacao * dias_atraso * 0.01)
    return valor_final
valor_prestacao = (float(input("Qual o valor da compra? ")))
dias_atraso = (int(input("Quantos dias de atraso? ")))
print("O valor final a ser pago com juros e multa é de R${}" .format(valor_pagamento(valor_prestacao,dias_atraso)))