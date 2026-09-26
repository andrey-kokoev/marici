"""Symbolic payload identities and termination rank for the fixed query-net topology."""
from copy import deepcopy
from pathlib import Path
import json
import sympy as s
from four_cell_query_net import construct_queries

records={}
for family in ('zero2','zero3'):
    residue=s.Symbol('r_'+family)
    for suffix,sign in (('E_B',-1),('F_B',1)):
        key=family+'_'+suffix
        records[key]={'family':family,'members':frozenset([key]),
                      'pole':sign*residue,
                      'value':s.symbols(key+'_c0:2')}
net=construct_queries(records)
expected=net.meanings()

def rank(net):
    weights={'EB':2,'FB':2,'VALUE':1,'READ':1,'OUT':0,'ANSWER':0}
    return sum(weights[kind] for kind,_ in net.nodes.values())

def signature(net):
    """Compare all port-labelled adjacency, payloads and boundaries modulo names.
    Every node has a unique constructor-derived semantic identifier in this domain.
    """
    def identity(n):
        kind,payload=net.nodes[n]
        if kind in ('OUT','READ'):return kind,tuple(payload)
        return kind,tuple(sorted(payload['members']))
    identities=[identity(n) for n in net.nodes]
    assert len(identities)==len(set(identities))
    nodes=tuple(sorted((identity(n),repr(payload)) for n,(_,payload) in net.nodes.items()))
    wires=tuple(sorted((identity(n),port,identity(m),other)
                       for (n,port),(m,other) in net.wires.items()))
    return nodes,wires

visited=set();edges=diamonds=terminals=0

def visit(state):
    global edges,diamonds,terminals
    key=signature(state)
    if key in visited:return
    visited.add(key)
    assert state.meanings()==expected
    choices=state.enabled()
    if not choices:
        assert state.completed()==4 and rank(state)==0
        terminals+=1
    for i,a in enumerate(choices):
        for b in choices[i+1:]:
            assert set(a).isdisjoint(b)
            ab=deepcopy(state);ab.step(a);assert b in ab.enabled();ab.step(b)
            ba=deepcopy(state);ba.step(b);assert a in ba.enabled();ba.step(a)
            assert signature(ab)==signature(ba)
            diamonds+=1
    for pair in choices:
        child=deepcopy(state);child.step(pair)
        assert rank(child)==rank(state)-2
        assert child.meanings()==state.meanings()
        edges+=1;visit(child)
visit(net)
assert terminals==1
# Arbitrary scalar weights on individually named channels remain unconstrained.
weights=s.symbols('weight0:4')
labels=sorted(expected)
weighted=tuple(s.expand(sum(weights[j]*expected[label][2][i]
                           for j,label in enumerate(labels))) for i in range(2))
assert all(all(v in expr.free_symbols for v in weights) for expr in weighted)
report={'passed':True,'symbolic_values':'eight independent component symbols; two arbitrary residue symbols',
 'unique_states_modulo_names':len(visited),'unique_state_edges':edges,
 'local_diamonds_checked':diamonds,'terminal_signatures':terminals,
 'rank':'2*(EB+FB) + VALUE + READ; decreases by exactly 2 per rule',
 'symbolic_channel_meanings_preserved':True,
 'scope':'All reachable schedules of this fixed two-family constructor with symbolic payloads. Algebraic payload checking is executable symbolic evidence; general finite-disjoint-union proof is written separately. Not arbitrary graph confluence or physical contour selection.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/four-cell-query-net-symbolic.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
