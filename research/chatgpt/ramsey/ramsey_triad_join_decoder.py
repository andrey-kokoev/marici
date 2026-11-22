"""Decode a join against every relabeling of the selected ordered strip. Separately allow all permutations, preserve entry apex, or preserve tetrahedral orientation as well. No preferred successor permutation supplied to decoder."""
from itertools import permutations,combinations
from ramsey_triad_schedule_glue import check,P,T,X,D,json,final,move,R

def run():
    M,=final;N=move(M,R);out=[]
    for orig,steps in zip(((M,N),(N,M)),check()):
        frames=[]
        for p in permutations(range(1,5)):
            ix=[X.index(tuple(sorted(p[i-1] for i in e))) for e in X];du=lambda d:tuple(sorted(ix[k] for k in d));h=[P.index(du(d)) for d in P]+[15+T.index(tuple(sorted(du(d) for d in t))) for t in T];a,b=[move(m,h) for m in orig];frames.append((p,a,next(d for d,j in b if j==29)))
        for step in steps:
            shared=step['shared'];reports=[]
            for s in ([shared[0]],[shared[1]],shared):
                for policy in ('all','root','root_even'):
                    fits=[(p,d) for p,a,d in frames if set(s)<=a and (policy=='all' or p[0]==1) and (policy!='root_even' or sum(x>y for x,y in combinations(p,2))%2==0)];reports.append(dict(flags=s,policy=policy,n=len(fits),next_exit=sorted({d for p,d in fits}),frames=[p for p,d in fits]))
            out.append(reports)
    return out
if __name__=='__main__':
    out=run();print(out[0]);(D/'ramsey_triad_join_decoder.json').write_text(json.dumps(out)+'\n')
