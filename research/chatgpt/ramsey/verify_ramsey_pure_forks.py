"""Reconstruct every graph from support masks, then check with independent split-half alpha verifier."""
from verify_ramsey_catalogue_free_chain import verify,D,json

def grow(A,S):
    n=len(A);r=n+len(S);assert all(0<=m<1<<n for m in S)
    return [v+sum(1<<(n+j) for j,m in enumerate(S) if m>>i&1) for i,v in enumerate(A)]+[m|1<<r for m in S]+[((1<<len(S))-1)<<n]

def replay(schedule):
    A=[2,1];out=[verify(A,2)]
    for k,S in enumerate(schedule,3):A=grow(A,S);out.append(verify(A,k))
    return A,out
if __name__=='__main__':
    long=json.loads((D/'ramsey_pure_port_fork.json').read_text());short=json.loads((D/'ramsey_pure_short_fork.json').read_text());_,s=replay(short);print('short',s)
    for S,expected in [([long['to35']],long['graph35']),([long['alternate']['to34'],long['alternate']['to39']],long['alternate']['graphs'][-1])]:
        A,s=replay(long['stem_supports']+S);assert A==expected;print('long',s)
