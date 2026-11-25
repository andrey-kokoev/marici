"""Select hard five-deletions from every repaired four-deletion (no fifth-level outcomes used)."""
from ramsey312_google_two_step import *
import csv,gzip
p={}
with gzip.open(D/'ramsey312_all_four_covers.csv.gz','rt') as f:
 for r in csv.DictReader(f):
    if int(r['repaired']):p[tuple(int(r[k]) for k in 'abcd')]=int(r['supports'])
selected=set();F=(1<<52)-1
for rank,(d,_) in enumerate(sorted(p.items(),key=lambda x:(-x[1],x[0]))):
 opts=[]
 for j in range(52):
    if j in d:continue
    z=tuple(sorted((*d,j)));h=F^sum(1<<v for v in z);opts.append((-sum((adj[v]&h).bit_count()<11 for v in bits(h)),z))
 selected.update(z for _,z in sorted(opts)[:48 if rank<12 else 1])
(D/'ramsey312_five_targets.txt').write_text(''.join(' '.join(map(str,z))+'\n' for z in sorted(selected)));print('selected',len(selected))
