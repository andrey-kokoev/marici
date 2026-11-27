"""Replay the two 5590 misses, relaxing only the all-boundary vertex assumption."""
from ramsey38_three_route_novelty import P,R,prev,json,graph
from ramsey38_three_matched_stars import predict,shelling,attaches,faces
from ramsey38_three_releases import setup,add,legal,boundary,prepare

def run():
    data=json.loads(P.read_text());comp=json.loads(R.read_text());assert comp['prediction_sha']==prev.sha(P.read_bytes());e=next(e for e in data['cases'] if e['record']==5590);z=next(z for z in comp['cases'] if z['record']==5590);g=graph(e['word']);u=e['u'];L,rows,ts,dec,stage,chains=prepare(g,u);diagnoses=[]
    for p in z['feasible']:
        goal=tuple(p['goal']);ms=tuple(map(tuple,p['moves']));ss,=[ss for j,m,ss in chains if j==goal and m==ms];missing=[]
        for i,s in enumerate(p['stages']):
            assert tuple(s['bd']) in ss[i];bd=set(map(dec,s['bd']));missing.append(sorted(set(L)-set.union(set(),*bd)))
            if i:
                seq=list(map(frozenset,s['append']));prevbd=set(map(dec,p['stages'][i-1]['bd']));assert 1<=len(seq)<=2 and bd^prevbd==boundary(seq)
        diagnoses.append(dict(goal=goal,off_boundary=missing))
    before,_=predict(g,u);assert not before;after,cnt=predict(g,u,allow_interior=True);cert=[]
    for p in after:
        h=g;cells=set(map(frozenset,p['mesh']));orders=[];buried=[];types=[]
        for i,(m,b) in enumerate(zip(p['moves'],p['shells'])):
            _,rs,moves=setup(h,u);assert m in moves;buried.append(dec(rs[m[0]]));h=add(h,m);assert legal(h);_,rs,_=setup(h,u)
            if i:
                for t in map(frozenset,p['additions'][i-1]):assert t not in cells and attaches(cells,t);cells.add(t)
            bd=boundary(cells);assert bd==set(map(dec,b)) and not (set(buried)&bd);assert all(any(dec(s)<=t for t in cells) for s in rs.values());assert sorted(j for j,s in rs.items() if s.bit_count()<4 and not any(dec(s)<=f for f in bd))==sorted(p['goal'][:i+1]);o=shelling(cells);assert o;orders.append([sorted(t) for t in o]);types.append(sorted(set.union(set(),*cells)-set.union(set(),*bd)))
        cert.append(dict(plan=p,orders=orders,interior=types));print(p['goal'],list(map(len,orders)),types,p['sizes'],p['pin'])
    print(diagnoses,len(after));prev.save(prev.out/'ramsey38_interior_route_audit.json',dict(record=5590,root=u,diagnoses=diagnoses,original=len(before),results=cert,chains_tested=cnt))
if __name__=='__main__':run()
