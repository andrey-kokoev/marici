"""Separate proposal-pool uniqueness from actual graph-forced red support."""
from ramsey38_blind_swap_row import R,prev,gzip,json,graph,propose,protocol,Counter,Fraction
from collections import defaultdict

def independent_sevens(g):
    ans=[]
    def walk(rest,chosen):
        if len(chosen)==7:ans.append(frozenset(chosen));return
        while len(rest)+len(chosen)>=7:
            x=min(rest);rest=rest-{x};walk(rest-g[x],chosen+[x])
    walk(set(g),[]);return ans

def run(diagnose=False):
    misses=[];reasons=Counter();sizes=Counter();edits=Counter()
    ref=json.loads(R.read_text());rows={z['record']:z for z in ref['per_root']};strata=defaultdict(Counter);expected=defaultdict(Fraction);total=Counter();examples={}
    with gzip.open(prev.catalogue,'rt') as f:
        for i,w in enumerate(f,1):
            if i not in rows:
                if i>max(rows):break
                continue
            g=graph(w.strip());u=rows[i]['root'];L=g[u];O=set(g)-L-{u};seven=independent_sevens(g);labels=sorted(L);subsets=[frozenset(x for j,x in enumerate(labels) if m>>j&1) for m in range(128)]
            for v in sorted(O):
                vis={x:frozenset(g[x]&L) for x in O-{v}};fixed=g[v]&O;choices,base=propose(L,vis,fixed);truth=frozenset(g[v]&L);forbid=set().union(*(vis[x] for x in fixed));needs={s&L for s in seven if v not in s and s.isdisjoint(fixed)}
                legal={q for q in subsets if not(q&forbid) and all(q&n for n in needs)};assert truth in legal
                total['masked']+=1;total['forced']+=len(legal)==1;total['hits']+=truth in choices
                if not choices:continue
                pool='singleton' if len(base)==1 else 'all_guessed' if choices==base else 'strict_choice';status='forced' if len(legal)==1 else 'ambiguous';k=pool+' / '+status;c=strata[k];c['issued']+=1;c['guesses']+=len(choices);c['hits']+=truth in choices;c['recoverable']+=truth in base;c['legal_guesses']+=len(choices&legal);expected[k]+=Fraction(len(choices),len(base)) if truth in base else 0
                examples.setdefault(k,dict(record=i,root=u,row=v,base=len(base),legal=len(legal),choices=len(choices),hit=truth in choices))
                if diagnose and k=='strict_choice / forced':
                    assert truth not in base
                    triples=set(s for s in vis.values() if len(s)==3)
                    why='wrong size' if len(truth)!=3 else 'already visible' if truth in triples else 'no one-swap source'
                    if why=='no one-swap source':assert all(len(t&truth)!=2 for t in triples)
                    # Feasible masks are upward-closed among triangle-safe labels.
                    # Unique iff all safe labels are individually indispensable.
                    safe=L-forbid;assert truth==safe;blockers={}
                    for a in sorted(safe):
                        witness=next(s for s in seven if v not in s and s.isdisjoint(fixed) and s&safe=={a});blockers[a]=sorted(witness)
                    dist=min(len(s^truth) for s in triples);edits[dist]+=1;sizes[len(truth)]+=1;reasons[why]+=1
                    misses.append(dict(record=i,root=u,row=v,support=sorted(truth),why=why,already_visible=truth in vis.values(),min_bit_changes_from_visible_triple=dist,blue_seven_blocking_each_omission=blockers))
    if diagnose:
        old=prev.out/'ramsey38_swap_choice_strata.json';assert len(misses)==json.loads(old.read_text())['issued']['strict_choice / forced']['issued'];print(reasons,sizes,edits);prev.save(prev.out/'ramsey38_swap_forced_pool_misses.json',dict(source_sha=prev.sha(old.read_bytes()),reasons=dict(reasons),sizes=dict(sizes),min_bit_changes=dict(edits),rows=misses));return
    assert total['hits']==ref['counts']['hits'] and sum(expected.values())==Fraction(str(ref['expected_same_budget']));res={k:dict(c,control=float(expected[k])) for k,c in strata.items()};print(total,res);prev.save(prev.out/'ramsey38_swap_choice_strata.json',dict(source_sha=prev.sha(R.read_bytes()),counts=dict(total),issued=res,examples=examples))
if __name__=='__main__':
    import sys
    run('--diagnose' in sys.argv)
