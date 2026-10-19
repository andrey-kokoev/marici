"""Independent density-route versus Fock-branch overlap, exact and model-only."""
import argparse
import copy
import itertools
import json
from fractions import Fraction as F
from pathlib import Path
import check_physics_geometric_candidate as G
import check_physics_observation_resource_interface as O

ROOT=G.ROOT
CONTRACT='research/nima/contracts/physics-overlap-catalog.v1.json'
MODES=tuple(range(-1,10))  # -1 is vacuum


def clean(d):return {k:v for k,v in d.items() if v}
def occ(mode):return G.VAC if mode==-1 else G.occupation([mode])
def mode(n):
    G.require(sum(n)<=1,'outside total single-excitation domain')
    return -1 if not any(n) else n.index(1)


def density(branches):
    out={}
    for memory,state in branches:
        for a,x in state.items():
            for b,y in state.items():
                key=((mode(a),memory),(mode(b),memory))
                out[key]=out.get(key,F(0))+x*y
    return clean(out)


def cp(rho,columns):
    out={}
    for cols in columns:
        for (a,b),x in rho.items():
            for c,u in cols.get(a,{}).items():
                for d,v in cols.get(b,{}).items():
                    out[c,d]=out.get((c,d),F(0))+x*u*v
    return clean(out)


def trace(rho):return sum(x for (a,b),x in rho.items() if a==b)


def port_columns(k):
    # Independent field-equation route; no call to G.round_map.
    cols={};active=(1+3*k,0,2+3*k,3+3*k)
    for memory in ('R','D'):
        for m in MODES:
            if m not in active:cols[m,memory]={(m,memory):F(1)};continue
            inputs=[F(i==active.index(m)) for i in range(4)]
            yr,yt,xn,ye=O.cavity(*inputs)
            cols[m,memory]=clean({(a,memory):v for a,v in zip(active,(yr,xn,yt,ye))})
    return cols


# Source local basis is |0R>,|1R>,|0D>,|1D>.
# Each tuple is a distinct environmental Kraus label, even for equal outcomes.
LOCAL={'C':[(2,1,F(3,5))],
       'N':[(0,0,F(1)),(0,1,F(4,5)),(0,2,F(3,5)),
            (2,2,F(4,5)),(0,3,F(3,5)),(2,3,F(4,5))]}


def detector_columns(port,outcome):
    result=[]
    for out_local,in_local,amplitude in LOCAL[outcome]:
        cols={}
        for memory in ('R','D'):
            for m in MODES:
                local=(0 if memory=='R' else 2)+int(m==port)
                if local!=in_local:continue
                spectator=-1 if m==port else m
                G.require(out_local%2==0,'unexpected source non-destructive branch')
                cols[m,memory]={(spectator,'R' if out_local<2 else 'D'):amplitude}
        result.append(cols)
    return result


def occupation_mean(rho):return sum(v for (a,b),v in rho.items() if a==b and a[0]!=-1)


def check_history(records):
    G.require(len(records)<=3,'history horizon')
    previous=None;seen=set()
    for k,r in enumerate(records):
        G.require(r['source_id']=='passive-port-fock-memory.v1' and r['round']==k
                  and r['port']==2+3*k and r['outcome'] in 'CN' and len(r['outcome'])==1,'history operation/source')
        G.require(r['record_id'] and r['record_id'] not in seen and r['previous_record_id']==previous,'history occurrence/attachment')
        G.require(r['memory_policy']=='retain' and r['clock']=='ordered-model-bin','hidden reset or physical clock promotion')
        seen.add(r['record_id']);previous=r['record_id']
    return True


def main():
    p=argparse.ArgumentParser();p.add_argument('--pin',action='store_true');args=p.parse_args()
    c=G.load(CONTRACT);paths={CONTRACT}|set(c['source_evidence']);pin=ROOT/c['source_pins']
    if args.pin:
        G.require(not pin.exists(),'refusing implicit re-pin')
        pin.write_text(json.dumps({'source_sha256':{p:G.sha(p) for p in sorted(paths)}},indent=2)+'\n',encoding='utf-8')
    pins=G.load(c['source_pins']);G.require(set(pins['source_sha256'])==paths,'pin coverage')
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source drift: '+path)
    G.require(c['decision']=='accept_scoped_overlap_specification' and not c['physical_transport_admitted']
              and not c['source_law_independently_selected'],'physical promotion')
    G.require(c['source_witness_id']==G.load('research/nima/contracts/physics-geometric-candidate.v1.json')['source_id'],'source mismatch')
    ports=[port_columns(k) for k in range(3)]
    detectors={(k,y):detector_columns(2+3*k,y) for k in range(3) for y in 'CN'}
    # Kraus completeness on all matrix units, including spectator off-diagonal terms.
    ncomplete=0
    states=[(m,mem) for mem in ('R','D') for m in MODES]
    for k in range(3):
        for a,b in itertools.product(states,repeat=2):
            rho={(a,b):F(1)}
            output=cp(rho,detectors[k,'C']+detectors[k,'N'])
            G.require(trace(output)==F(a==b),'tensor Kraus trace-preservation')
            ncomplete+=1
    vectors=[{occ(m):F(1)} for m in MODES]
    vectors += [{occ(a):F(1),occ(b):F(1)} for a,b in itertools.combinations(MODES,2)]
    checks=resources=0
    for memory in ('R','D'):
        for vector in vectors:
            initial=[(memory,vector)];rho0=density(initial)
            frontier=[(initial,rho0)]
            for k in range(3):
                next_frontier=[]
                for branches,rho in frontier:
                    forward=G.evolve(G.round_map(k),branches)
                    port_rho=cp(rho,[ports[k]])
                    G.require(density(forward)==port_rho,'passive inclusion square')
                    before=occupation_mean(port_rho);after_sum={}
                    for y in 'CN':
                        fock=G.instrument(2+3*k,y,forward)
                        direct=cp(port_rho,detectors[k,y])
                        G.require(density(fock)==direct and G.probability(fock)==trace(direct),'outcome/posterior square')
                        for key,v in direct.items():after_sum[key]=after_sum.get(key,F(0))+v
                        next_frontier.append((fock,direct))
                        checks+=1
                    # This node's unconditioned loss is retained separately; readiness is not added.
                    loss=before-occupation_mean(after_sum)
                    G.require(loss>=0 and trace(after_sum)==trace(port_rho),'occupation balance/completeness')
                    resources+=1
                frontier=next_frontier
            G.require(sum(trace(r) for _,r in frontier)==trace(rho0),'complete three-bin word normalization')
    # A no-click at an empty port must retain mode interference among spectators.
    spectator={occ(0):F(3,5),occ(1):F(4,5)}
    rho=density([('R',spectator)])
    G.require(cp(rho,detectors[0,'N'])==rho,'spectator coherence')
    # Resetting memory after a click cannot be a silent identity even when the current photon is consumed.
    dead={( (-1,'D'),(-1,'D')):F(1)}
    ready={( (-1,'R'),(-1,'R')):F(1)}
    G.require(cp(dead,detectors[0,'N'])!=cp(ready,detectors[0,'N']),'hidden reset alias')
    guard=False
    try:mode(G.occupation([2,2]))
    except ValueError:guard=True
    G.require(guard,'silent multiphoton inclusion')
    records=[{'source_id':c['source_witness_id'],'round':k,'port':2+3*k,'outcome':y,
              'record_id':str(k),'previous_record_id':str(k-1) if k else None,
              'memory_policy':'retain','clock':'ordered-model-bin'} for k,y in enumerate('NCN')]
    G.require(check_history(records),'valid complete history rejected')
    controls=[]
    for name in ('dropped-no-click','duplicate-occurrence','hidden-reset','physical-clock','foreign-source'):
        bad=copy.deepcopy(records)
        if name=='dropped-no-click':bad.pop(0)
        elif name=='duplicate-occurrence':bad[1]['record_id']=bad[0]['record_id']
        elif name=='hidden-reset':bad[1]['memory_policy']='reset-ready'
        elif name=='physical-clock':bad[1]['clock']='seconds'
        else:bad[1]['source_id']='native-bool-square-pilot'
        try:check_history(bad)
        except ValueError:controls.append(name)
        else:raise AssertionError('accepted '+name)
    out={'schema':c['schema'],'status':'pass','source_witness_id':c['source_witness_id'],
         'real_polarization_vectors_per_memory':len(vectors),'outcome_posterior_squares':checks,
         'kraus_completeness_matrix_units':ncomplete,'occupation_balance_nodes':resources,
         'spectator_coherence_preserved':True,'hidden_reset_distinguished':True,'multiphoton_guard':guard,
         'verification':'Exact real polarization controls; complex-linear Kraus intertwining and all-history induction supplied in written specification',
         'rejected_history_hostiles':controls,'physical_transport_admitted':False,'source_sha256':pins['source_sha256'],'checker_sha256':G.sha(Path(__file__))}
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source changed during run')
    (ROOT/c['result']).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='source_sha256'},indent=2))

if __name__=='__main__':main()
