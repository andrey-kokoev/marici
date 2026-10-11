"""Exact minimal linear-quadratic observer closure for the memory swap.
Physical record subspace has zero record mean. No new dynamics is added.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from check_four_packet_record_feedback import mm,transpose,basis,rank
from check_twelve_triangle_positive_geometry import POINTS,mean
from check_phase_memory_first_moment import step
ROOT=Path(__file__).resolve().parents[1]
n=12

def add(a,b):return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def scale(a,c):return tuple(tuple(c*x for x in row) for row in a)
def block(a,b,c,d):return tuple(tuple(r)+tuple(s) for r,s in zip(a,b))+tuple(tuple(r)+tuple(s) for r,s in zip(c,d))
def diag(v):return tuple(tuple(v[i] if i==j else F(0) for j in range(n)) for i in range(n))
def evaluate(a,z):return sum(z[i]*sum(w*v for w,v in zip(row,z)) for i,row in enumerate(a))
def main():
    rows=json.loads((ROOT/'results/twelve-triangle-positive-geometry.json').read_text())['triangles_and_transports']
    points=dict(POINTS)
    for row in rows:
        f=row['triangle'][0];points[f]=mean([POINTS[k] for k in f[2:]])
    positions=[mean([(F(0),)*3]+[points[k] for k in row['triangle']]) for row in rows]
    P=tuple((F(1,n),)*n for _ in range(n));I=basis(n);Z=scale(I,0);Q=add(I,scale(P,-1))
    U=block(P,Q,Q,P)
    # Coordinate embedding: all 12 carrier coefficients and 11 independent
    # record contrasts r_k=e_k-e_11. The induced metric need not be identity.
    columns=[tuple(e)+(F(0),)*12 for e in I]
    for k in range(11):columns.append((F(0),)*12+tuple(F(int(i==k)-int(i==11)) for i in range(12)))
    embedding=transpose(tuple(columns))
    restrict=lambda a:mm(mm(transpose(embedding),a),embedding)
    evolve=lambda a:mm(mm(transpose(U),a),U)
    obs={'A':block(I,Z,Z,Z),'B':block(Z,Z,Z,I),'h':block(P,Z,Z,Z)}
    for k,label in enumerate('xyz'):
        X=diag(tuple(p[k] for p in positions));PX=mm(P,X);XP=mm(X,P)
        assert mm(PX,P)==Z
        obs['a'+label]=block(X,Z,Z,Z)
        obs['b'+label]=block(Z,Z,Z,X)
        obs['s'+label]=block(add(PX,XP),Z,Z,Z)
        obs['r'+label]=block(Z,PX,XP,Z)
    expected={'A':add(obs['h'],obs['B']),'B':add(obs['A'],scale(obs['h'],-1)),'h':obs['h']}
    for label in 'xyz':
        expected['a'+label]=add(obs['b'+label],obs['r'+label])
        expected['b'+label]=add(obs['a'+label],scale(obs['s'+label],-1))
        expected['s'+label]=obs['r'+label];expected['r'+label]=obs['s'+label]
    for name,a in obs.items():assert restrict(evolve(a))==restrict(expected[name])
    original=[obs[k] for k in ('A','B','ax','bx','ay','by','az','bz')]
    flat=lambda a:sum(restrict(a),())
    assert rank(tuple(flat(a) for a in original))==8
    assert rank(tuple(flat(a) for a in original+[evolve(a) for a in original]))==15
    assert rank(tuple(flat(a) for a in obs.values()))==15
    # Direct checks on actual three-step histories and general rational states.
    controls=0
    i=next(k for k,r in enumerate(rows) if r['outer_arrow']=='AB');j=next(k for k,r in enumerate(rows) if r['outer_arrow']=='BA')
    for sign in (-1,1):
        x=tuple(F(1)+sign*(int(k==i)-int(k==j)) for k in range(n));r=(F(0),)*n
        for _ in range(3):
            current=x+r;xx,rr=step(x,r);next_state=xx+rr
            for name in obs:assert evaluate(obs[name],next_state)==evaluate(expected[name],current)
            x,r=xx,rr;controls+=1
    for t in range(5):
        x=tuple(F((k+1)*(t+2)-k*k,7) for k in range(n))
        raw=tuple(F(k*k+t*k,11) for k in range(n));avg=sum(raw)/n;r=tuple(v-avg for v in raw)
        xx,rr=step(x,r)
        for name in obs:assert evaluate(obs[name],xx+rr)==evaluate(expected[name],x+r)
        controls+=1
    result=dict(schema='marici.nima.closed-phase-moment-observer.v1',status='pass',
        original_quadratic_readout_dimension=8,closed_dimension=15,additional_independent_readouts=7,
        closure={'budgets':'A_next=h+B; B_next=A-h; h_next=h',
                 'first_moments':'a_next=b+r; b_next=a-s',
                 'phase_correlations':'s_next=r; r_next=s'},
        definitions={'h':'||P x||^2','s_j':'2 Re((P x)^dagger X_j x)','r_j':'2 Re((P x)^dagger X_j record)'},
        exact_operator_identities=15,direct_transition_controls=controls,
        minimality='The span of the eight original quadratic forms and their evolved forms has dimension 15 on the zero-mean record subspace. This is minimal among linear spaces of quadratic readouts containing those forms, not among arbitrary nonlinear encodings.',
        normalization='All quantities here use coefficient weights. Multiply by 20/3 for the prior mode-norm convention; barycenters are unchanged ratios.',
        scope='Closed observation of the conditional memory swap, not amplitude reconstruction, a physical energy law or a new particle mechanism.')
    (ROOT/'results/closed-phase-moment-observer.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
