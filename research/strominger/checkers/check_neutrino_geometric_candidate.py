#!/usr/bin/env python3
"""Exact exploratory triangle/spin-lift candidate; no physical identification."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/voevodsky/checkers'))
from assemble_relative_geometry import assemble, apply, subtract

# Q(sqrt(-3)); conjugation is exact, avoiding floating point spin phases.
def mul(x, y):
    a,b=x; c,d=y
    return (a*c-3*b*d, a*d+b*c)
def conj(x): return (x[0],-x[1])
def power(x,n):
    out=(Q(1),Q(0))
    for _ in range(n): out=mul(out,x)
    return out

def boundary(cells):
    out={}
    for cell in cells:
        for i in range(len(cell)):
            face=cell[:i]+cell[i+1:]
            inversions=sum(face[a]>face[b] for a in range(len(face)) for b in range(a+1,len(face)))
            key=tuple(sorted(face))
            out[key]=out.get(key,0)+(-1)**(i+inversions)
    return {key:value for key,value in out.items() if value}

def main():
    source_path=ROOT/'research/strominger/inputs/relative-neutrino-candidate.json'
    source=json.loads(source_path.read_text())
    geometry=assemble(source)
    vertices=[tuple(map(Q,p)) for p in geometry['vertices']]
    raw=source['generators'][0]
    gen=(tuple(tuple(map(Q,r)) for r in raw['matrix']),tuple(map(Q,raw['translation'])))
    index={p:i for i,p in enumerate(vertices)}
    permutation=[index[apply(gen,p)] for p in vertices]
    center=tuple(map(Q,geometry['center']))
    outer=boundary(geometry['cone_cells'])
    z=(Q(1,2),Q(1,2))
    minus=(-Q(1),Q(0)); one=(Q(1),Q(0))
    checks={
        'three_vertices':len(vertices)==3,
        'intrinsic_dimension_two':geometry['dimension']==2,
        'equal_squared_edges_eight':all(Q(geometry['squared_distances'][i][j])==8 for i,j in combinations(range(3),2)),
        'three_oriented_cone_triangles':len(geometry['cone_cells'])==3,
        'interior_edges_cancel':len(outer)==3 and all(3 not in edge for edge in outer),
        'boundary_squared_zero':not boundary([list(edge) if coefficient==1 else list(reversed(edge)) for edge,coefficient in outer.items()]),
        'cycle_order_three':all(permutation[permutation[permutation[i]]]==i for i in range(3)) and permutation!=list(range(3)),
        'center_fixed':apply(gen,center)==center,
        'one_marked_attachment_edge':len(geometry['retained_attachment_interfaces'])==1,
        'spin_lift_unitary':mul(z,conj(z))==one,
        'spin_lift_determinant_one':mul(z,conj(z))==one,
        'three_spin_steps_minus_identity':power(z,3)==minus and power(conj(z),3)==minus,
        'six_spin_steps_identity':power(z,6)==one,
        'adjoint_phase_is_triangle_rotation':power(z,2)==(-Q(1,2),Q(1,2)),
        'neutral_action_declared_not_inferred':True,
    }
    # Admission controls inherited from the shared constructor.
    bad=json.loads(json.dumps(source)); bad['metric'][0][0]=7
    try: assemble(bad); checks['metric_change_rejected']=False
    except ValueError: checks['metric_change_rejected']=True
    bad=json.loads(json.dumps(source)); bad['generators']=[]
    try: assemble(bad); checks['generator_deletion_rejected']=False
    except ValueError: checks['generator_deletion_rejected']=True
    bad=json.loads(json.dumps(source)); bad['target_cells']=[[0,1,2]]
    try: assemble(bad); checks['target_injection_rejected']=False
    except ValueError: checks['target_injection_rejected']=True
    unmarked=json.loads(json.dumps(source)); unmarked['seeds'][0]['role']='carrier'
    unmarked_geometry=assemble(unmarked)
    checks['attachment_mark_is_extra_datum']=not unmarked_geometry['retained_attachment_interfaces'] and unmarked_geometry['vertices']==geometry['vertices']
    catalogue=[]
    for name in ('proton','neutron','electron'):
        path=ROOT/f'research/voevodsky/inputs/relative-{name}.json'
        model=assemble(json.loads(path.read_text()))
        catalogue.append({'label':name,'source':str(path.relative_to(ROOT)).replace('\\','/'),'dimension':model['dimension'],'counts':model['counts'],'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    catalogue.append({'label':'neutrino candidate','source':str(source_path.relative_to(ROOT)).replace('\\','/'),'dimension':2,'counts':geometry['counts'],'physical_identification':False})
    dependencies=[source_path,Path(__file__),ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py']
    out={
        'schema':'marici.strominger.neutrino-geometric-candidate.v1',
        'status':'passed' if all(checks.values()) else 'failed',
        'physical_identification':False,
        'geometry':geometry,'cycle_vertex_permutation':permutation,
        'oriented_boundary':{','.join(map(str,k)):v for k,v in outer.items()},
        'internal_decoration':{'spin_space':'C^2','lift':'diag((1+sqrt(-3))/2,(1-sqrt(-3))/2)','charge_operator':'0_2 (declared)','chiral_options':'two rank-one coordinate projectors; neither selected','meaning':'finite rotation double cover, not a Lorentz/Weyl equation or exchange-statistics derivation'},
        'catalogue':catalogue,'checks':checks,
        'source_hashes':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies},
        'open_gates':['source selection of triangle and metric','physical chirality and Lorentz propagation','weak interaction coupling to electron/proton/neutron sectors','mass and mixing mechanism','Dirac versus Majorana and particle/antiparticle identification'],
        'claim_boundary':'An exact decorated planar carrier added to the comparative geometric catalogue. Three vertices do not represent three flavors; neutral charge and spin decoration are new inputs, not consequences of triangle geometry.'}
    output=ROOT/'research/strominger/results/neutrino_geometric_candidate.json'
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'checks':len(checks),'catalogue':catalogue},indent=2))
    if not all(checks.values()): raise SystemExit(1)

if __name__=='__main__': main()
