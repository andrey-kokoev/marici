"""Read the literal rank/column incidence in both directions, no external sign mask."""
from itertools import combinations
from pathlib import Path
import json


def extrema(matrix):
    def read(lines):
        lows=list(map(min,lines)); highs=list(map(max,lines))
        return dict(max_of_min=max(lows), min_of_max=min(highs), minima=lows,maxima=highs)
    return dict(by_rank=read(matrix),by_column=read(list(zip(*matrix))))


def run():
    out={};profiles=set()
    for row in combinations(range(1,8),3):
        if min(row[1]-row[0],row[2]-row[1])<2:continue
        red=[[int(x==j) for j in range(1,8)] for x in row]
        # Blue is the complement of a column's membership in the WHOLE triple,
        # not the complement of equality with any one rank.
        inv=[[1-v for v in line] for line in red];a,b=extrema(red),extrema(inv)
        assert a['by_column']['maxima']==[int(j in row) for j in range(1,8)]
        assert b['by_column']['minima']==[int(j not in row) for j in range(1,8)]
        prof=tuple((z[t]['max_of_min'],z[t]['min_of_max']) for z in (a,b) for t in ('by_rank','by_column'));profiles.add(prof)
        out[''.join(map(str,row))]=dict(hit=a,miss=b)
    assert len(out)==10 and len(profiles)==1;path=Path(__file__).resolve().parents[1]/'results/ramsey_excel_extremal_roles.json';path.write_text(json.dumps(dict(scope='literal rank equality only, not the proposed signed or GA comparison',rows=out),indent=2)+'\n');print(profiles)

if __name__=='__main__':run()
