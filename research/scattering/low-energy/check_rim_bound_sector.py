"""Exact full-rim point-sector audit; no owner solver or protocol is executed."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
from check_rim_threshold import audit as threshold_audit, inverse, SOURCE
from check_low_energy_net_v4 import ROOT, multiply as mm, transpose as tr, identity as eye, load

HOME=Path(__file__).resolve().parent
PROOF=HOME/'RIM-BOUND-SECTOR.md'
RESULT=HOME/'results/rim-bound-sector.v1.json'


def rref(A):
    A=copy.deepcopy(A);pivots=[];r=0
    for j in range(len(A[0])):
        p=next((i for i in range(r,len(A)) if A[i][j]),None)
        if p is None:continue
        A[p],A[r]=A[r],A[p];d=A[r][j];A[r]=[v/d for v in A[r]]
        for i in range(len(A)):
            if i!=r:
                c=A[i][j];A[i]=[a-c*b for a,b in zip(A[i],A[r])]
        pivots.append(j);r+=1
        if r==len(A):break
    return A,pivots


def nullspace(A):
    R,pivots=rref(A);n=len(A[0]);vectors=[]
    for free in range(n):
        if free in pivots:continue
        v=[Q(int(i==free)) for i in range(n)]
        for row,p in enumerate(pivots):v[p]=-R[row][free]
        vectors.append(v)
    return tr(vectors)


def inertia(A):
    """Symmetric rational congruence, including zero-diagonal 2x2 pivots."""
    A=copy.deepcopy(A);assert A==tr(A);pos=neg=zero=0
    while A:
        n=len(A);p=next((i for i in range(n) if A[i][i]),None)
        if p is not None:
            order=[p]+[i for i in range(n) if i!=p]
            A=[[A[i][j] for j in order] for i in order];d=A[0][0]
            pos+=int(d>0);neg+=int(d<0)
            A=[[A[i][j]-A[i][0]*A[0][j]/d for j in range(1,n)] for i in range(1,n)]
        else:
            pair=next(((i,j) for i in range(n) for j in range(i+1,n) if A[i][j]),None)
            if pair is None:zero+=n;break
            order=list(pair)+[i for i in range(n) if i not in pair]
            A=[[A[i][j] for j in order] for i in order];b=A[0][1];pos+=1;neg+=1
            A=[[A[i][j]-(A[i][0]*A[1][j]+A[i][1]*A[0][j])/b for j in range(2,n)] for i in range(2,n)]
    return pos,neg,zero


def add(A,B):return [[a+b for a,b in zip(r,s)] for r,s in zip(A,B)]
def scale(c,A):return [[c*a for a in r] for r in A]
def encode(A):return [[str(v) for v in row] for row in A]
def zeros(A):return all(not a for row in A for a in row)


def finite_audit():
    threshold=threshold_audit() # Fresh positive metric/source and full threshold inverse.
    src=load(ROOT/SOURCE)
    full=[[Q(v) for v in row] for row in src['full_joint_H_without_mu']]
    M=[[Q(v) for v in row[2:]] for row in src['source_metric'][2:]]
    K=[row[2:] for row in full[2:]];g=Q(src['parameters']['g'])
    B=[[v/g for v in row[:2]] for row in full[2:]]
    S=scale(Q(1,3),mm(tr(B),M));assert mm(S,B)==eye(2)
    P=mm(B,S);basis=[];queue=tr(B);cursor=0
    while cursor<len(queue):
        v=queue[cursor];cursor+=1
        if len(rref(basis+[v])[1])>len(basis):
            basis.append(v);queue.append([row[0] for row in mm(K,tr([v]))])
    V=tr(basis);assert len(basis)==5
    D=nullspace(mm(tr(V),M));assert len(D[0])==19
    def restrict(T):
        gram=mm(mm(tr(T),M),T);left=mm(mm(inverse(gram),tr(T)),M)
        small=mm(mm(left,K),T)
        assert mm(K,T)==mm(T,small)
        return gram,left,small
    Hb,Lb,Kb=restrict(V);Hd,Ld,Kd=restrict(D)
    assert zeros(mm(S,D)) and zeros(mm(mm(tr(V),M),D))
    Pd=mm(D,Ld);Pb=mm(V,Lb)
    assert add(Pd,Pb)==eye(24) and mm(Pd,Pd)==Pd
    assert mm(Pd,K)==mm(K,Pd) and zeros(mm(Pd,B))
    assert mm(M,Pd)==tr(mm(M,Pd))
    pb=mm(mm(Lb,P),V)
    assert inertia(mm(Hb,Kb))[1]==inertia(mm(Hd,Kd))[1]==0
    assert inertia(mm(Hb,pb))==(2,0,3) and mm(pb,pb)==pb
    theta=Q(1,2)
    dark_zero=inertia(mm(Hd,Kd));dark_edge=inertia(mm(Hd,add(Kd,scale(-theta,eye(19)))))
    def secular(q):return add(add(Kb,scale(q*q-theta,eye(5))),scale(2*q/(1+q),pb))
    def at(q):return inertia(mm(Hb,secular(q)))
    edge=at(Q(0));far=at(Q(1));assert edge==(3,2,0) and far==(5,0,0)
    assert dark_zero==(13,0,6) and dark_edge==(13,6,0)
    # Exact rational bisection in q=sqrt(theta-E); no source numerical roots used.
    pending=[(Q(0),Q(1),edge,far)];brackets=[]
    while pending:
        lo,hi,a,b=pending.pop();count=a[1]-b[1]
        if not count:continue
        if count==1 and hi*hi-lo*lo<=Q(1,10**12):
            assert a[2]==b[2]==0
            elo,ehi=theta-hi*hi,theta-lo*lo;assert 0<elo<ehi<theta
            brackets.append({'decay_interval':[str(lo),str(hi)],'energy_interval':[str(elo),str(ehi)],
                'inertia_at_low_decay':list(a),'inertia_at_high_decay':list(b),'multiplicity':1})
        else:
            mid=(lo+hi)/2;c=at(mid);assert c[2]==0,'rational root: use an exact-root certificate'
            pending.extend(((lo,mid,a,c),(mid,hi,c,b)))
    brackets.sort(key=lambda b:Q(b['energy_interval'][0]));assert len(brackets)==2
    assert Q(brackets[0]['energy_interval'][1])<Q(brackets[1]['energy_interval'][0])
    standard_zero=[j for j in range(24) if all(not K[i][j] for i in range(24)) and all(Pd[i][j]==int(i==j) for i in range(24))]
    assert standard_zero==list(range(18,24))
    controls=[]
    for name in ('erase-dark-sector','miscount-accessible-roots','call-all-modes-below-threshold'):
        try:
            if name=='erase-dark-sector':assert zeros(Pd)
            elif name=='miscount-accessible-roots':assert edge[1]-far[1]==1
            else:assert dark_edge[0]==0
        except AssertionError:controls.append(name)
        else:raise AssertionError('hostile control accepted: '+name)
    return {'schema':'marici.scattering.rim-bound-sector.v1','status':'pass',
        'accessible_core_dimension':5,'dark_core_dimension':19,'accessible_basis':encode(V),'dark_basis':encode(D),
        'dark_core_operator':encode(Kd),'dark_core_inertia':list(dark_zero),'dark_core_minus_threshold_inertia':list(dark_edge),
        'standard_core_coordinates_with_zero_energy_and_pure_dark_projection':standard_zero,
        'accessible_secular_at_zero_decay_inertia':list(edge),'accessible_secular_at_unit_decay_inertia':list(far),
        'accessible_simple_bound_modes':2,'certified_accessible_bound_brackets':brackets,
        'total_point_subspace_dimension':21,'point_modes_below_threshold_counted_with_multiplicity':dark_edge[1]+2,
        'embedded_point_modes_counted_with_multiplicity':dark_edge[0],
        'no_point_mode_at_threshold':True,'dark_projector':'D (D^T M D)^(-1) D^T M',
        'physical_core_norm':'x* M x / 3',
        'retention_bound':'For initially central x0, core probability at all times >= ||P_D x0||_(M/3)^2.',
        'source_dark_sector_already_retained':True,'source_stationary_solver_replayed':False,
        'singular_continuous_absence_proved_here':False,'wave_operator_completeness_proved_here':False,
        'analytic_argument_machine_formalized':False,
        'new_live_proposition_admitted':False,'C12_protocol_renewed':False,'physical_outcomes_admitted':False,
        'hostile_controls_refused':controls},threshold


def build():
    result,threshold=finite_audit()
    paths={ROOT/p for p in threshold['source_sha256']}
    paths.update((Path(__file__),PROOF,HOME/'test_rim_bound_sector.py'))
    result['source_sha256']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert load(RESULT)==r,'stale rim bound-sector receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    keys=('status','dark_core_dimension','dark_core_inertia','dark_core_minus_threshold_inertia','accessible_simple_bound_modes',
          'total_point_subspace_dimension','point_modes_below_threshold_counted_with_multiplicity','embedded_point_modes_counted_with_multiplicity','hostile_controls_refused')
    print(json.dumps({k:r[k] for k in keys}))


if __name__=='__main__':main()
