"""Replay fixed-shell search with/without a monotone partial boundary-edge cycle veto."""
from ramsey38_shared_twist10 import P,prev,inputs,json,faces,combinations,Counter

def search(labs,bd,req,target,prune,lookahead=False):
    ts=sorted(map(frozenset,combinations(labs,4)),key=sorted);ALL=(1<<len(ts))-1;carrier=lambda f:sum(1<<i for i,t in enumerate(ts) if f<=t);tri=[(f,carrier(f)) for f in map(frozenset,combinations(labs,3))];needs=[carrier(r) for r in req];on=sum(carrier(r) for r in req if len(r)==4);stats=Counter();events=[];answers=[]
    # Every added tet supplies a segment opposite each of its six edges.
    rim=sorted({e for f in bd for e in combinations(sorted(f),2)});segs={e:[(1<<i,*sorted(t-set(e))) for i,t in enumerate(ts) if set(e)<=t] for e in rim}
    def veto(m):
        for e,ss in segs.items():
            adj={}
            for bit,a,b in ss:
                if not m&bit:continue
                todo=[a];seen={a}
                while todo:
                    for w in adj.get(todo.pop(),()):
                        if w not in seen:seen.add(w);todo.append(w)
                if b in seen:return e
                adj.setdefault(a,[]).append(b);adj.setdefault(b,[]).append(a)
    def visit(m,n):
        stats['nodes']+=1
        while True:
            if m&n:return
            if prune and (e:=veto(m)):
                events.append(dict(edge=e,chosen=m.bit_count(),unknown=(ALL&~(m|n)).bit_count()));return
            forced=blocked=0
            for f,c in tri:
                count=(m&c).bit_count();free=c&~(m|n);possible=count+free.bit_count();k=1 if f in bd else 2
                if count>k or (count or f in bd) and possible<k:return
                if count==k or possible<k:blocked|=free
                elif possible==k and (count or f in bd):forced|=free
            for c in needs:
                if c&m:continue
                free=c&~n
                if not free:return
                if free.bit_count()==1:forced|=free
            if lookahead and not (forced|blocked):
                free=ALL&~(m|n)
                while free:
                    bit=free&-free;free^=bit
                    if veto(m|bit):blocked|=bit
                stats['preblocked']+=blocked.bit_count()
            if not (forced|blocked):break
            if forced&blocked:return
            # Install required cells one at a time, checking immediately instead of
            # waiting for an entire propagation batch to finish.
            while forced:
                bit=forced&-forced;m|=bit;forced^=bit
                if prune and (e:=veto(m)):
                    events.append(dict(edge=e,chosen=m.bit_count(),unknown=(ALL&~(m|n)).bit_count(),pending_batch=(forced|blocked).bit_count()));return
            n|=blocked
        free=ALL&~(m|n)
        if not free:answers.append(faces(t for i,t in enumerate(ts) if m>>i&1));return
        b=free&-free;visit(m|b,n);visit(m,n|b)
    visit(on,carrier(target) if target is not None else 0);result=dict(nodes=stats['nodes'],leaves=answers,vetoes=events)
    if lookahead:result['preblocked']=stats['preblocked']
    return result

def run():
    audit=json.loads((prev.out/'ramsey38_early_sign_join_and_links.json').read_text());old=json.loads((prev.out/'ramsey38_twist10_edge_certificate.json').read_text());e=next(e for e in json.loads(P.read_text())['cases'] if e['record']==162 and e['u']==5);b,_,x,rs,v=inputs(e);labs=sorted(b[5]);dec=lambda m:frozenset(a for i,a in enumerate(labs) if m>>i&1);S=rs[x];rs[x]|=v;target=frozenset((8,10,19,24));out=[]
    for z in audit['unfilled']:
        if z['core'] is not None:continue
        assert (z['record'],z['root'])==(162,5);bd=set(map(dec,z['bd']));req=set(map(dec,rs.values()))|{dec(S)|{z['tip']}};base,cut=[search(labs,bd,req,target,k) for k in [False,True]];prior=next(c for c in old['cases'] if c['row']==z['row']);assert sorted(base['leaves'])==sorted(a['cells'] for a in prior['alternatives']) and not cut['leaves'];out.append(dict(row=z['row'],baseline=base,pruned=cut));print(z['row'],base['nodes'],cut)
    prev.save(prev.out/'ramsey38_incremental_fan_prune.json',out)
if __name__=='__main__':run()
