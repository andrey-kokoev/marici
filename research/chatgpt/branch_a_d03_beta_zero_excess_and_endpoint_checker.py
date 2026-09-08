#!/usr/bin/env python3
"""D03 packet through beta=0, with native and occurrence normals separate.

Self-contained, Python standard library only. Reconstructs all 430 states and
checks the original four witnesses, formal graph base change, all-order unit
conjugacy with beta NOT inverted, endpoint/Q restrictions, and two Koszul
excess calculations. The inherited witnesses are embedded and reverified.
Finite matrix identities certify the whole polynomial family; formal-series
controls are explicitly distinguished from the all-order argument.
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


def main(output):
    old=Complex('original');raw=Complex('graph');M=Complex('family');C0=Complex('central');C1=Complex('linear')
    check(old.states==raw.states==M.states==C0.states==C1.states,'identical_labelled_bases')
    oldchains={name:{(j,tuple(p)):c for j,c,p in rows} for name,rows in INPUT_CHAINS.items()}
    old_mu=mono('t15','t24','u14','u25',old=True)
    check(not old.boundary(oldchains['Omega']),'input_Omega_closed')
    check(old.boundary(oldchains['Wu'])==mul(oldchains['Omega'],mono('u03',old=True)),'input_Wu_equation')
    check(old.boundary(oldchains['Wmu'])==mul(oldchains['Omega'],old_mu),'input_Wmu_equation')
    check(oldchains['Theta']==add(mul(oldchains['Wmu'],mono('u03',old=True)),mul(oldchains['Wu'],old_mu),-1),'input_Theta_definition')
    check(not old.boundary(oldchains['Theta']),'input_Theta_closed')
    for j in range(430):
        oldb={(j,OLD_ZERO):1};b={(j,ZERO):1}
        check(raw.boundary(graph(oldb))==graph(old.boundary(oldb)),'entire_graph_base_change',j)
        check(M.boundary(gauge(b,M))==gauge(raw.boundary(b),M),'unit_only_normal_conjugacy',j)
        check(gauge(gauge(b,M),M,True)==b,'unit_conjugacy_inverse',j)
        check(not any(p[9] for k,p in gauge(b,M)),'normal_conjugacy_never_uses_beta_inverse',j)
        check(beta_coeff(M.boundary(b),0)==C0.boundary(b),'beta_zero_base_change',j)
        check(at_beta_one(M.boundary(b))==C1.boundary(b),'beta_one_control',j)
        n1={}
        for i,p,c in M.normal[j]:
            pp=list(p);pp[9]-=1;put(n1,(i,tuple(pp)),c)
        check(M.boundary(b)==add(C0.boundary(b),mul(n1,mono('beta'))),'d_equals_d0_plus_beta_d1',j)

    images={name:gauge(graph(C),M) for name,C in oldchains.items()}
    av=mono('v02','v04','v13');bv=mono('v03');cv=mono('v15','v24','v14','v25')
    beta=mono('beta');x=mono('X03');Y=mono('X14','X25');x35=mono('X35')
    beta4=mono(*(['beta']*4));beta5=mono(*(['beta']*5))
    O=factor(images['Omega'],av)
    H=factor(images['Wu'],pplus(pplus(pplus(av,bv),beta),x))
    G=factor(images['Wmu'],pplus(pplus(pplus(av,cv),beta4),Y))
    Z=add(G,H,-1)
    check(images['Theta']==mul(Z,pplus(pplus(pplus(pplus(pplus(av,bv),cv),beta5),x),Y)),'entire_Theta_factorization')
    for name,C in [('O',O),('H',H),('G',G),('Z',Z)]:
        check(all(not any(p[10:]) for j,p in C),'normalized_has_only_X_beta',name)
    check(M.boundary(H)==O,'primary_primitive_over_beta_family')
    check(M.boundary(G)==O,'second_primitive_over_beta_family')
    check(not M.boundary(Z),'secondary_closed_over_beta_family')
    check(not M.project(H,M.V),'primary_primitive_endpoint_zero')
    check(not M.project(O,M.V),'primary_cycle_endpoint_zero')

    Psi={(M.idx[F,F,0],mono(*(['beta']*(3-len(F))))):(-1)**(len(F)*(len(F)+1)//2) for F in M.faces}
    check(not M.boundary(Psi),'weighted_all_marked_cycle')
    check(replace_native35(Psi,M)==Z,'secondary_structural_identity')
    for j in range(430):
        b={(j,ZERO):1}
        check(M.boundary(replace_native35(b,M))==replace_native35(M.boundary(b),M),'native_to_occurrence_chain_map',j)
        check(replace_native35(replace_native35(b,M),M)==replace_native35(b,M),'native_to_occurrence_idempotent',j)
        check(all(M.states[k][0]==M.states[j][0] for k,p in replace_native35(b,M)),'native_replacement_preserves_face',j)
        check(add(M.boundary(occurrence_homotopy(b,M)),occurrence_homotopy(M.boundary(b),M))==mul(b,x35),'occurrence_parameter_homotopy',j)

    neg=M.idx[tuple(sorted(MINUS)),tuple(sorted(MINUS)),0]
    negocc=M.idx[tuple(sorted(MINUS)),tuple(sorted(MINUS)),1]
    posocc=M.idx[tuple(sorted(PLUS)),('13','15'),1]
    check(M.project(Z,M.V)=={(neg,ZERO):1,(posocc,beta):1},'exact_endpoint_frame_over_beta')
    top=M.idx[(),(),0];topocc=M.idx[(),(),1]
    qexpected={(top,mono('beta','beta','beta')):1}
    for l in LONG:qexpected[(M.idx[(l,),(l,),0],mono('beta','beta'))]=-1
    check(M.project(Z,M.Q)==qexpected,'complete_Q_component_over_beta')
    check(M.project(H,M.Q)=={(M.idx[('03',),('03',),0],mono('beta','beta')):1},'first_primitive_Q_frame')
    check(M.project(O,M.Q)=={(M.idx[('03',),(),0],mono('beta','beta','beta','X03')):1},'primary_Q_frame')

    # Strict summand detected at the full negative endpoint, not the generic top.
    upper={key:-c for key,c in occurrence_homotopy(Z,M).items()}
    Qd={0:[],1:[(0,x35,-1)]}
    section={0:Z,1:upper}
    def project_pair(C,lo,hi):
        out={}
        for (j,p),c in C.items():
            if j==lo:put(out,(0,p),c)
            elif j==hi:put(out,(1,p),c)
        return out
    check(M.boundary(upper)==mul(Z,x35,-1),'endpoint_summand_section_boundary')
    for k in range(2):
        q={(k,ZERO):1}
        check(M.boundary(section[k])==scalar_matrix_apply(section,matrix_apply(Qd,q)),'endpoint_summand_chain_section',k)
        check(project_pair(section[k],neg,negocc)==q,'endpoint_summand_retraction_identity',k)
        check(project_pair(section[k],top,topocc)==mul(q,mono('beta','beta','beta')),'generic_top_of_endpoint_section',k)
    for j in range(430):
        b={(j,ZERO):1}
        check(project_pair(M.boundary(b),neg,negocc)==matrix_apply(Qd,project_pair(b,neg,negocc)),'full_endpoint_top_projection_chain_map',j)
        check(project_pair(M.boundary(b),top,topocc)==matrix_apply(Qd,project_pair(b,top,topocc)),'full_generic_top_projection_chain_map',j)
    for d in SHORT:
        p=mono('X'+d,'X35')
        check(survives(p)==(d in PLUS),'X35_monomial_annihilator_generators',d)

    # All beta-coefficient coherence equations, including the endpoint changes.
    Zparts=[beta_coeff(Z,k) for k in range(4)]
    d1={j:[(i,pminus(p,beta),c) for i,p,c in M.normal[j]] for j in range(430)}
    for k in range(5):
        lhs=C0.boundary(Zparts[k]) if k<4 else {}
        if k>0:lhs=add(lhs,matrix_apply(d1,Zparts[k-1]))
        check(not lhs,'complete_beta_filtration_lift_equations',k)
    check([len(a) for a in Zparts]==[9,21,13,2],'secondary_beta_orders_term_counts')
    Z0_expected={(M.idx[F,F,0],ZERO):1 for F in M.faces if len(F)==3 and '35' not in F}
    check(Zparts[0]==Z0_expected,'central_secondary_nine_native_vertex_cycles')
    check(not M.project(Zparts[0],M.Q),'central_secondary_Q_zero')
    check(M.project(Zparts[0],M.V)=={(neg,ZERO):1},'central_secondary_negative_endpoint_nonzero')
    check(not beta_coeff(O,0),'central_raw_primary_zero')
    check(add(beta_coeff(G,0),beta_coeff(H,0),-1)==Zparts[0],'central_difference_of_recorded_primitives')
    check((len(beta_coeff(H,0)),len(beta_coeff(G,0)))==(2,7),'central_primitive_term_counts')
    # O is exactly beta-divisible. H is not beta-divisible: retaining this
    # distinction exposes a genuine beta-torsion class instead of erasing it.
    Os=factor(O,beta)
    check(M.boundary(H)==mul(Os,beta),'beta_annihilates_saturated_primary')
    check(M.boundary(G)==mul(Os,beta),'second_beta_annihilating_primitive')
    check(not M.boundary(Os),'saturated_primary_closed')
    check(beta_order(H)==0,'first_primitive_not_beta_divisible')

    # Complete occurrence-weight-zero central component. Each permitted
    # coefficient monomial is forced, so this is not a degree cutoff.
    coeff={}
    for j,(F,Hm,e) in enumerate(M.states):
        powers=[0]*len(VARS)
        for a in F:powers[DIAG_POS[a]]+=1
        for a in Hm:powers[DIAG_POS[a]]-=1
        powers[DIAG_POS['35']]-=e
        if min(powers[:9])>=0 and survives(powers):coeff[j]=tuple(powers)
    central_matrix={j:{} for j in coeff}
    for j,power in coeff.items():
        for i,q,c0 in C0.d[j]:
            total=pplus(power,q)
            if not survives(total):continue
            check(i in coeff and coeff[i]==total,'complete_central_homogeneous_degree',j)
            put(central_matrix[j],i,c0)
    reduction=integer_retract(central_matrix,M.deg)
    check(reduction['homology']=={1:6,2:21,3:14},'central_complete_homology')
    def vector(C):
        out={}
        for (j,power),c0 in C.items():
            check(j in coeff and coeff[j]==power,'homogeneous_witness_is_complete')
            put(out,j,c0)
        return out
    primary0=vector(beta_coeff(Os,0))
    primary_coordinates=int_apply(reduction['p'],primary0)
    check(primary_coordinates=={246:1,326:1},'saturated_primary_primitive_nonzero_detector')
    # A lift H of the specialized cycle H_0 has dH=beta*Os. Thus its
    # beta connecting class is the nonzero class Os_0, with conormal retained.
    check(not C0.boundary(beta_coeff(H,0)),'central_first_primitive_is_cycle')

    # Two genuine maps K(beta)[2] -> C_beta, derived from the same packet.
    source_beta={0:[],1:[(0,beta,1)]}
    first={0:Os,1:H};second={0:Os,1:G};difference={0:{},1:Z}
    for j in range(2):
        b={(j,ZERO):1}
        for name,Fm in [('first',first),('second',second),('difference',difference)]:
            check(M.boundary(Fm[j])==scalar_matrix_apply(Fm,matrix_apply(source_beta,b)),
                  'single_beta_supported_chain_map_'+name,j)
        check(add(second[j],first[j],-1)==difference[j],'two_supported_maps_actual_difference',j)
    # Exact homotopies annihilate the difference by beta and X35.
    hom_beta={0:Z,1:{}};hom_x35={0:{},1:occurrence_homotopy(Z,M)}
    for j in range(2):
        b={(j,ZERO):1}
        for scale,hom,name in [(beta,hom_beta,'beta'),(x35,hom_x35,'X35')]:
            lhs=add(M.boundary(hom[j]),scalar_matrix_apply(hom,matrix_apply(source_beta,b)))
            check(lhs==mul(difference[j],scale),'supported_difference_annihilating_homotopy_'+name,j)
    # Projected Hom^-2 -> Hom^-1 -> Hom^0 has columns (-X35,-beta)
    # and row (beta,-X35). Hence H^0=R/(beta,X35), and the difference is 1.
    endpoint_hom_d={0:[(1,x35,-1),(2,beta,-1)],1:[(3,beta,1)],2:[(3,x35,-1)],3:[]}
    for j in range(4):
        check(not matrix_apply(endpoint_hom_d,matrix_apply(endpoint_hom_d,{(j,ZERO):1})),
              'complete_endpoint_mapping_complex_squared',j)
    check(project_pair(difference[1],neg,negocc)=={(0,ZERO):1},'supported_difference_endpoint_unit')
    # A two-normal map retaining H and G would need a chain Y with dY=beta Z.
    # The endpoint quotient forces -X35 * coefficient(Y) = beta.
    # Modulo X35 and beta^2, beta is still nonzero: first-order lift obstruction.
    candidate_obstruction=mul(Z,beta)
    check(not M.boundary(candidate_obstruction),'two_normal_top_obstruction_closed')
    check(project_pair(candidate_obstruction,neg,negocc)=={(0,beta):1},'two_normal_obstruction_endpoint_beta')
    check(beta[POS['X35']]==0 and beta[9]==1,'two_normal_obstruction_nonzero_mod_X35_beta_squared')

    # The two-normal chain map exists on beta=0 but its first thickening
    # cannot retain these degree-one images. Verify the central map on all
    # four source generators before interpreting its lift obstruction.
    central_pair_images={0:beta_coeff(Os,0),1:beta_coeff(H,0),2:beta_coeff(G,0),3:{}}
    for j in range(4):
        check(not C0.boundary(central_pair_images[j]),'central_two_normal_map_columns_closed',j)
    detector={(216,mono('X03')):1,(246,mono('X24')):1}
    check(sum(detector.get(k,0)*c0 for k,c0 in beta_coeff(Os,0).items())==1,
          'two_row_saturated_primary_detector')

    # Original two spectator Rees divisors now have a single beta divisor.
    _,Kspec=polynomial_koszul((mono('beta','v04'),mono('beta','v35')))
    _,Kbb=polynomial_koszul((beta,beta))
    def unitpair(C):
        gs=(ZERO,mono('v04'),mono('v35'),mono('v04','v35'))
        return {(j,pplus(p,gs[j])):c for (j,p),c in C.items()}
    # K(beta) tensor Lambda(eta), ordered e before eta.
    Kex={0:[],1:[(0,beta,1)],2:[],3:[(2,beta,1)]}
    split={0:{(0,ZERO):1},1:{(1,ZERO):1},2:{(2,ZERO):1,(1,ZERO):-1},3:{(3,ZERO):1}}
    invsplit={0:{(0,ZERO):1},1:{(1,ZERO):1},2:{(1,ZERO):1,(2,ZERO):1},3:{(3,ZERO):1}}
    for j in range(4):
        b={(j,ZERO):1}
        check(matrix_apply(Kbb,unitpair(b))==unitpair(matrix_apply(Kspec,b)),'spectator_unit_only_Koszul_comparison',j)
        check(matrix_apply(Kbb,scalar_matrix_apply(split,b))==scalar_matrix_apply(split,matrix_apply(Kex,b)),'spectator_excess_chain_isomorphism',j)
        check(scalar_matrix_apply(invsplit,scalar_matrix_apply(split,b))==b,'spectator_excess_inverse',j)
    eta={(2,mono()):1,(1,mono()):-1}
    check(not matrix_apply(Kbb,eta),'spectator_excess_generator_closed')
    check(matrix_apply(Kbb,{(3,ZERO):1})==mul(eta,beta),'spectator_excess_generator_annihilated_by_beta')

    # The annihilator pair has common beta, so it is not a regular pair.
    _,Kann=polynomial_koszul((pplus(beta,x),pplus(beta4,Y)))
    rho={(1,mono('beta','beta','beta','X14','X25')):-1,(2,x):1}
    check(not matrix_apply(Kann,rho),'annihilator_pair_syzygy')
    check(matrix_apply(Kann,{(3,ZERO):1})==mul(rho,beta),'annihilator_pair_excess_top_boundary')
    check(not matrix_apply(Kann,matrix_apply(Kann,{(3,ZERO):1})),'annihilator_pair_d_squared')
    # Ordered unit changes use only v03, v15*v24*v14*v25, never beta.
    det_units=pplus(bv,cv)
    check(det_units[9]==0 and all(e==0 for e in det_units[:9]),'annihilator_determinant_change_only_existing_units')

    # Formal-series control; all-order invertibility follows from v(0)=1.
    series_order=14
    v=[Fraction(1,factorial(n+1)) for n in range(series_order)]
    inv=[Fraction(1)]+[Fraction(0)]*(series_order-1)
    for n in range(1,series_order):inv[n]=-sum(v[k]*inv[n-k] for k in range(1,n+1))
    for n in range(series_order):
        check(sum(v[k]*inv[n-k] for k in range(n+1))==(1 if n==0 else 0),'formal_unit_series_inverse_control',n)
    check(v[0]==1,'formal_unit_nonzero_constant_all_order_criterion')

    normalized={'Omega_beta':O,'H03_beta':H,'Hmu_beta':G,'Z_beta':Z,'Psi_beta':Psi,
                'occurrence_annihilating_primitive':occurrence_homotopy(Z,M),
                'endpoint_section_upper':upper,'saturated_Omega_beta':Os}
    orders={name:beta_order(C) for name,C in images.items()}
    check(orders=={'Omega':1,'Wu':1,'Wmu':4,'Theta':5},'raw_packet_exact_beta_valuations')
    for name,C in normalized.items():
        check(all(p[9]>=0 and all(e>=0 for e in p[:9]) for j,p in C),'all_output_chains_polynomial_in_beta_X',name)

    certificate={
        'schema':'marici.branch_a.d03_beta_zero_excess_endpoint.v1',
        'repository_commit':REPOSITORY_COMMIT,
        'ring':'Z[beta,X_d,v_d^{+-1}]/(X_even X_odd), formal physical units substituted over characteristic zero',
        'normal_coefficients':'beta*X_d; occurrence partner coefficient X35',
        'variables':list(VARS),
        'all_states':[{'i':j,'F':list(F),'H':list(H),'occ':e,'degree':M.deg[j]} for j,(F,H,e) in enumerate(M.states)],
        'family_differential':serial_matrix(M.d),
        'central_differential':serial_matrix(C0.d),
        'support_counts':{'full':430,'endpoint':32,'short':416,'Q':14},
        'input_witness_provenance_content_sha256':INPUT_CONTENT_SHA256,
        'input_witnesses':{n:serial_chain(C,old,OLD_VARS) for n,C in oldchains.items()},
        'graph_and_unit_frame_images':{n:serial_chain(C,M) for n,C in images.items()},
        'normalized_chains':{n:serial_chain(C,M) for n,C in normalized.items()},
        'beta_filtration_of_Z':{str(k):serial_chain(C,M) for k,C in enumerate(Zparts)},
        'beta_valuations_raw_packet':orders,
        'normalized_beta_valuations':{n:beta_order(C) for n,C in normalized.items()},
        'Z_beta_term_counts_by_beta_power':[len(C) for C in Zparts],
        'Z_zero_endpoint':'negative native top with coefficient 1; positive occurrence top has coefficient beta before specialization',
        'Q_component':'beta^2*(beta*T-h03-h14-h25)',
        'summand':{'degrees':[4,3],'differential':'-X35','projection':'negative endpoint all-native top and its occurrence partner',
                   'lower_section':'Z_beta','upper_section':'-S35 Z_beta','generic_top_projection_of_section':'beta^3 id',
                   'H3':'R/(X35)','H4':'Ann_R(X35)=(X02,X04,X24)',
                   'beta_torsion_of_selected_H3':'none'},
        'spectator_excess':{'ordered_pair':['beta*v04','beta*v35'],
                            'after_unit_change':'K(beta,beta) = K(beta) tensor Lambda(eta)',
                            'eta':'e35/v35-e04/v04',
                            'H0':'R/(beta)','H1':'R/(beta)*eta','H2':'0',
                            'determinant_factor':'v04*v35',
                            'split_columns':{str(j):[[i,c,list(p)] for (i,p),c in sorted(col.items())] for j,col in split.items()}},
        'annihilator_pair_excess':{'pair':['beta*X03','beta^4*X14*X25'],
                                  'primitive_syzygy':'-beta^3*X14*X25*e_u+X03*e_mu',
                                  'top_boundary':'beta times primitive syzygy',
                                  'H0':'R/(beta*X03,beta^4*X14*X25)',
                                  'H1':'R/(beta)','H2':'0'},
        'formal_series_control_order':series_order-1,
        'central_occurrence_zero_component':{
            'ranks':dict(sorted(Counter(M.deg[j] for j in coeff).items())),
            'homology':reduction['homology'],
            'basis_coefficient_monomials':{str(j):list(p) for j,p in coeff.items()},
            'differential':central_matrix,'contraction':reduction,
            'saturated_primary_coordinates':primary_coordinates,
            'explicit_primary_detector':[['02 03 04','02 04','X03',1],['02 04 24','02 04','X24',1]]},
        'single_beta_supported_comparison':{
            'source':'K(beta) in homological degrees 3 -> 2',
            'first_map':{'bottom':'saturated_Omega_beta','top':'H03_beta'},
            'second_map':{'bottom':'saturated_Omega_beta','top':'Hmu_beta'},
            'difference':{'bottom':'0','top':'Z_beta'},
            'exact_cyclic_annihilator':['beta','X35'],
            'endpoint_Hom_d_minus2':['-X35','-beta'],
            'endpoint_Hom_d_minus1':['beta','-X35'],
            'endpoint_comparison_class':'1 modulo (beta,X35)',
            'beta_annihilating_homotopy':{'bottom':'Z_beta','top':'0'},
            'X35_annihilating_homotopy':{'bottom':'0','top':'S35 Z_beta'},
            'endpoint_frame_preserved_by_difference':False},
        'two_beta_normal_lift_obstruction':{
            'required_top_boundary':'beta*Z_beta',
            'negative_endpoint_equation':'-X35*Y = beta',
            'first_infinitesimal_lift_exists':False,
            'scope':'retains the two recorded primitive images; does not assert a geometric identification of their labels'},
        'conclusions':{
            'primary_exact_without_beta_inversion':True,
            'saturated_primary_exact_beta_annihilator_in_Z_beta':'(beta)',
            'raw_packet_on_beta_zero':'all four chains zero',
            'recorded_factored_difference_on_beta_zero':'nine-term nonzero closed native vertex chain',
            'single_beta_map_difference_module':'R/(beta,X35), detected by an endpoint quotient',
            'same_endpoint_frame_for_two_primitives':False,
            'rank_two_regular_Gysin_at_beta_zero':False,
            'computed_physical_Delta_J':False,
            'scope':'coefficient-family continuation, not a physical resonant six-functor or amplitude theorem'},
        'verification':{'families':dict(sorted(COUNTS.items())),'exact_checks':sum(COUNTS.values())},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    certificate['content_sha256']=sha256(json.dumps(certificate,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(certificate,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'exact_checks':sum(COUNTS.values()),'support_counts':certificate['support_counts'],
                      'beta_valuations':orders,'Z_beta_terms':certificate['Z_beta_term_counts_by_beta_power'],
                      'normalized_orders':certificate['normalized_beta_valuations'],
                      'content_sha256':certificate['content_sha256'],'certificate':str(output)},sort_keys=True,indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('branch_a_d03_beta_zero_excess_and_endpoint_certificate.json'))
    main(parser.parse_args().output)
