import datetime
ano = int(input("Que ano você deseja analisar (informe 0 para analisar o ano atual): "))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"{ano} é um ano bissexto!")
else:
    print(f"{ano} não é um ano bissexto!")
