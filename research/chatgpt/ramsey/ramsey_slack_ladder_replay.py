"""Replay from order 17 using a calibrated 2-layer schedule; search final attachments without target incidences."""
from ramsey_port_chain_from_17 import read_seed,D,json,search
from ramsey_port_deletion_chain import independent,induce,combinations
from ramsey_ports_saturated_core import four

def verify(A,k):
    assert all(not A[i]&A[j] for i,j in combinations(range(len(A)),2) if A[i]>>j&1) and not independent(A,(1<<len(A))-1,k)
def attach(H,S):
    n=len(H);A=H[:]+[0]*(len(S)+1);root=len(A)-1
    for v,s in enumerate(S,n):
        A[v]=s|1<<root;A[root]|=1<<v
        for j in range(n):
            if s>>j&1:A[j]|=1<<v
    return A
if __name__=='__main__':
    s=json.loads((D/'ramsey_slack_ladder_schedule.json').read_text());A=read_seed((D/'pauli-realization-catalogues/r36_17.g6').read_bytes().splitlines()[s['seed_index']-1]);trace=[]
    for u,v in s['delete_edges']:A[u]^=1<<v;A[v]^=1<<u
    A=induce(A,[i for i in range(17) if i!=s['delete_vertex']]);verify(A,6)
    for k,name in [(7,'to21'),(8,'to26')]:
        S=s[name];A=attach(A,S);verify(A,k);trace.append({'k':k,'supports':S,'graph':A});print(k,len(A),list(map(int.bit_count,S)),flush=True)
    r=search(A,9,8);A=r['graph'];verify(A,9);trace.append({'k':9,'supports':r['supports'],'graph':A});print(9,len(A),flush=True)
    H=induce(A,range(1,35));F=(1<<34)-1
    for i,j in combinations(range(34),2):
        if not H[i]>>j&1 or independent(H,F&~(H[i]|H[j]),7):continue
        B=H[:];B[i]^=1<<j;B[j]^=1<<i;r=four(B)
        if r['supports']:
            A=attach(B,r['supports']);verify(A,10);trace.append({'k':10,'delete_vertex':0,'open_edge_original':[i+1,j+1],'supports':r['supports'],'graph':A});print(10,len(A),flush=True);break
    else:raise AssertionError('no final completion')
    (D/'ramsey_slack_ladder_certificates.json').write_text(json.dumps(trace)+'\n')
