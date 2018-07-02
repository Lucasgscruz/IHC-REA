#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eel

eel.init('rea_gui')
hexa = ['-','0','1','2','3','4', '5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f']
decimal = ['-','0','1','2','3','4','5','6','7','8','9']
octal = ['-','0','1','2','3','4','5','6','7']
binario = ['-','0','1']

# def calcular(numero1, numero2, operacao):
#     if operacao == '+':
#         resultado = numero1+numero2
#     elif operacao == '-':
#         resultado = numero1-numero2
#     elif operacao == '*':
#         resultado = numero1*numero2
#     elif operacao == '/':
#         resultado = numero1/numero2
#
#     return resultado
#
@eel.expose
def verificaSimbolos2(numero1, numero2, base, operacao):
    """Verifica se os numeros pertcencem a base de origem"""
    numero1 = str(numero1)
    numero2 = str(numero2)
    base = str(base)
    operacao = str(operacao)
    cont = 0

    print base, numero1, numero2

    while (cont < len(numero1)):
        if(numero1[cont] == '-' and cont > 0):
            eel.realizaOperacao(False)
            return None
        cont += 1
    cont = 0

    while (cont < len(numero2)):
        if(numero2[cont] == '-' and cont > 0):
            eel.realizaOperacao(False)
            return None
        cont += 1

    if base == '2':
        for i in numero1:
            if i not in binario:
                eel.realizaOperacao(False)
                return None
        for i in numero2:
            if i not in binario:
                eel.realizaOperacao(False)
                return None
    elif base == '8':
        for i in numero1:
            if i not in octal:
                eel.realizaOperacao(False)
                return None
        for i in numero2:
            if i not in octal:
                eel.realizaOperacao(False)
                return None
    elif base == '10':
        for i in numero1:
            if i not in decimal:
                eel.realizaOperacao(False)
                return None
        for i in numero2:
            if i not in decimal:
                eel.realizaOperacao(False)
                return None
    elif base == '16':
        for i in numero1:
            if i not in hexa:
                eel.realizaOperacao(False)
                return None
        for i in numero2:
            if i not in hexa:
                eel.realizaOperacao(False)
                return None

    print "Valido!"
    eel.realizaOperacao(True,numero1,numero2,base,operacao)


@eel.expose
def verificaSimbolos(base, numero):
    """Verifica se os numeros pertcencem a base de origem"""
    base = str(base)
    numero = str(numero)
    cont = 0

    print base, numero

    while (cont < len(numero)):
        if(numero[cont] == '-' and cont > 0):
            eel.autenticaSimbolos(False)
            return None
        cont += 1
    if base == '2':
        for i in numero:
            if i not in binario:
                eel.autenticaSimbolos(False)
                return None
    elif base == '8':
        for i in numero:
            if i not in octal:
                eel.autenticaSimbolos(False)
                return None
    elif base == '10':
        for i in numero:
            if i not in decimal:
                eel.autenticaSimbolos(False)
                return None
    elif base == '16':
        for i in numero:
            if i not in hexa:
                eel.autenticaSimbolos(False)
                return None

    print "Valido!"
    eel.autenticaSimbolos(True, base, numero)

@eel.expose
def coverteBase(baseOrigem, numero):
    """Realiza conversao entre as bases numéricas"""
    baseOrigem = int(baseOrigem)
    numero = str(numero)

    conversao = []
    if(numero[0] != '-'):
        numeroDecimal = int(numero, baseOrigem)
        conversao.append(bin(numeroDecimal)[2:])
        conversao.append(oct(numeroDecimal)[1:])
        conversao.append(str(numeroDecimal))
        conversao.append(hex(numeroDecimal)[2:].upper())
        eel.mudaTabela(conversao)
    else:
        numeroDecimal = int(numero, baseOrigem)
        conversao.append('-' + bin(numeroDecimal)[3:])
        conversao.append('-' + oct(numeroDecimal)[2:])
        conversao.append('-' + str(numeroDecimal))
        conversao.append('-' + hex(numeroDecimal)[3:].upper())
        eel.mudaTabela(conversao)

# @eel.expose
# def calcula(baseOrigem, numero1, numero2, operacao):
#     """Realiza operação entre dois numeros"""
#     aux1 = numero1
#     aux2 = numero2
#     numero1 = ''
#     numero2 = ''
#
#     if baseOrigem == '2':
#         numero1 += '0b'
#         numero2 += '0b'
#         numero1 += aux1
#         numero2 += aux2
#
#     elif baseOrigem == '8':
#         numero1 += '0'
#         numero2 += '0'
#         numero1 += aux1
#         numero2 += aux2
#
#     elif baseOrigem == '16':
#         numero1 += '0x'
#         numero2 += '0x'
#         numero1 += aux1
#         numero2 += aux2
#
#     return calcular(numero1, numero2, operacao)
eel.start('calculadora.html', options = {'port': 9014})
