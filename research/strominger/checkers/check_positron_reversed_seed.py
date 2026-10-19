#!/usr/bin/env python3
"""Add a reversed-electron seed to the comparative collection; exact checks only."""
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from assemble_relative_geometry import assemble,apply
from check_relative_geometry_mode_selection import select

def gen(source):
    g=source['generators'][0]
    return tuple(tuple(map(Q,r)) for r in g['matrix']),tuple(map(Q,g['translation']))
def iterate(g,p,n):
    for _ in range(n):p=apply(g,p)
    return p

def main():
    electron_path=ROOT/'research/voevodsky/inputs/relative-electron.json'
    positron_path=ROOT/'research/strominger/inputs/relative-positron-candidate.json'
    electron=json.loads(electron_path.read_text());positron=json.loads(positron_path.read_text())
    E=assemble(electron);P=assemble(positron)
    g,h=gen(electron),gen(positron)
    d=len(electron['metric']);basis=[(Q(0),)*d]+[tuple(Q(i==j) for i in range(d)) for j in range(d)]
    vertices=[tuple(map(Q,p)) for p in E['vertices']]
    forward={(p,apply(g,p)) for p in vertices};backward={(p,apply(h,p)) for p in vertices}
    ES,_=select(electron);PS,_=select(positron)
    # On corner coefficient records, reversal is C5 -> C5^-1=C5^4.
    # Polynomial character ring Q[z]/(1+z+z^2+z^3+z^4), z a primitive fifth root.
    def multiply(a,b):
        raw=[Q(0)]*7
        for i,x in enumerate(a):
            for j,y in enumerate(b):raw[i+j]+=x*y
        for k in range(6,3,-1):
            coefficient=raw[k]
            for j in range(5):raw[k-4+j]-=coefficient
        return tuple(raw[:4])
    one=(Q(1),Q(0),Q(0),Q(0));z=(Q(0),Q(1),Q(0),Q(0))
    powers=[one]
    for _ in range(5):powers.append(multiply(powers[-1],z))
    def power(k):return powers[k%5]
    forward_modes=[];reverse_modes=[]
    for k in range(5):
        v=[power(k*j) for j in range(5)]
        forward_modes.append(v[1:]+v[:1]==[multiply(power(k),x) for x in v])
        reverse_modes.append(v[-1:]+v[:-1]==[multiply(power(-k),x) for x in v])
    checks={
        'same_metric_and_seed_roles':electron['metric']==positron['metric'] and electron['seeds']==positron['seeds'],
        'affine_inverse_both_orders':all(apply(g,apply(h,p))==p and apply(h,apply(g,p))==p for p in basis),
        'reverse_equals_four_forward_steps':all(apply(h,p)==iterate(g,p,4) for p in basis),
        'both_order_five':all(iterate(g,p,5)==p and iterate(h,p,5)==p for p in basis),
        'each_primitive_arrow_reversed':backward=={(b,a) for a,b in forward},
        'same_complete_geometry':E==P,
        'same_attachment_interface':E['retained_attachment_interfaces']==P['retained_attachment_interfaces'],
        'same_centroid_selector_output':ES==PS,
        'fifth_root_exact_return':powers[5]==one,
        'forward_characters_derived':all(forward_modes),
        'reverse_characters_are_inverse':all(reverse_modes),
        'reversal_changes_nontrivial_characters':power(1)!=power(-1),
    }
    collection=[]
    for label,source_path in [('proton',ROOT/'research/voevodsky/inputs/relative-proton.json'),('neutron',ROOT/'research/voevodsky/inputs/relative-neutron.json'),('electron',electron_path),('neutrino candidate #1',ROOT/'research/strominger/inputs/relative-neutrino-candidate.json'),('positron candidate',positron_path)]:
        src=json.loads(source_path.read_text())
        # Active neutrino hypothesis has no newly introduced attachment mark.
        if label.startswith('neutrino'):src['seeds'][0]['role']='carrier'
        geometry=assemble(src)
        collection.append({'label':label,'source_path':str(source_path.relative_to(ROOT)).replace('\\','/'),'source_sha256':hashlib.sha256(source_path.read_bytes()).hexdigest(),'effective_source':src,'geometry':geometry,'physical_identification_derived':False,'arrow_reversal_of':'electron' if label=='positron candidate' else None})
    seed_point=tuple(map(Q,electron['seeds'][0]['point']))
    labelled={iterate(g,seed_point,i):'ABCDE'[i] for i in range(5)}
    out={'schema':'marici.strominger.positron-reversed-electron-seed.v1','status':'passed' if all(checks.values()) else 'failed','scientific_disposition':'reversed electron geometric candidate added; no charge-conjugation identification','electron_seed_cycle':['A','B','C','D','E','A'],'positron_seed_cycle':['A','E','D','C','B','A'],'label_coordinates':{label:list(map(str,p)) for p,label in labelled.items()},'checks':checks,'geometry':P,'mode_analysis':{'forward':'C5(a0,a1,a2,a3,a4)=(a1,a2,a3,a4,a0)','reverse':'C5^-1=C5^4','character_permutation':[0,4,3,2,1],'forward_eigenvalues':'zeta^k','reverse_eigenvalues':'zeta^-k','selected_character':None,'scope':'derived five-corner cyclic modes, not the existing full native spinor coefficient protocol'},'collection':collection,'not_derived':['opposite electric charge','physical charge conjugation','reversal of every native coefficient arrow','fermionic statistics','annihilation or beta-decay vertex'],'claim_boundary':'Inverting the supplied affine seed generator reverses its five primitive seed arrows and preserves the full relative assembly. Seed reversal is not yet charge conjugation or a reversal of the full coefficient protocol.'}
    deps=[Path(__file__),electron_path,positron_path,ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py',ROOT/'research/voevodsky/checkers/check_relative_geometry_mode_selection.py']
    out['source_hashes']={str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps}
    (ROOT/'research/strominger/results/positron_reversed_seed.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'checks':checks,'collection_labels':[x['label'] for x in collection]},indent=2))
    if not all(checks.values()):raise SystemExit(1)
if __name__=='__main__':main()
