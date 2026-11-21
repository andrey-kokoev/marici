"""Test conjecture 2 without extra capacity, degree or independence tests on port tuples."""
from ramsey_final_miss_levels import D,json,attach,bits
from collections import Counter

def run():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());alt=p['alternate'];H=attach(p['stem_graphs'][-1],alt['to34']);u=alt['removed_incidence'];v=26+alt['thinned_port_index_among_retained'];ends=(1<<u)|(1<<v);old={p['to35'][alt['omitted_port']]|1<<33,H[u]|1<<v,H[v]|1<<u};I=[0]
    for j,r in enumerate(H):I += [t|1<<j for t in I if not t&r]
    allowed=set(I)-old;M=sorted(s for s in allowed if not any((s|1<<j) in allowed for j in range(34) if not s>>j&1));T=[t for t in I if t.bit_count()==8 and t&ends!=ends];new=[t for t in I if t.bit_count()==8 and t&ends==ends];local=[H[j] for j in (2,22,16,9,23,3)];cols=[sum(1<<i for i,t in enumerate(T) if t>>j&1) for j in range(34)];F=(1<<len(T))-1;miss=[]
    for s in M:
        h=0
        for j in bits(s):h|=cols[j]
        miss.append(F^h)
    adj=[sum(1<<j for j in range(i,len(M)) if not a&miss[j]) for i,a in enumerate(miss)];cover=[sum(1<<j for j,s in enumerate(M) if s&t) for t in local];total=0;relaxed=0;ex=None
    smaller=[s for s in I if s.bit_count() in (6,7)];f=(1<<len(smaller))-1;mask7=sum(1<<i for i,s in enumerate(smaller) if s.bit_count()==7);c=[sum(1<<i for i,t in enumerate(smaller) if t>>j&1) for j in range(34)];sm=[]
    for s in M:
        a=f
        for j in bits(s):a&=~c[j]
        sm.append(a)
    inherited_small=sum(1<<i for i,s in enumerate(smaller) if s&ends!=ends);strong=0;strong_ex=None;parent_only_plus_six=0
    for i,row in enumerate(adj):
        for j in bits(row):
            common=row&adj[j]
            for k in bits(common):
                tail=common&adj[k];total+=tail.bit_count()
                if not tail:continue
                for t,col in zip(local,cover):
                    hits=sum(bool(M[z]&t) for z in (i,j,k))
                    if hits==0:tail=0;break
                    if hits==1:tail&=col
                relaxed+=tail.bit_count()
                if tail:
                    a,b,c=sm[i],sm[j],sm[k];tr=a&b&c
                    if not tr&mask7&inherited_small:
                        inherited_danger=(tr|(((a&b)|(a&c)|(b&c))&mask7))&inherited_small
                        parent_only_plus_six+=sum(not sm[l]&inherited_danger for l in bits(tail))
                    if not tr&mask7:
                        danger=tr|(((a&b)|(a&c)|(b&c))&mask7)
                        for l in bits(tail):
                            if not sm[l]&danger:
                                strong+=1
                                if strong_ex is None:strong_ex=[M[z] for z in (i,j,k,l)]
                if ex is None and tail:ex=[M[z] for z in (i,j,k,next(bits(tail)))]
    out=dict(inherited_rows=len(T),new_rows=len(new),maximal_allowed=len(M),inherited_pair_quads=total,after_six=relaxed,example=ex)
    out.update(after_inherited_smaller=parent_only_plus_six,after_all_smaller=strong,strong_example=strong_ex)
    if strong_ex:
        bad=[t for t in I if t.bit_count()+sum(not s&t for s in strong_ex)>=10];assert bad and set(bad)<=set(new);out.update(strong_failed_rows=bad)
    if ex:
        bad=[s for s in I if s.bit_count()+sum(not s&t for t in ex)>=10];assert not(set(bad)&set(T+local)) and set(bad)&set(new) and all(t in allowed for t in ex);out.update(failed_rows_by_size=dict(Counter(map(int.bit_count,bad))),failed_new_example=next(iter(set(bad)&set(new))))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_inherited_ablation.json').write_text(json.dumps(out)+'\n')
