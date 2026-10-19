#!/usr/bin/env python3
"""Enumerate complementary five-cycle cuts with inherited labels and endpoint gluing.
No new vertex identification, mode decoration, or particle-dependent assembly rule.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import sys
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from assemble_relative_geometry import assemble,apply
from check_neutrino_arrow_seed_science import rank

def matmul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def characteristic(M):
    n=len(M);P=[[Q(i==j) for j in range(n)] for i in range(n)]
    traces=[]
    for _ in range(n):P=matmul(P,M);traces.append(sum(P[i][i] for i in range(n)))
    coefficients=[Q(1)]
    for k in range(1,n+1):coefficients.append(-sum(coefficients[k-j]*traces[j-1] for j in range(1,k+1))/k)
    return coefficients

def paths(sign):
    return [(start,length,tuple((start+sign*j)%5 for j in range(length+1))) for start in range(5) for length in (2,3)]

def analyse(ep,pp,gluing):
    e_start,el,e=ep;p_start,pl,p=pp
    arrows=[('electron',i,a,b) for i,(a,b) in enumerate(zip(e,e[1:]))]+[('positron',i,a,b) for i,(a,b) in enumerate(zip(p,p[1:]))]
    vertices=sorted(set(e+p));edges=sorted({tuple(sorted((a,b))) for _,_,a,b in arrows})
    d1=[[Q(int(v==b)-int(v==a)) for _,_,a,b in arrows] for v in vertices]
    K=[[Q(a[3]==b[2]) for a in arrows] for b in arrows]
    oriented={edge:sum((1 if (a,b)==edge else -1) for _,_,a,b in arrows if tuple(sorted((a,b)))==edge) for edge in edges}
    comparison={edge:sum((1 if (a,b)==edge else -1)*(1 if owner=='electron' else -1) for owner,_,a,b in arrows if tuple(sorted((a,b)))==edge) for edge in edges}
    n=len(arrows);I=[[Q(i==j) for j in range(n)] for i in range(n)]
    P=I;nilpotent_index=None
    for k in range(1,n+1):
        P=matmul(P,K)
        if not any(x for row in P for x in row):nilpotent_index=k;break
    klass=f'parallel_{el}_{pl}' if gluing=='parallel' else f'return_{el}_{pl}'
    return {'class':klass,'electron_path':['ABCDE'[i] for i in e],'positron_path':['ABCDE'[i] for i in p],'electron_length':el,'positron_length':pl,'endpoint_gluing':gluing,'vertices':len(vertices),'edge_supports':len(edges),'arrow_occurrences':len(arrows),'incidence_rank':rank(d1),'incidence_kernel_dimension':len(arrows)-rank(d1),'continuation_rank':rank(K),'continuation_characteristic_coefficients':[str(x) for x in characteristic(K)],'continuation_nilpotent_index':nilpotent_index,'occurrence_manifest':[{'owner':owner,'local_step':i,'source':'ABCDE'[a],'target':'ABCDE'[b]} for owner,i,a,b in arrows],'oriented_support_chain':{''.join('ABCDE'[i] for i in edge):value for edge,value in oriented.items() if value},'electron_minus_positron_chain':{''.join('ABCDE'[i] for i in edge):value for edge,value in comparison.items() if value},'primitive_continuation':[[int(x) for x in row] for row in K]}

def main():
    electron_path=ROOT/'research/voevodsky/inputs/relative-electron.json'
    positron_path=ROOT/'research/strominger/inputs/relative-positron-candidate.json'
    E=json.loads(electron_path.read_text());P=json.loads(positron_path.read_text())
    eg=E['generators'][0];pg=P['generators'][0]
    g=(tuple(tuple(map(Q,r)) for r in eg['matrix']),tuple(map(Q,eg['translation'])))
    h=(tuple(tuple(map(Q,r)) for r in pg['matrix']),tuple(map(Q,pg['translation'])))
    point=tuple(map(Q,E['seeds'][0]['point']));coords=[]
    for _ in range(5):coords.append(point);point=apply(g,point)
    assert all(apply(h,coords[i])==coords[(i-1)%5] for i in range(5))
    rows=[];unmatched=0
    for ep in paths(1):
        for pp in paths(-1):
            e,p=ep[2],pp[2]
            if e[0]==p[0] and e[-1]==p[-1]:rows.append(analyse(ep,pp,'parallel'))
            elif e[0]==p[-1] and e[-1]==p[0]:rows.append(analyse(ep,pp,'return'))
            else:unmatched+=1
    classes={}
    for row in rows:
        key=row['class'];classes.setdefault(key,{'count':0,'example':row});classes[key]['count']+=1
    # Keep the existing affine generators: any nonempty partial seed vertex
    # closes to the original five-vertex orbit, not a new particle shape.
    completed=assemble(E);both=json.loads(json.dumps(E));both['generators']+=P['generators']
    bidirectional_completion=assemble(both)
    closure_all=[]
    for row in rows:
        selected={coords['ABCDE'.index(name)] for name in row['electron_path']+row['positron_path']}
        frontier=list(selected)
        while frontier:
            p=frontier.pop()
            for generator in (g,h):
                q=apply(generator,p)
                if q not in selected:selected.add(q);frontier.append(q)
        closure_all.append(len(selected)==5)
    parallel=[r for r in rows if r['endpoint_gluing']=='parallel'];returns=[r for r in rows if r['endpoint_gluing']=='return']
    # Complex photon pair has lambda^2+lambda+1; all resulting characteristic
    # polynomials are explicitly incompatible with that factor.
    def mod_c3(coeffs):
        # Horner evaluation at omega, omega^2+omega+1=0, pairs a+b*omega.
        a=b=Q(0)
        for c in map(Q,coeffs):a,b=c-b,a-b
        return (a,b)
    checks={
        'one_hundred_path_pairs_enumerated':len(rows)+unmatched==100,
        'twenty_matching_endpoint_pairs':len(rows)==20,
        'ten_parallel_complementary_cuts':len(parallel)==10 and all(r['electron_length']+r['positron_length']==5 for r in parallel),
        'ten_returns_use_equal_lengths':len(returns)==10 and all(r['electron_length']==r['positron_length'] for r in returns),
        'mixed_two_three_cannot_make_endpoint_return':not any(r['endpoint_gluing']=='return' and r['electron_length']!=r['positron_length'] for r in rows),
        'parallel_continuation_nilpotent_index_three':all(r['continuation_nilpotent_index']==3 for r in parallel),
        'backtracking_return_cancels_support_not_occurrences':all(not r['oriented_support_chain'] and r['arrow_occurrences']>0 for r in returns),
        'no_prior_photon_C3_pair_in_cut_continuation':all(mod_c3(r['continuation_characteristic_coefficients'])!=(0,0) for r in rows),
        'inherited_generators_close_every_cut_to_five_vertices':all(closure_all),
        'same_full_shape_with_forward_and_reverse_generators':completed==bidirectional_completion,
    }
    out={'schema':'marici.strominger.half-electron-positron-seeds.v1','status':'passed' if all(checks.values()) else 'failed','scientific_disposition':'no distinct photon seed from the tested endpoint-matched two/three-arrow cuts under unchanged assembly','cut_rule':'All contiguous length-two and length-three paths of each oriented five-cycle; retain occurrence owner and history. Glue only already equal endpoint labels.','path_pairs_examined':100,'unmatched_endpoint_pairs':unmatched,'classes':classes,'matching_pairs':rows,'checks':checks,'common_processor_completion':completed['counts'],'scope_boundary':'A path is not an affine seed-generator library. With the original generators retained, orbit completion gives the existing four-simplex. Feeding a path-only input requires a new admitted realization operation; no such operation is invented here.','next_options':['Specify a different arrow-level gluing with explicit label-identification witnesses','Use an existing retained comparison/quotient operation and compute its actual output','Do not replace equal endpoint labels by convenient geometric coincidences'],'source_hashes':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),electron_path,positron_path,ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py',ROOT/'research/strominger/checkers/check_neutrino_arrow_seed_science.py']}}
    target=ROOT/'research/strominger/results/half_electron_positron_seeds.json'
    target.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'checks':checks,'classes':{key:{'count':value['count'],'electron_path':value['example']['electron_path'],'positron_path':value['example']['positron_path'],'continuation_polynomial':value['example']['continuation_characteristic_coefficients']} for key,value in classes.items()}},indent=2))
    if not all(checks.values()):raise SystemExit(1)
if __name__=='__main__':main()
