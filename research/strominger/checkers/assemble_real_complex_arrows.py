"""Typed real/complex arrow frontend to the unchanged shared assembler.

Coordinates: real components followed by (a,b) for each a+i*sqrt(q)*b.
Each arrow family specifies one affine action on a spanning point set.
No particle dispatch, target faces, fitted ranks or coefficient operators.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse,hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from assemble_relative_geometry import assemble,apply
from evolve_relative_geometry_modes import evolve


def infer_action(points,arrows):
    labels=set(points)
    if not arrows or any(not isinstance(a,list) or len(a)!=2 for a in arrows):raise ValueError('Expected directed endpoint pairs')
    if len(arrows)!=len(labels) or {a[0] for a in arrows}!=labels or {a[1] for a in arrows}!=labels:
        raise ValueError('Arrow family must permute all declared vertices exactly once')
    d=len(next(iter(points.values())))
    rows=[list(points[a]) + [Q(1)] + list(points[b]) for a,b in arrows]
    r=0
    for j in range(d+1):
        p=next((i for i in range(r,len(rows)) if rows[i][j]),None)
        if p is None:raise ValueError('Arrow sources do not determine a unique affine action')
        rows[r],rows[p]=rows[p],rows[r]
        pivot=rows[r][j];rows[r]=[x/pivot for x in rows[r]]
        for i in range(len(rows)):
            if i!=r:
                factor=rows[i][j];rows[i]=[x-factor*y for x,y in zip(rows[i],rows[r])]
        r+=1
    if any(any(row[d+1:]) for row in rows[r:]):raise ValueError('Arrows are inconsistent with one affine action')
    matrix=tuple(tuple(rows[j][d+1+i] for j in range(d)) for i in range(d))
    shift=tuple(rows[d][d+1+i] for i in range(d))
    assert all(apply((matrix,shift),points[a])==points[b] for a,b in arrows)
    return {'matrix':[list(map(str,row)) for row in matrix],'translation':list(map(str,shift))}


def decode(source):
    if set(source)!={'schema','imaginary_square','vertices','arrow_families','seeds'} or source['schema']!='marici.real-complex-arrows.v1':raise ValueError('Expected real-complex-arrows.v1 fields only')
    q=Q(source['imaginary_square'])
    if q<=0:raise ValueError('imaginary_square must be positive')
    if not source['vertices']:raise ValueError('No vertices')
    points={};shape=None
    for name,v in source['vertices'].items():
        if set(v)!={'real','complex'} or any(len(z)!=2 for z in v['complex']):raise ValueError('Expected real coordinates and complex coefficient pairs')
        dims=(len(v['real']),len(v['complex']))
        if shape is None:shape=dims
        if dims!=shape:raise ValueError('Mixed coordinate dimensions')
        points[name]=tuple(map(Q,v['real']))+tuple(Q(x) for z in v['complex'] for x in z)
    if len(set(points.values()))!=len(points):raise ValueError('Distinct labels have identical coordinates')
    weights=[Q(1)]*shape[0]+[x for _ in range(shape[1]) for x in (Q(1),q)]
    if not weights:raise ValueError('Empty coordinate space')
    if not source['arrow_families']:raise ValueError('No arrow families')
    generators=[infer_action(points,arrows) for arrows in source['arrow_families']]
    seeds=[]
    for seed in source['seeds']:
        if set(seed)!={'vertex','role'} or seed['vertex'] not in points:raise ValueError('Unknown seed or seed fields')
        seeds.append({'point':list(map(str,points[seed['vertex']])),'role':seed['role']})
    return {'metric':[[str(w if i==j else 0) for j in range(len(weights))] for i,w in enumerate(weights)],'generators':generators,'seeds':seeds},points,shape


def run(source):
    decoded,points,shape=decode(source)
    geometry=assemble(decoded);cycle=evolve(decoded)
    generated={tuple(map(Q,p)) for p in geometry['vertices']}
    if generated!=set(points.values()):raise ValueError('Seed orbits do not recover all declared arrow vertices')
    def encode(p):
        p=list(map(Q,p));r,c=shape
        return {'real':list(map(str,p[:r])),'complex':[list(map(str,p[r+2*i:r+2*i+2])) for i in range(c)]}
    vs=[tuple(map(Q,p)) for p in geometry['vertices']]
    centroids=[tuple(sum(vs[i][j] for i in ids)/len(ids) for j in range(len(vs[0]))) for ids in geometry['supporting_facets']]
    return {'schema':'marici.real-complex-assembly.v1','arrow_source':source,'decoded_source':decoded,'geometry':geometry,'cycle':cycle,
            'coordinates':{'vertices':[encode(p) for p in vs],'center':encode(geometry['center']),'facet_centroids':[encode(p) for p in centroids]},
            'scope':'One metric affine arrow frontend and unchanged geometry/cycle assembler. Coordinates and roles are supplied; no physical particle identification or coefficient protocol inferred.'}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--source',required=True);ap.add_argument('--output',required=True);args=ap.parse_args()
    source=Path(args.source);result=run(json.loads(source.read_text()))
    paths=[source.resolve(),Path(__file__).resolve(),ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py',ROOT/'research/voevodsky/checkers/evolve_relative_geometry_modes.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'counts':result['cycle']['geometry']['counts'],'return_steps':result['cycle']['scheduled_atomic_steps_to_word_return']},indent=2))

if __name__=='__main__':main()
