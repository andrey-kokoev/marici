"""Generate exact one- and two-removal blue-eight vetoes before degree-budget search. No target embedding, learned ranking or complete removal-list data used for pruning."""
from ramsey_frozen_contacts_transfer import CAT,D,decode,budgets,check,bits,json,gzip,subprocess,tempfile,Path,Counter
from itertools import combinations
from collections import defaultdict
from ramsey_retention_slice import has

def vetoes(g,out,H,z):
    needs={i:g[i].bit_count()-(4 if (g[i]&H).bit_count()==1 else 6) for i in out};E=[(i,j) for i,j in combinations(out,2) if g[i]>>j&1 and min(needs[i],needs[j])>0];B=[~v for v in g];V=((1<<27)-1)^(1<<z);bans=defaultdict(list);singles=set()
    def dangerous(edges):
        S={v for e in edges for v in e};mask=sum(1<<i for i in S);p=V^mask
        if sum((g[i]&mask).bit_count() for i in S)!=2*len(edges):return False
        for i in S:p&=B[i]
        return has(B,p,8-len(S))
    for e in E:
        if dangerous([e]):singles.add(e);bans[e].append(frozenset([e]))
    for e,f in combinations([e for e in E if e not in singles],2):
        if any(needs[i]<2 for i in set(e)&set(f)):continue
        if dangerous([e,f]):
            ban=frozenset([e,f]);bans[e].append(ban);bans[f].append(ban)
    return {e:[frozenset([e])] for e in singles},bans

def propagate(g,out,H,one):
    need={i:g[i].bit_count()-(4 if (g[i]&H).bit_count()==1 else 6) for i in out};edges={(i,j) for i,j in combinations(out,2) if g[i]>>j&1 and (i,j) not in one};forced=[]
    while True:
        edges={e for e in edges if min(need[i] for i in e)>0};by={i:{e for e in edges if i in e} for i in out}
        if any(len(by[i])<k or k<0 for i,k in need.items()):return 'conflict',forced
        if not any(need.values()):return 'solved',forced
        batch=set().union(*(by[i] for i,k in need.items() if k==len(by[i])))
        if not batch:return 'stalled',forced
        for i,j in batch:need[i]-=1;need[j]-=1
        forced.append(sorted(batch));edges-=batch

def audit():
    prev=json.loads((D.parent/'ramsey_frozen_contacts_transfer.json').read_text());old={r['record']:r for r in prev['records']};G={i:decode(l.strip().decode()) for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rb')) if i in old};out=[]
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'frozen.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_frozen_contacts.rs')),'-o',str(exe)],check=True)
        for idx,a in G.items():
            zs=[i for i,v in enumerate(a) if v.bit_count()==7];lines=subprocess.run([str(exe)],input='\n'.join(' '.join(map(str,[z]+a)) for z in zs),text=True,capture_output=True,check=True).stdout.splitlines();st=Counter();survivors=[]
            for line in lines:
                z,e,f,H=map(int,line.split());g=[v&~(1<<z) for v in a];g[z]=0
                for m in [e,f]:i,j=bits(m);g[i]|=1<<j;g[j]|=1<<i
                outer=[i for i in range(27) if i!=z and not H>>i&1];one,two=vetoes(g,outer,H,z);status,trace=propagate(g,outer,H,one);st['prop_'+status]+=1;partial=budgets(g,outer,H,one);lists=budgets(g,outer,H,two);st['after_one']+=len(partial);st['after_two']+=len(lists)
                for rm in lists:
                    b=g[:]
                    for u,v in rm:b[u]^=1<<v;b[v]^=1<<u
                    if check(b,((1<<27)-1)^(1<<z),3,8):survivors.append(dict(z=z,adds=[bits(e),bits(f)],rm=rm,status=status,forced=trace))
            st['baseline']=old[idx]['counts'].get('removal_lists',0);st['legal']=len(survivors);assert st['legal']==old[idx]['counts'].get('legal',0) and st['baseline']>=st['after_one']>=st['after_two']>=st['legal'];out.append(dict(record=idx,counts=st,survivors=survivors))
    for name,rs in [('first',[r for r in out if r['record']==262402]),('second',[r for r in out if r['record']==236272]),('controls',[r for r in out if r['record'] in prev['sample']])]:print(name,sum((r['counts'] for r in rs),Counter()),'records alive at two',sum(bool(r['counts']['after_two']) for r in rs))
    (D.parent/'ramsey_partial_removal_veto.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
