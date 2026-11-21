"""Discover bridge by embedding the required 26-core as a (not necessarily induced) subgraph of generated order-27 outputs. Return a checked deletion-only recipe."""
from ramsey_port_clique_transfer import inputs,induce,D,json,independent,combinations

def embedding(H,G):
    n=len(H);m=len(G);hg=list(map(int.bit_count,H));gg=list(map(int.bit_count,G));dom=[sum(1<<x for x in range(m) if gg[x]>=hg[i]) for i in range(n)];R={}
    for i in range(n):
        for j in range(n):
            if i==j:continue
            edge=H[i]>>j&1;c=(H[i]&H[j]).bit_count();table=[]
            for x in range(m):
                z=0
                for y in range(m):
                    if x==y or not dom[j]>>y&1:continue
                    delta=(G[x]>>y&1)-edge;sl=gg[x]-hg[i];sr=gg[y]-hg[j]
                    if delta<0 or delta>min(sl,sr):continue
                    cc=(G[x]&G[y]).bit_count()
                    if c<=cc<=c+sl+sr-2*delta:z|=1<<y
                table.append(z)
            R[i,j]=table
    def dfs(U,L,assigned):
        if not U:return assigned
        i=min(U,key=lambda j:(L[j].bit_count(),-hg[j]));b=L[i];V=U-{i}
        while b:
            bit=b&-b;b-=bit;x=bit.bit_length()-1;N=L[:];union=0
            for j in V:
                N[j]&=R[i,j][x];union|=N[j]
                if not N[j]:break
            else:
                if union.bit_count()>=len(V):
                    p=dfs(V,N,assigned|{i:x})
                    if p:return p
    return dfs(set(range(n)),dom,{})

if __name__=='__main__':
    H=inputs(9)[0];rows=json.loads((D/'ramsey_port_lookahead.json').read_text())['27s'];order=sorted(range(len(rows)),key=lambda i:sum(r.bit_count() for r in rows[i]['graph']),reverse=True)
    for index in order:
        G=rows[index]['graph'];p=embedding(H,G)
        if p:
            V=[p[i] for i in range(len(H))];B=induce(G,V);assert all(h&b==h for h,b in zip(H,B));E=[(V[i],V[j]) for i,j in combinations(range(26),2) if (B[i]^H[i])>>j&1];rec={'row':index,'deleted_vertex':(set(range(27))-set(V)).pop(),'deleted_edges':E,'embedding':V};print(rec,flush=True);(D/'ramsey_27_to_35_embedding.json').write_text(json.dumps(rec));break
    else:print('no deletion-only bridge across all',len(rows),'27 types',flush=True)
