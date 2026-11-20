"""Select and check a single symmetric 0/1 index on the entire 16-role catalogue.
Finite cost model: same ordering, shape, boundary and fixed-width plan code in each
layout; minimize upper-triangle nonzero slots (unit cost per coordinate pair).
No latency claim. A face's identity is its five incident original vertex IDs.
"""
import gzip,json
from itertools import combinations
from collections import Counter
from pathlib import Path
HOME=Path(__file__).resolve().parents[1]; DATA=HOME.parent/'chatgpt/ramsey';OUT=HOME/'results'; N=16; PAIRS=list(combinations(range(N),2))
def members(m):
    while m:b=m&-m;yield b.bit_length()-1;m^=b

def build(line):
    bits=''.join(f'{x-63:06b}' for x in line[1:]);assert line[0]-63==N
    red={(a,b) for a,b in PAIRS if bits[b*(b-1)//2+a]=='1'};adj=[0]*N
    for a,b in red:adj[a]|=1<<b;adj[b]|=1<<a
    faces=[]
    def extend(mask,chosen,left):
        if left==0:faces.append(chosen);return
        while mask.bit_count()>=left:
            b=mask&-mask;mask^=b;extend(mask&~adj[b.bit_length()-1],chosen|b,left-1)
    extend((1<<N)-1,0,5);M=[0]*N+faces;blue=set(PAIRS)-red
    for j,s in enumerate(faces,N):
        for i in members(s):M[i]|=1<<j
    missing={(a,b) for a,b in blue if M[a]&M[b]==0}
    # These three comparable plans serve the same workload. Incidence-only is eligible iff complete.
    plans=[(len(missing),'patch',missing),(len(red),'red',red)]+([] if missing else [(0,'bare',set())]);_,mode,edges=min(plans,key=lambda p:(p[0],['bare','patch','red'].index(p[1])))
    for a,b in edges:M[a]|=1<<b;M[b]|=1<<a
    return {'vertex_count':N,'plan':mode,'rows_hex':[hex(x) for x in M]},faces,red,missing

def read(doc):
    n=doc['vertex_count'];m=[int(x,16) for x in doc['rows_hex']];V=(1<<n)-1;mode=doc['plan'];faces=m[n:];post=[x>>n for x in m[:n]];allf=(1<<len(faces))-1
    def blue(a,b):
        bit=bool(m[a]&1<<b);return not bit if mode=='red' else bit or bool(post[a]&post[b])
    def joint(a,b):return post[a]&post[b]
    D=[]
    for s in faces:
        hit=0
        for i in members(s):hit|=post[i]
        D.append(allf^hit)
    assert all(x&~V==0 for x in faces)
    return blue,joint,faces,D

def six(D):
    if 0 in D:return [D.index(0)]*6
    comp=[sum(1<<j for j in range(i+1,len(D)) if not d&D[j]) for i,d in enumerate(D)]
    def clique(mask,k):
        if k==0:return []
        while mask.bit_count()>=k:
            b=mask&-mask;mask^=b;i=b.bit_length()-1;sub=clique(mask&comp[i],k-1)
            if sub is not None:return [i]+sub
    return clique((1<<len(D))-1,6)

def main():
    ls=gzip.decompress((DATA/'r36_16.g6.gz').read_bytes()).splitlines();assert len(ls)==2576
    ctrl={e['graph6'] for e in json.loads((DATA/'ramsey_boundary_k6_witnesses.json').read_text())['records']};freq=Counter();plans=Counter();checks=Counter();examples={}
    for idx,l in enumerate(ls,1):
        doc,F,R,miss=build(l);blue,joint,f,D=read(doc);assert F==f
        for a,b in PAIRS:
            assert blue(a,b)==((a,b) not in R)
            assert [F[i] for i in members(joint(a,b))]==[s for s in F if s>>a&1 and s>>b&1]
        for i,s in enumerate(F):assert list(members(D[i]))==[j for j,t in enumerate(F) if not s&t]
        plans[doc['plan']]+=1;freq[len(miss)]+=1
        if len(R)==33 or l.decode() in ctrl:
            w=six(D);assert (w is not None)==(len(R)==34);checks[len(R)]+=1
            if w is not None:assert all(sum(not t&F[i] for i in w)<=1 for t in F)
        key=doc['plan'];
        if key not in examples:
            examples[key]={'catalogue_record':idx,'graph6':l.decode(),'missing_pairs':sorted(miss),'matrix_file':f'ramsey_square_index_{key}.json'};(OUT/examples[key]['matrix_file']).write_text(json.dumps(doc,indent=2)+'\n')
    assert checks=={33:39,34:2};res=dict(records=len(ls),unordered_pair_checks=len(ls)*len(PAIRS),plans=dict(plans),uncovered_pair_histogram=dict(sorted(freq.items())),port_controls=dict(checks),examples=examples);print(json.dumps(res,indent=2));(OUT/'ramsey_square_index_pilot.json').write_text(json.dumps(res,indent=2)+'\n')
if __name__=='__main__':main()
