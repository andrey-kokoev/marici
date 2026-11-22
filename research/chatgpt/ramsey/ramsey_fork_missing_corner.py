"""Which boundary role is omitted by the fan partition at the first fork? Recover it without using target frame permutations or native arrows. Compare full incoming local histories for ambiguity."""
from ramsey_folded_entry_handoff import D,json,P,T,X

def apexes(j):
    return [set(X[a])&set(X[b]) for a,b in T[j-15]]
def partner(d):
    e,=[X[k] for k in P[d] if 1 in X[k]];return sum(e)-1

def run():
    inp=json.loads((D/'ramsey_join_nonreturn_scale.json').read_text());out=[];contexts={}
    for r in inp:
        old,_,cur=r['previous'];unused,={P.index(q) for q in T[14]}-{old,cur};a=r['stay_or_reflect'];b=r['onward_no_flag_reversal'];i=next(k for k in range(len(a)) if a[k]!=b[k]);d=a[i-1];candidates=[j for j,t in enumerate(T,15) if P[d] in t and j!=a[i-2]];omit={}
        for j in candidates:
            fans=apexes(j);assert all(len(f)==1 for f in fans);v,=set(range(1,5))-set.union(*fans);omit[j]=v
        assert omit[a[i]]==partner(old) and omit[b[i]]==partner(unused);key=tuple(a[:i]);contexts.setdefault(key,set()).add(b[i]);out.append(dict(prior=old,arriving=cur,unused=unused,shared_prefix=key,missing=omit,onward=b[i],retain_old=partner(old)))
    assert len(contexts)==3 and all(len(q)==2 for q in contexts.values());return out
if __name__=='__main__':
    out=run();print(out[:1]);(D/'ramsey_fork_missing_corner.json').write_text(json.dumps(out)+'\n')
