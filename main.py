from module.CPU import CPU

cpu = CPU()
entrada = ""
valor = True

while True:
    linea = input()
    if linea.lower() == "":
        break

    if valor:
        entrada += linea
        valor = False
    else:
        entrada += '\n' + linea

codops = {
    "ADD": "00000", "SUB": "00001", "MUL": "00010", "DIV": "00011", "MOV": "00100", "DEC": "00101", "INC": "00110",
    "CMP": "00111", "JZ": "01000", "JNZ": "01001", "NOT": "01010", "AND": "01011", "OR": "01100", "XOR": "01101",
    "JA": "01110", "JAE": "01111", "JB": "10000", "JBE": "10001", "IN": "10010", "OUT": "10011"
}

programa = entrada.split('\n')
programa2 = []

for i in programa:
    i = i.replace(",", " ")
    instruccion = i.split(" ")

    codop = codops.get(instruccion[0])

    binario1 = bin(int(instruccion[1]))[2:]
    binario1 = binario1.zfill(8)

    binario2 = bin(int(instruccion[2]))[2:]
    binario2= binario2.zfill(8)

    ins = f"{codop}10000000{binario1}{binario2}"
    programa2.append(ins)


cpu.cargarInstrucciones(programa2)
cpu.run()



