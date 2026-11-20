"""Read entry by its B-R edge and exit by its N-N edge. On these tags compare keeping the shared R corner with taking the tetrahedral opposite. Test each return convention against all four full dualities."""
from ramsey_strip_ordered_boundary_dualities import rows,entry,exit,solutions,r
V=set(range(1,5));tags={};active=set()
for w,i,j in zip(rows,entry,exit):
    B=w.index('B')+1;R=w.index('R')+1;tags[i]=frozenset((B,R));tags[j]=frozenset(V-tags[i]);active.add(R)
port={v:i for i,v in tags.items()}
opp={i:port[frozenset(V-v)] for i,v in tags.items()};via={i:next(j for j,w in tags.items() if j!=i and v&w&active) for i,v in tags.items()}
assert all(via[opp[i]]==opp[via[i]]==r[i] for i in tags)
for ret in [via,opp]:
 f,=[f for f in solutions if all(f[i]==via[i] for i in entry) and all(f[j]==ret[j] for j in exit)];p=entry[0];seq=[p];
 for _ in range(4):p=f[p];seq.append(p)
 print('keep R on entry; return', 'keep R' if ret is via else 'opposite',seq,[sorted(tags[i]) for i in seq])
