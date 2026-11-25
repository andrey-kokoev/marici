"""On negative cores, separate certificate-family UNSAT from ordinary five-colorability. Replay obstruction by explicit candidate rectangles on the saved challenge supports."""
from ramsey312_google_two_step import *
from collections import Counter

def main():
 neg={tuple(x['d']):x for f in D.glob('ramsey312_f2995_*.jsonl') for x in map(json.loads,f.open()) if x['cert'] is None};out=[]
 for line,edge in zip((D/'ramsey312_five_neg_domains.txt').read_text().splitlines(),Path(sys.argv[1]).read_text().splitlines(),strict=True):
    row=line.split();es=edge.split();d=tuple(map(int,row[:5]));assert row[:5]==es[:5];s=list(map(int,row[7:]));h=F^sum(1<<v for v in d);anchors=[adj[i]&h for i in d];small=neg[d]['obstructing_supports'];assert set(small)<=set(s);full=(1<<len(small))-1;mask=[sum(1<<j for j,x in enumerate(small) if x>>v&1) for v in range(52)];options=[]
    for a in anchors:
        possibilities=set()
        for t in sets(h&~a,10):
            missed=full
            for v in bits(t):missed&=~mask[v]
            possibilities.update(missed&mask[v] for v in bits(a))
        maximal=[]
        for p in sorted(possibilities,key=int.bit_count,reverse=True):
            if not any(p&m==p for m in maximal):maximal.append(p)
        options.append(maximal)
    # One choice per anchor; any subset covered by an allowed rectangle lies in a maximal rectangle. Negative verified by explicit union recursion.
    def cover(i,rem):
        if not rem:return True
        if i==5:return False
        return any(cover(i+1,rem&~m) for m in options[i])
    assert not cover(0,full)
    edges=[tuple(map(int,t.split(':'))) for t in es[5:]];lit=lambda i,k:1+i*5+k
    with Solver(name='g4') as sl:
        for i in range(len(s)):sl.add_clause([lit(i,k) for k in range(5)])
        for k,a in enumerate(anchors):sl.add_clause([lit(s.index(a),k)])
        for i,j,m in edges:
            for k in range(5):sl.add_clause([-lit(i,k),-lit(j,k)])
        ok=sl.solve();model=set(sl.get_model()) if ok else set();color=[next(k for k in range(5) if lit(i,k) in model) for i in range(len(s))] if ok else None
        if ok:assert all(color[i]!=color[j] for i,j,_ in edges)
    out.append(dict(d=d,challenge=len(small),choices=[len(o) for o in options],supports=len(s),edges=len(edges),color=color));print(d,len(small),[len(o) for o in options],ok,flush=True)
 (D/'ramsey312_failed_cover_colorings.json').write_text(json.dumps(out))
if __name__=='__main__':main()
