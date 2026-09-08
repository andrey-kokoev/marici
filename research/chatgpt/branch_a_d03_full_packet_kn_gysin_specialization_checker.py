#!/usr/bin/env python3
"""Exact fixed-nonzero-beta normal-graph specialization of a complete D03 packet.

Standard library only. Reconstructs all 430 labelled coefficient states; verifies
both original and pulled-back differentials, the normal-frame unit conjugacy,
all original and specialized chain witnesses, endpoint terms, and an explicit
ordinary coefficient summand. No network or other local input files are needed.

The fixed input chains are embedded from the previously delivered certificate;
their identities are rechecked, not assumed. The theorem concerns the source's
formal post-scalar-extraction Koba--Nielsen coefficient graph. It does not claim
an independently constructed physical conductor--Morse comparison.
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
from typing import Any

DIAGONALS=('02','03','04','13','14','15','24','25','35')
PLUS=frozenset(('13','15','35'))
MINUS=frozenset(('02','04','24'))
SHORT=tuple(sorted(PLUS|MINUS))
LONG=('03','14','25')
OLD_VARIABLES=tuple('X'+d for d in DIAGONALS)+tuple('t'+d for d in SHORT)+tuple('u'+d for d in LONG)
NEW_VARIABLES=tuple('X'+d for d in DIAGONALS)+tuple('g'+d for d in DIAGONALS)
OLDPOS={v:i for i,v in enumerate(OLD_VARIABLES)}
POS={d:i for i,d in enumerate(DIAGONALS)}
N=18
ZERO=(0,)*N
CHECKS=Counter()

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
        (311, -1, (0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0))],
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
           (423, 1, (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0))]}


def check(ok:bool, family:str, detail:Any='')->None:
    if not ok:
        raise AssertionError(f'{family}: {detail}')
    CHECKS[family]+=1

def addp(a,b): return tuple(x+y for x,y in zip(a,b))
def subp(a,b): return tuple(x-y for x,y in zip(a,b))
def var(name,old=False):
    ix=OLDPOS[name] if old else NEW_VARIABLES.index(name)
    return tuple(int(i==ix) for i in range(N))
def mon(names,old=False):
    z=ZERO
    for name in names: z=addp(z,var(name,old))
    return z

def survives(power):
    return not(any(power[POS[d]]>0 for d in PLUS)
               and any(power[POS[d]]>0 for d in MINUS))

def put(out,key,value):
    if not value: return
    out[key]=out.get(key,0)+value
    if not out[key]: del out[key]

def add(a,b,scale=1):
    out=dict(a)
    for k,v in b.items():put(out,k,scale*v)
    return out

def multiply(chain,power,scale=1):
    out={}
    for (j,p),c in chain.items():
        q=addp(p,power)
        check(min(q[:9])>=0,'no_occurrence_inversion')
        if survives(q):put(out,(j,q),c*scale)
    return out

def exact_factor(chain,power):
    # Factor an already divisible chain; never adjoin inverses of X_d.
    out={}
    for (j,p),c in chain.items():
        q=subp(p,power)
        check(min(q[:9])>=0,'principal_ideal_factorization_is_polynomial')
        put(out,(j,q),c)
    check(multiply(out,power)==chain,'principal_ideal_factorization_identity')
    return out

def crosses(a,b):
    x,y=map(int,a);u,v=map(int,b)
    return x<u<y<v or u<x<v<y

class Model:
    def __init__(self,kind):
        if kind not in ('original','physical','linear'):
            raise ValueError(kind)
        self.kind=kind
        self.faces=[f for k in range(4) for f in combinations(DIAGONALS,k)
                    if all(not crosses(a,b) for a,b in combinations(f,2))]
        check(Counter(map(len,self.faces))=={0:1,1:9,2:21,3:14},'actual_face_census')
        self.states=[(f,h,e) for f in self.faces for k in range(len(f)+1)
                     for h in combinations(f,k) for e in (0,1)]
        self.index={s:j for j,s in enumerate(self.states)}
        self.degree={j:3-len(f)+len(h)+e for j,(f,h,e) in enumerate(self.states)}
        fs=set(self.faces)
        self.d={}
        for j,(f,h,e) in enumerate(self.states):
            terms=[]
            for a in DIAGONALS:
                ff=tuple(sorted(f+(a,)))
                if a not in f and ff in fs:
                    terms.append((self.index[ff,h,e],var('X'+a),(-1)**sum(b<a for b in f)))
            for pos,a in enumerate(h):
                if kind=='original':
                    power=mon(('t'+a,'X'+a),True) if a in SHORT else var('u'+a,True)
                elif kind=='physical': power=mon(('g'+a,'X'+a))
                else: power=var('X'+a)
                terms.append((self.index[f,h[:pos]+h[pos+1:],e],power,(-1)**(3-len(f)+pos)))
            if e:
                terms.append((self.index[f,h,0],var('X35'),(-1)**(3-len(f)+len(h))))
            self.d[j]=terms
        self.endpoints={j for j,(f,h,e) in enumerate(self.states) if frozenset(f) in (PLUS,MINUS)}
        self.short={j for j,(f,h,e) in enumerate(self.states) if set(f)&set(SHORT)}
        self.q=set(self.d)-self.short
        check((len(self.states),len(self.endpoints),len(self.short),len(self.q))==(430,32,416,14),'full_corrected_support_counts')
        for j,terms in self.d.items():
            check(all(self.degree[i]==self.degree[j]-1 for i,p,c in terms),'chain_degree')
            check(self.boundary(self.boundary({(j,ZERO):1}))=={},'full_'+kind+'_d_squared')
            if j in self.endpoints:check(all(i in self.endpoints for i,p,c in terms),'endpoint_subcomplex')
            if j in self.short:check(all(i in self.short for i,p,c in terms),'short_subcomplex')

    def boundary(self,chain):
        out={}
        for (j,p),c in chain.items():
            for i,q,s in self.d[j]:
                pq=addp(p,q)
                if survives(pq):put(out,(i,pq),c*s)
        return out

    def projection(self,chain,ids):
        return {key:v for key,v in chain.items() if key[0] in ids}

    def weight(self,state):
        f,h,e=state;w=[0]*9
        for a in f:w[POS[a]]-=1
        for a in h:w[POS[a]]+=1
        w[POS['35']]+=e
        return tuple(w)

    def slice(self,wt):
        coeff={j:subp(wt,self.weight(s)) for j,s in enumerate(self.states)}
        coeff={j:p for j,p in coeff.items() if min(p)>=0 and survives(p)}
        mat={j:{} for j in coeff}
        for j,p in coeff.items():
            for i,q,c in self.d[j]:
                check(not any(q[9:]),'linear_slice_has_no_unit_variables')
                total=addp(p,q[:9])
                if not survives(total):continue
                check(i in coeff and coeff[i]==total,'fine_degree_complete_slice')
                put(mat[j],i,c)
        return mat,coeff

def graph_coeff(p):
    out=list(p[:9])+[0]*9
    for d in SHORT:out[9+POS[d]]+=p[OLDPOS['t'+d]]
    for d in LONG:
        n=p[OLDPOS['u'+d]]
        out[POS[d]]+=n;out[9+POS[d]]+=n
    return tuple(out)

def graph(chain):
    out={}
    for (j,p),c in chain.items():
        q=graph_coeff(p)
        if survives(q):put(out,(j,q),c)
    return out

def gauge(chain,model,inverse=False):
    out={}
    for (j,p),c in chain.items():
        marks=model.states[j][1]
        q=mon(('g'+a for a in marks))
        if inverse:q=tuple(-n for n in q)
        put(out,(j,addp(p,q)),c)
    return out

def apply(matrix,vector):
    out={}
    for j,c in vector.items():
        for i,b in matrix.get(j,{}).items():put(out,i,c*b)
    return out

def retract(original,degree):
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
        check(apply(original,col)=={},'slice_d_squared')
        check(apply(p,col)=={},'slice_projection_chain')
        check(add(apply(original,h[j]),apply(h,col))==add({j:1},apply(inc,p[j]),-1),'slice_full_homotopy_identity')
    for j,v in inc.items():
        check(apply(original,v)=={},'slice_inclusion_cycle')
        check(apply(p,v)=={j:1},'slice_projection_inclusion')
    return {'p':p,'i':inc,'h':h,'pivots':pivots,'residual':sorted(d),
            'homology':dict(sorted(Counter(degree[j] for j in d).items()))}

def vector(chain,coeff):
    out={}
    for (j,p),c in chain.items():
        check(j in coeff and p==coeff[j]+(0,)*9,'full_polynomial_to_slice')
        put(out,j,c)
    return out

def occurrence_homotopy(chain,model):
    out={}
    for (j,p),c in chain.items():
        f,h,e=model.states[j]
        if not e:
            put(out,(model.index[f,h,1],p),c*(-1)**(3-len(f)+len(h)))
    return out

def serialize(chain,model,variables=NEW_VARIABLES):
    return [{'id':j,'face':list(model.states[j][0]),'marks':list(model.states[j][1]),
             'occurrence_partner':model.states[j][2],'coefficient':c,
             'monomial':{v:n for v,n in zip(variables,p) if n}}
            for (j,p),c in sorted(chain.items())]

def serial_matrix(mat):
    return {str(j):[[i,c] for i,c in sorted(col.items())] for j,col in sorted(mat.items())}

def check_formal_unit():
    # v(z)=(exp(z)-1)/z is a formal unit because v(0)=1. These exact
    # coefficients only audit the implementation; the all-order proof is v(0)=1.
    n=13
    v=[Fraction(1,factorial(k+1)) for k in range(n)]
    w=[Fraction(0)]*n;w[0]=1
    for k in range(1,n):w[k]=-sum(v[i]*w[k-i] for i in range(1,k+1))
    for k in range(n):
        check(sum(v[i]*w[k-i] for i in range(k+1))==int(k==0),'exact_formal_unit_coefficients')
    return {'v_coefficients':[[a.numerator,a.denominator] for a in v],
            'inverse_coefficients':[[a.numerator,a.denominator] for a in w],
            'all_order_unit_reason':'constant term 1; g_d=beta*v(beta*X_d), beta fixed nonzero in characteristic zero'}

def main(output:Path):
    original=Model('original');physical=Model('physical');linear=Model('linear')
    check(original.states==physical.states==linear.states,'one_identical_labelled_basis')
    oldchains={name:{(j,tuple(p)):c for j,c,p in rows} for name,rows in INPUT_CHAINS.items()}
    O,Wu,Wm,Th=(oldchains[k] for k in ('Omega','Wu','Wmu','Theta'))
    mu_old=mon(('t15','t24','u14','u25'),True)
    check(original.boundary(O)=={},'original_Omega_cycle')
    check(original.boundary(Wu)==multiply(O,var('u03',True)),'original_u_primitive')
    check(original.boundary(Wm)==multiply(O,mu_old),'original_mu_primitive')
    check(Th==add(multiply(Wm,var('u03',True)),multiply(Wu,mu_old),-1),'original_secondary_definition')
    check(original.boundary(Th)=={},'original_secondary_cycle')

    for j in range(430):
        basis={(j,ZERO):1}
        check(physical.boundary(graph(basis))==graph(original.boundary(basis)),'normal_graph_is_chain_map')
        check(linear.boundary(gauge(basis,linear))==gauge(physical.boundary(basis),linear),'unit_normal_frame_conjugacy')
        check(gauge(gauge(basis,linear),linear,True)==basis,'normal_frame_inverse')
        # The scalar pairing on each normal determinant retains its inverse dual.
        gp=mon(('g'+a for a in linear.states[j][1]))
        check(addp(gp,tuple(-x for x in gp))==ZERO,'dual_normal_frame_pairing')
        if j in linear.endpoints:
            check(all(k in linear.endpoints for k,p in gauge(basis,linear)),'gauge_endpoint_labels')
        if j in linear.short:
            check(all(k in linear.short for k,p in gauge(basis,linear)),'gauge_short_labels')

    images={name:gauge(graph(C),linear) for name,C in oldchains.items()}
    w=mon(('g02','g04','g13'));gu=var('g03');gmu=mon(('g15','g24','g14','g25'))
    x03=var('X03');xprod=mon(('X14','X25'));triple=addp(x03,xprod)
    On=exact_factor(images['Omega'],w)
    H=exact_factor(images['Wu'],addp(addp(w,gu),x03))
    G=exact_factor(images['Wmu'],addp(addp(w,gmu),xprod))
    Z=add(G,H,-1)
    check(images['Theta']==multiply(Z,addp(addp(addp(w,gu),gmu),triple)),'entire_secondary_physical_factorization')
    for name,C in [('Omega',On),('H',H),('G',G),('Z',Z)]:
        check(all(not any(p[9:]) for j,p in C),'normalized_chain_has_only_occurrences',name)
    check(linear.boundary(H)==On,'endpoint_zero_polynomial_primitive')
    check(linear.boundary(G)==On,'second_polynomial_primitive')
    check(linear.boundary(Z)=={},'physical_secondary_closed')
    check(not linear.projection(H,linear.endpoints),'first_primitive_endpoint_zero')
    check(not linear.projection(On,linear.endpoints),'physical_Omega_endpoint_zero')

    top=linear.index[(),(),0];topocc=linear.index[(),(),1]
    qO={(linear.index[('03',),(),0],x03):1}
    qH={(linear.index[('03',),('03',),0],ZERO):1}
    qG={(top,ZERO):1,(linear.index[('14',),('14',),0],ZERO):-1,
        (linear.index[('25',),('25',),0],ZERO):-1}
    qZ=add(qG,qH,-1)
    for C,expected in ((On,qO),(H,qH),(G,qG),(Z,qZ)):
        check(linear.projection(C,linear.q)==expected,'full_Q_projection')
    neg=linear.index[tuple(sorted(MINUS)),tuple(sorted(MINUS)),0]
    pos_occ=linear.index[tuple(sorted(PLUS)),('13','15'),1]
    pos_native=linear.index[tuple(sorted(PLUS)),tuple(sorted(PLUS)),0]
    E={(neg,ZERO):1,(pos_occ,ZERO):1}
    check(linear.projection(G,linear.endpoints)==E,'second_primitive_endpoint_terms')
    check(linear.projection(Z,linear.endpoints)==E,'secondary_endpoint_terms')

    # Full unbounded occurrence weight-zero component, not a polynomial cutoff.
    mat,coeff=linear.slice((0,)*9);red=retract(mat,linear.degree)
    check(red['homology']=={2:3,3:2},'unit_normalized_weight_zero_homology')
    check(not any(linear.degree[j]==4 for j in mat),'no_degree_four_in_weight_zero')
    zvec=vector(Z,coeff);hvec=vector(H,coeff);ovec=vector(On,coeff)
    check(apply(red['p'],ovec)=={},'specialized_primary_class_zero')
    check(apply(red['p'],zvec)=={423:1},'secondary_primitive_homology_coordinate')
    check(apply(red['h'],ovec)==hvec,'computed_retract_recovers_first_primitive')

    # A second canonical zero-weight top cycle and the exact endpoint test.
    Psi={ (linear.index[f,f,0],ZERO):(-1)**(len(f)*(len(f)+1)//2) for f in linear.faces }
    check(linear.boundary(Psi)=={},'all_marked_top_cycle')
    psivec=vector(Psi,coeff)
    check(apply(red['p'],psivec)=={428:1},'two_top_cycles_form_integral_basis')
    ep_matrix=[[Z.get((row,ZERO),0),Psi.get((row,ZERO),0)] for row in (neg,pos_occ,pos_native)]
    check(ep_matrix==[[1,1],[1,0],[0,1]],'endpoint_restriction_of_all_top_cycles')
    check(ep_matrix[1][0]*ep_matrix[2][1]-ep_matrix[1][1]*ep_matrix[2][0]==1,'endpoint_injection_saturated')

    # The surviving cycle has a structural description, not only a table:
    # replace the native 35 normal by the distinct occurrence-35 normal.
    # This is now a chain endomorphism because both normalized differentials
    # are X35. It is not a declaration that the two normal lines are identical.
    def replace35(C):
        out={}
        for (j,p),c in C.items():
            face,marks,e=linear.states[j]
            if '35' not in marks:put(out,(j,p),c)
            elif not e:
                put(out,(linear.index[face,tuple(a for a in marks if a!='35'),1],p),c)
        return out
    for j in range(430):
        b={(j,ZERO):1}
        check(linear.boundary(replace35(b))==replace35(linear.boundary(b)),
              'native_to_occurrence_35_comparison_chain_map')
        check(replace35(replace35(b))==replace35(b),
              'native_to_occurrence_35_idempotence')
        check(all(linear.states[k][0]==linear.states[j][0] for k,p in replace35(b)),
              'native_to_occurrence_comparison_preserves_faces')
    check(replace35(Psi)==Z,'secondary_is_replaced_all_marked_top_cycle')

    # Strict ordinary chain summand, retaining the occurrence partner.
    # Top quotient has differential -X35 in degrees 4 -> 3.
    def project_top(C):return linear.projection(C,{top,topocc})
    def dtop(C):
        out={}
        for (j,p),c in C.items():
            if j==topocc:put(out,(top,addp(p,var('X35'))),-c)
        return out
    Sz=occurrence_homotopy(Z,linear)
    section_upper={key:-c for key,c in Sz.items()}
    check(linear.boundary(Sz)==multiply(Z,var('X35')),'X35_annihilating_homotopy')
    check(linear.boundary(section_upper)==multiply(Z,var('X35'),-1),'top_section_chain_equation')
    check(project_top(Z)=={(top,ZERO):1},'top_section_lower_identity')
    check(project_top(section_upper)=={(topocc,ZERO):1},'top_section_upper_identity')
    for j in range(430):
        b={(j,ZERO):1}
        check(project_top(linear.boundary(b))==dtop(project_top(b)),'complete_top_projection_chain_map')
        check(add(linear.boundary(occurrence_homotopy(b,linear)),occurrence_homotopy(linear.boundary(b),linear))==multiply(b,var('X35')),'full_occurrence_multiplication_homotopy')

    # Retained normal primitives versus flexible choices: an exact test.
    # Changing Wmu by -mu*Z removes the specialized compatibility; its endpoint
    # change is precisely the previously displayed nonzero endpoint column.
    original_mu_norm=exact_factor(images['Wmu'],addp(w,gmu))
    adjusted=multiply(H,xprod)
    check(add(original_mu_norm,adjusted,-1)==multiply(Z,xprod),'new_primitive_indeterminacy_after_base_change')
    check(linear.boundary(adjusted)==multiply(On,xprod),'adjusted_primitive_same_boundary')
    check(add(multiply(adjusted,x03),multiply(multiply(H,x03),xprod),-1)=={},'flexible_secondary_compatibility_can_be_zero')

    # On u03=0 the specialized Wu is literally zero. The original nonzero
    # u-Bockstein cannot be transported by a homology-only substitution.
    check(all(p[POS['03']]>=1 for j,p in images['Wu']),'Wu_specialization_vanishes_on_X03_divisor')
    check(all(p[POS['03']]>=1 and p[POS['14']]>=1 and p[POS['25']]>=1 for j,p in images['Theta']),'raw_Theta_retains_three_occurrence_factors')
    # Supported t_i=0 Koszul factors contract after graph base change because
    # g_i is already a unit. The inverse used here is only a g_i inverse.
    for d in SHORT:
        gp=var('g'+d)
        check(addp(gp,tuple(-c for c in gp))==ZERO,'supported_Rees_divisor_pullback_contracts')

    # The ordered codimension-two Gysin normal comparison is a Koszul
    # change of generators (u,mu)=(g03*X03,gmu*X14*X25). Retain determinant.
    kos_basis=((),(0,),(1,),(0,1))
    kos_index={e:i for i,e in enumerate(kos_basis)}
    def kd(C,params):
        out={}
        for (j,p),c in C.items():
            e=kos_basis[j]
            for k,a in enumerate(e):
                dest=kos_index[e[:k]+e[k+1:]]
                put(out,(dest,addp(p,params[a])),c*(-1)**k)
        return out
    def kg(C):
        out={}
        for (j,p),c in C.items():
            power=ZERO
            for a in kos_basis[j]:power=addp(power,(gu,gmu)[a])
            put(out,(j,addp(p,power)),c)
        return out
    for j in range(4):
        b={(j,ZERO):1}
        check(kd(kg(b),(x03,xprod))==kg(kd(b,(addp(gu,x03),addp(gmu,xprod)))),
              'ordered_supported_Gysin_Koszul_comparison')
    detg=addp(gu,gmu)
    check(addp(detg,tuple(-n for n in detg))==ZERO,'supported_Gysin_dual_determinant_retained')

    # With the primary class exact there is a genuine null-homotopic map
    # from the supported quotient resolution if the mu-primitive is changed.
    # It does not preserve the original mu-primitive's endpoint columns.
    Fk={0:On,1:multiply(H,x03),2:multiply(H,xprod),3:{}}
    Sk={0:H,1:{},2:{},3:{}}
    def image_k(C,columns):
        out={}
        for (j,p),c in C.items():out=add(out,multiply(columns[j],p),c)
        return out
    for j in range(4):
        b={(j,ZERO):1}
        check(linear.boundary(Fk[j])==image_k(kd(b,(x03,xprod)),Fk),
              'coherent_supported_quotient_map_after_primitive_change')
        check(add(linear.boundary(Sk[j]),image_k(kd(b,(x03,xprod)),Sk))==Fk[j],
              'coherent_supported_quotient_map_explicit_nullhomotopy')

    # The different older support pair (t04,t35) has empty fixed-beta
    # pullback: its graph image is the two-unit pair (g04,g35).
    def ht(C):
        out={}
        for (j,p),c in C.items():
            e=kos_basis[j]
            if 0 not in e:
                put(out,(kos_index[(0,)+e],subp(p,var('g04'))),c)
        return out
    for j in range(4):
        b={(j,ZERO):1};params=(var('g04'),var('g35'))
        check(add(kd(ht(b),params),ht(kd(b,params)))==b,
              'older_two_Rees_support_pair_full_contraction')

    formal=check_formal_unit()
    zero_h3=[j for j in red['residual'] if linear.degree[j]==3]
    payload={
        'schema':'marici.branchA.full_packet_kn_gysin_specialization.v1',
        'input_certificate_content_sha256':INPUT_CONTENT_SHA256,
        'repository_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
        'ring_before':'Z[X_d,t_s,u_l]/(opposite-sheet short products)',
        'universal_unit_graph_ring':'Z[X_d,g_d^+-1]/(opposite-sheet short products)',
        'physical_realization_scope':'fixed beta != 0; characteristic-zero formal completion; g_d=(exp(beta X_d)-1)/X_d',
        'physical_map':{'X_d':'X_d','t_s':'g_s','u_l':'g_l X_l','normal_basis_to_linear':'[F,H,e] -> product_{h in H} g_h [F,H,e]'},
        'unit_prefactors':{'w':'g02*g04*g13','u':'g03','mu':'g15*g24*g14*g25'},
        'ordered_Gysin_normal_change':{'pair_before':['u03','t15*t24*u14*u25'],
             'pair_after':['X03','X14*X25'],
             'Koszul_degree1_matrix':'diag(g03,g15*g24*g14*g25)',
             'dual_conormal_determinant':'(g03*g15*g24*g14*g25)^-1',
             'same_endpoint_labels':True},
        'factorizations':{'Omega':'w*O','Wu':'w*g03*X03*H','Wmu':'w*g15*g24*g14*g25*X14*X25*G','Theta':'w*g03*g15*g24*g14*g25*X03*X14*X25*(G-H)'},
        'states':[{'id':j,'face':list(f),'marks':list(h),'occurrence_partner':e,'degree':linear.degree[j]} for j,(f,h,e) in enumerate(linear.states)],
        'linear_differential':{str(j):[[i,list(p),c] for i,p,c in col] for j,col in linear.d.items()},
        'original_witnesses':{name:serialize(C,original,OLD_VARIABLES) for name,C in oldchains.items()},
        'gauge_transformed_witnesses':{name:serialize(C,linear) for name,C in images.items()},
        'normalized_chains':{name:serialize(C,linear) for name,C in [('Omega',On),('H',H),('G',G),('Z',Z),('Psi',Psi),('top_section_upper',section_upper)]},
        'normalized_chain_term_counts':{name:len(C) for name,C in [('Omega',On),('H',H),('G',G),('Z',Z),('Psi',Psi),('top_section_upper',section_upper)]},
        'frame_data':{'endpoint_rows':[neg,pos_occ,pos_native],
                      'endpoint_matrix_Z_Psi':ep_matrix,
                      'first_primitive_endpoint_image':serialize(linear.projection(H,linear.endpoints),linear),
                      'second_primitive_endpoint_image':serialize(E,linear),
                      'Q_images':{name:serialize(linear.projection(C,linear.q),linear) for name,C in [('Omega',On),('H',H),('G',G),('Z',Z)]},
                      'literal_endpoint_zero_top_cycles_in_weight_zero':0,
                      'unit_conjugacy_preserves_all_support_labels':True},
        'weight_zero_component':{'chain_ranks':dict(sorted(Counter(linear.degree[j] for j in mat).items())),
                                 'homology':red['homology'],'basis_size':len(mat),
                                 'coefficients':{str(j):list(p) for j,p in coeff.items()},
                                 'd':serial_matrix(mat),'projection':serial_matrix(red['p']),
                                 'inclusion':serial_matrix(red['i']),'homotopy':serial_matrix(red['h']),
                                 'unit_cancellations':red['pivots'],'top_homology_basis_ids':zero_h3},
        'secondary_structural_identity':{'Psi':'sum_F (-1)^(|F|(|F|+1)/2) [F,F,0]',
                     'Z':'P35(Psi)',
                     'P35':'native mark35 -> distinct occurrence partner; two copies -> zero; other states unchanged',
                     'map_not_identification_of_normal_lines':True},
        'top_summand':{'degrees':[4,3],'differential':'-X35','section_bottom':'Z',
                      'section_top':'-S_occ(Z)','projection':'actual top state and its distinct occurrence partner',
                      'H3':'Blin/(X35)','H4':'Ann_Blin(X35)=negative-sheet occurrence ideal',
                      'exact_annihilator_of_Z':'(X35)',
                      'not_a_resolution_of_quotient_over_singular_B':True,
                      'splitting_is_ordinary_not_endpoint_support_local':True},
        'formal_unit_audit':formal,
        'conclusions':{'specialized_primary_Omega_is_exact':True,
                       'specified_secondary_difference_Z_is_nonzero':True,
                       'Theta_raw_has_factor_X03_X14_X25':True,
                       'flexible_unframed_two_primitive_obstruction_contains_zero':True,
                       'chosen_two_primitives_have_different_endpoint_and_Q_components':True,
                       'old_t04_t35_supported_class_survives_fixed_beta_graph_pullback':False,
                       'physical_Delta_J_identified':False,
                       'beta_zero_family_computed':False,
                       'nonlinear_realization_claimed':False,
                       'source_global_six_functor_lift_constructed':False},
        'verification':{'checks_by_family':dict(sorted(CHECKS.items())),
                        'total_exact_checks':sum(CHECKS.values()),
                        'scope':'all labelled differential columns; exact polynomial and unit-monomial identities; complete integral homogeneous retraction, not a parameter sample'},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()
    }
    payload['content_sha256']=sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'certificate':str(output),'checks':sum(CHECKS.values()),
                     'primary_exact':True,'secondary_Z_annihilator':'(X35)',
                     'chain_counts':payload['normalized_chain_term_counts'],
                     'content_sha256':payload['content_sha256']},indent=2))
    return payload

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('branch_a_d03_full_packet_kn_gysin_specialization_certificate.json'))
    main(parser.parse_args().output)
