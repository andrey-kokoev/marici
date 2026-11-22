"""Refine a join incidence with its active-cycle provenance: does the second shared flag even have a phase on the candidate's active cycle? Preserve only labels/roles already retained by the matching pair."""
from ramsey_triad_join_decoder import run,final,move,R,X,P,T,D,json

def lift(p):
    ix=[X.index(tuple(sorted(p[i-1] for i in e))) for e in X];du=lambda d:tuple(sorted(ix[k] for k in d));return [P.index(du(d)) for d in P]+[15+T.index(tuple(sorted(du(d) for d in t))) for t in T]

def window(a,b,exitflag):
    # Root at exit, depart via second matching; report positive distance forward between flag occurrences.
    inv={j:i for i,j in b};f=dict(a);j=29;word=[]
    for _ in range(15):
        i=inv[j];word.append((i,j));j=f[i];word.append((i,j));
        if j==29:break
    assert len(word)==10 and exitflag in word
    k=word.index(exitflag);return word[k+1:]+word[:k+1]

def offset(a,b,exitflag,other):
    w=window(a,b,exitflag);return (w.index(other)+1)%10 if other in w else None

def check():
    M,=final;N=move(M,R);out=[];frames=run()
    for row,(orig,base) in enumerate((((M,N),0),((N,M),3))):
        old=orig
        for choices in frames[base:base+3]:
            both=next(q for q in choices if q['policy']=='root' and len(q['flags'])==2);ex,other=both['flags'];prior=offset(*old,ex,other);results=[];hist=[]
            for p in both['frames']:
                h=lift(p);a,b=[move(s,h) for s in orig];nxt=next(i for i,j in b if j==29);results.append(dict(next_exit=nxt,offset=offset(a,b,ex,other),other_static=other in a&b,back=b==old[0]));
                hist.append(window(a,b,ex));
                if b!=old[0]:onward=(a,b)
            k=next(k for k in range(10) if hist[0][-1-k]!=hist[1][-1-k]);out.append(dict(shared=both['flags'],previous_offset=prior,candidates=results,common_arrival=hist[0][-k:],first_difference=[w[-1-k] for w in hist]));old=onward
    return out
if __name__=='__main__':
    out=check();print(out);(D/'ramsey_join_flag_phase.json').write_text(json.dumps(out)+'\n')
