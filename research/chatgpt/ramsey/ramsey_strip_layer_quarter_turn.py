"""Build the modulo-ten quarter-turn as a global cage automorphism, and compare its square and pole action with the literal row swap."""
from ramsey_all_ten_cycle_layers import N
from ramsey_strip_matching_restart import r
C=[0,16,13,19,7,29,4,27,12,17];M=[next(iter(N[x]-set(C))) for x in C];D=[next(iter(N[x]-set(C)-set(M))) for x in M]
assert len(set(C+M+D))==30
for sign in (1,-1):
 f=list(range(30))
 for i in range(10):
    j=sign*3*i%10;f[C[i]]=D[j];f[M[i]]=M[j];f[D[i]]=C[j]
 assert all({f[y] for y in N[x]}==N[f[x]] for x in range(30))
 assert all(f[f[x]]==r[x] for x in range(30))
 print('sign',sign,'poles (0,29) images',(f[0],f[29]),'pair/partition types exchanged',all((x<15)!=(f[x]<15) for x in range(30)))
print('layer labels C,M,D',C,M,D)
