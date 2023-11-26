faturamento = 1000 #numero inteiro
custo = 700

novas_vendas = 300
faturamento = faturamento + novas_vendas

taxa_imposto = 0.1 #numero decimal -> float
mensagem = "O faturaamento foi de 1000" # string
teve_lucro = False # boolean

imposto = taxa_imposto * faturamento
print("Faturamento", faturamento)
print("Custo", custo)
print("Lucro", faturamento - custo - imposto)
