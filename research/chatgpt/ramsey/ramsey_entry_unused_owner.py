"""Read the unused duad at the entry partition. Inspect the common owner and its tetrahedral fan count, without tracing a complementary path. Distinguish conditional from unconditional sufficiency."""
from ramsey_folded_entry_handoff import P,T,X,D,json
from ramsey_row_quotient_constructor import move,R

def run():
    rows=json.loads((D/'ramsey_literal_swap_polarity_controls.json').read_text());s=next(q for q in rows if q['selected']);out=[]
    for q in rows:
        m=frozenset(map(tuple,q['matching']));n=move(m,R);z={P.index(d) for d in T[1]}-{x for x,j in m|n if j==16};d,=z;owner=dict(m)[d];common=(d,owner) in n;fans=sum(bool(set(X[a])&set(X[b])) for a,b in T[owner-15]);target=q['entry_cycle']==s['entry_cycle'] and q['exit_thread']==s['exit_thread'] and len(m&n)==10;out.append(dict(target=target,unused=d,owner=owner,common=common,fans=fans,selected=q['selected']))
    return out
if __name__=='__main__':
    out=run();print([q for q in out if q['target']]);print(sum(q['common'] and q['fans']==3 for q in out));(D/'ramsey_entry_unused_owner.json').write_text(json.dumps(out)+'\n')
