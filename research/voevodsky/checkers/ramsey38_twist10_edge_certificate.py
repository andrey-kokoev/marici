"""Which individual edge tests reject both target-free assignments?"""
from ramsey38_shared_twist10 import P,prev,inputs,json,faces,face_assignments,combinations,Counter

def failures(ts,bd):
    out={}
    for edge in sorted({e for t in ts for e in combinations(sorted(t),2)}):
        e=set(edge);segs=[t-e for t in ts if e<=t];rim={v for f in bd if e<=f for v in f-e};deg=Counter(v for s in segs for v in s);todo=set(deg);parts=[]
        while todo:
            part={min(todo)}
            for _ in segs:
                for s in segs:
                    if s&part:part.update(s)
            parts.append(sorted(part));todo-=part
        assert set(deg.values())<={1,2} and {v for v,n in deg.items() if n==1}==rim and len(rim) in (0,2)
        if len(parts)>1:out[edge]=dict(rim=sorted(rim),segments=faces(segs),components=parts)
    return out

def run():
    e=next(e for e in json.loads(P.read_text())['cases'] if (e['record'],e['u'])==(162,5));b,_,x,rs,v=inputs(e);labs=sorted(b[5]);dec=lambda m:frozenset(a for i,a in enumerate(labs) if m>>i&1);S=rs[x];rs[x]|=v;target=frozenset((8,10,19,24));results=[];shared=None
    for z in json.loads((prev.out/'ramsey38_early_sign_join_and_links.json').read_text())['unfilled']:
        if (z['record'],z['root'])!=(162,5) or z['core'] is not None:continue
        bd=set(map(dec,z['bd']));req=set(map(dec,rs.values()))|{dec(S)|{z['tip']}};avoid=[t for t in face_assignments(labs,req,bd) if target not in t];assert len(avoid)==2;ds=[failures(t,bd) for t in avoid];both=set.intersection(*map(set,ds));print(z['row'],[sorted(d) for d in ds],sorted(both),[[(ed,d[ed]) for ed in sorted(both)] for d in ds]);shared=both if shared is None else both&shared
        results.append(dict(row=z['row'],tip=z['tip'],common_bad_edges=sorted(both),alternatives=[dict(cells=faces(t),bad_edges=[dict(edge=k,**v) for k,v in sorted(d.items())]) for t,d in zip(avoid,ds)]))
    assert len(results)==2;prev.save(prev.out/'ramsey38_twist10_edge_certificate.json',dict(shared_edges=sorted(shared),cases=results))
if __name__=='__main__':run()
