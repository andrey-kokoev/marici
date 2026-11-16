# Algebraic simplex-composition and antipodal Hall laws

## Scope

Let d≥4 be even, V=F₂^d, and S={e₁,…,e_d, 1̲} where 1̲=e₁+⋯+e_d.
Let F_d=Cayley(V,S) be the A-graph and B its complement.

These identities concern walks and contacts in this fixed family of graphs.
They do **not** prove a general Ramsey-number formula or create independent higher homotopy fillers.

## Theorem 1: complete minimal-composition hierarchy

The only F₂-linear relation on S is the sum of all d+1 generators. Each vertex
w of Hamming weight t has precisely two representations as subsets of S:
{e_i: w_i=1}, of cardinality t, and its complement in S, of cardinality d+1−t.
Any shortest word uses each generator at most once because s+s=0.
Since d+1 is odd, the shorter subset is unique.

Hence

    dist_A(0,w) = min(t,d+1−t).

If r is this distance, the number of shortest ordered A-paths to w is exactly r!.
There are binom(d+1,r) vertices in distance layer r, for 0≤r≤d/2.
In particular, the common A-neighbor count of two distinct vertices u,v is

    c_2(u,v)=2 if |u+v|∈{2,d−1}, and 0 otherwise.

The adjacency eigenvalue for character χ of weight j is

    λ_j=d−2j+(−1)^j.

For even d, combining equal eigenvalues at j=2r−1,2r yields the spectrum

    λ_r=d+1−4r, multiplicity binom(d+1,2r), 0≤r≤d/2.

For walks of arbitrary length k,

    W_k(w) = 2^(−d) Σ_{χ∈F₂^d} (−1)^{χ·w} λ_{|χ|}^k.

The proof is character orthogonality on F₂^d; no graph search is needed.

## Theorem 2: Clebsch neighborhood expansion from strong regularity

For d=4, F_4 is the 16-vertex Clebsch graph with SRG parameters (16,5,0,2).
An A-independent pair has exactly two common A-neighbors.
These two neighbors each meet three other vertices, all B-adjacent to both
pair endpoints. Their additional three-neighbor sets are disjoint (their
only common neighbors are the endpoints). They exhaust the six possible
B-common neighbors of the original pair. Therefore every A-independent
triple has exactly one common A-neighbor.

By inclusion-exclusion, an independent triple has A-neighborhood union
15−3·2+1=10. It has 16−3−10=3 independent extensions.
There are 80 independent pairs, and hence 80·6/3=160 independent triples and
160·3/4=120 independent four-sets.

For an independent four-set X, all triple subsets have a unique common
A-neighbor. Inclusion-exclusion yields |N_A(X)|=12−e, where e=1 iff all
four lie in N_A(q) for some q, otherwise e=0. There are 16·5=80 sets with
e=1: every such set determines q uniquely since two q's share at most
two A-neighbors. They each have exactly one independent extension. The
other 40 independent four-sets have no extension. Thus there are 16
independent five-sets, precisely the sixteen neighborhoods N_A(q).
No six-element independent set exists.

    |X|   # sets    |N_A(X)|
      1       16         5
      2       80         8
      3      160        10
      4       80        11
      4       40        12
      5       16        11

There are exactly 392 nonempty independent sets. This replaces that
part of the earlier Hall computations with a structural derivation.

## Theorem 3: antipodal-quotient Hall formula in every even dimension

Split F_d into lower and upper halves of 2^(d−1) vertices. Suppose local
A-recompositions alter only lower-half edges and newborn A-ports are also
in the lower half; the original two crossing A-generators remain intact.

In each half, the original induced graph is the ordinary (d−1)-cube.
Every lower vertex v has exactly two upper A-neighbors: v and v+1̲_(d−1).
These form an antipodal quotient class. There are M=2^(d−2) classes.

The upper cube is the bipartite double cover of the quotient graph
Q=F_(d−2), the folded cube on M vertices with d−1 generators.
For any lower A-independent set I, let D(I) be the quotient classes
meeting I, U(I)=Q\D(I), and p(I)=|I|−|D(I)|.
Then the upper vertices available to join I form the double cover of Q[U].
By Kőnig's theorem their maximum independent-set size equals

    |U|+h_Q(U),
    h_Q(U)=max_{X⊆U} (|X|−|N_Q(X)∩U|).

Here X may be restricted to A-independent sets of Q. Indeed, for any X,
let X₀=X\N_Q(X) be the vertices isolated in the induced Q[X]. Then
N_Q(X₀)∩U⊆(N_Q(X)∩U)\X and the deficit of X₀ is at least that of X.

For any subset T of newborns with port union P_T, the exact old B-link
capacity is

    β_d(T)=M + max_{I⊆lower: I A-independent, I∩P_T=∅}
                    [p(I)+h_Q(U(I))].

This is valid for all even d≥4. It does not require Clebsch strong
regularity, although evaluating h_Q becomes harder for d≥8.

## Theorem 4: exceptional two-mode collapse in the four-birth F_6 family

For the original 8-square edited lower-half geometry, four births use all
8 square cells, with four first- and four second-orientation contacts.
For any selected birth subset T, let I range over lower-half A-independent
sets avoiding the selected ports.

Two explicit lower/upper choices give the capacities:

    E₀(T)=16+max_I (|I|−|D(I)|),
    E₅(T)=10+max_{q,I: D(I)∩N_Q(q)=∅} |I|.

E₀ uses a fixed upper parity class, one vertex per untouched class.
E₅ uses both upper lifts of the five-cell independent neighborhood N_Q(q).

The **exact** identity

    β_6(T)=max(E₀(T),E₅(T))

was verified against the full Hall formula for *every* marked contact
pattern, using 24+48+24+6 symmetry-orbit representatives and their complete
4,830-case multiplicities:

    # selected births       total marked patterns       disagreements
             1                   1,120                      0
             2                   2,520                      0
             3                   1,120                      0
             4                      70                      0

The equality is a complete **finite** theorem for this family, not yet a
dimension-free algebraic normal-form proof. Its two terms explain the
previous singleton/pair witness forms (12+10, 11+10, 10+11) and the
parity witness for four births.

For d=6 the quotient Q is Clebsch and all non-A pairs there have two
length-2 A-compositions. For d=8 the quotient is F_6, which has non-A
pairs with zero length-2 A-compositions (weight 3 or 4). Thus the uniform
Clebsch 2-step neighborhood argument does *not* extend unchanged.

## Reproduction

Run:

    python ramsey_simplex_direction_theorem.py
    python ramsey_hall_extreme_test.py

Both standard-library scripts check the stated finite identities.
