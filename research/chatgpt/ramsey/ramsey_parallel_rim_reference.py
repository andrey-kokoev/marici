"""Compare marker reread from entry with parallel transport around a single row's directed rim. No native coordinates used to extract the two references."""
from ramsey_oriented_overlap_reader import cycle,m,r,orient,X,D,json
from ramsey_first_fan_rim_probe import apex
from itertools import permutations

def run():
    ds=cycle(m)[::2];records=[]
    for d in (ds,[r[v] for v in ds]):
        step=orient(d,X);succ=dict(s['arrow'] for s in step[:4]);tail,head=step[-1]['arrow'];entry=apex(d[0]);other,=set.intersection(*map(set,step[-1]['companions']));parallel={i:succ[succ[i]] for i in succ};assert parallel[tail]==head and parallel[entry]==other
        records.append(dict(entry=entry,companion=other,diagonal=[tail,head],halfturn=parallel,successor=succ))
    a,b=records;g=a['halfturn'];assert g==b['halfturn'];fits=[]
    for perm in permutations(range(1,5)):
        f=dict(enumerate(perm,1));
        if [f[i] for i in a['diagonal']]!=b['diagonal']:continue
        to=lambda s:all(f[a['successor'][i]]==s[f[i]] for i in f);fits.append(dict(image=perm,preserves_source_orientation=to(a['successor']),intertwines_row_rims=to(b['successor']),moves_entry=f[a['entry']]!=b['entry']))
    assert len(fits)==2 and all(x['moves_entry']==x['preserves_source_orientation']!=x['intertwines_row_rims'] for x in fits);return dict(rows=records,extensions=fits)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_parallel_rim_reference.json').write_text(json.dumps(out)+'\n')
