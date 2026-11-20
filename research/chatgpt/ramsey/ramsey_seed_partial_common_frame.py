"""Orbit closure of boundary flags within the four directly constructed row-compatible frames. Check partial matching consistency before full quotient completion and irreducibility."""
from ramsey_row_quotient_constructor import frame_records,action,move,R
obs={(0,16),(7,29)}
for k,(G,H,matchings) in enumerate(frame_records,1):
 forced=frozenset().union(*(move(obs,action(g)) for g in G));consistent=len(forced)==len({i for i,j in forced})==len({j for i,j in forced});survivors=[m for m in matchings if obs<=m];primitive=[m for m in survivors if len(m&move(m,R))==10]
 print('frame',k,'orbit-closed observed flags',len(forced),'partial matching consistent',consistent,'quotient completions',len(survivors),'elementary row transitions',len(primitive));assert bool(survivors)==consistent
 if consistent:assert all(forced<=m for m in survivors)
