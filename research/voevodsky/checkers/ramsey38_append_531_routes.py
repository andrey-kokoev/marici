"""Relax record 531's route one choice at a time; allow any number of attachments."""
from ramsey38_append_failure_audit import P,prev,json,graph,setup,add,attaches,faces,face_assignments,shelling
from ramsey38_two_move_trial import finals,options
from functools import lru_cache

def extend(a,b):
    @lru_cache(None)
    def go(s):
        if s==b:return ()
        for t in sorted(b-s,key=sorted):
            if attaches(s,t):
                tail=go(s|{t})
                if tail is not None:return (t,)+tail
    return go(a) if a<=b else None

def run():
    e=next(e for e in json.loads(P.read_text())['cases'] if e['record']==531);p=next(d['pick'] for d in e['requests'] if (d['j'],d['l'])==(12,11));g=graph(e['word']);u=e['u'];L,rs,moves=setup(g,u);dec=lambda m:frozenset(w for i,w in enumerate(L) if m>>i&1);f=finals(e,True);out=[];best=None;pairs=0
    for z in options(L,rs,moves,12,True):
        a=tuple(z['edge']);x,v=a;h=add(g,a);r1=set(map(dec,setup(h,u)[1].values()));
        for tip in z['tips']:
            req=r1|{dec(rs[x])|{tip}};starts=[frozenset(ts) for ts in face_assignments(L,req,set(map(dec,z['bd']))) if shelling(ts)]
            for (m,b),zs in f.items():
                if m!=a:continue
                r2=set(map(dec,setup(add(h,b),u)[1].values()));
                for c in zs:
                    if c['hidden']!=[11,12]:continue
                    for ts in face_assignments(L,r2,set(map(dec,c['bd']))):
                        B=frozenset(ts)
                        if not shelling(B):continue
                        for A in starts:
                            pairs+=1;score=(len(A-B),len(B-A));best=min(score,best or score);order=extend(A,B)
                            if order is not None:out.append(dict(first=a,second=b,tip=tip,bd=z['bd'],end=c['bd'],initial_order=[sorted(t) for t in shelling(A)],append=[sorted(t) for t in order]))
    print('pairs',pairs,'min differences',best,'extensions',len(out));
    for r in out[:5]:print(r['first'],r['second'],r['tip'],r['bd']==p['bd'],r['end']==p['end'],r['append'])
    prev.save(prev.out/'ramsey38_append_531_routes.json',dict(pairs=pairs,min_difference=best,extensions=out))
if __name__=='__main__':run()
