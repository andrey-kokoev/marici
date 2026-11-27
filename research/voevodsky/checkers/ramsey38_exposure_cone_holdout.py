"""Fresh conditional mesh prediction without proposing a final shell or attachment path."""
from ramsey38_middle_choice_holdout import P as old,prev,freeze,compare,json,sys,boundary,Counter
from ramsey38_exposure_cone_filter import fan_paths,fit,witness
P=prev.out/'ramsey38_cone_holdout_predictions.json';R=prev.out/'ramsey38_cone_holdout_comparison.json';S=prev.out/'ramsey38_cone_holdout_scores.json'
protocol='First five canonical novel competing reachable early-burial middle pools by prior record/root eligibility after record 95000 through 165000; stop by eligible record count only. All scripts and edge targets at chosen roots. Freeze exact mesh sets and lexical first choices, before final shells or continuation tests. Compare sealed only, closure of target edge and promoted triangle, and same closure plus exterior-cone planar links.'
def select(L,pool,survivors,req,short,goal,l,old):
    triangle=old[-1];edge=short[l];prot={j:s for j,s in short.items() if j not in goal};ps=set(prot.values());joint=[];cone=[]
    for i in survivors:
        M=pool[i];sealed=set(L)-set.union(set(),*boundary(M));has=False;passed=False
        for walk,E in fan_paths(L,M,edge,sealed):
            if not fit(M,E,req,ps):continue
            U=M|E|{s for s in req if len(s)==4};n=sum(triangle<=s for s in U);opts=[U] if n==2 else [U|{c} for v in set(L)-triangle for c in [triangle|{v}] if c not in U and not c&sealed and fit(M,E|{c},req,ps)] if n==1 else []
            has|=bool(opts);passed|=any(witness(C,prot,L) is None for C in opts)
            if passed:break
        if has:joint.append(i)
        if passed:cone.append(i)
    return dict(edgeface=next(iter(joint),None),cone=next(iter(cone),None),joint=joint,passes=cone)
def score():
    compare(P,R);it=iter(json.loads(R.read_text())['results']);cnt=Counter();diff=[]
    for e in json.loads(P.read_text())['cases']:
        for d in e['requests']:
            r=next(it);assert r['goal']==d['goal'] and r['moves']==d['moves'] and e['record']==r['record'];ok=set(r['ok']);
            for k in ('joint','passes'):
                a=set(d[k]);cnt[k+'_extra']+=len(a-ok);cnt[k+'_miss']+=len(ok-a);cnt[k+'_exact']+=a==ok
            if d['joint']!=d['passes'] or d['passes']!=r['ok']:diff.append(dict(record=e['record'],goal=d['goal'],moves=d['moves'],joint=d['joint'],passes=d['passes'],actual=r['ok']))
    print(cnt,'differences',len(diff));prev.save(S,dict(comparison_sha=prev.sha(R.read_bytes()),counts=dict(cnt),differences=diff))
if __name__=='__main__':
    if sys.argv[1]=='freeze':freeze(95000,165000,(old,),select,P,protocol)
    elif sys.argv[1]=='compare':score()
