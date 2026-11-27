"""Compile every pre-promotion support envelope for the five-cell trap, in column-index coordinates."""
from ramsey38_trap_markability import view,prev,json,permutations

def run():
    path=prev.out/'ramsey38_interior_edge_trap_census.json';trap,=json.loads(path.read_text())['traps'];rows=set()
    for p in permutations(range(7)):
        cells={frozenset(p[v] for v in t) for t in trap['start']};cl,bd=view(cells);mask=lambda s:sum(1<<v for v in s);edge,=[mask(s) for s in cl-bd if len(s)==2];allowed=sum(1<<mask(s) for s in cl if len(s)==4 or s in bd or mask(s)==edge)|1
        for s in cl-bd:
            if len(s)!=3:continue
            for t in cells:
                if set(s)<=t:rows.add((mask(s),next(iter(t-set(s))),edge,allowed))
    out=prev.out/'ramsey38_inverse_trap_templates.tsv';out.write_text(''.join('%d\t%d\t%d\t%d\n'%r for r in sorted(rows)));print(len(rows))
if __name__=='__main__':run()
