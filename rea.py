#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eel
eel.init('rea_gui')

def calcular(numero1, numero2, operacao):
    if operacao == '+':
        resultado = numero1+numero2
    elif operacao == '-':
        resultado = numero1-numero2
    elif operacao == '*':
        resultado = numero1*numero2
    elif operacao == '/':
        resultado = numero1/numero2

    return resultado

@eel.expose
def verificaBase(base, numero):
    """Verifica se os numeros pertcencem a base de origem"""
    for i in numero:
        if int(i) >= int(base):
            return False
    return True

@eel.expose
def coverteBase(baseOrigem, numero):
    """Realiza conversao entre as bases numéricas"""
    conversao = []
    numeroDecimal = int(numero, baseOrigem)
    conversao.append(bin(numeroDecimal)[2:])
    conversao.append(oct(numeroDecimal)[1:])
    conversao.append(int(numeroDecimal))
    conversao.append(hex(numeroDecimal)[2:])
    return conversao

@eel.expose
def calcula(baseOrigem, numero1, numero2, operacao):
    """Realiza operação entre dois numeros"""
    aux1 = numero1
    aux2 = numero2
    numero1 = ''
    numero2 = ''

    if baseOrigem == '2':
        numero1 += '0b'
        numero2 += '0b'
        numero1 += aux1
        numero2 += aux2

    elif baseOrigem == '8':
        numero1 += '0'
        numero2 += '0'
        numero1 += aux1
        numero2 += aux2

    elif baseOrigem == '16':
        numero1 += '0x'
        numero2 += '0x'
        numero1 += aux1
        numero2 += aux2

    return calcular(numero1, numero2, operacao)


eel.start('calculadora.html')
