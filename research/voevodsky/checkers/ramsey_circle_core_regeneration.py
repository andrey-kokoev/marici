"""Extract one root core, scramble its labels, then reconstruct from adjacency alone. Enumerate unordered maximal-port multisets via necessary pair compatibility. Check all 9-clique obstructions, and test single link deletions to exclude nonmaximal alternatives when all such deletions fail."""
from pathlib import Path
from itertools import combinations
from random import Random
import json,hashlib
H=Path(__file__).resolve().parents[1]
def reconstruct(P):
 n=len(P);assert n==26;U=(1<<n)-1;sets=[]
 def enum(s,m):
    sets.append(s)
    while m:
        x=m&-m;m-=x;enum(s|x,m&~P[x.bit_length()-1])
 enum(0,U);assert max(map(int.bit_count,sets))==7 and all(not(P[i]&P[j]) for i in range(n) for j in range(i) if P[i]>>j&1)
 rows=[s for s in sets if all(s&((1<<i)|P[i]) for i in range(n))];sevens=[s for s in sets if s.bit_count()==7];D=[sum(1<<j for j,t in enumerate(sevens) if not s&t) for s in rows];assert all(D) # equal maximal rows forbidden even on distinct ports
 G=[sum(1<<j for j in range(i+1,len(D)) if not d&D[j]) for i,d in enumerate(D)]
 def packs(ch,m):
    if len(ch)==8:yield [rows[j] for j in ch];return
    while m.bit_count()>=8-len(ch):
        x=m&-m;m-=x;j=x.bit_length()-1;yield from packs(ch+[j],m&G[j])
 def safe(pack):
    # For each independent core set, add every port nonadjacent to it in plus.
    return all(s.bit_count()+sum(not(s&t) for t in pack)<9 for s in sets)
 total=0;sol=[];deletions=[]
 for pack in packs([],(1<<len(rows))-1):
    total+=1
    if not safe(pack):continue
    sol.append(sorted(pack));deletions.append(sum(safe(pack[:j]+[s^(1<<v)]+pack[j+1:]) for j,s in enumerate(pack) for v in range(n) if s>>v&1))
 return dict(maximal_rows=len(rows),minus_sevens=len(sevens),compatible_eight_packs=total,legal_maximal_packs=sol,legal_single_deletions=deletions)
def main():
 def edge(i,j):return (i-j)%35 in (1,34,7,28,11,24,16,19)
 core=[v for v in range(1,35) if not edge(0,v)];Random(917).shuffle(core);adj=[sum(1<<j for j,w in enumerate(core) if edge(v,w)) for v in core];r=reconstruct(adj);expected=sorted(sum(1<<j for j,w in enumerate(core) if edge(v,w)) for v in range(1,35) if edge(0,v));assert expected in r['legal_maximal_packs'];r.update(source_core_labels=core,reference_pack=expected,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());print({k:v for k,v in r.items() if k not in ('source_core_labels','reference_pack','checker_sha256')});(H/'results/ramsey_circle_core_regeneration.json').write_text(json.dumps(r,indent=2)+'\n')
if __name__=='__main__':main()
