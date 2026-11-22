"""Recover every incoming active incidence by inverse matching lookup at the partition, with no previous-flag cache. Count counterexamples to recovering the same inbound flag from boundary plus outbound flag alone."""
from collections import Counter
from ramsey_seed_affine_witness import P,T,m,mate,r
from ramsey_folded_entry_handoff import D,json

def run():
    rows=[]
    for M,N in ((m,mate),(mate,m)):
        back={j:i for i,j in M};other={j:i for i,j in N};active={j for j in back if back[j]!=other[j]};assert len(active)==5;turns={j:(back[j],other[j]) for j in sorted(active)};x=0;prefix=[]
        for _ in range(2):
            j=dict(M)[x];out=other[j];assert turns[j]==(x,out);prefix.append((j,out));x=out
        rows.append(dict(active_turns=turns,queried_exits=prefix))
    hist=Counter();total=0
    def visit(i,taken,pairs):
        nonlocal total
        if i==15:
            total+=1;forward=dict(pairs);inv={j:d for d,j in pairs};j,out=rows[0]['queried_exits'][1];
            if forward[r[out]]==r[j]:hist[inv[j]]+=1
            return
        for j,t in enumerate(T,15):
            if j not in taken and P[i] in t and (i!=0 or j==16) and (i!=7 or j==29):visit(i+1,taken|{j},pairs+[(i,j)])
    visit(0,set(),[]);assert total==36;return dict(selected=rows,boundary_matchings=total,compatible_predecessors=hist)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_partition_turn_lookup.json').write_text(json.dumps(out)+'\n')
