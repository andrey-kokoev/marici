"""Exact bounded-extension slack filtration for R(3,t) rooted neighborhoods.
No external libraries or graph catalog downloads. Preloaded graph6 examples are
from the McKay Ramsey-critical graph catalogue, as preserved in this project.

Checks the one-vertex theorem against brute-force extensions of small graphs,
a pair with identical full scalar boundary profiles and different extensions,
and slack statistics for a 13-vertex (3,5), seven 17-vertex (3,6), and ten
22-vertex (3,7) Ramsey-critical examples.
"""
from itertools import combinations
from collections import Counter

G6_17 = (
'P??GaOo`XMGsIcT?pSLaGuA?',
'P?C?I_h`SDEQQcLAh`dU?tG?',
'P@oGQA?`ACcdCtDYC]Ah?goC',
'PG?OSAKccKGiGwJSI[@oWUA_',
'PGD?OkeO_WAEGQobP_s`cgU?',
'Ps`A?WIDGeCdGsQEKK?oLL_O',
'Ps`A?_KChFCiBoQSKCOoXL_O',
)
G6_22 = (
'U???GOOGIGPB`SQgg[cEoKaagg@iI@w@`ROCrGA?',
'U???GOWH@CAGn?O{hBbHGTQ@y?CHWKSgQPWOgwG?',
'U???GOcEKBGRPACoag`SDoWEcPEPBAsOG{CGgs_?',
'U???GQ?HGhHACxPWGX@SQh@IPOSobAt?QbK?Z?`?',
'U???GSOGKCgIb@RAOkAT?K?}adBBS@wWATOOUcG?',
'U???GWI_?ch@HLO[CYDOQd@XkOCeGLBO@S_oU__O',
'U???OGOGIGOROwQXPJCWcKQEgg@wK@kB@ROCpgA?',
'U???OGOGIGOTOwQTPJCWcKQEgg@wK@kB@ROCpgA?',
'U???OGPGhwEWI?D?gXKESQDUCedPAAgcFXO?xg??',
'U???OGUCooCHHEPaHGS@JRCCx@CkHDEOR?eCyK??',
)

def graph6(s):
    n=ord(s[0])-63; A=[0]*n
    bits=((ord(c)-63>>k)&1 for c in s[1:] for k in range(5,-1,-1))
    for (i,j),b in zip(((i,j) for j in range(1,n) for i in range(j)), bits):
        if b: A[i]|=1<<j; A[j]|=1<<i
    return A

def circulant(n,steps):
    return [sum(1<<j for j in range(n) if i!=j and min((i-j)%n,(j-i)%n) in steps) for i in range(n)]

def add_edge(A,i,j):
    A[i]|=1<<j; A[j]|=1<<i

def triangle_free(A):
    return all(not(A[i]&A[j]) for i in range(len(A)) for j in range(i+1,len(A)) if A[i]>>j&1)

def independent_number(A,subset):
    # Bitmask recursion, with a simple pruning by memoization
    cache={0:0}
    def alpha(M):
        if M in cache: return cache[M]
        b=M&-M; v=b.bit_length()-1; R=M^b
        out=max(alpha(R),1+alpha(R&~A[v]));cache[M]=out
        return out
    return alpha(subset)

def is_valid(A,t):
    return triangle_free(A) and independent_number(A,(1<<len(A))-1)<t

def profile(A,v,t):
    n=len(A); d=A[v].bit_count(); S=[u for u in range(n) if A[v]>>u&1]
    T=[u for u in range(n) if u!=v and not(A[v]>>u&1)]
    supports=[sum(1<<i for i,s in enumerate(S) if A[u]>>s&1) for u in T]
    m=len(T); assert m<=19
    # Compute independent sets, aggregating their support unions.
    # Then upward SOS max to get h(F) for every F.
    by=[0]*(1<<d); count_ind=[0]*(1<<d)
    ind=bytearray(1<<m); ind[0]=1
    un=[0]*(1<<m)
    for mask in range(1,1<<m):
        lb=mask&-mask; j=lb.bit_length()-1; rest=mask^lb
        if ind[rest] and not((sum(1<<i for i,u in enumerate(T) if A[T[j]]>>u&1))&rest):
            ind[mask]=1;un[mask]=un[rest]|supports[j]
            c=mask.bit_count(); f=un[mask]
            if c>by[f]:by[f]=c
    h=by[:]
    for i in range(d):
        for f in range(1<<d):
            if f>>i&1:
                if h[f^(1<<i)]>h[f]:h[f]=h[f^(1<<i)]
    sig=[t-1-d+f.bit_count()-h[f] for f in range(1<<d)]
    rho=t-2-h[(1<<d)-1]
    assert min(sig)>=0 and rho>=0,(n,v,t,sig,rho)
    return S,T,h,sig,rho,supports

def tiny_countermodel():
    t=5
    records=[]
    for internal_edge in ((2,3),(4,5)):
        A=[0]*6; add_edge(A,0,1); add_edge(A,*internal_edge)
        assert is_valid(A,t)
        S,T,h,sig,rho,D=profile(A,0,t)
        assert S==[1] and T==[2,3,4,5] and D==[0]*4
        assert h==[3,3] and sig==[0,1] and rho==0
        B=A+[0]; add_edge(B,6,2)   # Identical new vertex attachment for both graphs
        valid=is_valid(B,t)
        # One vertex with E=empty, N={2}. Triangle-free holds.
        witnesses=[tuple(I) for size in range(3,4) for I in combinations(T,size)
                   if all(not(A[i]>>j&1) for i,j in combinations(I,2))]
        hits=[bool(set(I)&{2}) for I in witnesses]
        records.append({'old_edges':internal_edge,'valid':valid,'critical_independent_sets':witnesses,'all_hit':all(hits)})
    assert records[0]['valid']==False and records[1]['valid']==True
    assert records[0]['all_hit']==False and records[1]['all_hit']==True
    return records

def audit_one_vertex():
    checks=0; valid_bases=0
    # Every graph with n<=4 and every root, for t in [3,4,5].
    for n in range(2,5):
        pairs=list(combinations(range(n),2))
        for bits in range(1<<len(pairs)):
            A=[0]*n
            for k,(u,w) in enumerate(pairs):
                if bits>>k&1:add_edge(A,u,w)
            if not triangle_free(A):continue
            for t in range(3,6):
                if not is_valid(A,t):continue
                valid_bases+=1
                for v in range(n):
                    S,T,h,sig,rho,D=profile(A,v,t)
                    d=len(S)
                    for E in range(1<<d):
                        for N in range(1<<len(T)):
                            B=A+[0]
                            for i,s in enumerate(S):
                                if E>>i&1:add_edge(B,n,s)
                            for i,u in enumerate(T):
                                if N>>i&1:add_edge(B,n,u)
                            # root v to z = B
                            must_check=triangle_free(B)
                            if must_check:
                                # Saturated constraints: z increases h(F) iff it
                                # joins an independent maximum set in X_F.
                                bad=(rho==0 and independent_number(A, sum(1<<u for u in T if not(B[n]>>u&1)))==h[(1<<d)-1])
                                for F in range(1<<d):
                                    if sig[F] !=0 or E&~F:continue
                                    TF=sum(1<<u for u,Du in zip(T,D) if Du&~F==0)
                                    nTF=TF&~B[n]
                                    if independent_number(A,nTF)==h[F]:
                                        bad=True;break
                                assert (not bad)==is_valid(B,t),(n,v,t,E,N,A)
                            checks+=1
    return valid_bases,checks

def critical_stats():
    cases={5:[circulant(13,{2,3})],6:[graph6(s) for s in G6_17],7:[graph6(s) for s in G6_22]}
    summary=[]
    for t,graphs in cases.items():
        assert all(is_valid(A,t) for A in graphs),(t,'invalid source')
        for A in graphs:
            for v in range(len(A)):
                S,T,h,sig,rho,D=profile(A,v,t)
                summary.append({'t':t,'n':len(A),'root':v,'d':len(S),
                    'saturated':sig.count(0),'near':sum(s<=1 for s in sig),
                    'all':len(sig),'rho':rho,'sat_nontriv':sum(s==0 and h[f]>0 for f,s in enumerate(sig))})
    for t in cases:
        rows=[row for row in summary if row['t']==t]
        print('critical t=',t,'graphs=',len(cases[t]),'roots=',len(rows),
            'degrees=',dict(sorted(Counter(r['d'] for r in rows).items())),
            'saturated[min,max,avg]=',min(r['saturated'] for r in rows),max(r['saturated'] for r in rows),round(sum(r['saturated'] for r in rows)/len(rows),2),
            'within_1[min,max,avg]=',min(r['near'] for r in rows),max(r['near'] for r in rows),round(sum(r['near'] for r in rows)/len(rows),2),
            'root_cap_sat=',sum(r['rho']==0 for r in rows),
            'sat_with_nonempty_witness=',sum(r['sat_nontriv'] for r in rows))
    return summary

if __name__=='__main__':
    print('TINY countermodel',tiny_countermodel())
    print('ONE-VERTEX theorem exhaustive valid bases / attachments',audit_one_vertex())
    critical_stats()
    print('ALL PASSED')

# Multi-vertex formula audit: for any attachment U all B-adjacent to the root,
# h'(F)=max_{J subset U, J A-independent, support(J) subset F}
#       (|J| + alpha(T[X_F minus N_A(J)])).
def audit_two_vertex_formula():
    checked=0
    n=4
    pairs=list(combinations(range(n),2))
    for bits in range(1<<len(pairs)):
        A=[0]*n
        for k,(i,j) in enumerate(pairs):
            if bits>>k&1:add_edge(A,i,j)
        v=0; S,T,h,_,_,D=profile_unchecked(A,v,6)
        d=len(S)
        for mask in range(1<<(2*(n-1)+1)):
            B=A+[0,0]
            idx=0
            for z in (n,n+1):
                for u in S+T:
                    if mask>>idx&1:add_edge(B,z,u)
                    idx+=1
            if mask>>idx&1:add_edge(B,n,n+1)
            S2,T2,h2,_,_,_=profile_unchecked(B,v,6)
            assert S2==S
            for F in range(1<<d):
                X=sum(1<<u for u,Du in zip(T,D) if not(Du&~F))
                best=0
                for J in ((),(n,),(n+1,),(n,n+1)):
                    if len(J)==2 and (B[n]>>(n+1)&1):continue
                    if any(any(B[z]>>s&1 for s in S if not(F>>S.index(s)&1)) for z in J):continue
                    old_allowed=X
                    for z in J:old_allowed&=~B[z]
                    best=max(best,len(J)+independent_number(A,old_allowed))
                assert best==h2[F],(bits,mask,F,best,h2[F])
            checked+=1
    return checked

def profile_unchecked(A,v,t):
    n=len(A);d=A[v].bit_count();S=[u for u in range(n) if A[v]>>u&1];T=[u for u in range(n) if u!=v and not A[v]>>u&1]
    D=[sum(1<<i for i,s in enumerate(S) if A[u]>>s&1) for u in T]
    h=[independent_number(A,sum(1<<u for u,Du in zip(T,D) if not(Du&~F))) for F in range(1<<d)]
    return S,T,h,[t-1-d+F.bit_count()-h[F] for F in range(1<<d)],t-2-h[-1],D

if __name__=='__main__':
    print('TWO-VERTEX formula exact checked attachments',audit_two_vertex_formula())
