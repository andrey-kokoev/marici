"""Does new shared residue choose the sequence, or just exclude already covered tracks? Test every start before using overlap as a tie breaker."""
from ramsey_strip_unique_restart_memory import states,turn
ids=(2,3,5);C={i:states[i,0]&turn(states[i,0]) for i in ids};core=set.intersection(*(set(c) for c in C.values()));petals={i:set(C[i])-core for i in ids}
assert len(core)==2 and all(len(p)==2 for p in petals.values());assert all(not(petals[i]&petals[j]) for i in ids for j in ids if i!=j)
print('core',sorted(core),'private pairs',{i:sorted(p) for i,p in petals.items()})
for i in ids:
    gains={j:len(C[j]-C[i]) for j in ids if j!=i};print('after',i,'residue gains',gains);assert set(gains.values())=={2}
print('After any specified start, two next tracks tie; after either choice, the remaining track is the sole residue-progress option')
