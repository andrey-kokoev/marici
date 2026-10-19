"""Typed finite chart extension; source-native and supplied costs stay symbolic."""
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
from electron_packet_interface import ACTIONS,I,F,E,act,adj,gmm,sm,G0,G1,norm
from check_electron_three_direction_trial import chart

GRID=tuple(product((F(-1),F(0),F(1)),repeat=3))
CHARTS={u:chart(u) for u in GRID}
def key(matrix): return sha256(repr(matrix).encode()).hexdigest()
def neighbors(u,v):
    return u in CHARTS and v in CHARTS and sum(abs(x-y) for x,y in zip(u,v))==1
EDGES=tuple((u,v) for u in GRID for v in GRID if neighbors(u,v))

def matrix(u,v):
    if not neighbors(u,v): raise ValueError('edge domain')
    return gmm(CHARTS[v],adj(CHARTS[u]))

def admit(mode,current,u,v):
    if mode not in ('native_only','supplied_grid'): raise ValueError('unknown policy')
    if current!=u: raise ValueError('source vertex guard')
    T=matrix(u,v)
    if mode=='native_only' and T not in ACTIONS: raise ValueError('nonnative capability')
    return T

def cost_token(T):
    return {'symbol':('c_native:' if T in ACTIONS else 'c_supplied:')+key(T),
            'native':T in ACTIONS,'numeric_primitive_cost':None}

@dataclass(frozen=True)
class ChartState:
    vertex:tuple
    spinor:tuple
    reference:tuple
    start:tuple
    edge_word:tuple=()

def validate(mode,s):
    if s.start not in CHARTS or norm(s.reference)!=G1: raise ValueError('reference/start')
    current=s.start
    for u,v in s.edge_word:
        admit(mode,current,u,v);current=v
    if current!=s.vertex or s.spinor!=act(CHARTS[current],s.reference):
        raise ValueError('chart state/history')

def seed(mode,reference,start):
    s=ChartState(start,act(CHARTS[start],reference),reference,start)
    validate(mode,s)
    return s

def step(mode,s,u,v):
    validate(mode,s)
    T=admit(mode,s.vertex,u,v)
    return ChartState(v,act(T,s.spinor),s.reference,s.start,s.edge_word+((u,v),))

def ledger(word):
    # Deliberately no matrix multiplication, cancellation or numerical valuation.
    return tuple(cost_token(matrix(u,v)) for u,v in word)
