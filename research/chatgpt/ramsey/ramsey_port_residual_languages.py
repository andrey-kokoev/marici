"""Exact right languages of TWO-port histories, fixed labelled (3,6) core and attachment alphabet.
Enumerate multiset faces bottom-up; a minimal new blue seven must use ALL current ports
if all one-port deletions were legal. Compare full languages, not next menus alone.
"""
from pathlib import Path
from itertools import combinations_with_replacement
from collections import defaultdict
from ramsey_clique_power_blowup import layers

def main():
    lines=(Path(__file__).with_name('pauli-realization-catalogues')/'r36_17.g6').read_bytes().splitlines()
    for idx,line in enumerate(lines,1):
        n=line[0]-63;bits=''.join(f'{b-63:06b}' for b in line[1:]);A=[sum(1<<j for j in range(n) if j!=i and bits[max(i,j)*(max(i,j)-1)//2+min(i,j)]=='1') for i in range(n)]
        F=layers(A);assert max(map(int.bit_count,F))==5;labels=range(len(F));faces=[{()}, {(i,) for i in labels}];menu={():set(labels)};miss={}
        for k in range(2,7):
            tests=[s for s in F if s.bit_count()==7-k];miss=[sum(1<<j for j,s in enumerate(tests) if not t&s) for t in F];prev=faces[-1];new=set();nextmenu=defaultdict(set)
            for h in prev:
                avail=menu[h[:-1]]
                for a in avail:
                    if a<h[-1]:continue
                    u=h+(a,)
                    if any(u[:j]+u[j+1:] not in prev for j in range(k-1)):continue
                    z=miss[a]
                    for b in h:z &=miss[b]
                    if z:continue
                    new.add(u)
                    for j in range(k):nextmenu[u[:j]+u[j+1:]].add(u[j])
            faces.append(new);menu=nextmenu
            if not new:break
        assert not faces[-1] and len(faces)<=6
        # Record all nonempty continuations of each pair by deleting a chosen pair from each legal face.
        from itertools import combinations
        L=defaultdict(set)
        for level in faces[3:]:
            for u in level:
                for i,j in combinations(range(len(u)),2):L[u[i],u[j]].add(tuple(x for b,x in enumerate(u) if b not in (i,j)))
        groups=defaultdict(set);examples={}
        for h in sorted(faces[2]):
            lang=frozenset(L[h]);one=frozenset(w for w in lang if len(w)==1);groups[one].add(lang);examples.setdefault(lang,h)
        splits=[v for v in groups.values() if len(v)>1];print('core',idx,'legal multisets by port count',[len(s) for s in faces], 'menus',len(groups),'full languages',sum(map(len,groups.values())),'split menus',len(splits),flush=True)
        if len(faces)>5 and faces[4]:
            from collections import Counter
            long=Counter(frozenset(L[h]) for h in faces[2] if any(len(w)>1 for w in L[h]));print('two-port histories reaching four',sum(long.values()),'full languages among those',len(long),'class sizes',dict(Counter(long.values())),flush=True)
            from itertools import permutations
            # A core automorphism is determined by an isomorphism preserving red adjacency.
            import igraph as ig
            g=ig.Graph(n,[(i,j) for i in range(n) for j in range(i) if A[i]>>j&1]);perms=g.get_automorphisms_vf2();quad={tuple(sorted(F[i] for i in u)) for u in faces[4]};orbits=[]
            while quad:
                u=min(quad);orb={tuple(sorted(sum(1<<p[i] for i in range(n) if t>>i&1) for t in u)) for p in perms};assert orb<=quad;orbits.append(len(orb));quad-=orb
            print('core automorphisms',len(perms),'four-port orbit sizes',orbits,flush=True)
        if splits:
            a,b=list(splits[0])[:2];w=next(iter(a^b));print('counterexample red masks: histories',[[hex(F[i]) for i in examples[l]] for l in (a,b)],'distinguishing suffix',[hex(F[i]) for i in w], 'accepted by first?',w in a,flush=True)
if __name__=='__main__':main()
