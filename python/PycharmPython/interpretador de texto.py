with open("modulo de entrada.txt","w") as modulo:
    modulo.write(";esta linha não deve ser impressa\n"
                 ">esta linha deve ser impressa\n"
                 "*esta linha deve ser centralizada")
with open("modulo de entrada.txt","r") as modulo:
    for linha in modulo.readlines():
        if linha[0] ==";":
            continue
        elif linha[0] == ">":
            print(linha)
        else:
            print(linha.center(50,"-"))

filmes = {
    "comedia":["filme 1", "filme 2 "],
    "drama":['filme 3, " filme 4'],
    "romance":["filme 5", "filme 6"]
}


with open("arquivo_html.html","w", encoding="utf-8") as pagina:
    pagina.write("""<!DOCTYPE HTML>\n
    <html lang="pt-br"
    <head>
        <title>meu site em python </title>
    </head>
    <body>
    """)
    for c, v in filmes.items():
        pagina.write(f"<h1>{c} </h1>")
        for e in v:
            pagina.write(f"<p>{e}</p>")
    pagina.write("</body> </html>")
