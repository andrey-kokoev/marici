"""Test local non-reversal of a restart (track level), not a global visited set. Detect periodicity on ordered pairs, not just the current track."""
from ramsey_strip_unique_restart_memory import states,turn

def walk(start):
    seq=[(start,0)];pairs=set()
    while True:
        i,b=seq[-1];recent={n for n,_ in seq[-2:]}
        options={q:len(turn(states[i,b]) & m) for q,m in states.items() if q[1]!=b and q[0] not in recent}
        best=[q for q,k in options.items() if k==max(options.values())];
        if len(best)!=1:return seq,best
        q,=best;key=(seq[-1],q);seq.append(q)
        if key in pairs:return seq,[]
        pairs.add(key)
for start in (2,3,5):
    seq,tie=walk(start);print('start',start,seq,'tie',tie)
    if start!=5:assert seq[:2]==seq[6:] and len(set(seq[:6]))==6
    else:assert len(tie)==2
