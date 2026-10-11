"""Conditional conservative memory lift of the existing 12-mode projector.
Retained record-swap mechanism, no fitted gain; bank/schedule remain explicit.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from check_twelve_triangle_positive_geometry import POINTS,mean
from check_four_packet_record_feedback import basis,mm,transpose,rank
ROOT=Path(__file__).resolve().parents[1]
N=12

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def project(a):return (sum(a)/N,)*N

def step(x,r):
    # Orthogonal swap of the discarded contrast, retaining the readable mean.
    return add(project(x),sub(r,project(r))),add(sub(x,project(x)),project(r))
def total(x,r):return F(20,3)*sum(t*t for t in x+r)
def moments(x,r,positions):
    wx=tuple(F(20,3)*a*a for a in x);wr=tuple(F(20,3)*a*a for a in r)
    def first(w):return tuple(sum(a*p[k] for a,p in zip(w,positions)) for k in range(3))
    def center(w):return tuple(a/sum(w) for a in first(w)) if sum(w) else None
    cross=tuple(F(40,3)*sum(a*b*p[k] for a,b,p in zip(x,r,positions)) for k in range(3))
    joint=add(add(first(wx),first(wr)),cross)
    return dict(active_budget=str(sum(wx)),record_budget=str(sum(wr)),
                active_center=None if center(wx) is None else list(map(str,center(wx))),
                record_center=None if center(wr) is None else list(map(str,center(wr))),
                incoherent_combined_center=list(map(str,center(add(wx,wr)))),
                cross_first_moment=list(map(str,cross)),
                recombined_first_moment=list(map(str,joint)))

def main():
    src=json.loads((ROOT/'results/twelve-triangle-positive-geometry.json').read_text())
    rows=src['triangles_and_transports'];pts=dict(POINTS)
    for row in rows:
        label=row['triangle'][0];pts[label]=mean([POINTS[k] for k in label[2:]])
    positions=[mean([(F(0),)*3]+[pts[k] for k in row['triangle']]) for row in rows]
    i=next(k for k,r in enumerate(rows) if r['outer_arrow']=='AB')
    j=next(k for k,r in enumerate(rows) if r['outer_arrow']=='BA')
    d=tuple(F(1) if k==i else F(-1) if k==j else F(0) for k in range(N))
    u=(F(1),)*N;zero=(F(0),)*N
    columns=[]
    for v in basis(24):
        a,b=step(v[:N],v[N:]);columns.append(a+b)
    U=transpose(tuple(columns))
    assert mm(transpose(U),U)==basis(24) and mm(U,U)==basis(24)
    contrast=tuple(tuple(F(i==j)-F(1,N) for j in range(N)) for i in range(N))
    assert rank(contrast)==11
    trajectories={};states={}
    for sign in (1,-1):
        initial=add(u,tuple(sign*a for a in d));x=initial;r=zero;budget=total(x,r)
        trace=[];history=[]
        for depth in range(4):
            assert total(x,r)==budget==F(280,3)
            assert sum(r)==0 and add(x,r)==initial
            row=moments(x,r,positions);row['depth']=depth;trace.append(row);history.append((x,r))
            assert row['recombined_first_moment']==trace[0]['recombined_first_moment']
            if depth<3:x,r=step(x,r)
        assert history[2]==history[0]
        assert trace[0]['active_center']==['1/12',str(F(sign,42)),str(F(-sign,42))]
        assert trace[1]['active_center']==['0','0','0']
        assert trace[1]['cross_first_moment']==['0',str(F(20*sign,9)),str(F(-20*sign,9))]
        trajectories[str(sign)]=trace;states[sign]=history
    # Same current intensities and budgets, different NEXT active first moment.
    intensity=lambda state:tuple(a*a for a in state[0]+state[1])
    assert intensity(states[1][1])==intensity(states[-1][1])
    assert intensity(states[1][2])!=intensity(states[-1][2])
    # Erasing the records prevents the return and loses their positive budget.
    erased=step(u,zero)
    assert erased==(u,zero) and total(*erased)==80
    result=dict(schema='marici.nima.phase-memory-first-moment.v1',status='pass',
        law='x_next=P x+(I-P)r; r_next=(I-P)x+P r',
        source='Orthogonal extension of the existing collective projector using the prior discarded-coordinate swap mechanism.',
        stored_contrast_dimension=11,formal_storage_coordinates=12,storage_constraint='sum(r)=0',
        exact_operator_checks=['orthogonal','involution','x+r invariant'],
        trajectories=trajectories,
        observer_obstruction='At depth one both runs have identical active and record intensities, but their next active first moments differ. Phase-blind observations are not closed under the supplied return.',
        conservation_scope='Total quadratic budget is conserved. Separate active/record intensity first moments need not sum to a conserved spatial moment. The cross-coherent readout restores the constant first moment of x+r; this is not a derived matter center-of-mass law.',
        boundary='Conditional memory bank and reuse schedule, not a newly selected physical interaction. No electron charge, mass, lifetime, force or recoil is derived. Three advances only.')
    (ROOT/'results/phase-memory-first-moment.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='trajectories'},indent=2))

if __name__=='__main__':main()
