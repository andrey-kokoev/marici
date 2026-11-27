"""Test the literal rank-to-column relation, without a graph or target order."""
import json
from hashlib import sha256
from itertools import combinations
from pathlib import Path

D = Path(__file__).resolve().parents[1] / 'results'


def array(k):
    return [s for s in combinations(range(1, k+1), 3) if min(s[1]-s[0], s[2]-s[1]) >= 2]


def reduce(rows, k):
    cells = {}
    for row in rows:
        for i, pos in enumerate(row, 1):
            for j in range(1,k+1):
                cells.setdefault((i,j), {}).setdefault(pos==j, row)
    true = {ij for ij, fiber in cells.items() if True in fiber}
    split = {ij for ij, fiber in cells.items() if len(fiber)==2}
    assert set(cells)=={(i,j) for i in range(1,4) for j in range(1,k+1)}
    for (i,j), f in cells.items():
        assert set(f)==set(cells[4-i,k+1-j])
    return dict(rows=len(rows),product=len(cells),true_links=len(true),cells=sum(map(len,cells.values())),split=sorted(split),witnesses={f'{i}:{j}':dict(hit=cells[i,j][True],miss=cells[i,j][False]) for i,j in sorted(split)})


def run():
    rows=array(7); insert=rows[:7]+[(1,3,7),(1,4,7)]+rows[7:8]+[(1,5,7)]+rows[8:];slide=rows.copy();slide[4]=(2,4,7);slide[2:2]=[(1,4,6),(2,4,6)]
    charts={str(k):reduce(array(k),k) for k in (6,7,8)}
    for name,rr in [('insert',insert),('slide_insert',slide)]:
        assert rr==[tuple(8-v for v in reversed(s)) for s in reversed(rr)]
        charts[name]=reduce(rr,7)
    for k in (6,7,8):assert len(charts[str(k)]['split'])==3*(k-4)
    p=D/'ramsey_excel_rank_column_protocol.md';out=dict(protocol_sha=sha256(p.read_bytes()).hexdigest(),charts=charts);(D/'ramsey_excel_rank_column.json').write_text(json.dumps(out,indent=2)+'\n');print([(k,v['product'],v['cells']) for k,v in charts.items()])

if __name__=='__main__':run()
