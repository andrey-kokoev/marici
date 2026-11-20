"""Which relabelings of the joins exchange the two repairs? No completed graph is used to propose a relabeling."""
from itertools import combinations
from collections import Counter
import igraph as ig
from ramsey_35_all_optimal_words import enumerate_repairs


def main():
    _,words=enumerate_repairs();counts=Counter()
    for w,repairs in sorted(words.items()):
        V=range(13);direct={(i,j) for i in V for j in V if w[i+1]==w[j]};rev={(j,i) for i,j in direct};graph=ig.Graph(13,[(i,j) for i,j in combinations(V,2) if (i,j) in direct or (j,i) in direct]);A,B=[{(i-1,j-1) for i,j in s} for s in repairs];hits=set();best=None
        for p in graph.get_automorphisms_vf2():
            image={tuple(sorted((p[i],p[j]))) for i,j in A};assert image in (A,B)
            if image!=B:continue
            hits.add('undirected');d={(p[i],p[j]) for i,j in direct}
            if d==direct:hits.add('directed')
            if d==rev:hits.add('all reversed')
            if p==list(reversed(V)):hits.add('chain reversed')
            moves=[(i+1,p[i]+1) for i in V if i!=p[i]]
            if best is None or len(moves)<len(best):best=moves
        counts.update(hits);print(''.join(chr(65+i) for i in w),sorted(hits),best)
    print(counts)
if __name__=='__main__':main()
