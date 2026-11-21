"""Forward-only branching ladder. Reads only 17-vertex seeds. Root reciprocity and eight-anchor regular lookahead are model restrictions, not necessary for all Ramsey witnesses."""
from ramsey_reciprocal_port_layer import reciprocal,attach,verify,read_seed,induce,independent,D,json,combinations,Counter,nxgraph,nx
from ramsey_hall_anchor_ports import anchor_lift
from ramsey_ports_saturated_core import four
import subprocess,sys

def run(exe,seeds=None):
    seen={};stats=Counter();total=0
    if seeds is None:seeds=map(read_seed,(D/'pauli-realization-catalogues/r36_17.g6').read_bytes().splitlines())
    for idx,A in enumerate(seeds,1):
        for v in range(17):
            V=[j for j in range(17) if j!=v];H=induce(A,V)
            for u,r in enumerate(H):
                for a,b in combinations([i for i in range(16) if r>>i&1],2):
                    C=H[:];C[u]^=(1<<a)|(1<<b);C[a]^=1<<u;C[b]^=1<<u;stats['openings']+=1
                    if independent(C,65535,6):continue
                    stats['valid16']+=1;g=nxgraph(C);bucket=seen.setdefault(tuple(sorted(map(int.bit_count,C))),[])
                    if any(nx.is_isomorphic(g,j) for j in bucket):continue
                    bucket.append(g);stats['distinct16']+=1
                    for s,K in reciprocal(C):
                        stats['21s']+=1
                        proc=subprocess.run([exe,*map(str,K)],capture_output=True,text=True,check=True)
                        for l in proc.stdout.splitlines():
                            t=list(map(int,l.split()));G=attach(K,t);stats['26s']+=1;res=anchor_lift(G,9)
                            if not res or 'graph' not in res:continue
                            X=res['graph'];stats['35s']+=1;B=induce(X,range(1,35));F=(1<<34)-1
                            for i,j in combinations(range(34),2):
                                if not B[i]>>j&1 or independent(B,F&~(B[i]|B[j]),7):continue
                                Y=B[:];Y[i]^=1<<j;Y[j]^=1<<i;z=four(Y)
                                if z['supports'] is None:continue
                                Z=attach(Y,z['supports']);graphs=[C,K,G,X,Z]
                                for k,Q in enumerate(graphs,6):verify(Q,k)
                                return dict(seed_index=idx,seed_drop=v,opened=[[V[u],V[a]],[V[u],V[b]]],to21=s,to26=t,to35=res['supports'],last_drop=0,last_open=[i+1,j+1],to39=z['supports'],graphs=graphs,counts=dict(stats))
    raise AssertionError('no schedule found')
if __name__=='__main__':
    ans=run(sys.argv[1]);(D/'ramsey_forward_reciprocal_chain.json').write_text(json.dumps(ans)+'\n');print({k:v for k,v in ans.items() if k!='graphs'})
