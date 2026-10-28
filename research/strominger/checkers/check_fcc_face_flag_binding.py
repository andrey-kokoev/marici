"""Bind actual FCC route triangles and central flags to normalized chains/duals.
Linearized incidence audit, not a P/E evolution or an analytical-field proof.
"""
from collections import defaultdict
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[3]
INPUTS=['research/strominger/results/fcc-first-transport.json',
        'research/strominger/results/esd7-seven-stage-handoff.json',
        'research/voevodsky/results/esd7_explicit_analytical_census.json']


def clean(c):return {s:k for s,k in c.items() if k}
def plus(*chains):
    out=defaultdict(int)
    for c in chains:
        for s,k in c.items():out[s]+=k
    return clean(out)
def neg(c):return {s:-k for s,k in c.items()}
def oriented(vs):
    sign=(-1)**sum(vs[i]>vs[j] for i in range(len(vs)) for j in range(i+1,len(vs)))
    return {tuple(sorted(vs)):sign}
def boundary(c):
    out=defaultdict(int)
    for s,k in c.items():
        if len(s)>1:
            for i in range(len(s)):out[s[:i]+s[i+1:]]+=k*((-1)**i)
    return clean(out)
def basis(vs):return [s for n in range(1,len(vs)+1) for s in combinations(tuple(sorted(vs)),n)]
def restrict(c,bs):return {s:k for s,k in c.items() if s in bs}
def coboundary(c,bs):return clean({s:sum(k*c.get(f,0) for f,k in boundary({s:1}).items()) for s in bs})


def main():
    adapter,handoff,census=[json.loads((ROOT/p).read_text(encoding='utf-8')) for p in INPUTS]
    checks=[]
    def check(name,condition):
        if not condition:raise AssertionError(name)
        checks.append(name)
    check('adapter and handoff receipts bind the same live census',adapter['source_sha256'][INPUTS[2]]==handoff['source_sha256']==hashlib.sha256((ROOT/INPUTS[2]).read_bytes()).hexdigest())
    for receipt in (adapter,handoff):
        assert receipt['status']=='passed'
    verts={r['id']:tuple(r['barycentric']) for r in census['vertices']}
    ids={v:id for id,v in verts.items()}
    cells={r['id']:(r['id'],) for r in census['vertices']}
    for kind in ['edges','triangles','tetrahedra']:
        cells.update({r['id']:tuple(sorted(r['vertices'])) for r in census[kind]})
    triangle_ids={v:id for id,v in cells.items() if len(v)==3}
    edge_ids={v:id for id,v in cells.items() if len(v)==2}
    route_records=[];tetra_count=0;comparisons=0
    for cell in adapter['coarse_cells']:
        if not cell['id'].startswith('oct-'):continue
        a,b=[ids[tuple(v)] for v in cell['selected_diagonal']]
        diagonal=oriented((a,b));fillers=[];paths=[]
        for route in cell['diagonal_root_paths']:
            m=route['middle'];p=plus(oriented((a,m)),oriented((m,b)))
            h=oriented((a,m,b))
            assert triangle_ids[tuple(sorted((a,m,b)))]==route['comparison_face']
            assert boundary(h)==plus(p,neg(diagonal))
            fillers.append(h);paths.append(p)
            route_records.append({'octahedron':cell['id'],'diagonal':[a,b],'middle':m,
                                  'route_edges':[edge_ids[tuple(sorted((a,m)))],edge_ids[tuple(sorted((m,b)))]],
                                  'comparison_face':route['comparison_face'],'face_orientation':next(iter(h.values()))})
        for i,j,k in product(range(4),repeat=3):
            hij=plus(fillers[i],neg(fillers[j]));hjk=plus(fillers[j],neg(fillers[k]))
            assert boundary(hij)==plus(paths[i],neg(paths[j]))
            assert plus(hij,hjk)==plus(fillers[i],neg(fillers[k]))
            comparisons+=1
        for id in cell['refinement']:
            t=oriented(cells[id]);assert boundary(boundary(t))=={}
            assert len(boundary(t))==4
            tetra_count+=1
    check('224 source faces fill route-minus-diagonal boundaries',len(route_records)==224)
    check('3584 ordered route-comparison triples compose',comparisons==56*4**3)
    check('224 actual octahedral refinement tetrahedra retain closed four-face boundaries',tetra_count==224)
    # Deliberately reverse one triangle while keeping its route boundary fixed.
    r=route_records[0];a,b=r['diagonal'];m=r['middle']
    check('wrong comparison orientation is detected',boundary(neg(oriented((a,m,b))))!=plus(oriented((a,m)),oriented((m,b)),neg(oriented((a,b)))))
    flag_records=[];asc=desc=projection_failures=0
    for bridge in handoff['central_flag_bridges']:
        stages=bridge['seven_presentations'];bs=[basis(cells[id]) for id in stages]
        for i in range(3):
            small,big=bs[i],bs[i+1]
            assert set(small)<=set(big)
            for s in small:assert set(boundary({s:1}))<=set(small)
            asc+=1
        failures=[]
        for i in range(3,6):
            big,small=bs[i],bs[i+1]
            assert set(small)<=set(big)
            # Dual restriction commutes with cochain differential on every basis vector.
            for s in big:
                assert restrict(coboundary({s:1},big),small)==coboundary(restrict({s:1},small),small)
            # Evaluation naturality: <inclusion c,phi>=<c,restriction phi>.
            for c,phi in product(small,big):assert int(c==phi)==restrict({phi:1},small).get(c,0)
            hostile=next(s for s in big if restrict(boundary({s:1}),small)!=boundary(restrict({s:1},small)))
            failures.append({'from':stages[i],'to':stages[i+1],'chain_projection_counterexample':hostile,
                             'project_after_boundary':[(list(s),k) for s,k in restrict(boundary({hostile:1}),small).items()],
                             'boundary_after_project':[(list(s),k) for s,k in boundary(restrict({hostile:1},small)).items()]})
            projection_failures+=1;desc+=1
        flag_records.append({'presentations':stages,'incidence_ranks':[len(cells[id]) for id in stages],
                             'chain_basis_sizes':[len(b) for b in bs],
                             'leg_types':['chain inclusion']*3+['dual restriction']*3,
                             'central_interface':'evaluation pairing between C_*(T184) and its dual, not an asserted state-evolution map',
                             'rejected_chain_projections':failures})
    check('all72 ascending flag inclusions preserve chain boundaries',asc==72)
    check('all72 descending dual restrictions preserve coboundaries and evaluation',desc==72)
    check('all72 naive descending chain projections fail a boundary test',projection_failures==72)
    check('all24 flags retain seven presentations with the same central rank profile',len(flag_records)==24 and all(r['incidence_ranks']==[1,2,3,4,3,2,1] for r in flag_records))
    check('incidence depth is not total chain-space dimension',all(r['chain_basis_sizes']==[1,3,7,15,7,3,1] for r in flag_records))
    # The paired center does not authorize a silent chain-to-cochain identity map.
    center_basis=basis(cells['T184']);v=next(s for s in center_basis if len(s)==1)
    check('basis identification at center does not intertwine boundary and coboundary',boundary({v:1})!=coboundary({v:1},center_basis))
    sources=INPUTS+['research/strominger/checkers/check_fcc_face_flag_binding.py','research/nima/full-esd7-graded-tate-torus-realization.md']
    report={'status':'passed','checks':checks,'check_count':len(checks),'route_face_bindings':route_records,'central_flag_bindings':flag_records,
            'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
            'scope':'Normalized simplicial chains and dual cochains of actual source cells. Chain fillings are a linearized incidence realization, not proof of equality of arbitrary analytical edge operators. Reverse-leg dualization is explicitly typed. No chain/cochain central handoff, Fourier coefficient action, P/E readout, or28-stage selector is constructed.',
            'disposition':'Actual route faces and both flag legs are bound. The central chain-to-dual realization is the next specific missing interface; a pairing alone is not an evolution operator.'}
    dest=ROOT/'research/strominger/results/fcc-face-flag-binding.json'
    dest.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'passed','checks':len(checks),'route_faces':len(route_records),'comparison_triples':comparisons,'flags':len(flag_records),'rejected_naive_projections':projection_failures,'result':str(dest)}))


if __name__=='__main__':main()
