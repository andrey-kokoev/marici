"""Explain the frozen 68 hits: re-observation vs same move supported by different tails."""
from ramsey38_visible_swap_path import P,R,graph,gzip,json,Counter,combinations,prev
from collections import defaultdict

def run():
    ref=json.loads(R.read_text());assert ref['protocol_sha']==prev.sha(P.read_bytes());roots={e['record']:e for e in ref['records']};tot=Counter();examples={};out=[]
    with gzip.open(prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i not in roots:
                if i>max(roots):break
                continue
            g=graph(line.strip());u=roots[i]['root'];L=g[u];rows={v:frozenset(g[v]&L) for v in g.keys()-L-{u}};c=Counter()
            for x,y in combinations(sorted(rows),2):
                s,t=rows[x],rows[y];tail=s&t;swap=s^t
                if not(len(s)==len(t)==3 and len(tail)==2):continue
                c['eligible']+=1;visible={r for v,r in rows.items() if v not in (x,y) and len(r)==3};tails=defaultdict(set)
                for a,b in combinations(visible,2):
                    if len(a&b)==2:tails[a^b].add(a&b)
                ts=tails[swap];new=ts-{tail};same=tail in ts
                assert same==(s in visible and t in visible)
                if ts:
                    cat='both' if same and new else 'same_only' if same else 'new_only';c[cat]+=1
                if new:
                    c['new']+=1;c['disjoint_possible']+=any(not z&tail for z in new);c['one_label_overlap_possible']+=any(len(z&tail)==1 for z in new);c['neither_hidden_support_visible']+=s not in visible and t not in visible;examples.setdefault('new',dict(record=i,root=u,hidden_rows=[x,y],hidden_supports=[sorted(s),sorted(t)],swap=sorted(swap),visible_witness_tails=sorted(map(sorted,new))))
                # Diagnostic control: keep the revealed tail fixed, average the same
                # new-tail predicate over all ten possible exchanges disjoint from it.
                c['null_numerator']+=sum(bool(tails[frozenset(ab)]-{tail}) for ab in combinations(L-tail,2))
            old=roots[i]['counts'];assert sum(c[k] for k in ('both','same_only','new_only'))==old['hits'] and c['eligible']==old['eligible'];tot.update(c);out.append(dict(record=i,root=u,counts=dict(c)))
    print(tot,examples);prev.save(prev.out/'ramsey38_swap_context_audit.json',dict(source_sha=prev.sha(R.read_bytes()),counts=dict(tot),roots_with_new=sum(e['counts'].get('new',0)>0 for e in out),conditional_expected_new=tot['null_numerator']/10,examples=examples,per_root=out))
if __name__=='__main__':run()
