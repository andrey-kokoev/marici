"""Check whether catalogue row supports can fit a choice-sensitive starting mesh."""
from collections import Counter
import gzip,json
from ramsey38_trap_markability import prev


def run():
    geom=prev.out/'ramsey38_forward_greedy_closure.json';inv=prev.out/'ramsey38_inverse_trap_scan.txt';old=prev.out/'ramsey38_interior_edge_trap_census.json'
    traps=json.loads(old.read_text())['traps'];rows=json.loads(geom.read_text())['unsafe'];blocked=[r for r in rows if not r['extendible']];assert [(r['start'],r['end']) for r in blocked]==[(r['start'],r['end']) for r in traps]
    widths=[len(set().union(*map(set,r['start']))) for r in rows if r['extendible']];assert all(w<7 for w in widths)
    # Decode the graph6 upper triangle in six-bit chunks. OR the vertex incidence
    # contributions for each chunk; check the actual external-neighbour union of
    # every seven-column root, without consulting promotion/move lists.
    pairs=[(i,j) for j in range(27) for i in range(j)];tab=[]
    for k in range(0,len(pairs),6):
        vals=[]
        for code in range(64):
            vals.append([(i,j) for h,(i,j) in enumerate(pairs[k:k+6]) if code&(32>>h)])
        tab.append(vals)
    deg=Counter();width=Counter();records=0;flags=[1<<i for i in range(27)]
    with gzip.open(prev.catalogue,'rb') as f:
        for line in f:
            w=line.strip();assert len(w)==60 and w[0]==90;g=[0]*27;records+=1
            for chunk,c in zip(tab,w[1:]):
                for i,j in chunk[c-63]:g[i]|=flags[j];g[j]|=flags[i]
            deg[min(t.bit_count() for t in g)]+=1
            for u,L in enumerate(g):
                if L.bit_count()!=7:continue
                cover=0
                for j,t in enumerate(g):
                    if j!=u and not L&flags[j]:cover|=t
                width[(cover&L).bit_count()]+=1
    assert width.keys()=={7} and 'template_matches=0' in inv.read_text();out=dict(records=records,min_degree_histogram=dict(deg),external_row_union_width=dict(width),extendible_unsafe_start_widths=widths,geometry_sha=prev.sha(geom.read_bytes()),catalogue_sha=prev.sha(prev.catalogue.read_bytes()),inverse_scan_sha=prev.sha(inv.read_bytes()));print(out);prev.save(prev.out/'ramsey38_greedy_marked_coverage.json',out)
if __name__=='__main__':run()
