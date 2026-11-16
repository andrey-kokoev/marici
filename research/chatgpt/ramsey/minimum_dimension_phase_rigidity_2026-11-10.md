# Minimum-dimension phase rigidity of quadratic chirps

Date: 2026-11-10.

Status: A conjecture for all n >= 3, with the n = 3 case proved using an exactly rechecked cycle-rank certificate. The assertion fails for n = 2. A separate theorem excludes all translation-invariant counterexamples in every dimension. The unrestricted n = 4 case has not been solved here. No publication-priority claim is made.

## 1. Conjecture

Let Q_n be the vector space of Boolean polynomials of degree at most two with q(0) = 0. Put d = 2^n and N = |Q_n| = 2^{n(n+1)/2}. For q in Q_n define

\[
\psi_q(x)=d^{-1/2}(-1)^{q(x)},\qquad
G^0_{pq}=\langle\psi_p,\psi_q\rangle,\qquad
p_{pq}=(G^0_{pq})^2.
\]

Labels are retained. All vectors and Gram matrices in this note are real.

**Conjecture.** For every n >= 3, every real positive semidefinite Gram matrix G satisfying

\[
G_{qq}=1,\qquad G_{pq}^2=p_{pq},\qquad \operatorname{rank}G\le d
\]

has the form

\[
G=E G^0 E,\qquad E=\operatorname{diag}(\epsilon_q),\quad \epsilon_q\in\{\pm1\}.
\]

Equivalently, every real unit-vector realization v_q in R^d of the prescribed transition probabilities satisfies

\[
v_q=\epsilon_q O\psi_q
\]

for one common orthogonal matrix O. The competing vectors are not assumed to be chirps, flat, stabilizer states, or an orbit of the translation group.

The conjecture says that all pairwise squared overlaps determine the complete labelled projective configuration at its minimum possible real dimension. It does not assume any Bargmann invariant or overlap sign as input.

## 2. Minimum dimension and the exact matrix equation

For each fixed quadratic part, the d linear-phase variants form an orthonormal basis. Consequently,

\[
\sum_{q\in Q_n}|\psi_q\rangle\langle\psi_q|=\frac Nd I_d,
\qquad (G^0)^2=\frac Nd G^0.
\]

Every candidate G with the prescribed entrywise squares has

\[
\operatorname{Tr}G=N,\qquad \operatorname{Tr}(G^2)=N^2/d.
\]

If G is positive semidefinite of rank r, Cauchy-Schwarz on its positive eigenvalues yields

\[
N^2\le rN^2/d,\qquad r\ge d.
\]

Thus d is the minimum dimension forced by the data, not a freely fitted parameter. If rank G <= d, equality holds and all nonzero eigenvalues equal N/d. Hence

\[
G^2=(N/d)G.
\]

Conversely, a real symmetric G with diagonal 1 satisfying this matrix identity is positive semidefinite of rank d: its eigenvalues belong to {0,N/d}, and its trace is N.

The conjecture is therefore equivalent to an exact finite signing problem:

\[
G=G^T,\quad G_{qq}=1,\quad G_{pq}^2=p_{pq},\quad
G^2=(N/d)G
\quad\Longrightarrow\quad G=E G^0 E.
\]

## 3. Failure in two bits

For n = 2 there are two chirp bases: the four Walsh states indexed by linear polynomials, and the four states indexed by x_1x_2 plus a linear polynomial. Within each basis distinct states are orthogonal; every cross-basis squared overlap is 1/4.

Keep the first basis labelled as before. In the second basis exchange the labels x_1x_2 and x_1x_2+x_1, leaving the other labels unchanged. This preserves every labelled pairwise transition probability and the realization dimension four.

The cycle

\[
0,\quad x_1x_2,\quad x_2,\quad x_1x_2+x_2,\quad0
\]

has holonomy +1 before this exchange and -1 after it. Vertex-sign changes preserve cycle holonomy. The two labelled Gram matrices are therefore not gauge-equivalent.

The accompanying exact calculation checks both signed matrices satisfy G^2 = 2G.

## 4. Proof in three bits

Here N = 64 and d = 8. The exactly rechecked overlap graph has 896 edges and 3,584 triangles. Every nonzero off-diagonal Gram entry has magnitude 1/2. Its cycle space has dimension 833; triangle boundaries span dimension 832.

For any candidate G, Section 2 gives G^2 = 8G, so

\[
\operatorname{Tr}G^3=4096.
\]

Expanding the trace by diagonal terms, edges, and triangles gives

\[
\operatorname{Tr}G^3
=64+6(896)(1/4)
 +6\sum_{\{i,j,k\}\text{ triangle}}G_{ij}G_{jk}G_{ki}.
\]

Each triangle contribution is either +1/8 or -1/8. The maximum possible right-hand side is

\[
64+1344+6(3584)(1/8)=4096.
\]

Thus every triangle must have positive holonomy.

Modulo vertex-sign changes, sign assignments with positive triangle holonomies are classified by the dual of the cycle space modulo triangle boundaries. This quotient is one-dimensional, so exactly two gauge classes are possible.

One is the flat class, represented by the Gram signing with every nonzero overlap positive. That matrix has row sum 1 + 28/2 = 15, hence eigenvalue 15, contradicting G^2 = 8G. The only remaining class is the class of the actual chirp Gram matrix, which has a negative four-cycle.

Therefore the conjecture holds for n = 3. The proof uses the exact binary triangle-rank certificate, not a numerical search over signings.

## 5. Translation-invariant uniqueness in every dimension

This result does not settle the conjecture: an arbitrary Gram signing need not retain translation symmetry even when its entrywise square does.

**Theorem.** For n >= 2, a feasible minimum-rank Gram matrix that is translation-invariant in the polynomial labels is gauge-equivalent to G^0. The same conclusion holds if it can be made translation-invariant by vertex-sign changes.

### 5.1 The quadratic evaluation set has no short even dependence

Let A = Q_n and identify its dual A* with binary vectors of length n + binom(n,2). Define

\[
e(x)=(x_i,\ x_ix_j\ (i<j)),\qquad E=\{e(x):x\in\mathbb F_2^n\}.
\]

There is no zero sum of two, four, or six distinct elements of E.

Proof: Suppose k distinct x-values, with k in {2,4,6}, give such a relation. Form the matrix with these x-values as columns, and append an all-ones row. The evaluation equations say all these rows have zero binary dot products with one another, including themselves. Their row span R is therefore totally isotropic in F_2^k and has dimension at most k/2. It contains the all-ones vector. A generator matrix of R containing that vector as its first row has at most 2^{dim R-1} distinct columns. But the appended original columns are distinct and k > 2^{k/2-1} for k = 2,4,6, a contradiction.

In particular E is a Sidon set in the characteristic-two sense: each nonzero difference e(x)+e(y) has one unordered-pair representation.

### 5.2 Fourier reduction of a translation-invariant candidate

Write G_{pq} = g(p+q). The characters of A diagonalize G. Since its eigenvalues are 0 or N/d, there is a d-element subset T of A* such that

\[
g(u)=d^{-1}\sum_{t\in T}(-1)^{t(u)}.
\]

For the standard chirps the corresponding subset is E. The equality g(u)^2 = g_0(u)^2 for all u implies equality of the difference multiplicities of T and E, by Fourier inversion.

Thus T is also a d-element Sidon set, and its nonzero difference set is exactly

\[
\Delta E=\{e(x)+e(y):x\ne y\}.
\]

Translate T to contain zero. Its d-1 nonzero elements correspond to d-1 unordered pairs from E. Any two such pairs must intersect: disjoint pairs whose label sum belongs to Delta E would yield a zero sum of two, four, or six distinct elements of E, which Section 5.1 excludes.

A pairwise-intersecting family of distinct two-element subsets is either a star or a three-edge triangle. For n >= 3, the family has d-1 >= 7 elements and must be the full star through one point e(x). Consequently T is a translate of E.

For n = 2, a three-edge triangle is also combinatorially possible, but then those three labels sum to zero. Together with zero this would give a four-element dependence in T, contrary to its Sidon property. Again T is a translate of E.

Translation of the Fourier set multiplies g by a character. This is precisely a vertex-sign gauge transformation of G^0. The theorem follows.

### 5.3 Computational checks

The attached script checks the underlying line-graph identity for n = 2,3,4,5: the graph on Delta E joining two labels when their sum lies in Delta E is the line graph of the complete graph on E. The proof above establishes the statement for every n.

Any counterexample to the full conjecture must therefore be a Gram realization that cannot be made translation-invariant by sign changes. Restricting a search to translation-invariant matrices would discard every possible counterexample.

## 6. The first unresolved finite case in this analysis

For n = 4, N = 1024 and d = 16. The known Gram entries belong to {1,0,+/-1/2,+/-1/4}. Set K = 4G. The complete exact search problem is

\[
K=K^T,\quad K_{qq}=4,\quad K_{pq}^2=(K^0_{pq})^2,\quad
K^2=256K.
\]

Every solution is automatically a rank-sixteen positive semidefinite Gram matrix after division by four. Refutation requires a solution not of the form E K^0 E.

A spanning-tree gauge fixes 1023 redundant edge signs. There are 301056 nonorthogonality edges, leaving 300033 cycle-sign variables before the matrix equations are imposed. This describes a finite exact problem; no exhaustive solution has been performed here.

By the previously proved triangle-generation theorem, gauge inequivalence at n = 4 is equivalent to changing the sign of at least one nonzero triangle Bargmann invariant. Therefore an exact counterexample search can impose a triangle-sign discrepancy in addition to the equations above. Exhausting one prescribed triangle is not by itself a proof of the full n = 4 claim; all relevant discrepancies must be excluded, for example via a proved symmetry reduction.

A concrete test triangle is

\[
q_0=0,\qquad q_1=x_1+x_1x_2,\qquad
q_2=x_2x_3+x_4+x_1x_4.
\]

Its overlaps are 1/2, 1/4, -1/4 and its Bargmann invariant is -1/32. Keeping these magnitudes but changing the product to +1/32 produces a positive definite three-by-three Gram matrix: the determinants are respectively 9/16 and 11/16. Local three-vector positivity does not choose the sign. The issue is whether the changed sign extends to all 1024 vectors while retaining the exact rank-sixteen matrix equation.

An alternative feasible matrix is a decisive refutation. Failure to find one is not confirmation. A proof for all n requires a dimension-independent rigidity argument or a justified dimension-lifting theorem; the earlier graph-cycle lifting theorem does not automatically provide a Gram-rigidity lift.

## 7. What the alternatives establish

If true, the conjecture says pairwise transition probabilities and minimum real realization dimension determine all ordered projector products up to common orthogonal conjugation. In particular all cyclic traces are determined. Third- and higher-order phase data would be forced by global rank-one realizability, although they are not determined by an isolated pair or triple of vectors.

If false, the counterexample supplies two complete labelled rank-one configurations of minimum dimension with identical Hilbert-Schmidt Gram matrices of projectors and different Bargmann invariants. It establishes an irreducible loss of composition information in pairwise transition probabilities even after the full redundant dictionary and the minimal dimension are fixed.

This is different from assigning arbitrary signs to graph edges. A graph signing is a counterexample only if the entire signed Gram matrix is positive semidefinite of rank d, equivalently satisfies the exact matrix identity above.

This conjecture concerns real chirp projectors and their comparison geometry. It does not assert uniqueness of a marked binary-coordinate system, a specific Weyl basis, or a simplicial filling.

## 8. Relationship to existing results

Chien and Waldron, *A characterisation of projective unitary equivalence of finite frames*, arXiv:1312.5393, develop projective classification by Bargmann invariants and cycle spaces. The preceding quadratic-chirp cycle theorem is an instance-specific bound on the required cycle lengths.

Obst, Heimendahl, Singal, and Gross, *Wigner's Theorem for stabilizer states and quantum designs*, arXiv:2405.17565, classify several notions of symmetry of stabilizer-state sets, including transition-probability-preserving bijections. The conjecture here permits an arbitrary real Gram realization outside the known chirp set. A theorem about bijections of the original set alone does not settle this stronger realization problem.

## 9. Reproduction

The package includes the prior exact cycle verifier and a rechecked JSON certificate; `check_pairwise_rigidity_base.py` verifies the two-bit counterexample and numerical identities and cycle ranks used in the three-bit proof; `check_circulant_reduction.py` verifies the evaluation-set line-graph reduction through five bits. All calculations use exact integers and binary elimination. No floating-point feasibility search or unrestricted four-bit signing search is claimed.
