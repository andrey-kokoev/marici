"""Decode word supports at fixed B column directly from the partition. Can the third word occur as an ACTIVE exit with the literal row swap, even if the initial matching is changed?"""
from collections import Counter
from ramsey_history_matching_provenance import enum
from ramsey_folded_entry_handoff import P,T,X,rho,D,json

def run():
    words={}
    for pair in T[29-15]:
        e,=[X[k] for k in pair if 1 in X[k]];a=sum(e)-1;words[P.index(pair)]=''.join('B' if i==1 else 'R' if i==a else 'N' for i in range(1,5))
    counts=Counter();entry=Counter()
    for m in enum():
        n={(rho[i],rho[j]) for i,j in m};d,=[i for i,j in m if j==29];v,=[i for i,j in n if j==29];flag=(words[d],words[v],(d,29) in m^n);counts[flag]+=1
        if (0,16) in m:entry[flag]+=1
        assert flag[2]==(d!=9) and (v==9)==(d==9)
    return [dict(from_word=a,mate=b,active=k,all=n,with_entry=entry[a,b,k]) for (a,b,k),n in sorted(counts.items())]
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_third_word_active_exit.json').write_text(json.dumps(out)+'\n')
