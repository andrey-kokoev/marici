"""Test candidate tips against fixed additions by matching initial and final vertex stars."""
from ramsey38_append_holdout import P,prev,json,graph,setup,add
from ramsey38_tip_disk_domains import disks,propagate

def test(e,p):
    g=graph(e['word']);u=e['u'];L,rs,_=setup(g,u);dec=lambda m:frozenset(w for i,w in enumerate(L) if m>>i&1);m=p['first'];h=add(g,m);_,rows,_=setup(h,u);S=dec(rs[m[0]]);tips=sorted(set(L)-dec(rows[m[0]]));first=set(map(dec,rows.values()));end=set(map(dec,setup(add(h,p['second']),u)[1].values()));bd=set(map(dec,p['bd']));bd2=set(map(dec,p['end']));extra=set(map(frozenset,p['append']));assert set.union(set(),*bd)==set.union(set(),*bd2)==set(L);results=[]
    for tip in tips:
        need=S|{tip};D={a:disks(L,a,bd,first|{need}) for a in L};E={a:set(disks(L,a,bd2,end|{need}|extra)) for a in L};joined={a:[s for s in D[a] if not s&extra and s|{t for t in extra if a in t} in E[a]] for a in L};tr,conf=propagate(joined);start,_=propagate(D);fin,_=propagate({a:list(ss) for a,ss in E.items()});results.append(dict(tip=tip,initial_pass=all(start[-1].values()),final_pass=all(fin[-1].values()),paired_counts=tr,conflicts=conf,pass_filter=all(tr[-1].values())))
        if all(n==1 for n in tr[-1].values()):
            opts=joined
            for _ in tr[1:]:
                opts={a:[s for s in opts[a] if all(any({t for t in s if b in t}=={t for t in h if a in t} for h in opts[b]) for b in L if a!=b)] for a in L}
            mesh=set.union(set(),*(ss[0] for ss in opts.values()));assert all(len(ss)==1 and {t for t in mesh if a in t}==ss[0] for a,ss in opts.items());results[-1]['forced_mesh']=sorted(sorted(t) for t in mesh)
    return results

def run():
    out=[]
    for e in json.loads(P.read_text())['cases']:
        for d in e['requests']:
            p=d['pick']
            if not p:continue
            rs=test(e,p);out.append(dict(record=e['record'],root=e['u'],j=d['j'],l=d['l'],old_tip=p['tip'],results=rs));print(e['record'],d['j'],d['l'],p['tip'],[(r['tip'],r['initial_pass'],r['final_pass'],r['pass_filter']) for r in rs],flush=True)
            if (e['record'],d['j'],d['l'])==(531,12,11):print([(r['tip'],r['paired_counts'],r['conflicts']) for r in rs],flush=True)
    rare=next(c for c in out if (c['record'],c['j'],c['l'])==(531,12,11));good,=[r for r in rare['results'] if r['pass_filter']];known=json.loads((prev.out/'ramsey38_append_531_routes.json').read_text())['extensions'];assert good['forced_mesh']==sorted(known[0]['initial_order']);prev.save(prev.out/'ramsey38_collar_disk_filter_witness.json',dict(prediction_sha=prev.sha(P.read_bytes()),cases=out))
if __name__=='__main__':run()
