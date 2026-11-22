"""All maximal four-port multisets on two legal deletions of the same fresh parent. For each endpoint-using anchor, count unordered remaining triples by the first unmet size budget. Distinguish original seven-set coverage from compatibility with future ports."""
from ramsey_deletion_rank_new_parents import graph,induce,D,json,Counter
from ramsey_final_miss_levels import levels
from ramsey_fork_audit_uniform import inds

def run():
    data=json.loads((D/'ramsey_deletion_rank_new_parents.json').read_text())[0];P=induce(graph((1,7,11,16)),list(range(1,35))); 
    for a,b in data['added']:P[a]|=1<<b;P[b]|=1<<a
    old=[s for s in inds(P) if s.bit_count()==7];out=[]
    for r in data['rows']:
        u,v=r['edge'];
        if r['edge'] not in ([11,22],[16,17]):continue
        B=P[:];B[u]^=1<<v;B[v]^=1<<u;pair=(1<<u)|(1<<v);I=inds(B);anchors={s:Counter() for s in I if s&pair==pair and all(s>>i&1 or s&row for i,row in enumerate(B))};covered={s:sum(bool(s&t) for t in old) for s in anchors};any_anchor=Counter();failed_sevens=Counter()
        def collect(S,tag,obs):
            used=set(S)&anchors.keys();
            if used:
                any_anchor[tag]+=1
                if tag=='fails_triple':
                    masks=[S[i]|S[j]|S[k] for i,j,k in ((0,1,2),(0,1,3),(0,2,3),(1,2,3))];hits=[t for t in I if t.bit_count()==7 and any(not t&z for z in masks)];failed_sevens[('old' if any(t&pair!=pair for t in hits) else '')+(' new' if any(t&pair==pair for t in hits) else '')]+=1
            for s in used:anchors[s][tag]+=1
        allq=levels(B,on_classified=collect);summary=Counter();tiers={}
        for s,c in anchors.items():
            depth='six_pass' if c['valid'] else 'seven_pass' if c['fails_four'] else 'eight_pass' if c['fails_triple'] else 'no_eight_pass';summary[depth]+=1;tiers.setdefault(depth,[]).append(covered[s]);
        top=max(covered.values());assert top==r['hit'];out.append(dict(edge=r['edge'],anchors=len(anchors),any_anchor=dict(any_anchor),failed_sevens=dict(failed_sevens),no_anchor_valid=allq['counts'].get('valid',0)-any_anchor['valid'],depth=summary,coverage_ranges={k:[min(vals),max(vals)] for k,vals in tiers.items()},best=[dict(support=s,triple_counts=c) for s,c in anchors.items() if covered[s]==top],per_anchor=[dict(support=s,coverage=covered[s],counts=c) for s,c in anchors.items()]))
    return out
if __name__=='__main__':
    out=run();print([{k:v for k,v in r.items() if k!='per_anchor'} for r in out]);(D/'ramsey_fixed_reuse_matched_pair.json').write_text(json.dumps(out)+'\n')
