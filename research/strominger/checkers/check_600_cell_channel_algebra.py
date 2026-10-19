"""Exact input/output channel-factor certificate, not a new physical law."""
from datetime import datetime,timezone
from hashlib import sha256
from math import isqrt
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve()
SOURCE=ROOT/'research/strominger/results/tetrahedral-channel-capacity/verification.json'
PACKET=ROOT/'research/strominger/600-cell-channel-algebra.md'
MODEL=ROOT/'research/strominger/scc-models/600-cell-channel-algebra-v1.json'
OUT=ROOT/'research/strominger/results/600-cell-channel-algebra'


def quaternion_product(a,b):
    def dot(terms):
        x=y=0
        for i,j,s in terms:
            u,v=a[i];w,z=b[j];x+=s*(u*w+5*v*z);y+=s*(u*z+v*w)
        assert x%4==0 and y%4==0
        return (x//4,y//4)
    return (dot([(0,0,1),(1,1,-1),(2,2,-1),(3,3,-1)]),
            dot([(0,1,1),(1,0,1),(2,3,1),(3,2,-1)]),
            dot([(0,2,1),(1,3,-1),(2,0,1),(3,1,1)]),
            dot([(0,3,1),(1,2,1),(2,1,-1),(3,0,1)]))


def run(report):
    source=json.loads(SOURCE.read_text(encoding='utf-8'))
    checks=report['checks']
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    check('source_spectral_calculation_passed',source['status']=='pass' and all(source['checks'].values()))
    check('all_transitive_source_fingerprints_current',all(sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in source['source_sha256'].items()))
    selected=source['regular_candidates']['600-cell']
    vertices=[tuple(tuple(x) for x in v) for v in selected['geometry']['vertices']]
    lookup={v:i for i,v in enumerate(vertices)}
    table=[[lookup[quaternion_product(a,b)] for b in vertices] for a in vertices]
    n=len(vertices)
    identity=lookup[((4,0),(0,0),(0,0),(0,0))]
    inverse=[lookup[(v[0],)+tuple((-a,-b) for a,b in v[1:])] for v in vertices]
    check('all_14400_products_close_on_original_vertices',n==120 and len(lookup)==120 and all(len(row)==120 for row in table))
    check('identity_and_inverse_on_both_sides',all(table[identity][i]==table[i][identity]==i and table[i][inverse[i]]==table[inverse[i]][i]==identity for i in range(n)))
    check('all_1728000_associativity_cells_exact',all(table[table[a][b]][c]==table[a][table[b][c]] for a in range(n) for b in range(n) for c in range(n)))
    check('left_and_right_translations_are_permutations',all(len(set(row))==n for row in table) and all(len({table[i][j] for i in range(n)})==n for j in range(n)))
    adj=[set() for _ in vertices]
    for i,j in selected['geometry']['edges']:adj[i].add(j);adj[j].add(i)
    generators=adj[identity]
    check('geometry_adjacency_is_group_convolution',len(generators)==12 and all((j in adj[i])==(table[inverse[i]][j] in generators) for i in range(n) for j in range(n)))
    classes=[];unseen=set(range(n))
    while unseen:
        h=min(unseen);orbit={table[table[g][h]][inverse[g]] for g in range(n)}
        classes.append(sorted(orbit));unseen-=orbit
    check('nearest_neighbors_are_a_complete_conjugacy_class',any(set(c)==generators for c in classes))
    check('operator_commutes_with_all_left_and_right_translations',all(table[g][j] in adj[table[g][i]] and table[j][g] in adj[table[i][g]] for g in range(n) for i in range(n) for j in adj[i]))
    bands=selected['spectral_certificate']['bands']
    ranks=[band['scalar_rank'] for band in bands]
    dimensions=[isqrt(rank) for rank in ranks]
    check('distinct_bands_equal_number_of_simple_representation_blocks',len(bands)==len(classes)==9)
    check('all_band_ranks_are_exact_input_output_products',all(d*d==rank for d,rank in zip(dimensions,ranks)) and sum(ranks)==120)
    report.update({'classification':'verified_two_sided_channel_factorization_in_finite_group_algebra','group_size':n,
      'identity_index':identity,'inverse_indices':inverse,'multiplication_table':table,'conjugacy_classes':classes,'neighbor_class':sorted(generators),
      'scalar_band_ranks':ranks,'independent_index_dimensions':dimensions,'spin_resolved_capacities':[2*d*d for d in dimensions],
      'theorem':'Complex regular representation decomposes as direct sum V_rho tensor V_rho*. The operator commutes with both regular actions and is scalar on each simple block. Nine distinct eigenvalues and nine conjugacy classes imply one block per band, so its rank is dim(V_rho)^2.',
      'strength':'Finite algebraic factorization theorem using verified source data; explicit irrep bases are not chosen. Spin and fermionic occupancy remain assumptions, not group-algebra consequences.',
      'limits':'Finite group, not full SO4 continuum. Not P/N cell duality, an atomic Hamiltonian, Pauli derivation, charge assignment or a proof of observed filling.'})


def main():
    report={'schema':'marici.strominger.600-cell-channel-algebra.verification.v1','recorded_at':datetime.now(timezone.utc).isoformat(),'checks':{},
      'source_sha256':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in [HERE,SOURCE,PACKET,MODEL]}}
    try:run(report);report['status']='pass'
    except Exception as error:report.update(status='fail',error=repr(error));raise
    finally:
        OUT.mkdir(parents=True,exist_ok=True)
        (OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'status':report['status'],'classification':report.get('classification','execution_failure'),'checks':len(report['checks']),
          'index_dimensions':report.get('independent_index_dimensions'),'receipt':(OUT/'verification.json').relative_to(ROOT).as_posix()}))


if __name__=='__main__':main()
