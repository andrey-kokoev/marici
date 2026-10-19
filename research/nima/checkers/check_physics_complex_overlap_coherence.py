"""Complete complex-linear coefficient comparison of two conditional overlap routes."""
import argparse
import itertools
import json
from pathlib import Path
from fractions import Fraction as F
import check_physics_geometric_candidate as G
import check_physics_overlap_catalog as B

ROOT=G.ROOT
CONTRACT='research/nima/contracts/physics-complex-overlap-coherence.v1.json'


def fock_columns(k):
    w=G.round_map(k);columns={}
    for memory in ('R','D'):
        for m in B.MODES:
            output=G.lift_column(w,B.occ(m))
            columns[m,memory]={(B.mode(o),memory):a for o,a in output.items()}
    return columns


def fock_kraus_columns(port,outcome):
    # Occupation predicates reproduce the source's separate Kraus labels;
    # the other route uses local |0R>,|1R>,|0D>,|1D> tensor-factor indices.
    ks=[(1,'R','D',F(3,5))] if outcome=='C' else [
        (0,'R','R',F(1)),(1,'R','R',F(4,5)),
        (0,'D','R',F(3,5)),(0,'D','D',F(4,5)),
        (1,'D','R',F(3,5)),(1,'D','D',F(4,5))]
    columns=[]
    for number,mi,mo,amplitude in ks:
        one={}
        for m in B.MODES:
            o=B.occ(m)
            if o[port]!=number:continue
            target=list(o);target[port]=0
            one[m,mi]={(B.mode(tuple(target)),mo):amplitude}
        columns.append(one)
    return columns


def apply_coefficients(rho,kraus):
    # Independent explicit K E_ab K^T implementation. All nominal K are real,
    # so this is also K E_ab K*; coefficients may later be any complex numbers.
    result={}
    for (a,b),coefficient in rho.items():
        for k in kraus:
            left=k.get(a,{})
            right=k.get(b,{})
            for i,x in left.items():
                for j,y in right.items():
                    result[i,j]=result.get((i,j),F(0))+coefficient*x*y
    return {key:value for key,value in result.items() if value}


def main():
    p=argparse.ArgumentParser();p.add_argument('--pin',action='store_true');args=p.parse_args()
    c=G.load(CONTRACT);paths={CONTRACT}|set(c['source_evidence']);pin=ROOT/c['source_pins']
    if args.pin:
        G.require(not pin.exists(),'refusing implicit re-pin')
        pin.write_text(json.dumps({'source_sha256':{p:G.sha(p) for p in sorted(paths)}},indent=2)+'\n',encoding='utf-8')
    pins=G.load(c['source_pins']);G.require(set(pins['source_sha256'])==paths,'pin coverage')
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source drift: '+path)
    G.require(c['decision']=='constructed_conditional_full_operator_comparison' and c['horizon']==3 and c['ports']==[2,5,8]
              and all(c[k] is False for k in ('physical_transport_admitted','source_law_independently_selected','coherent_memory_completion_selected')),'scope promotion')
    ap=[fock_columns(k) for k in range(3)];bp=[B.port_columns(k) for k in range(3)]
    ak={(k,y):fock_kraus_columns(2+3*k,y) for k in range(3) for y in 'CN'}
    bk={(k,y):B.detector_columns(2+3*k,y) for k in range(3) for y in 'CN'}
    passive=outcomes=normalizations=0
    matrix_units=[((a,memory),(b,memory)) for memory in ('R','D') for a,b in itertools.product(B.MODES,repeat=2)]
    for a,b in matrix_units:
        initial={(a,b):F(1)};frontier=[((),initial,initial)]
        for k in range(3):
            following=[]
            for word,left,right in frontier:
                fa=apply_coefficients(left,[ap[k]]);pb=B.cp(right,[bp[k]])
                G.require(fa==pb,'complex coefficient passive square');passive+=1
                for y in 'CN':
                    fa_out=apply_coefficients(fa,ak[k,y]);pb_out=B.cp(pb,bk[k,y])
                    G.require(fa_out==pb_out,'complex coefficient posterior square')
                    G.require(B.trace(fa_out)==B.trace(pb_out),'record probability descent')
                    following.append((word+(y,),fa_out,pb_out));outcomes+=1
            frontier=following
        G.require(sum(B.trace(left) for _,left,_ in frontier)==F(a==b),'complete coefficient trace preservation')
        G.require(len({word for word,_,_ in frontier})==8,'outcome history erased')
        normalizations+=1
    # A genuine imaginary optical coherence cannot be tested only through traces.
    # i(E_01-E_10) is represented by its exact real coefficient of i.
    a=(-1,'R');b=(0,'R');imaginary_coefficient={(a,b):F(1),(b,a):F(-1)}
    after=apply_coefficients(imaginary_coefficient,[ap[0]])
    after=apply_coefficients(after,ak[0,'N'])
    G.require(after and B.trace(after)==0,'imaginary coherence hostile missing')
    diagonal_only={key:value for key,value in after.items() if key[0]==key[1]}
    G.require(diagonal_only!=after and B.trace(diagonal_only)==B.trace(after),'trace-only comparison falsely faithful')
    G.require(apply_coefficients(initial,[])=={},'empty Kraus family semantics')
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source changed during check')
    out={'schema':c['schema'],'status':'pass','complex_operator_basis_size':len(matrix_units),
         'passive_prefix_coefficient_squares':passive,'outcome_prefix_operator_squares':outcomes,
         'complete_coefficient_trace_controls':normalizations,'imaginary_coherence_preserved':True,
         'trace_only_dephasing_alias_detected':True,'physical_transport_admitted':False,
         'source_sha256':pins['source_sha256'],'checker_sha256':G.sha(Path(__file__))}
    (ROOT/c['result']).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='source_sha256'},indent=2))

if __name__=='__main__':main()
