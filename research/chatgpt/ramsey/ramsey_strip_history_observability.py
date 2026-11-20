"""Repeat the constructed 12-step word as an observability control, not as a uniquely selected continuation. Compare static seed outputs with ordered signature memory."""
from ramsey_strip_third_order_memory import seq,S
from ramsey_strip_unique_restart_memory import states,turn
from ramsey_strip_matching_restart import tracks,swapped

def observable(word):
    i,b=word[-1];p=tracks[i-1];p=swapped(p) if b else p;m=states[i,b]
    return p,m,turn(m),m&turn(m)
assert observable(seq)==observable(seq*2)
T={}
for w,a in S.items():
    for z,b in S.items():
        if len(w+z)<=3:T[w+z]=T.get(w+z,0)+a*b
assert all(T[w]==2*a for w,a in S.items() if len(w)==3)
assert all((w==() or len(w)==3) for w in T)
print('same final oriented path, matching pair, and residue at steps 12 and 24:',True)
print('third-order signature doubles:',True)
print('terminal state',seq[-1],'next row-compatible different tracks',[(i,1-seq[-1][1]) for i in (2,3,5) if i!=seq[-1][0]])
