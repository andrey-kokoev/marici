"""Record 531: exhaustive repair of the frozen initial filling at fixed edit, tip and shells."""
from ramsey38_append_holdout import P,R,json,prev,setup,graph,add,attaches,face_assignments,shelling,boundary,faces
from ramsey38_twist10_edge_certificate import failures
from ramsey38_novel_root8_diagonal import link_profile,sub
from collections import Counter

def run():
    assert json.loads(R.read_text())['prediction_sha']==prev.sha(P.read_bytes());e=next(e for e in json.loads(P.read_text())['cases'] if e['record']==531);p=next(d['pick'] for d in e['requests'] if (d['j'],d['l'])==(12,11));g=graph(e['word']);u=e['u'];L,rs,_=setup(g,u);dec=lambda m:frozenset(w for i,w in enumerate(L) if m>>i&1);x,v=p['first'];h=add(g,p['first']);r1=set(map(dec,setup(h,u)[1].values()))|{dec(rs[x])|{p['tip']}};r2=set(map(dec,setup(add(h,p['second']),u)[1].values()));bd=set(map(dec,p['bd']));end=set(map(dec,p['end']));seq=list(map(frozenset,p['append']));old=set(map(frozenset,p['mesh']));cnt=Counter();out=[]
    for ts in face_assignments(L,r1,bd):
        a=set(ts);o=shelling(a);fan=failures(a,bd);bad={}
        if not fan:
            for w in L:
                fs={t-{w} for t in a if w in t};chi=len(set.union(set(),*fs))-len(set.union(*(sub(f,2) for f in fs)))+len(fs);components,orient=link_profile(fs)
                if (components,orient,chi)!=(1,True,1):bad[w]=[components,orient,chi]
        cells=a|set(seq);fits=not a&set(seq) and all(attaches(a|set(seq[:i]),t) for i,t in enumerate(seq)) and boundary(cells)==end and all(any(s<=t for t in cells) for s in r2);fin=shelling(cells) if fits else [];cnt['starts']+=1;cnt['initial_shellable']+=bool(o);cnt['fits']+=fits;cnt['both']+=bool(fits and o and fin);out.append(dict(frozen=a==old,cells=faces(a),fan_conflicts=[dict(edge=k,**v) for k,v in fan.items()],non_disk=bad,initial_order=[sorted(t) for t in o],fits=fits,final_order=[sorted(t) for t in fin]));print(len(a),a==old,sorted(fan),bad,bool(o),fits,bool(fin))
    print(cnt);prev.save(prev.out/'ramsey38_append_failure_audit.json',dict(record=531,root=u,targets=[12,11],choice=p,counts=dict(cnt),assignments=out))
if __name__=='__main__':run()
