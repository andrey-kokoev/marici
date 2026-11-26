"""Reconcile the exact-eleven exclusion by marked graph and mask keys (not raw totals). Cross-check the sum of their orbit sizes against an independent labeled count by vertex-neighborhood recursion."""
from ramsey_unsaturated_eleven import P,ig,json,collections,itertools
from functools import lru_cache
@lru_cache(None)
def count(v,m,adj):
 if not m:return 1
 if v>=7 or m>(8-v)*(7-v)//2:return 0
 n=0;xs=[j for j in range(v+1,8) if not adj[v]>>j&1];
 # adj stores forbidden edges among remaining vertices (common earlier neighbor).
 for k in range(max(0,m-(7-v)*(6-v)//2),min(len(xs),m)+1):
  for nb in itertools.combinations(xs,k):
   a=list(adj);s=sum(1<<j for j in nb)
   for j in nb:a[j]|=s&~(1<<j)
   for j in range(v+1,8):a[j]&=~((1<<(v+1))-1)
   a[v]=0;n+=count(v+1,m-k,tuple(a))
 return n
if __name__=='__main__':
 src=json.loads((P/'ramsey_unsaturated_eleven.json').read_text());z=json.loads((P/'ramsey_eleven_extend.json').read_text());label=count(0,11,(0,)*8);assert label==sum(40320//ig.Graph(8,r['edges']).count_automorphisms() for r in src);assert len(src)==len({tuple(sorted(ig.Graph(8,r['edges']).permute_vertices(ig.Graph(8,r['edges']).canonical_permutation()).get_edgelist())) for r in src});keys={(i,a,b) for i,s in enumerate(src) for a,b in s.get('pairs',[])};assert keys=={(r['idx'],r['a'],r['b']) for r in z} and len(keys)==len(z);counts=sum((collections.Counter(r['counts']) for r in z),collections.Counter());assert set(counts)<={'forced4','unsat4'} and not any(r['win'] for r in z);out=dict(labeled_graphs=label,types=len(src),baseline=sum(r['base'] for r in src),marked_pairs=len(keys),quota_feasible_pairs=sum(bool(r['nraw']) for r in z),marked_completions=sum(r['nraw'] for r in z),counts=counts,unknown=sum(r.get('unknown',0) for r in src+z));print(out);(P/'ramsey_eleven_coverage.json').write_text(json.dumps(out)+'\n')
