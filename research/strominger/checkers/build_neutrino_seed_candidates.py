#!/usr/bin/env python3
"""Run numbered arrow hypotheses through the unchanged relative assembler.
Display projections use floats; all construction and incidence checks are exact.
"""
from pathlib import Path
from fractions import Fraction as Q
import copy
import hashlib
import json
import math
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from assemble_relative_geometry import assemble, apply

def simplex_source(n,cycles):
    d=n-1
    points=[(0,)*d]+[tuple(int(i==j) for i in range(d)) for j in range(d)]
    generators=[]
    for cycle in cycles:
        perm=list(range(n))
        for a,b in zip(cycle,cycle[1:]+cycle[:1]): perm[a]=b
        t=points[perm[0]]
        matrix=[[points[perm[j+1]][i]-t[i] for j in range(d)] for i in range(d)]
        generators.append({'matrix':matrix,'translation':list(t)})
    return {'metric':[[8 if i==j else 4 for j in range(d)] for i in range(d)],'generators':generators,'seeds':[{'point':list(points[0]),'role':'carrier'}]},dict(zip('ABCDEFG',points))

def project(points,G):
    # G=L L^T, so source-coordinate row x maps to x L.
    d=len(G); L=[[0.0]*d for _ in range(d)]
    for i in range(d):
        for j in range(i+1):
            v=float(Q(G[i][j]))-sum(L[i][k]*L[j][k] for k in range(j))
            L[i][j]=math.sqrt(v) if i==j else v/L[j][j]
    mapped=[[sum(float(Q(x[i]))*L[i][j] for i in range(d)) for j in range(d)] for x in points]
    mean=[sum(p[j] for p in mapped)/len(mapped) for j in range(d)]
    return [[(p[j]-mean[j]) if j<d else 0 for j in range(3)] for p in mapped]

def build():
    specs=[]
    for number,title,cycles in [(1,'Single three-cycle',[[0,1,2]]),(2,'Reversed three-cycle',[[0,2,1]]),(3,'Both orientations',[[0,1,2],[0,2,1]]),(4,'Two cycles sharing A',[[0,1,2],[0,3,4]])]:
        source,labels=simplex_source(3 if number<4 else 5,cycles)
        specs.append((number,title,source,labels,[["ABCDEFG"[i] for i in c]+["ABCDEFG"[c[0]]] for c in cycles],'regular-simplex metric fixture; dimension and metric supplied, not derived from arrows'))
    source=json.loads((ROOT/'research/voevodsky/inputs/relative-neutron.json').read_text())
    g=source['generators'][0];gen=(tuple(tuple(map(Q,r)) for r in g['matrix']),tuple(map(Q,g['translation'])))
    labels={}
    for prefix,seed in zip(('A','D'),source['seeds']):
        p=tuple(map(Q,seed['point']))
        for offset in range(3): labels[chr(ord(prefix)+offset)]=p; p=apply(gen,p)
    specs.append((5,'Two disjoint rim cycles',source,labels,[list('ABCA'),list('DEFD')],'existing neutron metric, two seed orbits, and reserved-cap roles retained as a control'))
    source={'metric':[[8,0],[0,8]],'generators':[{'matrix':[[0,-1],[1,0]],'translation':[1,0]}],'seeds':[{'point':[0,0],'role':'carrier'}]}
    specs.append((6,'Single four-cycle',source,dict(zip('ABCD',[(0,0),(1,0),(1,1),(0,1)])),[list('ABCDA')],'planar square realization supplied; NOT a regular tetrahedron inferred from four labels'))
    source=json.loads((ROOT/'research/voevodsky/inputs/relative-electron.json').read_text())
    _,labels=simplex_source(5,[[0,1,2,3,4]])
    specs.append((7,'Single five-cycle / electron control',source,labels,[list('ABCDEA')],'existing electron metric and attachment-pole role retained as a control'))
    candidates=[]
    for number,title,source,labels,cycles,convention in specs:
        geometry=assemble(source)
        vertices=[tuple(map(Q,p)) for p in geometry['vertices']]
        ids={p:i for i,p in enumerate(vertices)}
        cycle_ids=[[ids[tuple(map(Q,labels[k]))] for k in c] for c in cycles]
        # Each proposed arrow must be an action of at least one supplied generator.
        generators=[(tuple(tuple(map(Q,r)) for r in g['matrix']),tuple(map(Q,g['translation']))) for g in source['generators']]
        assert all(any(apply(g,vertices[a])==vertices[b] for g in generators) for c in cycle_ids for a,b in zip(c,c[1:]))
        names={ids[tuple(map(Q,p))]:name for name,p in labels.items()}
        projected=project(geometry['vertices'],geometry['metric'])
        projected.append([0,0,0])
        candidate={'id':number,'title':title,'seed_cycles':cycles,'cycle_vertex_ids':cycle_ids,'vertex_labels':[names[i] for i in range(len(vertices))]+['O'],'realization_convention':convention,'source':source,'geometry':geometry,'projected_vertices':projected,'projection_dimension':3,'projection_warning':geometry['dimension']>3,'physical_identification':False,'spin_decoration':False}
        candidates.append(candidate)
    assert candidates[0]['geometry']==candidates[1]['geometry']==candidates[2]['geometry']
    assert candidates[4]['geometry']==assemble(json.loads((ROOT/'research/voevodsky/inputs/relative-neutron.json').read_text()))
    assert candidates[6]['geometry']==assemble(json.loads((ROOT/'research/voevodsky/inputs/relative-electron.json').read_text()))
    return {'schema':'marici.strominger.neutrino-seed-candidates.v1','status':'passed','processor':'research/voevodsky/checkers/assemble_relative_geometry.py','processor_sha256':hashlib.sha256((ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py').read_bytes()).hexdigest(),'checks':{'all_seven_assembled':True,'all_seed_arrows_match_generators':True,'orientation_variants_same_geometry':True,'neutron_control_matches':True,'electron_control_matches':True},'candidates':candidates,'claim_boundary':'Numbered geometric hypotheses with explicit realization inputs, not seven neutrino species. No charge/spin/flavor decoration.'}

def main():
    out=build()
    result=ROOT/'research/strominger/results/neutrino_seed_candidates.json'
    result.write_text(json.dumps(out,indent=2)+'\n')
    page=ROOT/'papers/witness-generators/proton-neutron-assembly.html'
    text=page.read_text(encoding='utf-8')
    start='<script id="neutrino-seed-data" type="application/json">'
    if start in text:
        a=text.index(start)+len(start); b=text.index('</script>',a)
        text=text[:a]+json.dumps(out,separators=(',',':'))+text[b:]
        page.write_text(text,encoding='utf-8')
    print(json.dumps({'status':out['status'],'candidates':[{'id':c['id'],'dimension':c['geometry']['dimension'],'counts':c['geometry']['counts']} for c in out['candidates']]},indent=2))
if __name__=='__main__': main()
