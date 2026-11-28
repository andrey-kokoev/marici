"""Audit reductions, not merely solver totals: expand ordered pocket pairs, scan raw 21-core subsets, bypass the optional screen for omitted admissible cores."""
import gzip,json,tempfile,subprocess
from itertools import permutations,combinations
from pathlib import Path
from collections import Counter,defaultdict
from ramsey_retention_slice import CAT,D

def adj(s):
    v=ord(s[0])-63;g=[0]*v
    for k,(j,i) in enumerate((j,i) for j in range(1,v) for i in range(j)):
        if (ord(s[k//6+1])-63)&(32>>(k%6)):g[i]|=1<<j;g[j]|=1<<i
    return g

def autom(g):
    def rec(f):
        if len(f)==len(g):yield tuple(f);return
        i=len(f)
        for v in range(len(g)):
            if v not in f and all((g[i]>>j&1)==(g[v]>>h&1) for j,h in enumerate(f)):yield from rec(f+[v])
    return list(rec([]))
def audit():
    p=D.parent;x=json.loads((p/'ramsey_face_double_root.json').read_text());records=x['marked'];lines=(CAT/'r35_13.g6').read_text().splitlines();assert len(lines)==1;b=adj(lines[0]);assert all(v.bit_count()==4 for v in b);blue=[sum(1<<i for i in s) for s in combinations(range(13),4) if all(not(b[i]>>j&1) for i,j in combinations(s,2))];aut=autom(b);image=lambda v,f:sum(1<<f[i] for i in range(13) if v>>i&1);pairs={(q,t) for q in blue for t in blue if (q&t).bit_count()<2};covered=set();perms=list(permutations(range(5)));edge22=[sum(v.bit_count() for v in adj(s))//2 for s in (CAT/'r37_22.g6').read_text().splitlines()];one_max=0
    for r in records:
        q,t=r['q'],r['t'];orb={(image(q,f),image(t,f)) for f in aut};assert not covered&orb;covered|=orb;R=[i for i in range(13) if not (q|t)>>i&1];edges=sum(b[i]>>j&1 for i,j in combinations(R,2));assert r['e']==30+4*len(R)+edges
        if q&t:one_max=max(one_max,r['e'])
    assert covered==pairs and min(edge22)>one_max
    def bit(i,j):return max(i,j)*(max(i,j)-1)//2+min(i,j)
    canon=[min(sum(((s>>bit(f[i],f[j]))&1)<<bit(i,j) for i,j in combinations(range(5),2)) for f in perms) for s in range(1024)];wt=bytes([(i-63).bit_count() if 63<=i<=126 else 0 for i in range(256)]);src={};bytype=defaultdict(dict);layers=Counter()
    for i,s in enumerate(gzip.open(CAT.parent/'r37_21.g6.gz','rb')):
        s=s.strip();e=sum(s[1:].translate(wt));layers[e]+=1
        if e<=54:src[i]=(s.decode(),e)
    prior={r['type']:dict(r['matches']) for r in json.loads((p/'ramsey_face_bridge_screen.json').read_text())};tot=Counter();skip=[]
    with tempfile.TemporaryDirectory() as td:
        def run(name,data):
            exe=Path(td)/(name+'.exe');subprocess.run(['rustc','-O',str(Path(__file__).with_name(name+'.rs')),'-o',str(exe)],check=True);return subprocess.run([str(exe)],input=data,text=True,capture_output=True,check=True).stdout.splitlines()
        ls=run('ramsey_face_coverage_raw','\n'.join(f'{i} {s}' for i,(s,e) in src.items()));assert len(ls)==len(src)
        for l in ls:
            i,*rest=l.split();i=int(i);c=Counter()
            for z in rest:
                k,n=map(int,z.split(':'));c[canon[k]]+=n
            for typ,n in c.items():
                if str(typ) in x['shapes'] and src[i][1]==x['shapes'][str(typ)]['e']:bytype[typ][i]=n
        for r in records:
            if r['q']&r['t'] or not layers[r['e']]:continue
            q,t=r['q'],r['t'];R=[i for i in range(13) if not(q|t)>>i&1];key=sum((b[R[i]]>>R[j]&1)<<bit(i,j) for i,j in combinations(range(5),2));typ=canon[key];assert typ==r['type'] and bytype[typ]==dict(x['shapes'][str(typ)]['matches']);mult=sum(all((b[R[i]]>>R[j]&1)==(b[R[f[i]]]>>R[f[j]]&1) for i,j in combinations(range(5),2)) for f in perms);tot[r['e']]+=mult*sum(bytype[typ].values());assert prior[typ].items()<=bytype[typ].items();skip.extend((i,q,t) for i in bytype[typ].keys()-prior[typ].keys())
        bypass=run('ramsey_face_blue_six_scan','\n'.join(' '.join(map(str,[i,q,t,*adj(src[i][0]),*b])) for i,q,t in skip));assert all(int(l.split()[5])==0 for l in bypass)
    old=json.loads((p/'ramsey_face_layer52.json').read_text())['totals'];scanned={51:old['51'][0],52:old['52'][0],**{e:json.loads((p/f'ramsey_face_blind_layer{e}.json').read_text())['marking_counts'][0] for e in (53,54)}};assert sum(tot.values())==sum(scanned.values())+sum(int(l.split()[3]) for l in bypass);out=dict(ordered_pairs=len(pairs),orbits=len(records),automorphisms=len(aut),max_overlap_one_edges=one_max,order22_catalogue_floor=min(edge22),raw_core_counts={e:n for e,n in layers.items() if e<=54},markings_before_screen=tot,markings_previously_checked=scanned,screen_bypass=bypass);print(out);(p/'ramsey_face_coverage_audit.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
