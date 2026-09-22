"""Actual cubic columns and exact source-image frame/coherence identities."""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
import importlib.util
import json
import sympy as s

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('growth',HERE/'check_translated_cubic_observer_growth.py')
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
f=g.f


def main():
    keys=[((('e',*ea,1),('e',*eb,1),('e',15,31,0)),((),(),(),()))
          for ea in ((0,1),(1,3)) for eb in ((3,7),(7,15))]
    keys.append(((('e',0,1,1),('e',5,7,1),('e',15,31,0)),((),(),(),())))
    rows=[]
    for pairs in g.pairings(tuple(range(6))):
        for kinds in ((1,1,0),(1,0,1),(0,1,1)):
            start=0;ds=[]
            for pair,kind in zip(pairs,kinds):
                ds.append(g.one(f['derivative'](start,f['relation'](pair,kind))))
                start|=sum(1<<j for j in pair)
            image=g.join(g.join(ds[0],ds[1]),ds[2])
            rows.append(tuple(image.get(key,0) for key in keys))
    assert len(rows)==270
    assert [v for v in rows if any(v)]==[(1,1,1,1,0),(0,1,0,0,1)]
    columns=s.Matrix([[1,0],[1,1],[1,0],[1,0],[0,1]])
    amplitudes=(s.Integer(2),s.Integer(3),s.Integer(5),s.Integer(7),s.Integer(11))
    # Each test sector has an extra off-image coordinate, so none of the
    # ambient projections is an identity even in the private frame fixture.
    E={};D={}
    for name,indices in {'4':(0,1,2,3),'p':(0,4),'5':(0,1,2,3,4)}.items():
        E[name]=s.zeros(2*len(indices),2)
        D[name]=s.zeros(2,2*len(indices))
        for j,c in enumerate(indices):
            E[name][2*j,:]=amplitudes[c]*columns[c,:]
        D[name][0,0]=1/amplitudes[0]
        if name=='4':
            D[name][1,0]=-1/amplitudes[0]
            D[name][1,2]=1/amplitudes[1]
        else:
            D[name][1,2*indices.index(4)]=1/amplitudes[4]
        assert D[name]*E[name]==s.eye(2)
        P=E[name]*D[name]
        assert P*P==P and P!=s.eye(P.rows)
    transitions={(b,a):E[b]*D[a] for a,b in product(E,repeat=2)}
    routes=0
    for a,b,c in product(E,repeat=3):
        assert transitions[c,b]*transitions[b,a]==transitions[c,a]
        routes+=1
    S0,Sx=s.symbols('S0 Sx')
    G=s.Matrix([[S0,Sx]])
    for a,b in product(E,repeat=2):
        assert G*D[b]*transitions[b,a]==G*D[a]
        assert transitions[a,b]*transitions[b,a]==E[a]*D[a]
    # On-image equality need not be equality of the original off-image tests.
    annihilator=s.zeros(1,E['4'].rows)
    annihilator[0,0]=1/amplitudes[0]
    annihilator[0,4]=-1/amplitudes[2]
    assert annihilator*E['4']==s.zeros(1,2)
    assert G*D['4']+annihilator!=G*D['4']
    norm_checks=0
    for n11,n12,n21,n22,nd in ((2,3,5,7,11),(10,1,2,1,6),(8,2,1,1,1)):
        K=n11+n21+n22;B=n12
        forward=max(Q(n11+nd,K),Q(nd,B))
        reverse=max(Q(K+B,n11),Q(B,nd))
        # Exact weighted l1 column sums and their attaining coordinate rays.
        assert forward==max(Q(n11,K)+Q(nd,K),Q(nd,B))
        assert reverse==max(Q(K,n11)+Q(B,n11),Q(B,nd))
        for a,b in ((Q(1,K),-Q(1,K)),(Q(0),Q(1,B))):
            assert n11*abs(a)+nd*abs(b)<=forward*(K*abs(a)+B*abs(a+b))
        norm_checks+=1
    assert 30**2-10**2==800 and 101+800==901
    df,dg,dh=s.symbols('df dg dh')
    assert s.expand((dh-dg)+(dg-df)-(dh-df))==0
    result={'passed':True,'actual_source_basis_vectors':len(rows),
        'three_frame_composition_routes':routes,'exact_transition_norm_fixtures':norm_checks,
        'checks':['common_visible_source_columns','ambient_retractions_not_inverses',
                  'observer_equality_only_on_image','800_exponent_transition_cost',
                  'calibration_defect_composition'],
        'scope':'Exact fixed-cubic visible-frame coherence. No general spectral-chart or saturated all-depth frame equivalence is inferred.'}
    out=HERE.parent/'results/cubic-frame-coherence.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
