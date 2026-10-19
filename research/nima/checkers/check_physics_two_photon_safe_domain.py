"""Exact maximal initial N=2 domain for the fixed three-bin cavity/detector route."""
import argparse
import itertools
import json
from fractions import Fraction as F
from pathlib import Path
import check_physics_geometric_candidate as G

ROOT=G.ROOT
CONTRACT='research/nima/contracts/physics-two-photon-safe-domain.v1.json'


def constraints(bs):
    rows=[[] for _ in range(3)]
    for b in bs:
        state={b:F(1)}
        for k in range(3):
            state=G.lift_state(G.round_map(k),state);port=2+3*k
            rows[k].append(state.get(G.occupation([port,port]),F(0)))
            state={o:a for o,a in state.items() if o[port]==0}
    return rows


def rref(rows):
    a=[list(row) for row in rows];pivots=[];r=0
    for col in range(len(a[0])):
        p=next((i for i in range(r,len(a)) if a[i][col]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r];scale=a[r][col];a[r]=[v/scale for v in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][col]:
                q=a[i][col];a[i]=[u-q*v for u,v in zip(a[i],a[r])]
        pivots.append(col);r+=1
        if r==len(a):break
    return a,pivots


def null_basis(rows):
    reduced,pivots=rref(rows);out=[]
    for col in range(len(rows[0])):
        if col in pivots:continue
        v=[F(0)]*len(rows[0]);v[col]=F(1)
        for row,pivot in enumerate(pivots):v[pivot]=-reduced[row][col]
        G.require(all(sum(a*b for a,b in zip(row,v))==0 for row in rows),'nullspace construction')
        out.append(v)
    return out,pivots


def route(state,memory,word):
    branches=[(memory,state)]
    for k,y in enumerate(word):branches=G.instrument(2+3*k,y,G.evolve(G.round_map(k),branches))
    return branches


def main():
    p=argparse.ArgumentParser();p.add_argument('--pin',action='store_true');args=p.parse_args()
    c=G.load(CONTRACT);paths={CONTRACT}|set(c['source_evidence']);pin=ROOT/c['source_pins']
    if args.pin:
        G.require(not pin.exists(),'refusing implicit re-pin')
        pin.write_text(json.dumps({'source_sha256':{p:G.sha(p) for p in sorted(paths)}},indent=2)+'\n',encoding='utf-8')
    pins=G.load(c['source_pins']);G.require(set(pins['source_sha256'])==paths,'pin coverage')
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source drift: '+path)
    G.require(c['decision']=='constructed_conditional_maximal_horizon_domain' and c['horizon']==3
              and c['routed_ports']==[2,5,8] and c['physical_transport_admitted'] is False,'scope/schedule promotion')
    bs=G.basis(2);rows=constraints(bs);vectors,pivots=null_basis(rows)
    G.require(len(bs)==55 and len(pivots)==3 and len(vectors)==52,'domain dimension')
    counts=0
    # Linearly independent safe basis states and their pair sums test interference.
    probes=vectors+[ [a+b for a,b in zip(vectors[i],vectors[i+1])] for i in range(len(vectors)-1)]
    for v in probes:
        state={b:a for b,a in zip(bs,v) if a};norm=G.inner(state,state)
        for memory in ('R','D'):
            total=F(0)
            for word in itertools.product('CN',repeat=3):
                result=route(state,memory,word);total+=G.probability(result);counts+=1
            G.require(total==norm,'safe complete-outcome normalization')
    # Each row is necessary: solve preceding rows and force that earliest row nonzero.
    witnesses=[]
    for k in range(3):
        candidates=([ [F(i==j) for i in range(len(bs))] for j in range(len(bs))]
                    if k==0 else null_basis(rows[:k])[0])
        v=next(v for v in candidates if sum(a*b for a,b in zip(rows[k],v)))
        state={b:a for b,a in zip(bs,v) if a}
        for j in range(k):
            state=G.lift_state(G.round_map(j),state)
            state={o:a for o,a in state.items() if o[2+3*j]==0}
        before=G.lift_state(G.round_map(k),state)
        amplitude=before.get(G.occupation([2+3*k,2+3*k]),F(0))
        G.require(amplitude!=0,'earliest violated-row witness')
        try:G.instrument(2+3*k,'N',[('R',before)])
        except ValueError:pass
        else:raise AssertionError('unsafe domain input silently projected')
        witnesses.append({'earliest_failed_bin':k,'forbidden_coefficient':str(amplitude),
                          'forbidden_norm_in_unscaled_zero_absorption_branch':str(2*amplitude**2)})
    # The two-photon state from the previous assembly counterexample fails c0.
    bad=G.occupation([0,1]);bad_col=bs.index(bad)
    G.require(rows[0][bad_col]!=0,'lost earlier assembly obstruction')
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source changed during check')
    out={'schema':c['schema'],'status':'pass','initial_sector_dimension':len(bs),
         'independent_schedule_constraints':len(pivots),'maximal_safe_dimension':len(vectors),
         'pivot_occupancies':[list(bs[p]) for p in pivots],'constraint_rows':[[str(x) for x in row] for row in rows],
         'safe_basis_and_interference_probes':len(probes),'complete_history_evaluations':counts,
         'earliest_failure_witnesses':witnesses,'physical_transport_admitted':False,
         'source_sha256':pins['source_sha256'],'checker_sha256':G.sha(Path(__file__))}
    (ROOT/c['result']).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ('source_sha256','constraint_rows')},indent=2))

if __name__=='__main__':main()
