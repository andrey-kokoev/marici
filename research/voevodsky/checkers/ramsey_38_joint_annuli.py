"""For previously stalled rings, enumerate EVERY alternating first boundary (up to dihedral reindexing). Test both cyclic zipper orientations at both seams, keeping original poles/hub reserved. Stop on first success. DP state = position around other cycle, unrolled, at each successive inner vertex. Forbid a whole lap at a single vertex: this excludes precisely repeated bridges for a once-around monotone strip."""
from pathlib import Path
from itertools import permutations, combinations
from collections import Counter
import json
D=Path(__file__).resolve().parents[1]/'results';load=lambda f:json.loads((D/(f+'.json')).read_text());E=set(map(tuple,load('ramsey_38_root_glue')['witness']['plus_edges']));red=lambda u,v:int(tuple(sorted((u,v))) in E)
def bits(I):
    x=[0]
    for u,v in zip(I,I[1:]):x.append(x[-1]^red(u,v))
    return x if x[-1]==red(I[-1],I[0]) else None

def zipone(I,O):
    a=bits(I);m=len(I);n=len(O)
    for O in (O,O[::-1]):
        b=bits(O)
        if b is None:return
        for c in (0,1):
            masks=[sum(1<<j for j,y in enumerate(O) if red(x,y)==(a[i]^b[j]^c)) for i,x in enumerate(I)]
            if not all(masks):continue
            masks=[v|(v<<n) for v in masks];common=masks[-1]&masks[0]
            for j in range(n):
                if not common>>j&1:continue
                P={j:()};end=j+n
                for k in range(m):
                    Q={};m0=masks[k];m1=masks[(k+1)%m];
                    for u,hist in P.items():
                        for v in range(u,min(end,u+n-1)+1):
                            if not m0>>v&1:break
                            if m1>>v&1:Q[v]=hist+(v-u,)
                    P=Q
                    if not P:break
                if end in P:
                    faces=[];pos=j
                    for k,num in enumerate(P[end]):
                        for _ in range(num):faces.append([I[k],O[pos%n],O[(pos+1)%n]]);pos+=1
                        faces.append([I[k],I[(k+1)%m],O[pos%n]])
                    ed=Counter(tuple(sorted(e)) for f in faces for e in combinations(f,2));bd={tuple(sorted((u,v))) for L in [I,O] for u,v in zip(L,L[1:]+L[:1])};assert {e for e,v in ed.items() if v==1}==bd and max(ed.values())==2 and len(ed)==2*(m+n) and all(sum(red(u,v) for u,v in combinations(f,2))%2==0 for f in faces);return faces

def boundaries(Z,W):
    for tail in permutations(Z[1:]):
        z=(Z[0],)+tail
        def dfs(ws):
            k=len(ws)
            if k==len(z):
                if ws[0]<ws[-1]:yield [v for pair in zip(z,ws) for v in pair]
                return
            for w in W:
                if w not in ws and not red(z[k],w) and not red(z[(k+1)%len(z)],w):yield from dfs(ws+(w,))
        yield from dfs(())
def main():
    prev=load('ramsey_38_second_annulus');corr=load('ramsey_38_correction_continuation');known=load('ramsey_38_correction_disk');out=[]
    for i,(old,row) in enumerate(zip(prev,corr)):
        if old['certificate']:out.append(dict(index=i,status='previously certified'));continue
        I=row['ring'];seen=0;fit=0;sample=None
        for M in boundaries(row['Z'],row['W']):
            seen+=1;unused=sorted(set(row['W'])-set(M));assert len(unused)==3
            F=zipone(I,M)
            if not F:continue
            fit+=1;G=zipone(M,unused)
            if G:sample=dict(first=M,last=unused,faces1=F,faces2=G);break
        if not sample:assert seen==known[i]['disks']
        out.append(dict(index=i,poles=row['poles'],ring=I,status='rescued' if sample else 'exhausted',inspected=seen,first_attachable=fit,certificate=sample));print(i,out[-1]['status'],seen,fit,flush=True)
    print(Counter(r['status'] for r in out));(D/'ramsey_38_joint_annuli.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
