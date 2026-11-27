"""What final constraints were already settled when vertex 27 left the rim?"""
from ramsey38_early_interior_holdout import P,R,prev,json,graph,setup,prepare,add,faces
from ramsey38_three_releases import face_assignments,shelling,extend,boundary
from functools import lru_cache
from collections import Counter

def run():
    assert json.loads(R.read_text())['prediction_sha']==prev.sha(P.read_bytes());e=next(e for e in json.loads(P.read_text())['cases'] if e['plans']);p,=e['plans'];g=graph(e['word']);L,_,_,dec,stage,chains=prepare(g,e['u']);goal=tuple(p['goal']);ms=tuple(map(tuple,p['moves']));v,=p['buried'];ss,=[ss for j,m,ss in chains if (j,m)==(goal,ms)];r=[stage(tuple(sorted(ms[:k])))[0] for k in [1,2,3]];late,=r[2]-r[1];assert len(late)==4 and v in late;old=late-{v};assert old in r[1]
    def balls(i,inside):
        out=[]
        for b in ss[i]:
            bd=set(map(dec,b));
            if (not any(v in f for f in bd))!=inside:continue
            for ts in face_assignments(L,r[i],bd):
                if shelling(ts):out.append(frozenset(ts))
        return sorted(set(out),key=faces)
    starts,mids,ends=[balls(i,i>0) for i in range(3)];tip=lambda t:sorted(next(iter(s-old)) for s in t if old<s);star=lambda t:frozenset(s for s in t if v in s);cnt=Counter();out=[]
    for M in mids:
        pre=[a for a in starts if extend(a,M) is not None];post=[b for b in ends if extend(M,b) is not None];matching=[b for b in ends if star(M)==star(b)];assert all(star(M)==star(b) for b in post);covered=late in M;assert not post or covered;cnt['middle']+=1;cnt['pre']+=bool(pre);cnt['late_present']+=covered;cnt['matches_star']+=bool(matching);cnt['post']+=bool(post);cnt['both']+=bool(pre and post);out.append(dict(mesh=faces(M),pre=len(pre),post=len(post),final_star_matches=len(matching),late_present=covered,tips=tip(M),outside_comparisons=[dict(must_remove=faces(M-b),must_add=faces(b-M)) for b in matching]))
    stages=[set(map(frozenset,z['cells'])) for z in p['stages']];print('late',sorted(late),'tips by stage',[tip(t) for t in stages],'sealed cells',faces(star(stages[1])),'stage balls',list(map(len,[starts,mids,ends])),cnt);print(Counter((bool(z['pre']),z['late_present'],bool(z['final_star_matches']),bool(z['post'])) for z in out));prev.save(prev.out/'ramsey38_sealed_star_transitions.json',dict(record=e['record'],root=e['u'],goal=goal,moves=ms,buried=v,late_tet=sorted(late),tips_by_stage=[tip(t) for t in stages],sealed_cells=faces(star(stages[1])),stage_counts=list(map(len,[starts,mids,ends])),counts=dict(cnt),middle=out))
if __name__=='__main__':run()
