"""Small structural certificate: two independent sevens force a triangle-producing companion edge in a prescribed two-block completion problem."""
from pathlib import Path
from itertools import combinations,product
import json
from ramsey_hall_center_conjecture import decode
D=Path(__file__).parent;G=decode((D/'pauli-realization-catalogues'/'r37_22.g6').read_bytes().splitlines()[181]);removed=[(2,11),(8,21),(4,19),(10,17)];H=G[:]
for i,j in removed:H[i]^=1<<j;H[j]^=1<<i
choices_A=[[(2,8),(11,21)],[(2,21),(8,11)]];choices_B=[[(4,10),(17,19)],[(4,17),(10,19)]];candidates=set(e for choice in choices_A+choices_B for e in choice);I={0,10,11,15,16,17,21};J={1,2,3,4,6,8,11}
for S in (I,J):assert all(not(H[i]>>j&1) for i,j in combinations(S,2))
hit_I={e for e in candidates if set(e)<=I};hit_J={e for e in candidates if set(e)<=J};assert hit_I=={(11,21)} and hit_J=={(2,8),(8,11)};assert H[2]>>16&1 and H[8]>>16&1
checks=[]
for a,b in product(choices_A,choices_B):
 F=H[:]
 for i,j in a+b:F[i]|=1<<j;F[j]|=1<<i
 checks.append({'added':a+b,'hits_I':any(set(e)<=I for e in a+b),'hits_J':any(set(e)<=J for e in a+b),'triangle_2_8_16':all(F[i]>>j&1 for i,j in combinations((2,8,16),2))})
assert all(not(r['hits_I'] and r['hits_J']) or r['triangle_2_8_16'] for r in checks)
result={'source':182,'removed':removed,'blue_clause_I':sorted(I),'I_repair_options':sorted(hit_I),'blue_clause_J':sorted(J),'J_repair_options':sorted(hit_J),'guard_vertex':16,'completion_checks':checks};(D/'ramsey_two_clause_completion_certificate.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
