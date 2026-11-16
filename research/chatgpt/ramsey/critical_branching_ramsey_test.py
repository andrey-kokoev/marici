"""Finite control: cyclic word critical branchings and Ramsey extension obstructions.
All words retain their original sequences; rewrite rules are formal witness generators.
No identification of distinct paths is asserted.
"""
from itertools import combinations, product


def graph_edges(n, invert):
    E = set()
    for i in range(n):
        E.add(frozenset((i, (i+1) % n)))
        if invert is not None:
            E.add(frozenset((i, (i+invert) % n)))
    return E


def clique_count(nodes, size, E, red=True):
    return sum(all((frozenset(p) in E) == red for p in combinations(C, 2))
               for C in combinations(nodes, size))


def extension_stats(n, E, red_forbid, blue_forbid):
    seen = []
    for mask in range(1 << n):
        A = [i for i in range(n) if mask & (1 << i)]
        B = [i for i in range(n) if not mask & (1 << i)]
        red = clique_count(A, red_forbid-1, E, True)
        blue = clique_count(B, blue_forbid-1, E, False)
        seen.append((red, blue))
    return {
        'assignments': len(seen),
        'red_safe': sum(r==0 for r,b in seen),
        'blue_safe': sum(b==0 for r,b in seen),
        'both_safe': sum(r==0 and b==0 for r,b in seen),
        'min_new_forbidden_subgraphs': min(r+b for r,b in seen),
    }


def rewriting_rules(m, complete=False):
    rules = [('r'*m,'s','N'), ('ss','','U')]
    if complete:
        rules.append(('sr','rs','C'))
    return rules


def all_next(w, rules):
    return [(w[:i] + rhs + w[i+len(lhs):], name, i)
            for lhs, rhs, name in rules for i in range(len(w)-len(lhs)+1)
            if w[i:i+len(lhs)] == lhs]


def terminal_words(w, rules):
    todo=[w]
    visited={w}
    terminals=set()
    while todo:
        a=todo.pop()
        nxt=all_next(a,rules)
        if not nxt:
            terminals.add(a)
        for b,_,_ in nxt:
            if b not in visited:
                visited.add(b)
                todo.append(b)
    return terminals


def evaluate(w,m):
    return (w.count('r') + m*w.count('s')) % (2*m)


def overlap_count(m):
    # N against N: r^m has a positive proper suffix-prefix overlap
    # for each overlap length 1,..,m-1.
    return {'N_N': m-1, 'U_U': 1, 'total_orbits':m}


if __name__ == '__main__':
    c5=graph_edges(5,None)
    w8=graph_edges(8,4)
    print('C5->K6:',extension_stats(5,c5,3,3))
    print('W8->K9:',extension_stats(8,w8,3,4))
    for n,m,k in [(6,3,3),(8,4,4),(10,5,5)]:
        E=graph_edges(n,m)
        # This Cayley graph is the red graph; complement is the blue graph.
        # Compute max independence by searching subsets.
        independence=max(size for size in range(n+1)
                         if any(all(frozenset(p) not in E for p in combinations(S,2))
                                for S in combinations(range(n),size)))
        print(f'C_{n}(1,{m}): edges={len(E)}, red_triangles={clique_count(range(n),3,E)}, independence={independence}')
        print(f'  primitive critical overlaps: {overlap_count(m)}')
        old=rewriting_rules(m,False)
        full=rewriting_rules(m,True)
        ex='r'*(m+1)
        print(f'  r^{m+1} one-step branch:',[(z,name) for z,name,i in all_next(ex,old)])
        print('  N,U alone terminals:',sorted(terminal_words(ex,old)))
        checked=0
        for length in range(0,8):
            for tup in product('rs',repeat=length):
                w=''.join(tup)
                ts=terminal_words(w,full)
                assert len(ts)==1, (n,w,ts)
                nf=next(iter(ts))
                assert evaluate(w,m)==evaluate(nf,m)
                assert nf == 'r'*(evaluate(w,m)%m) + ('s' if evaluate(w,m)>=m else '')
                checked+=1
        print('  N,U,C normal form unique through length 7:',checked,'words')
