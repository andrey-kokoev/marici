#!/usr/bin/env python3
"""Branch A: exact beta-family endpoint-to-Q compatibility and transgression.

Self-contained Python standard-library verifier. Reconstructs all 430 states,
rechecks the inherited four-chain packet, and derives the full occurrence-
weight-zero top-cycle module, its endpoint and Q maps, the beta^2-supported
short-boundary class, and the lower obstruction to lifting the Q-homotopy.
No coefficient degree cutoff, beta inversion, numerical rank extrapolation,
or physical conductor identification is used.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from math import factorial
from pathlib import Path

DIAGONALS=('02','03','04','13','14','15','24','25','35')
PLUS=frozenset(('13','15','35'))
MINUS=frozenset(('02','04','24'))
SHORT=tuple(sorted(PLUS|MINUS))
LONG=('03','14','25')
OLD_VARS=tuple('X'+d for d in DIAGONALS)+tuple('t'+d for d in SHORT)+tuple('u'+d for d in LONG)
VARS=tuple('X'+d for d in DIAGONALS)+('beta',)+tuple('v'+d for d in DIAGONALS)
ZERO=(0,)*len(VARS)
OLD_ZERO=(0,)*len(OLD_VARS)
POS={v:i for i,v in enumerate(VARS)}
OLD_POS={v:i for i,v in enumerate(OLD_VARS)}
DIAG_POS={d:i for i,d in enumerate(DIAGONALS)}
COUNTS=Counter()
REPOSITORY_COMMIT='d1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
INPUT_CONTENT_SHA256='c3d401f7dd1a66335806314893f89d6df865c9da282db697a9b3a6fe844310c7'

INPUT_CHAINS={'Omega': [(2, 1, (1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0)),
           (6, 1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0)),
           (10, 1, (0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0)),
           (14, 1, (0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0)),
           (34, 1, (0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0)),
           (48, -1, (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0)),
           (50, 1, (1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0)),
           (56, -1, (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0)),
           (64, -1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0)),
           (112, -1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0)),
           (120, -1, (0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0)),
           (128, -1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0)),
           (136, -1, (0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0)),
           (143, 1, (0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0)),
           (144, -1, (0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0)),
           (183, 1, (0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0)),
           (199, 1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0)),
           (216, 1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)),
           (273, -1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0)),
           (307, -1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0)),
           (326, 1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0))],
 'Theta': [(0, 1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1)),
           (4, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1)),
           (8, -1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1)),
           (12, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1)),
           (16, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1)),
           (20, -1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1)),
           (24, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1)),
           (28, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1)),
           (32, -1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0)),
           (35, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1)),
           (44, -1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1)),
           (52, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1)),
           (60, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1)),
           (68, -1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0)),
           (73, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1)),
           (84, -1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1)),
           (92, -1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1)),
           (97, -1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1)),
           (108, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1)),
           (116, -1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1)),
           (124, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1)),
           (132, -1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1)),
           (140, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1)),
           (145, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1)),
           (156, -1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1)),
           (164, -1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1)),
           (172, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1)),
           (180, -1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0)),
           (185, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1)),
           (196, -1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0)),
           (201, -1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0)),
           (220, 1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1)),
           (231, 1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1)),
           (252, 1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1)),
           (268, 1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0)),
           (279, 1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0)),
           (300, 1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1)),
           (311, 1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1)),
           (332, 1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1)),
           (348, 1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1)),
           (364, 1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1)),
           (375, 1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1)),
           (396, 1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1)),
           (412, 1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0)),
           (423, 1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0))],
 'Wmu': [(0, 1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1)),
         (20, -1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1)),
         (24, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1)),
         (28, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1)),
         (32, -1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0)),
         (52, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1)),
         (60, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1)),
         (68, -1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0)),
         (116, -1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1)),
         (124, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1)),
         (132, -1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1)),
         (140, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1)),
         (145, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1)),
         (156, -1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1)),
         (164, -1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1)),
         (172, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1)),
         (180, -1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0)),
         (185, -1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1)),
         (196, -1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0)),
         (201, -1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0)),
         (252, 1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1)),
         (268, 1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0)),
         (279, 1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0)),
         (332, 1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1)),
         (348, 1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1)),
         (364, 1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1)),
         (375, 1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1)),
         (396, 1, (0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1)),
         (412, 1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0)),
         (423, 1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0))],
 'Wu': [(4, 1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0)),
        (8, 1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0)),
        (12, 1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0)),
        (16, 1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0)),
        (35, 1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0)),
        (44, 1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0)),
        (73, 1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0)),
        (84, 1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0)),
        (92, 1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0)),
        (97, 1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0)),
        (108, 1, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0)),
        (220, -1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)),
        (231, -1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0)),
        (300, -1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)),
        (311, -1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0))]}

def check(condition, family, detail=''):
    if not condition:
        raise AssertionError(f'{family}: {detail}')
    COUNTS[family]+=1

def pplus(a,b):
    if len(a)!=len(b): raise ValueError('polynomial rings differ')
    return tuple(x+y for x,y in zip(a,b))

def pminus(a,b):
    if len(a)!=len(b): raise ValueError('polynomial rings differ')
    return tuple(x-y for x,y in zip(a,b))

def mono(*names, old=False):
    variables=OLD_VARS if old else VARS
    p=[0]*len(variables)
    for name in names:p[variables.index(name)]+=1
    return tuple(p)

def survives(p):
    return not (any(p[DIAG_POS[d]] for d in PLUS) and any(p[DIAG_POS[d]] for d in MINUS))

def put(out,key,c):
    if c:
        out[key]=out.get(key,0)+c
        if not out[key]: del out[key]

def add(a,b,scale=1):
    out=dict(a)
    for k,c in b.items():put(out,k,scale*c)
    return out

def mul(a,p,scale=1):
    out={}
    for (j,q),c in a.items():
        r=pplus(q,p)
        if survives(r):put(out,(j,r),scale*c)
    return out

def factor(a,p):
    out={}
    for (j,q),c in a.items():
        r=pminus(q,p)
        check(all(e>=0 for e in r[:10]),'no_X_or_beta_inversion')
        put(out,(j,r),c)
    check(mul(out,p)==a,'exact_principal_ideal_factorization')
    return out

def crosses(a,b):
    x,y=map(int,a);s,t=map(int,b)
    return x<s<y<t or s<x<t<y

class Complex:
    def __init__(self,kind):
        if kind not in ('original','graph','family','central','linear'):
            raise ValueError(kind)
        self.kind=kind
        self.zero=OLD_ZERO if kind=='original' else ZERO
        self.faces=[F for n in range(4) for F in combinations(DIAGONALS,n)
                    if all(not crosses(a,b) for a,b in combinations(F,2))]
        self.states=[(F,H,e) for F in self.faces for n in range(len(F)+1)
                     for H in combinations(F,n) for e in (0,1)]
        self.idx={x:i for i,x in enumerate(self.states)}
        self.deg={j:3-len(F)+len(H)+e for j,(F,H,e) in enumerate(self.states)}
        self.V={j for j,(F,H,e) in enumerate(self.states) if frozenset(F) in (PLUS,MINUS)}
        self.B={j for j,(F,H,e) in enumerate(self.states) if set(F)&set(SHORT)}
        self.Q=set(range(len(self.states)))-self.B
        self.d={};self.rad_occ={};self.normal={}
        fs=set(self.faces)
        for j,(F,H,e) in enumerate(self.states):
            ro=[];normal=[]
            for a in DIAGONALS:
                FF=tuple(sorted(F+(a,)))
                if a not in F and FF in fs:
                    ro.append((self.idx[FF,H,e],mono('X'+a,old=kind=='original'),(-1)**sum(b<a for b in F)))
            for k,a in enumerate(H):
                if kind=='original':
                    p=mono('t'+a,'X'+a,old=True) if a in SHORT else mono('u'+a,old=True)
                elif kind=='graph':p=mono('beta','v'+a,'X'+a)
                elif kind=='family':p=mono('beta','X'+a)
                elif kind=='linear':p=mono('X'+a)
                else:continue
                normal.append((self.idx[F,H[:k]+H[k+1:],e],p,(-1)**(3-len(F)+k)))
            if e:ro.append((self.idx[F,H,0],mono('X35',old=kind=='original'),(-1)**(3-len(F)+len(H))))
            self.rad_occ[j]=ro;self.normal[j]=normal;self.d[j]=ro+normal
        check(Counter(map(len,self.faces))=={0:1,1:9,2:21,3:14},'face_census')
        check((len(self.states),len(self.V),len(self.B),len(self.Q))==(430,32,416,14),'complete_support_counts')
        for j in range(430):
            b={(j,self.zero):1}
            check(not self.boundary(self.boundary(b)),'d_squared_'+kind,j)
            check(all(self.deg[k]==self.deg[j]-1 for k,p,c in self.d[j]),'d_degree_'+kind,j)
            if j in self.V:check(all(k in self.V for k,p,c in self.d[j]),'endpoint_subcomplex_'+kind,j)
            if j in self.B:check(all(k in self.B for k,p,c in self.d[j]),'short_subcomplex_'+kind,j)

    def boundary(self,C,part=None):
        matrix=self.d if part is None else (self.rad_occ if part=='rad_occ' else self.normal)
        out={}
        for (j,p),c in C.items():
            for k,q,s in matrix[j]:
                r=pplus(p,q)
                if survives(r):put(out,(k,r),c*s)
        return out

    @staticmethod
    def project(C,ids):return {k:c for k,c in C.items() if k[0] in ids}

def graph(C):
    out={}
    for (j,p),c in C.items():
        q=list(p[:9])+[0]*10
        for d in SHORT:
            n=p[OLD_POS['t'+d]]
            q[POS['beta']]+=n;q[POS['v'+d]]+=n
        for d in LONG:
            n=p[OLD_POS['u'+d]]
            q[POS['X'+d]]+=n;q[POS['beta']]+=n;q[POS['v'+d]]+=n
        q=tuple(q)
        if survives(q):put(out,(j,q),c)
    return out

def gauge(C,model,inverse=False):
    out={}
    for (j,p),c in C.items():
        g=mono(*('v'+d for d in model.states[j][1]))
        if inverse:g=tuple(-v for v in g)
        put(out,(j,pplus(p,g)),c)
    return out

def beta_coeff(C,k):
    out={}
    for (j,p),c in C.items():
        if p[9]==k:
            q=list(p);q[9]=0;put(out,(j,tuple(q)),c)
    return out

def at_beta_one(C):
    out={}
    for (j,p),c in C.items():
        q=list(p);q[9]=0;put(out,(j,tuple(q)),c)
    return out

def beta_order(C):return min((p[9] for j,p in C),default=None)

def occurrence_homotopy(C,M):
    out={}
    for (j,p),c in C.items():
        F,H,e=M.states[j]
        if not e:put(out,(M.idx[F,H,1],p),c*(-1)**(3-len(F)+len(H)))
    return out

def replace_native35(C,M):
    out={}
    for (j,p),c in C.items():
        F,H,e=M.states[j]
        if '35' not in H:put(out,(j,p),c)
        elif not e:
            put(out,(M.idx[F,tuple(a for a in H if a!='35'),1],pplus(p,mono('beta'))),c)
    return out

def fmt_power(p,variables=VARS):
    return '*'.join(name if n==1 else f'{name}^{n}' for name,n in zip(variables,p) if n) or '1'

def serial_chain(C,M,variables=VARS):
    return [{'state_index':j,'face':list(M.states[j][0]),'marks':list(M.states[j][1]),
             'occurrence_partner':M.states[j][2],'degree':M.deg[j],'integer':c,
             'exponents':list(p),'monomial':fmt_power(p,variables)}
            for (j,p),c in sorted(C.items())]

def serial_matrix(matrix):
    return [[j,i,c,list(p)] for j,col in sorted(matrix.items()) for i,p,c in col]

def polynomial_koszul(params):
    states=((),(0,),(1,),(0,1));ix={s:i for i,s in enumerate(states)}
    mat={j:[] for j in range(4)}
    for j,s in enumerate(states):
        for k,a in enumerate(s):mat[j].append((ix[s[:k]+s[k+1:]],params[a],(-1)**k))
    return states,mat

def matrix_apply(mat,C):
    out={}
    for (j,p),c in C.items():
        for i,q,v in mat.get(j,[]):
            r=pplus(p,q)
            if survives(r):put(out,(i,r),c*v)
    return out

def scalar_matrix_apply(mat,C):
    # mat columns are polynomial vectors with the same representation.
    out={}
    for (j,p),c in C.items():out=add(out,mul(mat.get(j,{}),p),c)
    return out

def int_apply(matrix,vector):
    out={}
    for j,c in vector.items():
        for i,b in matrix.get(j,{}).items():put(out,i,c*b)
    return out

def integer_retract(original,degree):
    d={j:dict(col) for j,col in original.items()}
    p={j:{j:1} for j in d};inc={j:{j:1} for j in d};h={j:{} for j in d}
    active=set(d);pivots=[]
    while True:
        pivot=None
        for hi in sorted(active,key=lambda i:(-degree[i],i)):
            for lo,c in sorted(d[hi].items()):
                if abs(c)==1:pivot=(lo,hi,c);break
            if pivot:break
        if not pivot:break
        lo,hi,sg=pivot;rest={i:c for i,c in d[hi].items() if i!=lo};ihi=inc[hi]
        for j,v in list(p.items()):
            c=v.get(lo,0)
            if c:h[j]=add(h[j],ihi,sg*c)
            p[j]=add({i:a for i,a in v.items() if i not in (lo,hi)},rest,-sg*c)
        for j in sorted(active-{lo,hi}):
            c=d[j].get(lo,0)
            if c:inc[j]=add(inc[j],ihi,-sg*c)
            d[j]=add({i:a for i,a in d[j].items() if i not in (lo,hi)},rest,-sg*c)
        for j in (lo,hi):del d[j];del inc[j]
        active-={lo,hi};pivots.append(pivot)
    check(all(not c for c in d.values()),'integral_reduction_residual_zero')
    for j,col in original.items():
        check(int_apply(original,col)=={},'slice_d_squared')
        check(int_apply(p,col)=={},'slice_projection_chain')
        check(add(int_apply(original,h[j]),int_apply(h,col))==add({j:1},int_apply(inc,p[j]),-1),'slice_full_homotopy_identity')
    for j,v in inc.items():
        check(int_apply(original,v)=={},'slice_inclusion_cycle')
        check(int_apply(p,v)=={j:1},'slice_projection_inclusion')
    return {'p':p,'i':inc,'h':h,'pivots':pivots,'residual':sorted(d),
            'homology':dict(sorted(Counter(degree[j] for j in d).items()))}


REFERENCE_BETA_CERTIFICATE_SHA256='9637135904ec497f5e87ca9caaff16960831fdf9780987164fcbd5c00850e276'
TOP_MINOR_ROW_IDS=[2,6,10,14,18,22,26,30,34,40,48,56,64,71,72,80,88,95,96,104,112,120,128,136,143,144,152,160,168,176,183,184,192,199,200,214,225,230,246,262,273,278,294,305,310,326,342,358,369,374,390,406,417,422]
BOCKSTEIN_MINOR_ROW_IDS=[246,262,280,294,312,326,342,358,376,390,406,424]


def bareiss_determinant(matrix):
    """Fraction-free exact determinant; no floating-point arithmetic."""
    n=len(matrix)
    if n==0:return 1
    if any(len(row)!=n for row in matrix):raise ValueError('square matrix required')
    a=[list(row) for row in matrix];previous=1;sign=1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:a[pivot],a[k]=a[k],a[pivot];sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*p-a[i][k]*a[k][j]
                if numerator%previous:raise ArithmeticError('nonintegral Bareiss division')
                a[i][j]=numerator//previous
            a[i][k]=0
        previous=p
    return sign*a[-1][-1]


def serial_int_columns(matrix):
    return [[j,i,c] for j,col in sorted(matrix.items()) for i,c in sorted(col.items())]


def occurrence_zero_complex(M):
    """All X-degree-zero terms; beta is a polynomial parameter, not specialized."""
    coefficient={}
    for j,(F,H,e) in enumerate(M.states):
        powers=[0]*len(VARS)
        for d in F:powers[DIAG_POS[d]]+=1
        for d in H:powers[DIAG_POS[d]]-=1
        powers[DIAG_POS['35']]-=e
        if min(powers[:9])>=0 and survives(powers):coefficient[j]=tuple(powers)
    d0={j:{} for j in coefficient};d1={j:{} for j in coefficient}
    for j,p in coefficient.items():
        for i,q,c in M.d[j]:
            pq=pplus(p,q)
            if not survives(pq):continue
            beta_power=pq[9]
            check(beta_power in (0,1),'slice_beta_exponent')
            pp=list(pq);pp[9]=0
            check(i in coefficient and tuple(pp)==coefficient[i],'complete_occurrence_zero_slice')
            check(beta_power==len(M.states[j][1])-len(M.states[i][1]),'beta_weight_on_every_arrow')
            put((d1 if beta_power else d0)[j],i,c)
    for j in coefficient:
        check(not int_apply(d0,d0[j]),'occurrence_slice_d0_squared',j)
        check(not add(int_apply(d0,d1[j]),int_apply(d1,d0[j])),'occurrence_slice_mixed_square',j)
        check(not int_apply(d1,d1[j]),'occurrence_slice_d1_squared',j)
    return coefficient,d0,d1


def main(output):
    old=Complex('original');raw=Complex('graph');M=Complex('family');C0=Complex('central')
    beta=mono('beta');beta2=mono('beta','beta');x35=mono('X35')
    inherited={name:{(j,tuple(p)):c for j,c,p in rows} for name,rows in INPUT_CHAINS.items()}
    mu=mono('t15','t24','u14','u25',old=True)
    check(not old.boundary(inherited['Omega']),'inherited_primary_cycle')
    check(old.boundary(inherited['Wu'])==mul(inherited['Omega'],mono('u03',old=True)),'inherited_first_primitive')
    check(old.boundary(inherited['Wmu'])==mul(inherited['Omega'],mu),'inherited_second_primitive')
    check(inherited['Theta']==add(mul(inherited['Wmu'],mono('u03',old=True)),mul(inherited['Wu'],mu),-1),'inherited_secondary_definition')
    check(not old.boundary(inherited['Theta']),'inherited_secondary_closed')
    for j in range(430):
        original_basis={(j,OLD_ZERO):1};basis={(j,ZERO):1}
        check(raw.boundary(graph(original_basis))==graph(old.boundary(original_basis)),'complete_graph_base_change',j)
        check(M.boundary(gauge(basis,M))==gauge(raw.boundary(basis),M),'unit_only_normal_gauge',j)
        check(gauge(gauge(basis,M),M,True)==basis,'normal_gauge_inverse',j)
        check(not any(p[9] for k,p in gauge(basis,M)),'gauge_does_not_invert_beta',j)
        check(add(M.boundary(occurrence_homotopy(basis,M)),occurrence_homotopy(M.boundary(basis),M))==mul(basis,x35),'full_occurrence_homotopy',j)

    images={name:gauge(graph(C),M) for name,C in inherited.items()}
    av=mono('v02','v04','v13');bv=mono('v03');cv=mono('v15','v24','v14','v25')
    A=factor(images['Omega'],pplus(av,beta))
    H=factor(images['Wu'],pplus(pplus(pplus(av,bv),beta),mono('X03')))
    G=factor(images['Wmu'],pplus(pplus(pplus(av,cv),mono('beta','beta','beta','beta')),mono('X14','X25')))
    Z=add(G,H,-1)
    check(M.boundary(H)==mul(A,beta),'H_beta_equation')
    check(M.boundary(G)==mul(A,beta),'G_beta_equation')
    check(not M.boundary(A),'A_beta_closed')
    check(not M.project(A,M.V) and not M.project(H,M.V),'recorded_first_map_endpoint_zero')
    check(images['Theta']==mul(Z,pplus(pplus(pplus(pplus(av,bv),cv),mono('beta','beta','beta','beta','beta')),mono('X03','X14','X25'))),'full_Theta_identity')

    Psi={(M.idx[F,F,0],mono(*(['beta']*(3-len(F))))):(-1)**(len(F)*(len(F)+1)//2) for F in M.faces}
    check(not M.boundary(Psi),'fundamental_cycle')
    check(replace_native35(Psi,M)==Z,'recorded_Z_is_structural_cycle')
    Zplus=add(Psi,Z,-1)
    check(not M.boundary(Z) and not M.boundary(Zplus),'two_top_cycles_closed')
    neg=M.idx[tuple(sorted(MINUS)),tuple(sorted(MINUS)),0]
    pos=M.idx[tuple(sorted(PLUS)),tuple(sorted(PLUS)),0]
    posocc=M.idx[tuple(sorted(PLUS)),('13','15'),1]
    negocc=M.idx[tuple(sorted(MINUS)),tuple(sorted(MINUS)),1]
    posnativeocc=M.idx[tuple(sorted(PLUS)),tuple(sorted(PLUS)),1]
    check(M.project(Z,M.V)=={(neg,ZERO):1,(posocc,beta):1},'Z_endpoint_values')
    check(M.project(Zplus,M.V)=={(pos,ZERO):1,(posocc,beta):-1},'complement_endpoint_values')

    # Both fully native endpoint-top quotients and their chain sections.
    quotient_d={0:[],1:[(0,x35,-1)]}
    def projection_pair(C,lo,hi):
        out={}
        for (j,p),c in C.items():
            if j==lo:put(out,(0,p),c)
            elif j==hi:put(out,(1,p),c)
        return out
    sections={}
    for name,cycle in [('negative',Z),('positive',Zplus)]:
        sections[name]={0:cycle,1:{k:-c for k,c in occurrence_homotopy(cycle,M).items()}}
        check(M.boundary(sections[name][1])==mul(cycle,x35,-1),'endpoint_section_boundary',name)
    for label,lo,hi in [('negative',neg,negocc),('positive',pos,posnativeocc)]:
        for j in range(430):
            base={(j,ZERO):1}
            check(projection_pair(M.boundary(base),lo,hi)==matrix_apply(quotient_d,projection_pair(base,lo,hi)),'endpoint_top_quotient_chain_'+label,j)
        for other,section in sections.items():
            for k in range(2):
                check(projection_pair(section[k],lo,hi)==({(k,ZERO):1} if label==other else {}),'two_endpoint_section_identity')

    # Complete polynomial-in-beta X-degree-zero top kernel, not a beta cutoff.
    coefficients,d0,d1=occurrence_zero_complex(M)
    ranks=dict(sorted(Counter(M.deg[j] for j in coefficients).items()))
    check(ranks=={0:8,1:59,2:108,3:56},'complete_slice_ranks')
    check(not any(M.deg[j]>=4 for j in coefficients),'no_occurrence_zero_degree_four')
    top_columns=[j for j in coefficients if M.deg[j]==3 and j not in (neg,pos)]
    check(len(top_columns)==54,'top_kernel_complement_rank')
    for i in TOP_MINOR_ROW_IDS:check(i in coefficients and M.deg[i]==2,'top_minor_rows_valid')
    integer_minor=[[d0[j].get(i,0)+d1[j].get(i,0) for j in top_columns] for i in TOP_MINOR_ROW_IDS]
    det=bareiss_determinant(integer_minor)
    exponent=sum(len(M.states[j][1]) for j in top_columns)-sum(len(M.states[i][1]) for i in TOP_MINOR_ROW_IDS)
    check((det,exponent)==(1,48),'top_minor_exact_beta_monomial_determinant')
    for i in TOP_MINOR_ROW_IDS:
        for j in top_columns:
            c=d0[j].get(i,0)+d1[j].get(i,0)
            if c:
                power=len(M.states[j][1])-len(M.states[i][1])
                check(power in (0,1),'minor_weight_factorization')
                check((d1 if power else d0)[j].get(i,0)==c,'minor_entry_homogeneity')
    # The two displayed cycles have endpoint matrix identity. The nonzero
    # beta^48 minor makes the other 54 columns injective over Z[beta].
    for name,C,values in [('negative',Z,(1,0)),('positive',Zplus,(0,1))]:
        check(C.get((neg,ZERO),0)==values[0] and C.get((pos,ZERO),0)==values[1],'top_kernel_endpoint_basis_'+name)
        for (j,p),c in C.items():
            pp=list(p);pp[9]=0
            check(j in coefficients and tuple(pp)==coefficients[j],'top_cycle_full_polynomial_slice')

    # First-order beta obstruction on all central degree-three cycles.
    reduction=integer_retract(d0,M.deg)
    central_top=[j for j in reduction['residual'] if M.deg[j]==3]
    central_two=[j for j in reduction['residual'] if M.deg[j]==2]
    obstruction={j:int_apply(reduction['p'],int_apply(d1,reduction['i'][j])) for j in central_top}
    endpointless=[j for j in central_top if j not in (neg,pos)]
    check(len(central_top)==14 and len(endpointless)==12,'central_endpoint_fixed_cycle_counts')
    Bminor=[[obstruction[j].get(i,0) for j in endpointless] for i in BOCKSTEIN_MINOR_ROW_IDS]
    check(bareiss_determinant(Bminor)==-1,'first_order_endpoint_fixed_obstruction_is_injective_saturated')
    for C in (Psi,Z):
        leading={j:c for (j,p),c in beta_coeff(C,0).items()}
        coords=int_apply(reduction['p'],leading)
        check(not int_apply(obstruction,coords),'two_central_surviving_cycles_have_zero_first_obstruction')

    # Genuine fourteen-state Q; seven states contribute to X-degree zero.
    top=M.idx[(),(),0]
    phi={(top,beta):1}
    for l in LONG:phi[(M.idx[(l,),(l,),0],ZERO)]=-1
    chi=M.boundary(phi)
    W=add(mul(phi,beta2),Z,-1)
    check(not M.project(chi,M.Q),'transgression_lands_in_actual_short_boundary')
    check(not M.project(chi,M.V),'transgression_has_zero_endpoint_components')
    check(not M.boundary(chi),'transgression_is_closed')
    check(M.project(Z,M.Q)==mul(phi,beta2),'negative_endpoint_to_Q_exact_beta_squared')
    check(not M.project(Zplus,M.Q),'positive_endpoint_generator_Q_zero')
    check(not M.project(W,M.Q),'beta_squared_primitive_is_short_supported')
    check(M.boundary(W)==mul(chi,beta2),'exact_beta_squared_annihilating_primitive')
    check(M.project(W,M.V)=={(neg,ZERO):-1,(posocc,beta):-1},'annihilating_primitive_endpoint_terms')
    check((len(phi),len(chi),len(W))==(4,18,41),'complete_transgression_term_counts')
    boundary_endpoint=M.boundary(M.project(W,M.V))
    check(len(boundary_endpoint)==6,'six_endpoint_connecting_corrections_retained')
    check(M.boundary(add(W,M.project(W,M.V),-1))==add(mul(chi,beta2),boundary_endpoint,-1),'dropping_endpoint_terms_breaks_primitive_identity')
    # Verify the Q quotient on every one of the 430 source columns.
    def qd(C):return M.project(M.boundary(C),M.Q)
    for j in range(430):
        base={(j,ZERO):1}
        check(M.project(M.boundary(base),M.Q)==qd(M.project(base,M.Q)),'complete_Q_projection_chain_map',j)
    qids=[j for j in coefficients if j in M.Q]
    qtop=[j for j in qids if M.deg[j]==3]
    qlow=[j for j in qids if M.deg[j]==2]
    check(len(qtop)==4 and len(qlow)==3,'Q_occurrence_zero_is_full_seven_state_component')
    for l in LONG:
        h=M.idx[(l,),(l,),0];p=M.idx[(l,),(),0]
        check(qd({(h,ZERO):1})=={(p,mono('beta','X'+l)):1},'Q_native_normal_equation')
    check(qd({(top,ZERO):1})=={(M.idx[(l,),(),0],mono('X'+l)):1 for l in LONG},'Q_top_equation')
    check(not qd(phi),'full_Q_top_cycle')

    # An independent integral central-fibre detector for the transgression.
    short_d0={j:{i:c for i,c in col.items() if i in M.B}
              for j,col in d0.items() if j in M.B}
    short_central_reduction=integer_retract(short_d0,M.deg)
    chi0={j:c for (j,p),c in beta_coeff(chi,0).items()}
    chi0_coordinates=int_apply(short_central_reduction['p'],chi0)
    check(chi0_coordinates.get(80)==1,'central_transgression_primitive_integral_detector')

    # The supported difference has a unique homogeneous Q-nullhomotopy.
    # U is its labelled graded lift, not asserted to be closed in C.
    source={0:[],1:[(0,beta,1)]}
    difference={0:{},1:Z}
    U={0:mul(phi,beta),1:{}}
    deltaU={j:add(M.boundary(U[j]),scalar_matrix_apply(U,matrix_apply(source,{(j,ZERO):1}))) for j in (0,1)}
    check(deltaU[0]==mul(chi,beta),'lifted_Q_homotopy_lower_obstruction')
    check(deltaU[1]==mul(phi,beta2),'lifted_Q_homotopy_top_component')
    short_map={j:add(difference[j],deltaU[j],-1) for j in (0,1)}
    check(short_map[0]==mul(chi,beta,-1),'supported_short_lift_bottom')
    check(short_map[1]=={k:-c for k,c in W.items()},'supported_short_lift_top')
    for j in (0,1):
        check(not M.project(short_map[j],M.Q),'supported_short_lift_Q_zero')
        check(M.boundary(short_map[j])==scalar_matrix_apply(short_map,matrix_apply(source,{(j,ZERO):1})),'supported_short_lift_chain_equation')
        check(M.project(deltaU[j],M.Q)==M.project(difference[j],M.Q),'Q_nullhomotopy_complete_chain_equation')
    # A single beta^2-supported source maps into the short subcomplex.
    double_source={0:[],1:[(0,beta2,1)]};double_map={0:chi,1:W}
    for j in (0,1):
        check(M.boundary(double_map[j])==scalar_matrix_apply(double_map,matrix_apply(double_source,{(j,ZERO):1})),'nonreduced_beta_squared_source_chain_map')

    # Required correction is endpoint-forced in the computed component.
    check(add(G,Z,-1)==H,'endpoint_correction_recovers_recorded_first_primitive')
    check(M.project(add(G,Z,-1),M.V)=={},'corrected_primitive_endpoint_zero')
    check(M.project(G,M.Q)==add(M.project(H,M.Q),mul(phi,beta2)),'forced_Q_change_of_endpoint_correction')
    for C in (phi,chi,W,Z,Zplus):
        for (j,p),c in C.items():
            check(min(p[:10])>=0,'every_new_chain_is_unlocalized')
    # The no-lift proofs use the exact top-kernel and Q equations above:
    # (i) Ann_{Z[beta]}[chi]=(beta^2);
    # (ii) no nonzero scalar multiple is a boundary with endpoint-zero primitive;
    # (iii) lifting U_Q while keeping the common bottom map has obstruction beta*chi.
    # They are mathematical implications, not hard-coded boolean "tests".

    chains={'A_beta':A,'H_beta':H,'G_beta':G,'Z_negative':Z,'Z_positive':Zplus,
            'Psi_beta':Psi,'Q_cycle_lift':phi,'short_transgression':chi,
            'beta_squared_primitive':W,'primitive_endpoint_boundary':boundary_endpoint,
            'Q_homotopy_lift_on_p':U[0],
            'short_supported_map_on_p':short_map[0],'short_supported_map_on_e':short_map[1]}
    cert={
        'schema':'marici.branch_a.beta_endpoint_q_transgression.v1',
        'repository_commit':REPOSITORY_COMMIT,
        'reference_beta_certificate_sha256':REFERENCE_BETA_CERTIFICATE_SHA256,
        'coefficient_ring':'Z[beta,X_d]/(X_even X_odd); native units retained separately',
        'normal_differential':'beta*X_d',
        'occurrence_partner_differential':'X35',
        'physical_scope':'formal coefficient continuation; no beta-zero geometric purity or physical Delta_J claimed',
        'homogeneous_scope':'all polynomial beta powers at occurrence weight zero',
        'variables':list(VARS),
        'all_states':[{'i':j,'F':list(F),'H':list(Hm),'occ':e,'degree':M.deg[j]} for j,(F,Hm,e) in enumerate(M.states)],
        'complete_family_differential':serial_matrix(M.d),
        'full_support_counts':{'full':430,'short':416,'endpoint':32,'Q':14},
        'new_chains':{name:serial_chain(C,M) for name,C in chains.items()},
        'chains_inherited_before_graph':{name:serial_chain(C,old,OLD_VARS) for name,C in inherited.items()},
        'occurrence_zero':{'ranks':ranks,'basis_occurrence_monomials':{str(j):list(p) for j,p in coefficients.items()},
            'd0':serial_int_columns(d0),'d1':serial_int_columns(d1),
            'degree_three_cycle_basis':['Z_negative','Z_positive'],
            'endpoint_coordinate_matrix':[[1,0],[0,1],[1,-1]],
            'endpoint_coordinate_rows':['negative native top','positive native top','positive occurrence top / beta'],
            'Q_homology_matrix':['beta^2','0'],
            'top_kernel_minor':{'rows':TOP_MINOR_ROW_IDS,'columns':top_columns,'matrix_at_beta_1':integer_minor,
                'integer_determinant':det,'beta_exponent':exponent,'exact_polynomial_determinant':'beta^48'}},
        'central_first_order_obstruction':{'central_homology':reduction['homology'],
            'contraction':reduction,'source_ids':central_top,'target_ids':central_two,
            'Bockstein_matrix':serial_int_columns(obstruction),
            'endpoint_zero_source_ids':endpointless,
            'minor_rows':BOCKSTEIN_MINOR_ROW_IDS,'minor_matrix':Bminor,'minor_determinant':-1,
            'endpoint_zero_class_count':12,'endpoint_zero_first_order_kernel_rank':0},
        'short_boundary_central_control':{
            'homology':short_central_reduction['homology'],
            'contraction':short_central_reduction,
            'transgression_coordinates':chi0_coordinates,
            'primitive_detector_residual_row':80,
            'primitive_detector_value':1},
        'transgression':{
            'definition':'chi_beta = d(lift(beta*T-h03-h14-h25))',
            'degree':2,'terms':18,'endpoint_components':'zero','Q_components':'zero',
            'ordinary_cyclic_module_over_Z_beta':'Z[beta]/(beta^2)',
            'annihilating_primitive':'beta^2*Q_cycle_lift-Z_negative',
            'primitive_terms':41,'primitive_endpoint_components':'-E_- - beta*E_+occ',
            'strict_endpoint_zero_cyclic_module_over_Z_beta':'Z[beta]',
            'normalization':'coefficient of phi_Q is 1; no division by beta or occurrences',
            'not_claimed':'full occurrence-ring annihilator or physical conductor identification'},
        'supported_Q_homotopy':{
            'source':'K(beta) in degrees 3 -> 2',
            'difference_on_p':'0','difference_on_e':'Z_negative',
            'unique_Q_homotopy_on_p':'beta*phi_Q','unique_Q_homotopy_on_e':'0',
            'graded_lift_defect_on_p':'beta*chi_beta',
            'short_boundary_representative_on_p':'-beta*chi_beta',
            'short_boundary_representative_on_e':'-beta_squared_primitive',
            'homotopy_preserves_common_bottom_cochain':False},
        'endpoint_correction':{
            'with_required_endpoint_values':'Z_negative uniquely, in occurrence degree zero',
            'strict_Q_preserving_correction_exists':False,
            'forced_Q_change':'beta^2*phi_Q',
            'after_correction':'G_beta-Z_negative=H_beta'},
        'verification':{'exact_checks':sum(COUNTS.values()),'families':dict(sorted(COUNTS.items()))},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    cert['content_sha256']=sha256(json.dumps(cert,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(cert,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'exact_checks':sum(COUNTS.values()),'source_states':430,
        'homogeneous_ranks':ranks,'top_kernel':'Z[beta]^2',
        'top_minor':'beta^48','Q_image_ideal':'(beta^2)',
        'short_transgression_annihilator_over_Z_beta':'(beta^2)',
        'endpoint_fixed_central_first_order_kernel':0,
        'content_sha256':cert['content_sha256'],'certificate':str(output)},indent=2,sort_keys=True))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('branch_a_beta_endpoint_q_transgression_certificate.json'))
    main(parser.parse_args().output)
