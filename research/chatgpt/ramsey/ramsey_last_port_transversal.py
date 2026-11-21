"""With three ports fixed, solve the fourth as an independent hitting set for residual tight rows."""
from itertools import combinations
from collections import Counter
from ramsey_slack_ladder_replay import attach,D,json,verify

def residual(H,fixed,k):
    I=[0]
    for i,r in enumerate(H):I += [s|1<<i for s in I if not s&r]
    deficit=lambda s:k-1-s.bit_count()-sum(not(s&t) for t in fixed)
    assert all(deficit(s)>=0 for s in I)
    rows=sorted((s for s in I if deficit(s)==0),key=int.bit_count);minimal=[]
    for s in rows:
        if not any(s&t==t for t in minimal):minimal.append(s)
    return I,rows,minimal

def hist(seq):return dict(sorted(Counter(s.bit_count() for s in seq).items()))
if __name__=='__main__':
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=attach(p['stem_graphs'][-1],p['alternate']['to34']);ex=json.loads((D/'ramsey_final_miss_levels.json').read_text())['thinned']['examples'];bad=set(ex['fails_four']['supports']);good=set(ex['valid']['supports']);fixed=sorted(bad&good);assert len(fixed)==3
    bad,=bad-good;good,=good-set(fixed);I,rows,mini=residual(H,fixed,10);ok=[s for s in I if all(s&t for t in mini)];M=[s for s in ok if all(s>>i&1 or s&r for i,r in enumerate(H))];viol=[t for t in mini if not bad&t];added=good&~bad
    out={'fixed':fixed,'bad':bad,'good':good,'tight_counts':hist(rows),'minimal_tight_counts':hist(mini),'bad_misses':viol,'repaired_by':dict(Counter(t&added for t in viol)),'independent_transversals':hist(ok),'maximal_transversals':hist(M),'minimal_transversals':hist([s for s in ok if all((s^(1<<i)) not in ok for i in range(len(H)) if s>>i&1)])};print(out);verify(attach(H,fixed+[good]),10);assert all(good&t for t in rows);(D/'ramsey_last_port_transversal.json').write_text(json.dumps(out)+'\n')
