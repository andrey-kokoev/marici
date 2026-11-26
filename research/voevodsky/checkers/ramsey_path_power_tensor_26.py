"""Compressed exact threshold hypergraphs for the same residue-port experiment as the 13-grid. Each constraint (footprint F,capacity c) forbids every (c+1)-subset of ports outside F."""
from pathlib import Path
import csv,json
D=Path(__file__).resolve().parents[1]/'results'
def calc(l,k):
 if min(l,k)==1:return '-',None,None,[]
 n=(l-1)*(k-2)
 if l==2 and n:return 'x',None,None,[]
 order=[0,*range(l-1,0,-1),l];full=(1<<(l+1))-1
 # Greedy maximum blue set on any allowed residue union starts at the first available position. If its residue is positive it repeats that residue (its predecessor is unavailable). From 0 it descends cyclically until the first missing predecessor, then repeats. Thus a maximizing blue set has singleton or prefix footprint, including the full residue set.
 fs={0}|{1<<j for j in range(l)};p=0
 for j in order[:-1]:p|=1<<j;fs.add(p)
 data=[]
 for root in (0,l-1):
    cs=[]
    for f in sorted(fs):
        j=v=0
        while j<n:
            if f>> (j%l)&1:v+=1;j+=l-1
            else:j+=1
        cap=k-1-v-int(not(f>>root&1));
        if cap<(full^f).bit_count():cs.append((f,cap))
    data.append(cs)
 def possible(cs,q,allowed):
    if allowed.bit_count()<q:return False
    sel=0
    for f,c in cs:
        if f.bit_count()==1 and q>c:sel|=f
    if sel&~allowed or sel.bit_count()>q:return False
    # After mandatory singletons, fill smallest prefixes first: maximizes coverage of every nested non-singleton footprint simultaneously.
    for i in order:
        if sel.bit_count()==q:break
        sel|=allowed&(1<<i)
    return all((sel&~f).bit_count()<=c for f,c in cs)
 repair=[l+1-max(q for q in range(l+2) if possible(cs,q,full)) for cs in data];diff=[]
 for bad,good in (data,data[::-1]):
    for f,c in bad:
        if possible(good,c+1,full^f):diff.append(c+1)
 return str(min(diff)) if diff else '=',*repair,data
if __name__=='__main__':
 old={(int(z['l']),int(z['k'])):z for z in csv.DictReader((D/'ramsey_path_power_tensor_grid.csv').open())};rows=[];lines=[]
 for l in range(1,27):
    line=[]
    for k in range(1,27):
        t,a,c,cs=calc(l,k);line.append(t);rows.append((l,k,t,a,c,json.dumps(cs)))
        if (l,k) in old:
            z=old[l,k];want={'boundary':'-','root already red-illegal':'x'}.get(z['state'],z['arity'] or '=');assert t==want and str(a or 0)==(z['repair_A'] or '0') and str(c or 0)==(z['repair_C'] or '0'),(l,k,t,want)
    lines.append(f'{l:2}  '+' '.join(f'{t:>2}' for t in line))
 text=' l   '+' '.join(f'{k:2}' for k in range(1,27))+'\n'+'\n'.join(lines);print(text);(D/'ramsey_path_power_tensor_grid_26.txt').write_text(text+'\n');
 with (D/'ramsey_path_power_tensor_grid_26.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['l','k','first_difference','repair_A','repair_C','constraints_A_C']);w.writerows(rows)
