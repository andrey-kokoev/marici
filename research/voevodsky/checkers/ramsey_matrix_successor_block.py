"""Derive the named S block and internal constraints from the saved width step, then check an endpoint."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import runpy,json
D=Path(__file__).resolve().parent;R=D.parent/'results'


def derive(x):
    old,new=x['layers'];root_chart=next(c for c in old['charts'] if c['half']=='upper');oldbit={i:b for b,i in root_chart['corner_occurrence'].items()};roles=sorted(oldbit.values());seen=set();patches=[];height=len(new['X'])
    for m in x['upper_relative_role_maps']:
        current={j:oldbit[i] for i,j in m['occurrences']};fresh=sorted(set(current)-seen);seen.update(current)
        if len(fresh)==8:continue
        assert len(fresh)==4;upper={current[j] for j in fresh};mir={''.join(str(1-int(k)) for k in reversed(b)) for b in upper};lower=[height+1-j for j in fresh];chart=next(c for c in new['charts'] if c['half']=='mirror' and c['start']==[new['width']-v for v in reversed(m['new_start'])]);assert {b for b,j in chart['corner_occurrence'].items() if j in lower}==mir
        patches.extend([(frozenset(upper),fresh),(frozenset(mir),lower)])
    faces={f for f,_ in patches};edges={f&g for f,g in combinations(faces,2) if f&g};corners={frozenset([r]) for r in roles};assert [len(faces),len(edges),len(corners)]==[6,12,8]
    def name(cell):return ''.join(next(iter(v)) if len(v)==1 else '*' for v in map(set,zip(*cell)))
    cells={name(c):c for c in faces|edges|corners};labels=sorted(cells);S=[[int(r in cells[c]) for c in labels] for r in roles];overlap=[[len(cells[i]&cells[j]) for j in labels] for i in labels];assert all(sum(row)==7 for row in S);forced=sum(overlap[i][j]>0 for i,j in combinations(range(26),2));return dict(port_roles=roles,core_labels=labels,S=S,source_face_occurrences={name(f):ids for f,ids in patches},internal_block=[[None if i!=j and not v else 0 for j,v in enumerate(row)] for i,row in enumerate(overlap)],forced_blue_off_diagonal_pairs=forced,unassigned_pairs=325-forced)


def audit():
    out=derive(json.loads((R/'ramsey_matrix_width_step.json').read_text()));g=runpy.run_path(str(D/'ramsey_cube_construct35.py'));cs=out['core_labels'];bits=out['port_roles'];S=out['S'];known=out['internal_block'];assert all(S[i][j]==(g['G'][26+g['corner'].index(b)]>>g['cells'].index(c)&1) for i,b in enumerate(bits) for j,c in enumerate(cs));assert all(known[i][j] is None or not(g['G'][g['cells'].index(c)]>>g['cells'].index(d)&1) for i,c in enumerate(cs) for j,d in enumerate(cs));print('verified entries',8*26,'red',sum(map(sum,S)),'forced blue pairs',out['forced_blue_off_diagonal_pairs'],'unknown',out['unassigned_pairs']);(R/'ramsey_matrix_successor_block.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
