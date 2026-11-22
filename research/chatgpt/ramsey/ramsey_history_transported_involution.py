"""Fit contiguous pieces to transported copies of the actual selected matching pair. Enumerate all optimal cuts; keep matching parity fixed. Conjugate the literal (23) along with each copy."""
from itertools import permutations,combinations
from ramsey_join_flag_phase import lift,final,move,R,D,json

def run():
    m,=final;n=move(m,R);frames={p:tuple(move(s,lift(p)) for s in (m,n)) for p in permutations(range(1,5))};history=json.loads((D/'ramsey_return_address_memory.json').read_text())['either']['last_collision'][0];out=[]
    for end in (None,4,7):
        path=history+([] if end is None else [end]);edges=list(zip(path,path[1:]));records={}
        for policy in ('rooted','root_even','unchanged_swap'):
            ps=[p for p in frames if p[0]==1 and (policy!='root_even' or sum(a>b for a,b in combinations(p,2))%2==0) and (policy!='unchanged_swap' or set(p[1:3])=={2,3})];allowed=[{p for p in ps if tuple(sorted(e)) in frames[p][k%2]} for k,e in enumerate(edges)];witness=[]
            if all(allowed):
                for k in range(len(edges)):
                    for cuts in combinations(range(1,len(edges)),k):
                        ix=(0,)+cuts+(len(edges),);opts=[set.intersection(*allowed[a:b]) for a,b in zip(ix,ix[1:])];
                        if all(opts):witness.append(dict(after=list(cuts),visits=[path[c] for c in cuts],options=[sorted(s) for s in opts]))
                    if witness:break
            records[policy]=dict(min_changes=len(witness[0]['after']) if witness else None,cuts=witness)
        out.append(dict(departure=end,records=records))
    return out
if __name__=='__main__':
    out=run();print([(q['departure'],[(k,v['min_changes'],[x['after'] for x in v['cuts']]) for k,v in q['records'].items()]) for q in out]);(D/'ramsey_history_transported_involution.json').write_text(json.dumps(out)+'\n')
