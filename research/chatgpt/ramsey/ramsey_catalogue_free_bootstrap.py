"""Construct 17-seeds from the empty graph, without graph files. Canonical deduplication by exact isomorphism. Upper stages optionally consume these seeds in memory."""
from ramsey_port_lookahead import nxgraph,nx,completions,independent,Counter,D,json
from collections import defaultdict

def uniq(stream):
    buckets=defaultdict(list);out=[]
    for A in stream:
        key=tuple(sorted(map(int.bit_count,A)));G=nxgraph(A);group=buckets[key]
        if any(nx.is_isomorphic(G,H) for H in group):continue
        group.append(G);out.append(A)
    return out

def one_vertex(A,k):
    I=[0];n=len(A)
    for v,row in enumerate(A):I += [s|1<<v for s in I if not s&row]
    top=[s for s in I if s.bit_count()==k-1]
    for s in I:
        if all(s&t for t in top):yield [row|((s>>v&1)<<n) for v,row in enumerate(A)]+[s]

def short_branch(seeds):
    from ramsey_port_deletion_chain import search
    for idx,A in enumerate(seeds,1):
        first=search(A,7,4)
        if 'graph' not in first:continue
        second=search(first['graph'],8,4)
        if 'graph' in second:return {'seed_index':idx,'seed_graph':A,'steps':[first,second]}
    raise AssertionError('no short branch')

def bootstrap():
    level=[[]];small={}
    for n in range(1,9):
        level=uniq(B for A in level for B in one_vertex(A,4));small[n]=level;print('base (3,4)',n,len(level),flush=True)
    def generate12():
        for n in (7,8):
            d=11-n
            for H in small[n]:
                for _,B in completions(H,5,d):
                    if min(map(int.bit_count,B))>=d:yield B
    mids=uniq(generate12());print('12 cores',len(mids),flush=True)
    seeds=uniq(B for H in mids for _,B in completions(H,6,4));print('generated 17s',len(seeds),flush=True)
    for A in seeds:assert not independent(A,(1<<17)-1,6)
    return seeds
if __name__=='__main__':
    import sys
    seeds=bootstrap();(D/'ramsey_generated_17_seeds.json').write_text(json.dumps(seeds)+'\n')
    short=short_branch(seeds);(D/'ramsey_catalogue_free_short.json').write_text(json.dumps(short)+'\n');print('short branch seed',short['seed_index'],'orders',[len(r['graph']) for r in short['steps']],flush=True)
    if len(sys.argv)>1:
        from ramsey_forward_reciprocal_chain import run
        ans=run(sys.argv[1],seeds=seeds);ans['seed_graph']=seeds[ans['seed_index']-1];(D/'ramsey_catalogue_free_chain.json').write_text(json.dumps(ans)+'\n');print('winning seed',ans['seed_index'],'orders',list(map(len,ans['graphs'])),ans['counts'])
