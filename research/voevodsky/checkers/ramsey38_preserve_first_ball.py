"""Can the recovered route 477:15->18 keep all old tetrahedra? Enumerate both stages."""
from ramsey38_two_goal_holdout import P,R,prev,json,graph,setup
from ramsey38_shared_twist10 import face_assignments,faces
from ramsey38_support_ball_completion import shelling
from ramsey38_compare_support_fillings import boundary
from itertools import permutations

def run():
    e=next(e for e in json.loads(P.read_text())['cases'] if e['record']==477);p=next(d['look'] for d in e['requests'] if (d['j'],d['l'])==(15,18));(m,b1,w),(n,b2)=p;comp=json.loads(R.read_text());assert comp['prediction_sha']==prev.sha(P.read_bytes());z=next(c for c in comp['cases'] if c['record']==477);L,rs,_=setup(graph(e['word']),e['u']);dec=lambda m:frozenset(a for i,a in enumerate(L) if m>>i&1);x,v=m;y,t=n;s1=dec(rs[x]);rs[x]|=1<<L.index(v);req=set(map(dec,rs.values()));starts={};ends={}
    def balls(b,req):
        bd=set(map(dec,b));
        for ts in face_assignments(L,req,bd):
            o=shelling(ts)
            if o:assert boundary(ts)==bd;yield frozenset(ts)
    for c in z['first_certs']['15']:
        if c['edge']!=m:continue
        for tip in c['tips']:
            for ts in balls(c['bd'],req|{s1|{tip}}):starts[ts]=(c['bd'],tip)
    rs[y]|=1<<L.index(t);req=set(map(dec,rs.values()));
    for d in z['final_certs']:
        if (d['a'],d['b'])!=(m,n):continue
        for c in d['shells']:
            if c['hidden']==[15,18]:
                for ts in balls(c['bd'],req):ends[ts]=c['bd']
    results=[]
    for name,A,B in [('frozen',[ts for ts,(bd,tip) in starts.items() if bd==b1 and tip==w],[ts for ts,bd in ends.items() if bd==b2]),('keep_first_shell',[ts for ts,(bd,tip) in starts.items() if bd==b1 and tip==w],ends),('any_shell',starts,ends)]:
        scores=[(len(a-b),len(b-a),a,b) for a in A for b in B];i,j,a,b=min(scores,key=lambda q:(q[0],q[1],faces(q[2]),faces(q[3])));r=dict(scope=name,starts=len(A),ends=len(B),nested=sum(s[0]==0 for s in scores),min_removed=i,added=j,old=faces(a),remove=faces(a-b),add=faces(b-a),old_bd=starts[a][0],old_tip=starts[a][1],new_bd=ends[b]);print(name,len(A),len(B),r['nested'],i,j,r['remove'],r['add']);results.append(r)
    extensions=[]
    for a,(bd,tip) in starts.items():
        for b,end in ends.items():
            if not a<=b:continue
            orders=[]
            for seq in permutations(sorted(b-a,key=sorted)):
                acc=set(a)
                for t in seq:
                    hits=[t&s for s in acc];facets=[h for h in hits if len(h)==3]
                    if not 1<=len(facets)<=3 or len(set(facets))!=len(facets) or not all(any(h<=f for f in facets) for h in hits):break
                    acc.add(t)
                else:orders.append([sorted(t) for t in seq])
            extensions.append(dict(initial_order=[sorted(t) for t in shelling(a)],old_bd=bd,old_tip=tip,new_bd=end,attachment_orders=orders));print('nested',tip,'initial cells',len(a),'valid orders',len(orders),'same end?',end==b2)
    prev.save(prev.out/'ramsey38_preserve_first_ball_extensions.json',dict(record=477,root=e['u'],targets=[15,18],moves=[m,n],results=results,extensions=extensions))
if __name__=='__main__':run()
