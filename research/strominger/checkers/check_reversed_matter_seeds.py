#!/usr/bin/env python3
"""Exact reversed seed records for antiproton, antineutron and antineutrino."""
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from assemble_relative_geometry import assemble,apply
from check_relative_geometry_mode_selection import select

def gen(raw):return tuple(tuple(map(Q,row)) for row in raw['matrix']),tuple(map(Q,raw['translation']))
def main():
    registry_path=ROOT/'research/strominger/results/neutrino_seed_candidates.json'
    registry=json.loads(registry_path.read_text())
    registry_source=registry['candidates'][0]['source']
    models=[];checks={};deps=[Path(__file__),registry_path,ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py',ROOT/'research/voevodsky/checkers/check_relative_geometry_mode_selection.py']
    for name in ('proton','neutron','neutrino'):
        anti_path=ROOT/f'research/strominger/inputs/relative-anti{name}-candidate.json'
        anti=json.loads(anti_path.read_text());deps.append(anti_path)
        if name=='neutrino':source=registry_source;source_path=registry_path
        else:
            source_path=ROOT/f'research/voevodsky/inputs/relative-{name}.json'
            source=json.loads(source_path.read_text());deps.append(source_path)
        geometry=assemble(source);reversed_geometry=assemble(anti)
        selected,_=select(source);anti_selected,_=select(anti)
        d=geometry['dimension'];basis=[(Q(0),)*d]+[tuple(Q(i==j) for i in range(d)) for j in range(d)]
        points=[tuple(map(Q,p)) for p in geometry['vertices']];ids={p:i for i,p in enumerate(points)}
        forward=[];backward=[]
        checks[f'{name}_metric_and_roles_retained']=source['metric']==anti['metric'] and source['seeds']==anti['seeds']
        checks[f'{name}_same_generator_count']=len(source['generators'])==len(anti['generators'])
        for index,(raw,inv_raw) in enumerate(zip(source['generators'],anti['generators'])):
            g,h=gen(raw),gen(inv_raw)
            checks[f'{name}_generator_{index}_affine_inverse']=all(apply(g,apply(h,p))==p and apply(h,apply(g,p))==p for p in basis)
            f={(ids[p],ids[apply(g,p)]) for p in points};b={(ids[p],ids[apply(h,p)]) for p in points}
            checks[f'{name}_generator_{index}_arrows_reversed']=b=={(j,i) for i,j in f}
            forward.append(sorted(f));backward.append(sorted(b))
        checks[f'{name}_complete_geometry_unchanged']=geometry==reversed_geometry
        checks[f'{name}_centroid_selection_unchanged']=selected==anti_selected
        models.append({'label':f'anti{name} candidate','source_path':str(anti_path.relative_to(ROOT)).replace('\\','/'),'source_sha256':hashlib.sha256(anti_path.read_bytes()).hexdigest(),'effective_source':anti,'geometry':reversed_geometry,'arrow_reversal_of':name if name!='neutrino' else 'neutrino candidate #1','physical_identification_derived':False,'forward_generator_arrow_tables':forward,'reversed_generator_arrow_tables':backward})
    out={'schema':'marici.strominger.reversed-matter-seeds.v1','status':'passed' if all(checks.values()) else 'failed','models':models,'checks':checks,'reversal_rule':'invert every supplied affine seed generator separately; preserve labels, metric, seed roles and records','scope':'seed-generator reversal; not reversal of every derived native coefficient arrow','source_hashes':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps}}
    (ROOT/'research/strominger/results/reversed_matter_seeds.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'checks':len(checks),'models':[m['label'] for m in models]},indent=2))
    if not all(checks.values()):raise SystemExit(1)
if __name__=='__main__':main()
