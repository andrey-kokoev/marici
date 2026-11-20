"""Test endpoint exchange as the reason for paired column frequencies, independent of closure labels. Identify induced row permutations, all profile column pairings, and control at other lengths with the same literal poles and frozen readers."""
from ramsey_strip_complete_stitch_duality import solutions,r,s,t
from ramsey_strip_mixed_mod_holdout import H,rules,dist
from collections import Counter
import json
rows=json.loads((H/'ramsey_strip_length_control.json').read_text());rows=[z for z in rows if (z['path'][0],z['path'][-1])==(s,t)];ref=[z for z in json.loads((H/'ramsey_strip_closure_control.json').read_text()) if (z['path'][0],z['path'][-1])==(s,t)];br=ref[0]['bridge'][0];assert rules[1]=={k[::-1] for k in rules[0]};assert all(r[x]==x for x in br)
canon=lambda p:min(tuple(p),tuple(r[v] for v in p));perm=Counter();index={canon(z['path']):i+1 for i,z in enumerate(ref)}
for f in solutions:
 assert [f[x] for x in br]==br[::-1];perm[tuple(index[canon([f[v] for v in reversed(z['path'])])] for z in ref)]+=1
print('row permutations',perm)
for L in sorted({z['length'] for z in rows}):
 R=[z for z in rows if z['length']==L];profiles=lambda z:[tuple(dist[v][b] for b in br) for v in z['path'][1:-1]];cols=[[tuple(k in rule for k in profiles(z)) for z in R] for rule in rules];sums=[[sum(a) for a in zip(*c)] for c in cols];assert sums[0]==sums[1][::-1];variable=[n for n in sums[0] if 0<n<len(R)];best=[j for j,n in enumerate(sums[0]) if variable and n==max(variable)];print(L,'N',len(R),'F counts',sums[0],'top pairs and agreement hits',[(j+1,L-j-1,sum((a[j]==b[-1-j])==z['closes'] for a,b,z in zip(*cols,R))) for j in best]);
