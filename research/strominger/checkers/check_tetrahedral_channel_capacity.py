"""Exact geometry-to-operator test. Run with: uv run --with sympy python ...

Neither atomic reference populations nor 2n^2 enter graph construction/spectra.
The two-state spin factor and fermionic occupation remain declared assumptions.
"""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from functools import cmp_to_key
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from pathlib import Path
import subprocess
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve()
FIXTURE = ROOT / 'research/strominger/inputs/tetrahedral-channel-capacity-v1.json'
PACKET = ROOT / 'research/strominger/tetrahedral-channel-capacity.md'
MODEL = ROOT / 'research/strominger/scc-models/tetrahedral-channel-capacity-v1.json'
OUT = ROOT / 'research/strominger/results/tetrahedral-channel-capacity'
X = sp.Symbol('x')


def qsign(value):
    """Sign of integer a+b sqrt5, with no floating decisions."""
    a,b=value
    if b==0:return (a>0)-(a<0)
    if a==0:return (b>0)-(b<0)
    if a>0 and b>0:return 1
    if a<0 and b<0:return -1
    comparison=a*a-5*b*b
    return ((comparison>0)-(comparison<0)) if a>0 else -((comparison>0)-(comparison<0))


def qdot(u,v):
    return (sum(a*c+5*b*d for (a,b),(c,d) in zip(u,v)),
            sum(a*d+b*c for (a,b),(c,d) in zip(u,v)))


def coordinate_sources():
    zero=(0,0)
    axes=[]
    for axis in range(4):
        for sign in (-1,1):
            v=[zero]*4;v[axis]=(4*sign,0);axes.append(tuple(v))
    simplex=[tuple((0,x) for x in v)+((-1,0),) for v in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
    simplex.append((zero,zero,zero,(4,0)))
    vertices=set(axes)
    vertices.update(tuple((2*s,0) for s in signs) for signs in product((-1,1),repeat=4))
    even=[p for p in permutations(range(4)) if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2==0]
    for s,t,u in product((-1,1),repeat=3):
        base=[zero,(2*s,0),(t,t),(-u,u)]
        vertices.update(tuple(base[i] for i in p) for p in even)
    return {'5-cell':simplex,'16-cell':axes,'600-cell':sorted(vertices)}


def geometry(name,vertices,check):
    n=len(vertices)
    dots=[[qdot(a,b) for b in vertices] for a in vertices]
    check(name+'_all_vertices_on_unit_S3',all(dots[i][i]==(16,0) for i in range(n)))
    check(name+'_origin_in_full_dimensional_positive_hull',all(sum(v[i][j] for v in vertices)==0 for i in range(4) for j in range(2)) and all(
        (sum(v[i][0]*v[j][0]+5*v[i][1]*v[j][1] for v in vertices),sum(v[i][0]*v[j][1]+v[i][1]*v[j][0] for v in vertices)) == (4*n if i==j else 0,0)
        for i in range(4) for j in range(4)))
    values={dots[i][j] for i in range(n) for j in range(i+1,n)}
    closest=max(values,key=cmp_to_key(lambda a,b:qsign((a[0]-b[0],a[1]-b[1]))))
    adj=[set() for _ in range(n)]
    for i,j in combinations(range(n),2):
        if dots[i][j]==closest:adj[i].add(j);adj[j].add(i)
    tetra=[]
    for i in range(n):
        for j,k,l in combinations(sorted(v for v in adj[i] if v>i),3):
            if k in adj[j] and l in adj[j] and l in adj[k]:tetra.append((i,j,k,l))
    triangles=Counter(face for cell in tetra for face in combinations(cell,3))
    edge_count=sum(map(len,adj))//2
    expected={'5-cell':(5,10,10,5),'16-cell':(8,24,32,16),'600-cell':(120,720,1200,600)}[name]
    check(name+'_computed_tetrahedral_boundary_f_vector',(n,edge_count,len(triangles),len(tetra))==expected)
    check(name+'_closed_triangle_pairing_and_Euler',all(count==2 for count in triangles.values()) and n-edge_count+len(triangles)-len(tetra)==0)
    bound=(16+3*closest[0],3*closest[1])
    support=True
    for cell in tetra:
        for v in range(n):
            s=(sum(dots[i][v][0] for i in cell),sum(dots[i][v][1] for i in cell))
            sign=qsign((bound[0]-s[0],bound[1]-s[1]))
            if sign!=(0 if v in cell else 1):support=False
    check(name+'_all_enumerated_tetrahedra_are_exact_supporting_facets',support)
    c=(closest[0]+closest[1]*sp.sqrt(5))/16
    check(name+'_tetrahedral_cones_have_positive_nondegenerate_volume',sp.simplify((1-c)**3*(1+3*c)).is_positive is True)
    return adj,{'coordinate_encoding':'(a+b sqrt5)/4','vertices':vertices,'nearest_inner_product_numerator_over16':closest,
                'edges':[(i,j) for i in range(n) for j in adj[i] if i<j], 'tetrahedral_facets':tetra,'f_vector':expected}


def equitable_partition(adj):
    cells=[[0],list(range(1,len(adj)))]
    while True:
        index={v:i for i,cell in enumerate(cells) for v in cell}
        refined=[]
        for cell in cells:
            buckets=defaultdict(list)
            for v in cell:
                count=[0]*len(cells)
                for u in adj[v]:count[index[u]]+=1
                buckets[tuple(count)].append(v)
            refined.extend(buckets[key] for key in sorted(buckets))
        if len(refined)==len(cells):break
        cells=refined
    index={v:i for i,cell in enumerate(cells) for v in cell}
    quotient=[]
    for cell in cells:
        counts=[]
        for v in cell:
            row=[0]*len(cells)
            for u in adj[v]:row[index[u]]+=1
            counts.append(row)
        assert all(row==counts[0] for row in counts)
        quotient.append(counts[0])
    return cells,quotient


def spectrum(name,adj,check):
    n=len(adj)
    check(name+'_simple_symmetric_regular_graph',all(i not in neighbors and all(i in adj[j] for j in neighbors) for i,neighbors in enumerate(adj)) and len({len(row) for row in adj})==1)
    reached={0};pending=[0]
    for v in pending:
        for u in adj[v]:
            if u not in reached:reached.add(u);pending.append(u)
    check(name+'_connected',len(reached)==n)
    degree=len(adj[0])
    cells,quotient=equitable_partition(adj)
    p=sp.Matrix(quotient).charpoly(X).as_poly().sqf_part()
    coefficients=[int(c) for c in reversed(p.all_coeffs())]
    power=[[int(i==j) for j in range(n)] for i in range(n)]
    residual=[[0]*n for _ in range(n)]
    traces=[]
    for k,c in enumerate(coefficients):
        traces.append(sum(power[i][i] for i in range(n)))
        if c:
            for i in range(n):
                for j in range(n):residual[i][j]+=c*power[i][j]
        if k<len(coefficients)-1:
            power=[[sum(power[u][j] for u in adj[i]) for j in range(n)] for i in range(n)]
    check(name+'_quotient_polynomial_annihilates_FULL_operator',all(x==0 for row in residual for x in row))
    roots=sp.real_roots(p)
    check(name+'_all_annihilator_roots_simple_real',len(roots)==p.degree() and len(set(roots))==len(roots))
    bands=[];projectors=0
    for r in reversed(roots):
        q,remainder=sp.div(p.as_expr(),X-r,X,extension=True)
        assert sp.simplify(remainder)==0
        polynomial=sp.Poly(q,X)
        numerator=sum(coefficient*traces[monomial[0]] for monomial,coefficient in polynomial.terms())
        derivative=p.diff().eval(r)
        multiplicity=sp.simplify(numerator/derivative)
        eigenvalue=sp.simplify(degree-r)
        check(name+'_integral_projector_rank_'+str(len(bands)+1),multiplicity.is_Integer is True and multiplicity>0 and eigenvalue.is_nonnegative is True)
        projector=sp.expand(q/derivative)
        projectors+=projector
        bands.append({'band':len(bands)+1,'laplacian_eigenvalue':str(eigenvalue),'scalar_rank':int(multiplicity),'spin_resolved_capacity':2*int(multiplicity),
                      'projector_polynomial_in_original_adjacency':str(projector)})
    check(name+'_projector_ranks_retain_every_original_channel',sum(b['scalar_rank'] for b in bands)==n and all(sp.simplify(c)==0 for c in sp.Poly(sp.expand(projectors-1),X).all_coeffs()))
    check(name+'_exact_band_order_certified',all(sp.simplify(sp.sympify(b['laplacian_eigenvalue'])-sp.sympify(a['laplacian_eigenvalue'])).is_positive is True for a,b in zip(bands,bands[1:])))
    return {'vertices':n,'degree':degree,'equitable_partition':cells,'equitable_quotient':quotient,'full_operator_annihilator':str(p.as_expr()),
            'full_graph_walk_trace_moments':traces,'annihilator_full_matrix_zero':True,'bands':bands}


def capacity_comparison(data):
    capacities=[b['spin_resolved_capacity'] for b in data['bands']]
    target=[2*n*n for n in range(1,7)]
    prefix=0
    for actual,expected in zip(capacities,target):
        if actual!=expected:break
        prefix+=1
    return {'all_band_capacities':capacities,'reference_first_six':target,'matching_prefix_length':prefix,
            'matches_all_first_six':len(capacities)>=6 and capacities[:6]==target,
            'interpretation':'Independent spin factor and fermionic exclusion are declared; a finite prefix is not an infinite shell theorem.'}


def fill(capacities,total):
    result=[]
    for capacity in capacities:
        if not total:break
        used=min(capacity,total);result.append(used);total-=used
    return result,total


def run(report):
    fixture=json.loads(FIXTURE.read_text(encoding='utf-8'))
    checks=report['checks']
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    candidates={}
    for name,vertices in coordinate_sources().items():
        adj,source=geometry(name,vertices,check)
        data=spectrum(name,adj,check)
        candidates[name]={'geometry':source,'spectral_certificate':data,'capacity_comparison':capacity_comparison(data)}
    code="import {periodicGraph} from './research/strominger/demos/dual-tetrahedral-lattices/model.mjs'; console.log(JSON.stringify([2,3,4].map(size=>periodicGraph(size))));"
    imported=subprocess.run(['node','--input-type=module','-e',code],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',check=True)
    graphs=json.loads(imported.stdout)
    controls={}
    for graph in graphs:
        ids={v['id']:i for i,v in enumerate(graph['vertices'])};adj=[set() for _ in ids]
        for e in graph['edges']:
            i,j=ids[e['source']],ids[e['target']];adj[i].add(j);adj[j].add(i)
        name='dual_periodic_'+str(graph['size']);data=spectrum(name,adj,check)
        controls[name]={'source_graph_with_deck_translations':graph,'spectral_certificate':data,'capacity_comparison':capacity_comparison(data)}
    comparisons=[]
    capacities=candidates['600-cell']['capacity_comparison']['all_band_capacities']
    for atom in fixture['reference_atoms']:
        predicted,left=fill(capacities,atom['Z'])
        observed=atom['shell_populations'];width=max(len(predicted),len(observed))
        residual=[(predicted[i] if i<len(predicted) else 0)-(observed[i] if i<len(observed) else 0) for i in range(width)]
        comparisons.append({**atom,'predicted_lowest_band_filling':predicted,'unplaced_electrons':left,'occupation_residual':residual,'matches':left==0 and not any(residual)})
    check('reference_populations_and_predicted_counts_are_conserved',all(sum(a['shell_populations'])==a['Z'] and sum(a['predicted_lowest_band_filling'])+a['unplaced_electrons']==a['Z'] for a in comparisons))
    report.update({'classification':'exact_capacity_comparisons_and_independent_atomic_filling_test_completed','regular_candidates':candidates,'existing_dual_lattice_controls':controls,
       'neutral_filling_test':comparisons,'spin_and_exclusion':'Two-state spin and one-fermion-per-mode are assumed, not derived from unique geometric links.',
       'native_scope':'Separate candidate channel arenas only. No attachment of reciprocal P/N tetrahedra to these boundaries, covariant electron operator, charge assignment or physical stability derived.'})


def main():
    fixture=json.loads(FIXTURE.read_text(encoding='utf-8'))
    paths=[HERE,FIXTURE,PACKET,MODEL,HERE.with_name('check_tetrahedral_channel_capacity_scc.py'),ROOT/fixture['dual_lattice_source']]
    report={'schema':'marici.strominger.tetrahedral-channel-capacity.verification.v1','recorded_at':datetime.now(timezone.utc).isoformat(),'checks':{},'sympy_version':sp.__version__,
            'source_sha256':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in paths}}
    try:
        run(report);report['status']='pass'
    except Exception as error:
        report.update(status='fail',error=repr(error));raise
    finally:
        OUT.mkdir(parents=True,exist_ok=True)
        (OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'status':report['status'],'classification':report.get('classification','execution_failure'),'checks':len(report['checks']),
          'capacity_prefixes':{n:d['capacity_comparison']['matching_prefix_length'] for n,d in report.get('regular_candidates',{}).items()},
          'filling_matches':{a['element']:a['matches'] for a in report.get('neutral_filling_test',[])},'receipt':(OUT/'verification.json').relative_to(ROOT).as_posix()}))


if __name__=='__main__':main()
