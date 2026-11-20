"""Greedy restart under explicit memory policies. No immediate reuse of the current track, no arbitrary tie breaking. Orientation toggles at every handoff."""
from ramsey_strip_matching_restart import M,turn
states={(i,b): (turn(m) if b else m) for i,ms in enumerate(M,1) for m in ms for b in (0,1)}
def run(start,mode):
    seq=[(start,0)]
    while True:
        i,b=seq[-1]; choices={q:len(turn(states[i,b])&m) for q,m in states.items() if q[1]!=b and q[0]!=i and not(mode=='track' and q[0] in {n for n,_ in seq}) and not(mode=='oriented' and q in seq)}
        if not choices:return seq,'exhausted'
        best=[q for q,v in choices.items() if v==max(choices.values())]
        if len(best)>1:return seq,('tie',best)
        q,=best;seq.append(q)
        if mode=='allow' and q in seq[:-1]:return seq,'cycle'
for mode in ('allow','track','oriented'):
    for start in (2,3,5):print(mode,start,run(start,mode))
