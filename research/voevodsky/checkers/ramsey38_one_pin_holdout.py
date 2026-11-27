"""One pin, no backtracking. Stop by observed ambiguity count, never by verification outcome."""
from ramsey38_matched_mesh_trial import P as prior,old,select,compare,freeze,prev,json,faces,attaches,sys
from ramsey38_mesh_single_pin import domains,reduce_domains
P=prev.out/'ramsey38_one_pin_predictions.json';R=prev.out/'ramsey38_one_pin_comparison.json'
protocol='New canonical eligible arrays after 591. Include every scanned eligible array until three arrays with a pin attempt, or twelve arrays, whichever first. All ordered distinct edge targets. Same commitment and singleton baseline. If nonempty unresolved domains, smallest ambiguous label; pin its lexicographically first star, propagate to fixed point once, no fallback. Attempt an exact append-only mesh only when uniquely determined. Independent exhaustive comparison, unrestricted collar length.'
def pin(e,L,rs,candidates):
    return apply_pin(e,select(e,L,rs,candidates))

def apply_pin(e,base,largest=False):
    r=dict(base);r['singleton_pick']=bool(r['pick']);r['pin']=None
    if r['pick'] or not r['commit'] or not all(r['sizes'].values()):return r
    Q,extra,_,_=domains(e,r['commit']);amb=[a for a,v in Q.items() if len(v)>1]
    if not amb:return r
    a=min(amb,key=lambda w:(-len(Q[w]),w)) if largest else min(amb);s=min(Q[a],key=faces);D,n=reduce_domains({**Q,a:[s]});r['pin']=dict(vertex=a,star=faces(s),rounds=n,sizes={k:len(v) for k,v in D.items()})
    if all(len(v)==1 for v in D.values()):
        mesh=frozenset.union(*(v[0] for v in D.values()));seq=sorted(extra,key=sorted)
        for o in (seq,seq[::-1]):
            if all(attaches(mesh|set(o[:i]),t) for i,t in enumerate(o)):r['pick']=dict(mesh=faces(mesh),append=[sorted(t) for t in o]);break
    return r
def done(es):return len(es)>=12 or sum(any(q['pin'] for q in e['requests']) for e in es)>=3
if __name__=='__main__':
    if sys.argv[1]=='freeze':freeze(591,(old,prior),pin,P,protocol,done)
    elif sys.argv[1]=='compare':compare(P,R)
