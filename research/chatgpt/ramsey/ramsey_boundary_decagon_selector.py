"""Test boundary and literal swap on bare cycles, not completed matchings. Are the two marked neighbours sufficient to determine an oriented half from 0 to 29?"""
from itertools import product
from ramsey_folded_entry_handoff import P,T,D,json
from ramsey_row_quotient_constructor import R

def run():
    adj={i:set() for i in range(30)}
    for j,t in enumerate(T,15):
        for d in t:i=P.index(d);adj[i].add(j);adj[j].add(i)
    def walk(w):
        if len(w)==10:
            if w[0] in adj[w[-1]] and w[1]<w[-1]:yield w
        else:
            for v in sorted(adj[w[-1]]-set(w)):
                if v>w[0]:yield from walk(w+[v])
    rows=[]
    for i in range(15):
        for w in walk([i]):
            arcs=[{tuple(sorted((w[k],w[(k+1)%10]))) for k in range(p,10,2)} for p in (0,1)];ex=any({tuple(sorted((R[x],R[y]))) for x,y in a}==b for a,b in [arcs]);entry=(0,16);exit=(7,29);en=any(entry in a for a in arcs);end=any(exit in a for a in arcs);same=any({entry,exit}<=a for a in arcs);rows.append(dict(cycle=w,swap=ex,entry=en,exit=end,same=same))
    qs={'all':lambda q:True,'swap':lambda q:q['swap'],'entry':lambda q:q['entry'],'exit':lambda q:q['exit'],'both':lambda q:q['entry'] and q['exit'],'same':lambda q:q['same'],'swap_entry':lambda q:q['swap'] and q['entry'],'swap_exit':lambda q:q['swap'] and q['exit'],'swap_both':lambda q:q['swap'] and q['entry'] and q['exit'],'swap_same':lambda q:q['swap'] and q['same']};return dict(counts={k:sum(f(q) for q in rows) for k,f in qs.items()},both=[q for q in rows if qs['both'](q)])
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_boundary_decagon_selector.json').write_text(json.dumps(out)+'\n')
