# -*- coding: utf-8 -*-
"""
se: https://magdalon.wordpress.com/2023/04/11/eksempeleksamen-r2-2022-oppgave-5/
for bedre forklaring
"""

from sympy import Symbol, Function
from sympy.series.sequences import RecursiveSeq
from sympy import rsolve
F = Function("F")
n = Symbol("n", integer = True)
#eksplisittUttrykk = rsolve('utrykk for f(n) som inneholder f(n-1)' - f(n), f(n), {'f(nummer man vet verdi til)' : 'verdi'})
eksplisittUttrykk = rsolve(1 + 2*F(n - 1) - F(n), F(n), {F(1) : 1})
print(f"5c) F(n) = {eksplisittUttrykk}")
