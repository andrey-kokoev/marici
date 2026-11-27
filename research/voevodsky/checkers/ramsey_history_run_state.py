from itertools import combinations, combinations_with_replacement
from collections import Counter
from ramsey_contact_path_parity import D, json, save, sha256
from ramsey_relative_sign_joint_context import grow,graph,verdict


def run():
    charts=json.loads((D.parent/'ramsey_double_flank_contact.json').read_text())['charts'];families=sorted({tuple(map(tuple,c['rows'])) for z in charts for c in z['cases'] if c['gap'] in (z['first'],z['first']+1)})
    pairs=list(combinations(range(5),2));states=[];example=None;stats={}
    for ss in families:
        rows=[tuple(x-1 for x in s) for s in ss];edges=[e for e in pairs if set(rows[e[0]]).isdisjoint(rows[e[1]])]
        for reds in ([],edges[:1],edges[1:],edges):
            ps=[]
            for p in range(32):
                if any((p>>a)&(p>>b)&1 for a,b in reds):continue
                b=sorted(set().union(*(rows[i] for i in range(5) if p>>i&1)));ends=[-1,*b,8];odd=sum(((v-u-1)%2)<<i for i,(u,v) in enumerate(zip(ends,ends[1:])));flips=[1<<sum(v<g for v in b) for g in range(9)];ps.append((p,2*p.bit_count()+8-len(b),odd,flips))
            best=max((s+m.bit_count())//2 for p,s,m,F in ps)
            if best<7:states.append((ss,rows,reds,sum(1<<pairs.index(e) for e in reds),ps,best))
    for depth in range(1,5):
        counts=Counter()
        for ss,rows,reds,col,ps,best in states:
            for h in combinations_with_replacement(range(9),depth):
                scores=[]
                for p,s,m,F in ps:
                    n=m
                    for g in h:n^=F[g]
                    scores.append(((s+m.bit_count())//2,(s+depth+n.bit_count())//2,p))
                actual=max(v for _,v,p in scores);kept=max(v for a,v,p in scores if a==best);child=rows
                for g in reversed(h):child=grow(child,g)
                assert verdict(graph(8+depth,child,col))==(actual<7);counts['final_checks']+=1
                if kept>=7 or actual<7:continue
                # Prefix legality is monotone under blank insertion. Try any last gap.
                for last in set(h):
                    pre=list(h);pre.remove(last);t=rows
                    for g in reversed(pre):t=grow(t,g)
                    if not verdict(graph(7+depth,t,col)):continue
                    counts['missed_from_legal_prefix']+=1
                    if example is None:example=dict(rows=ss,red=[(a+1,b+1) for a,b in reds],original_max=best,history=pre+[last],kept_max=kept,actual=actual,winning_group=next([i+1 for i in range(5) if p>>i&1] for a,v,p in scores if v==actual))
                    break
        stats[depth]=counts
        if example:break
    print(stats,example);out=dict(protocol_sha=sha256((D.parent/'ramsey_history_run_state_protocol.md').read_bytes()).hexdigest(),legal_sources=len(states),depths=stats,example=example);save(D.parent/'ramsey_history_run_state.json',out)

if __name__=='__main__':run()
