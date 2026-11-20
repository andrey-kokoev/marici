"""Conditional port, no closure trigger: monitor whether an FCC pair-site contains a marked tetrahedral label. Feed its two edge changes to the existing reader."""
from pathlib import Path
import json,sys
from collections import Counter
from fractions import Fraction
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'nima/checkers'))
from check_four_packet_cycle import UNIT,E2,tensor,sew
from check_four_packet_record_feedback import readout,cycle
D=json.loads((ROOT/'strominger/results/fcc-first-transport.json').read_text());left=('13','14','24');right=('13','23','24');perm=str.maketrans('1234','3412')
def run(path,mark):
    vals=[mark in s for s in path];bits=[int(a!=b) for a,b in zip(vals,vals[1:])];bank=tensor((UNIT,E2)[bits[1]],(UNIT,E2)[bits[0]]);return bits,readout(bank),cycle(UNIT,bank)[0]
if __name__=='__main__':
    ids={tuple(v['barycentric']):v['id'] for v in D['vertices']};edges={(e['source'],e['target']):tuple(e['sector']) for e in D['directed_moves']};count=0
    assert tuple(''.join(sorted(s.translate(perm))) for s in left)==right
    for c in D['coarse_cells']:
        if not c['id'].startswith('oct-'):continue
        b=tuple(map(min,zip(*c['vertices'])));site=lambda s:ids[tuple(v+(str(i+1) in s) for i,v in enumerate(b))];words=[[edges[site(u),site(v)] for u,v in zip(p,p[1:])] for p in (left,right)];assert words[0]==words[1][::-1];count+=1
    print('source cells checked',count)
    for m in '1234':
        a,ra,xa=run(left,m);b,rb,xb=run(right,m);t,rt,xt=run(right,m.translate(perm));assert ra==rb and xa==tuple(-v for v in xb) and (a,ra,xa)==(t,rt,xt);print(m,a,b,'fixed outputs',tuple(map(str,xa)),tuple(map(str,xb)),'co-transport matches',xt==xa)
