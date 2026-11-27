"""Candidate static BR/NN comparison: one column permutation exchanges sides in both literal rows."""
from itertools import permutations, combinations
from pathlib import Path
import sys,json
D=Path(__file__).resolve().parents[1]/'results';sys.path.insert(0,str(D.parents[1]/'chatgpt'/'ramsey'))
from ramsey_row_quotient_constructor import action,move,comp,R


def run():
    rows=('BRNN','BNRN');four=set(range(4));pos=[{i for i,x in enumerate(s) if x!='N'} for s in rows];ys=[p for p in permutations(range(4)) if all({p[i] for i in side}==four-side for side in pos)];y,=ys;edges=list(combinations(range(4),2));e=tuple(edges.index(tuple(sorted((y[i],y[j])))) for i,j in edges);Y=action(e);assert all(Y[Y[i]]==i and R[Y[i]]==Y[R[i]] for i in range(30));marks=((0,16),(7,29));targets=[(Y[i],Y[j]) for i,j in marks];cases=[]
    for c in json.loads((D/'ramsey_seed_boundary_residue.json').read_text())['cases']:
        G=set(map(tuple,c['frame']));m=frozenset(map(tuple,c['matching']));rm=move(m,R);states=[m,rm,move(m,Y),move(rm,Y)];assert states[-1]==move(states[2],R)
        cases.append(dict(components=1+len(c['other_cycles']),frame_preserved=G=={comp(e,comp(g,e)) for g in G},comparison=[[flag in s for flag in marks] for s in states],entry_image_selected=[targets[0] in s for s in states[:2]]))
    out=dict(definition='One permutation of physical columns exchanging BR and NN as unordered sides simultaneously in both rows. R below is literal row change, not within-side X.',rows=rows,permutation=[i+1 for i in y],flag_images=targets,state_order=['M','rM','YM','YrM=rYM'],cases=cases);print(out);(D/'ramsey_literal_side_exchange.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':run()
