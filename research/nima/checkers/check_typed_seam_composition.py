"""Finite all-state seam balancing, derived residuals, and scalar Green mates.

Memory multiplication is truncated at one common packet-wide capacity.
The source is the acyclic analytical path algebra with local letters 1,a,b.
"""
from itertools import product
from pathlib import Path
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
TAU=s.Rational(1,2)


def words(cap):
    return tuple(w for n in range(cap+1) for w in product(range(2),repeat=n))


def qword(w):
    return TAU**(2*len(w))*(-1)**sum(w)


def diag(values):
    return s.SparseMatrix(len(values),len(values),{(i,i):x for i,x in enumerate(values)})


def model(vertices, edges, cap):
    ws=words(cap)
    wi={w:i for i,w in enumerate(ws)}
    letters=((),(0,),(1,))
    c0=tuple((v,p,q) for v in vertices for p in ws for q in ws)
    c1=tuple((x,y,k,p,q) for x,y in edges for k in letters for p in ws for q in ws)
    i0={key:i for i,key in enumerate(c0)}
    i1={key:i for i,key in enumerate(c1)}
    d_entries={}
    for j,(x,y,k,p,q) in enumerate(c1):
        if len(p+k)<=cap:
            d_entries[i0[y,p+k,q],j]=1
        if len(k+q)<=cap:
            d_entries[i0[x,p,k+q],j]=-1
    d=s.SparseMatrix(len(c0),len(c1),d_entries)
    mu=s.SparseMatrix(len(ws),len(c0),{
        (wi[p+q],j):1 for j,(v,p,q) in enumerate(c0) if len(p+q)<=cap})
    assert mu*d==s.zeros(len(ws),len(c1))
    rank=d.rank()
    assert len(c0)-rank==len(ws)
    assert mu.rank()==len(ws)

    # Source-generated nondegenerate product forms, not a positive state.
    q0=[qword(p)*qword(q) for v,p,q in c0]
    q1=[qword(p)*qword(k)*qword(q) for x,y,k,p,q in c1]
    qr=[qword(w) for w in ws]
    Q0,Q1,QR=diag(q0),diag(q1),diag(qr)
    ds=diag([1/x for x in q1])*d.T*Q0
    mus=diag([1/x for x in q0])*mu.T*QR
    assert Q1*ds==d.T*Q0
    assert Q0*mus==mu.T*QR
    assert mus==mu.T  # Split the word and copy across cut vertices.
    assert mu*mus!=s.eye(len(ws))  # The mate is not an inverse.
    assert ds*mus==s.zeros(len(c1),len(ws))
    # Cochain dual differential is -d^sharp, from degree zero to one.
    assert -d.T*Q0==Q1*(-ds)

    # Shared-total-budget part is a subcomplex, not the whole derived tensor.
    low0=[i for i,(v,p,q) in enumerate(c0) if len(p+q)<=cap]
    low1=[i for i,(x,y,k,p,q) in enumerate(c1) if len(p+k+q)<=cap]
    high0=[i for i in range(len(c0)) if i not in low0]
    assert d.extract(high0,low1)==s.zeros(len(high0),len(low1))
    dl=d.extract(low0,low1)
    rank_low=dl.rank()
    assert len(low0)-rank_low==len(ws)

    # A full-memory basis class in degree -1: both actions overflow.
    top=(0,)*cap
    overflow=i1[edges[0][0],edges[0][1],(0,),top,top]
    assert d[:,overflow]==s.zeros(len(c0),1)
    assert overflow not in low1

    # Explicit degree-zero graph cycle if the diamond is present.
    cycle_test=False
    if tuple(vertices)==(2,4,6,12):
        cycle=s.zeros(len(c1),1)
        for edge,coefficient in zip(((2,4),(4,12),(2,6),(6,12)),(1,1,-1,-1)):
            cycle[i1[edge[0],edge[1],(),(),()],0]=coefficient
        assert cycle!=s.zeros(len(c1),1)
        assert d*cycle==s.zeros(len(c0),1)
        assert all(i in low1 for i,x in enumerate(cycle) if x)
        cycle_test=True
    return {
        'memory_dimension':len(ws),'complex_dimensions_minus_one_zero':[len(c1),len(c0)],
        'differential_rank':rank,'H_minus_one_dimension':len(c1)-rank,
        'H_zero_dimension':len(c0)-rank,
        'shared_budget_dimensions_minus_one_zero':[len(low1),len(low0)],
        'shared_budget_H_minus_one_dimension':len(low1)-rank_low,
        'shared_budget_H_zero_dimension':len(low0)-rank_low,
        'balanced_counit_chain_map':True,'signed_mates_and_dual_complex':True,
        'explicit_overflow_class':True,'forgotten_diamond_cycle':cycle_test,
    }


def hostile_tests():
    # Seam action on the first factor cannot descend to joined memory.
    # (1|b)-(b|1) lies in ker(mu); inserting a gives ab-ba, not zero.
    a,b=(0,),(1,)
    def join_combination(terms):
        out={}
        for (p,q),coefficient in terms.items():
            out[p+q]=out.get(p+q,0)+coefficient
        return {w:c for w,c in out.items() if c}
    delta={((),b):1,(b,()):-1}
    assert join_combination(delta)=={}
    acted={(p+a,q):c for (p,q),c in delta.items()}
    assert join_combination(acted)=={a+b:1,b+a:-1}
    assert a+b!=b+a
    # Independent local capacity one also breaks an outer prefix action:
    # mu(c_L^1(a) a |1)=0 but c_L^2(a)mu(a|1)=aa.
    create_left=lambda letter,word,cap:letter+word if len(letter+word)<=cap else None
    assert create_left(a,a,1) is None
    assert create_left(a,a,2)==a+a
    # Genuine right-left balancing in a common truncated algebra, all states.
    cap=2
    ws=words(cap)
    multiply=lambda x,y:x+y if x is not None and y is not None and len(x+y)<=cap else None
    for x,y,z in product(ws,repeat=3):
        assert multiply(multiply(x,y),z)==multiply(x,multiply(y,z))

    # R-linear prefix dual is not the scalar Green dual: the latter kills vacuum.
    g=s.Matrix([1+s.I,2-s.I])
    wi={w:i for i,w in enumerate(ws)}
    left=s.SparseMatrix(7,7,{(wi[(j,)+w],wi[w]):g[j] for w in ws if len(w)<2 for j in range(2)})
    right=s.SparseMatrix(7,7,{(wi[w+(j,)],wi[w]):g[j] for w in ws if len(w)<2 for j in range(2)})
    Q=diag([qword(w) for w in ws])
    sharp=diag([1/qword(w) for w in ws])*right.conjugate().T*Q
    vacuum=s.eye(7)[:,0]
    assert left*vacuum!=s.zeros(7,1) and sharp*vacuum==s.zeros(7,1)
    assert left!=sharp
    return {'non_descending_internal_action_commutator':True,
            'independent_capacity_outer_action_hostile':True,
            'all_state_common_capacity_associativity':True,
            'prefix_module_dual_not_scalar_green_dual':True}


def forgotten_boundary_pushout():
    # Vertex order 2,4,6,12; edges 24,26,4-12,6-12.
    incidence=s.Matrix([[-1,-1,0,0],[1,0,-1,0],[0,1,0,-1],[0,0,1,1]])
    # Glue the two path pieces along BOTH endpoint lines.
    boundary=s.Matrix([[1,1],[-1,-1]])
    F0=s.Matrix([[1,1,0,1],[0,0,1,0]])
    F1=s.Matrix([[0,-1,0,0],[0,0,0,1]])
    G0=s.Matrix([[0,0],[1,0],[0,1],[0,0]])
    G1=s.Matrix([[1,0],[-1,0],[0,-1],[0,1]])
    H=s.zeros(4)
    H[0,0]=-1
    H[2,3]=1
    assert F0*incidence==boundary*F1
    assert incidence*G1==G0*boundary
    assert F0*G0==s.eye(2) and F1*G1==s.eye(2)
    assert incidence*H==s.eye(4)-G0*F0
    assert H*incidence==s.eye(4)-G1*F1
    cycle=s.Matrix([1,-1,1,-1])
    assert incidence*cycle==s.zeros(4,1)
    assert F1*cycle==s.Matrix([1,-1])
    assert boundary.rank()==1
    # Replacing the two endpoint boundary by one line removes the cycle.
    compressed=s.Matrix([1,-1])
    assert compressed.rank()==1 and compressed.cols-compressed.rank()==0
    return {'explicit_chain_deformation_retract':True,
            'two_endpoint_pushout_H_minus_one_dimension':1,
            'forgotten_cycle_maps_to_endpoint_difference':True,
            'single_endpoint_compression_loses_cycle':True}


def main():
    edge=model((0,1),((0,1),),2)
    diamond=model((2,4,6,12),((2,4),(2,6),(4,12),(6,12)),1)
    assert (edge['H_minus_one_dimension'],edge['H_zero_dimension'])==(56,7)
    assert edge['shared_budget_H_minus_one_dimension']==0
    assert (diamond['H_minus_one_dimension'],diamond['H_zero_dimension'])==(75,3)
    assert diamond['shared_budget_H_minus_one_dimension']==11
    result={
        'schema':'marici.nima.typed-seam-composition.v1','passed':True,
        'one_edge_capacity_two':edge,'diamond_capacity_one':diamond,
        'hostiles':hostile_tests(),
        'forgotten_diamond_boundary_closure':forgotten_boundary_pushout(),
        'scope':'Exact truncated two-letter memory fixtures for a free acyclic analytical path algebra. Mathematical derived-tensor identification is in the note. No equivalence of the full seam complex with terminal memory, no identification of prefix dual with Green contraction, and no physical inverse arrows are claimed.'}
    out=ROOT/'research/nima/results/typed-seam-composition.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
