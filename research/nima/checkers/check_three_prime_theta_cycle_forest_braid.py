"""Three-prime arithmetic interval cube: exact forest and braid comparison.

Only the incidence layer is machine checked. Theta realization uses the
recorded injectivity theorem and fixed finite Gram reconstruction.
"""
import json
from itertools import permutations, product
from pathlib import Path
import sympy as s


def regularizer(k):
    return -s.trace(k)+s.trace(k*k)/2


def anomaly(a,b):
    return s.trace(a*a*b)+s.trace(a*b*b)+s.trace(a*b*a*b)/2


def main():
    primes=(2,3,5)
    nodes={mask:2*s.prod(primes[j] for j in range(3) if mask&(1<<j)) for mask in range(8)}
    vertices=sorted(nodes.values())
    edges=[(mask,mask|(1<<j),j) for mask in range(8) for j in range(3) if not mask&(1<<j)]
    n=len(edges)
    J=s.Matrix(7,n,lambda i,e:int(nodes[edges[e][0]]<=vertices[i] and vertices[i+1]<=nodes[edges[e][1]]))
    boundary=s.zeros(8,n)
    for e,(a,b,j) in enumerate(edges):
        boundary[vertices.index(nodes[a]),e]=-1
        boundary[vertices.index(nodes[b]),e]=1
    atom_boundary=s.zeros(8,7)
    for j in range(7):
        atom_boundary[j,j]=-1
        atom_boundary[j+1,j]=1
    words=list(permutations(range(3)))
    frames={}
    chords={}
    inverses={}
    paths={}
    for word in words:
        # A declared edge order gives a Kruskal spanning tree, not fitted frames.
        parent=list(range(8))
        def root(v):
            while parent[v]!=v:
                v=parent[v]
            return v
        tree=[]
        for e in sorted(range(n),key=lambda e:(word.index(edges[e][2]),nodes[edges[e][0]],e)):
            a,b,_=edges[e]
            ra,rb=root(a),root(b)
            if ra!=rb:
                parent[ra]=rb
                tree.append(e)
        chords[word]=[e for e in range(n) if e not in tree]
        Z=s.zeros(5,n)
        for row,e in enumerate(chords[word]):
            Z[row,e]=1
        frames[word]=J.col_join(Z)
        inverses[word]=frames[word].inv()
        c=s.zeros(n,1)
        mask=0
        for j in word:
            target=mask|(1<<j)
            c[edges.index((mask,target,j))]=1
            mask=target
        paths[word]=c
    transitions={(a,b):frames[b]*inverses[a] for a,b in product(words,repeat=2)}
    I=s.eye(n)
    checks={
        'boundary_factorization':atom_boundary*J==boundary,
        'seven_interval_and_five_cycle_dimensions':J.rank()==7 and boundary.rank()==7 and n==12,
        'all_six_presentations_unimodular':all(abs(f.det())==1 for f in frames.values()),
        'every_transition_preserves_all_interval_atoms':all(t[:7,:]==I[:7,:] for t in transitions.values()),
        'all_216_based_compositions':all(transitions[b,c]*transitions[a,b]==transitions[a,c] for a,b,c in product(words,repeat=3)),
        'all_inverse_transports':all(transitions[b,a]*transitions[a,b]==I for a,b in transitions),
        'source_normalized_determinants_are_units':all(transitions[a,b].det()*frames[a].det()/frames[b].det()==1 for a,b in transitions),
        'six_paths_have_same_interval_history':all(J*c==s.ones(7,1) for c in paths.values()),
        'six_paths_remain_distinct_with_cycle_port':len({tuple(frames[words[0]]*c) for c in paths.values()})==6,
    }
    # Two reduced adjacent-swap words for the three-prime reversal.
    start=(0,1,2)
    def braid(swaps):
        word=start
        result=I
        route=[word]
        for slot in swaps:
            new=list(word)
            new[slot],new[slot+1]=new[slot+1],new[slot]
            new=tuple(new)
            result=transitions[word,new]*result
            word=new
            route.append(word)
        return word,result,route
    end,left,route_left=braid((0,1,0))
    end2,right,route_right=braid((1,0,1))
    checks['braid_121_equals_212_on_full_packet']=end==end2 and left==right==transitions[start,end]
    # These are changes of forest presentation, not physical permutation of primes.
    a,b,c,d=words[:4]
    A=transitions[a,b]-I
    B=transitions[b,c]-I
    C=transitions[c,d]-I
    star=lambda x,y:x+y+x*y
    checks['ordered_plus_anomaly']=anomaly(B,A)==regularizer(star(B,A))-regularizer(B)-regularizer(A)
    checks['ordered_anomaly_cocycle']=(anomaly(C,B)+anomaly(star(C,B),A)==anomaly(B,A)+anomaly(C,star(B,A)))
    nonzero=[(a,b,c,anomaly(transitions[b,c]-I,transitions[a,b]-I))
             for a,b,c in product(words,repeat=3)
             if anomaly(transitions[b,c]-I,transitions[a,b]-I)!=0]
    checks['nonzero_bare_det3_anomaly_retained']=bool(nonzero)
    # A path difference is genuinely nonzero, not a null response packet.
    h=paths[start]-paths[(1,0,2)]
    full=frames[start]*h
    checks['path_cycle_hostile']=h!=s.zeros(n,1) and J*h==s.zeros(7,1) and full!=s.zeros(n,1)
    # Forgetting the sign and low counterterm is not determinant normalization.
    checks['rank_of_history_only_is_strictly_smaller']=J.rank()<frames[start].rank()
    assert all(checks.values()),checks
    labels=lambda w:[primes[j] for j in w]
    witness=nonzero[0]
    result={
        'schema':'marici.nima.three-prime-theta-cycle-forest-braid.v1',
        'strength':'finite_arithmetic_interval_constructor_with_recorded_analytic_premise',
        'vertices':[int(v) for v in vertices],
        'edge_count':n,'interval_atom_count':7,'cycle_dimension':5,
        'checks':checks,
        'braid_left':[labels(w) for w in route_left],
        'braid_right':[labels(w) for w in route_right],
        'cycle_hostile':[str(x) for x in h],
        'retained_cycle_response':[str(x) for x in full[7:,:]],
        'nonzero_anomaly_witness':{'frames':[labels(w) for w in witness[:3]],'value':str(witness[3])},
        'analytic_premise':'T_0 injectivity on interval step functions supported above log(2)',
        'theta_integrals_evaluated':False,
        'unsupported':['full four-phase successor','Euler low-grade identification','cutoff-uniform reconstruction','Haar-cycle closure'],
    }
    out=Path(__file__).resolve().parents[1]/'results/three-prime-theta-cycle-forest-braid.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
