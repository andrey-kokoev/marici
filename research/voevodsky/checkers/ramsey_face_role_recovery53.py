"""Freeze the unique marked core/pocket/bridge up to isomorphism, not the four retained-to-exterior assignments. Rebuild those rows unordered; compare labels only after enumeration."""
from ramsey_face_cube_mark_joint import G,cells,bits,check,D
from itertools import combinations,combinations_with_replacement,permutations
from collections import Counter
import json

def audit():
    F=(1<<35)-1;root=34;z=cells.index('0**');B=G[root]&G[z];fixed=(1<<root)|(1<<z);H=F&~(G[root]|G[z]|fixed);pocketfive=json.loads((D.parent/'ramsey_face_cube_mark_joint.json').read_text())['R'];X=H^sum(1<<i for i in pocketfive);xs=bits(X);assert len(xs)==16
    # Delete the four vertices, not just their links. No erased row is used in candidate generation.
    old=F^B;base=[v&old if old>>i&1 else 0 for i,v in enumerate(G)];need={i:8-base[i].bit_count() for i in xs};assert Counter(need.values())=={1:8,2:8};I=[0]
    for i in bits(old):I.extend([s|1<<i for s in I if not s&base[i]])
    assert max(map(int.bit_count,I))==8;Is=set(I);Q={k:[q for q in I if q.bit_count()==k and not q&fixed] for k in range(5,9)}
    candidates=[s for s in I if s&~X==0 and s.bit_count()==6 and (s|1<<root) in Is and (s|1<<z) in Is];S=[s for s in candidates if all(s&q for q in Q[8])];miss={k:{s:sum(1<<j for j,q in enumerate(qs) if not q&s) for s in S} for k,qs in Q.items() if k<8};st=Counter();answers=[]
    def dfs(rows,start,once,twice):
        if len(rows)==4:
            st['four_rows']+=1;assert once==X and twice==sum(1<<i for i in xs if need[i]==2)
            # Compare four unordered rows with the abstract face profile: each singleton twice,
            # and two copies of each pair along a four-cycle on the labels.
            masks=Counter(sum(1<<j for j,s in enumerate(rows) if s>>i&1) for i in xs);pairs=[m for m in masks if m.bit_count()==2];face=all(masks[1<<j]==2 for j in range(4)) and len(pairs)==4 and all(masks[m]==2 for m in pairs) and all(sum(m>>j&1 for m in pairs)==2 for j in range(4));
            if not face:return
            g=base[:];
            for j,s in zip(bits(B),rows):
                g[j]=s|fixed
                for i in bits(g[j]):g[i]|=1<<j
            assert all(n.bit_count()==8 for n in g) and check(g,F,3,9);answers.append(rows);return
        for j in range(start,len(S)):
            s=S[j];double=s&once
            if double&(twice|singles):continue
            if any(miss[8-len(sub)][s]&__import__('functools').reduce(int.__and__,(miss[8-len(sub)][u] for u in sub)) for k in range(1,len(rows)+1) for sub in combinations(rows,k)):continue
            dfs(rows+[s],j,once|s,twice|double)
    singles=sum(1<<i for i in xs if need[i]==1)
    stages=Counter()
    for rows in combinations_with_replacement(candidates,4):
        once=twice=0
        for s in rows:
            if s&once&(singles|twice):break
            twice|=s&once;once|=s
        else:
            stages['degree']+=1
            if not all(s in miss[7] for s in rows):continue
            stages['eight']+=1
            for n in (2,3,4):
                if any(__import__('functools').reduce(int.__and__,(miss[9-n][s] for s in sub)) for sub in combinations(rows,n)):break
                stages[str(9-n)]+=1
    dfs([],0,0,0);assert stages['5']==st['four_rows'];known=sorted(G[i]&X for i in bits(B));assert known in [sorted(v) for v in answers];out=dict(stages=stages,candidate_rows=len(candidates),single_row_pass=len(S),legal_before_face_pattern=st['four_rows'],legal_face_families=len(answers),original_only=all(sorted(v)==known for v in answers),exterior=xs,rows=[[bits(s) for s in panel] for panel in answers]);print(out);(D.parent/'ramsey_face_role_recovery53.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
