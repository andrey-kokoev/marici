# Cyclic witness compatibility in sixteen dimensions

## Result

Let G be the graph on Z/13Z with connection differences ±1 and ±5. Let I be its family of maximal independent sets. Exact enumeration gives α(G)=4 and 39 maximal independent sets, all maximum.

Among real matrices indexed by I × I and satisfying

    M[T,S] = 0 if and only if T intersects S,

the minimum rank is exactly 16. A symmetric matrix attaining the bound is invariant under simultaneous cyclic translation of its row and column labels. Its entries belong to a degree-12 real algebraic number field.

This packet contains an exact 39×16 times 16×39 factorization. The checker verifies every entry, the complete zero/nonzero pattern, the field's real embedding, and a coefficient-independent rank-16 lower bound. It also independently verifies the Fourier-polynomial upper-bound identities. Numerical optimization was used to discover a candidate; none of the certificate checks uses a numerical tolerance.

No novelty claim is made. The result concerns the compatibility readout, not identification of distinct path histories or a derivation of Ramsey thresholds.

## 1. Indexing the requirements

Use three base sets:

    A = {0,2,4,6}, B = {0,2,6,9}, C = {0,3,6,9}.

Their translates A+i, B+i, C+i, for i=0,...,12, are the 39 requirements. Index them in that order, from 0 through 38.

The nine cyclic support lists are

| Row orbit | Column orbit | Allowed differences j−i modulo 13 |
|---|---|---|
| A | A | 1,3,5,8,10,12 |
| A | B | 1,3,5,12 |
| A | C | 5 |
| B | A | 1,8,10,12 |
| B | B | 1,5,8,12 |
| B | C | 1,5,8,11 |
| C | A | 8 |
| C | B | 2,5,8,12 |
| C | C | 1,2,5,8,11,12 |

There are 442 required nonzero entries and 1,079 required zeros. These are exact disjointness supports, not adjustable data.

## 2. The lower bound

The following row and column sequences give a lower-triangular 16×16 support submatrix with nonzero diagonal:

    rows    = [0,2,4,17,6,19,13,23,8,10,12,25,3,1,5,11]
    columns = [1,7,9,28,11,27,21,15,0,2,4,36,6,32,23,29].

Every matrix with the prescribed zero/nonzero pattern therefore has a nonzero 16×16 determinant. The argument works over any field. It is the standard triangular-pattern, or visible-rank, lower bound; its particular indices are part of this certificate.

## 3. Exact coefficient field

Let t=2 cos(2π/13), the largest real root of

    f(t)=t^6+t^5−5t^4−4t^3+6t^2+3t−1.

Define

    c0=3t^5+t^4−16t^3−t^2+19t−4,
    c1=t^4−t^3−3t^2+3t,

and choose either real root λ of

    λ^2+c1 λ+c0=0.

For the displayed real embedding,

    t ≈ 1.7709120513064197918,
    λ ≈ −0.6131940792585343957

is one choice; the other is approximately 0.4273477203919401494.

The discriminant Δ=c1^2−4c0 is positive at this embedding. Its norm from Q(t) to Q is exactly 325. Since 325 is not a rational square, Δ is not a square in Q(t). Thus the quadratic extension is a field, of total degree 12. Every coefficient is represented uniquely as a(t)+b(t)λ, with a and b reduced to degree at most five.

The checker isolates t in the rational interval

    17709120513/10^10 < t < 17709120514/10^10

and verifies positivity of Δ there using exact rational interval arithmetic. It checks irreducibility of f and the discriminant norm.

## 4. Explicit cyclic construction

Work with polynomials in z modulo z^13−1. Set

    u=t^4−4t^2+2,
    v=t^5−5t^3+5t,
    d=t^4+t^3−2t^2−2t,
    p=−v+(1−u)λ,
    q=v+(t+1)λ.

The defining quadratic implies exactly

    p q = −1−u λ.

Define two pairs of eight-component vectors over Q(t):

    b0 = (
      −t^4+t^3+3t^2−2t−1,
      −t^5+3t^3+t^2−t−1,
      −3t^5+2t^4+10t^3−4t^2−6t+1,
       3t^5−3t^4−9t^3+7t^2+4t−2,
       t^4−t^3−3t^2+2t+2,
       t^5−4t^3−t^2+4t+2,
       1, 0)

    b1 = (
      −t^5+3t^3+t^2−t−1,
      −t^4+t^3+3t^2−2t−1,
       3t^5−3t^4−9t^3+7t^2+4t−2,
      −3t^5+2t^4+10t^3−4t^2−6t+1,
       t^5−4t^3−t^2+4t+2,
       t^4−t^3−3t^2+2t+2,
       0, 1)

    e0 = (
      −t^4+t^3+5t^2−3t−3,
       t^4−4t^2+t+3,
       t^5−4t^3+t^2+3t,
      −t^5+5t^3+t^2−4t−2,
       t^3−2t, 1, 1, 0)

    e1 = (
       t^4−4t^2+t+3,
      −t^4+t^3+5t^2−3t−3,
      −t^5+5t^3+t^2−4t−2,
       t^5−4t^3+t^2+3t,
       1, t^3−2t, 0, 1).

Let b=p b0+b1 and e=q e0+e1, with components numbered 0,...,7. Define

    A(z)=z+z^12
       +(3t+3t^2−t^3−t^4)(z^3+z^10)
       +(t+3t^2−t^4)(z^5+z^8),

    B(z)=b[0]z+b[1]z^3+b[2]z^5+b[3]z^12,
    C(z)=e[4]z+e[5]z^8+e[6]z^10+e[7]z^12,
    D(z)=λ(z+z^12+d(z^5+z^8)),
    E(z)=e[0]z+e[1]z^5+e[2]z^8+e[3]z^11,
    F(z)=b[4]z^2+b[5]z^5+b[6]z^8+b[7]z^12,

    H(z)=(−6−4t+9t^2+t^3−2t^4)(z+z^12)
       +(−6−10t+5t^2+10t^3−t^4−2t^5)(z^2+z^11)
       +(−2+2t^2−3t^3+t^5)(z^5+z^8).

The polynomial block matrix is

              [ A(z)  B(z)  z^5 ]
    P(z)  =   [ C(z)  D(z)  E(z)] .
              [ z^8   F(z)  H(z)]

Set

    g=λ−t^5+4t^3−3t+1,
    P_s(z)=diag(1,g,1) P(z).

The nonzero row scaling by g makes the certificate symmetric. For a,b in {0,1,2} and i,j in Z/13Z, define M[(a,i),(b,j)] to be the coefficient of z^(j−i) in P_s[a,b](z). This specifies all 1,521 entries and makes simultaneous translation invariance explicit.

The certificate JSON contains the reduced coefficients of all nine blocks. All 34 supported coefficients are nonzero in the exact field; the other 83 block coefficients are zero. Expanding the circulants gives the required 442/1,079 nonzero/zero counts.

## 5. Fourier proof of the upper bound

Let ζ=exp(2πi/13). Fourier transformation on each orbit decomposes the 39×39 matrix into the thirteen 3×3 matrices P_s(ζ^j).

Put

    Q(z)=(z^13−1)/((z−1)(z^2−u z+1)).

Because u=ζ^4+ζ^(−4), its ten roots are ζ^j with j not in {0,4,9}.

The checker verifies these polynomial identities exactly:

1. Every 2×2 minor of P_s(z), reduced modulo z^13−1, is divisible by Q(z).
2. det P_s(z) is zero modulo z^13−1.

At the ten ordinary modes the block rank is at most one. The entry z^5 is nonzero at every mode, so those ten ranks are exactly one. At modes 0,4,9 the determinant identity gives rank at most two. Therefore

    rank M ≤ 10·1+3·2=16.

The triangular lower bound forces equality. It also forces rank exactly two at each exceptional mode. In mode order 0,...,12, the ranks are

    2,1,1,1,2,1,1,1,1,2,1,1,1.

## 6. A second exact upper-bound certificate

Let R and C be the row and column sequences in Section 2. Define

    U=M[:,C],
    L=M[R,C],
    V=L^(−1)M[R,:].

Here L is lower triangular with nonzero diagonal. The supplied JSON contains all entries of U (39×16) and V (16×39), and the checker verifies M=UV entry by entry in the exact field. This check is independent of the Fourier-minor check.

There is also a same-feature bilinear representation. Let J be the sixteen selected column indices and let

    B=M[J,J]^(−1).

The certificate contains this symmetric, invertible 16×16 matrix and verifies

    V=B U^T,
    M=U B U^T.

Consequently a single vector w(T) in R^16 is assigned to each retained set label, and

    w(T)^T B w(S)=0 if and only if T intersects S.

The pairing is indefinite: every diagonal matrix entry is zero, while the matrix is nonzero, which excludes positive or negative semidefiniteness. This is not a Euclidean inner product or an identification of labels.

Cyclic translation also acts inside this feature space. If σ translates a set by one, define

    R^T=B U[σ(J),:].

The packet includes R and checks, in exact arithmetic,

    w(T+1)=R w(T),
    R^13=I,  R≠I,
    R^T B R=B.

Thus the thirteen-position translation has an actual order-13, pairing-preserving linear action on the sixteen-dimensional readout space. This derives a symmetry action for the certificate; it does not identify this action with an already admitted native path constructor.

## 7. Consequence for irreducible witness incompatibility

For an irreducibly incompatible family T_1,...,T_q, take a deletion witness S_i for every requirement T_i. Then

    T_i intersects S_j for i≠j,
    T_i is disjoint from S_i.

A deletion witness may be extended to a maximal independent set. It must still miss its omitted requirement, or it would witness the entire family. Thus the relevant submatrix of M is diagonal with nonzero diagonal, giving q≤rank M.

The same reasoning applies to arbitrary disjoint unions of copies of G. All maximal independent sets decompose componentwise and remain maximum. For two components, a requirement and a witness are disjoint exactly when they are disjoint in both components. Therefore tensor products preserve the exact zero pattern.

For t copies of G and b isolated edge components, use

    M^(tensor t) tensor [[0,1],[1,0]]^(tensor b).

Its rank is 16^t 2^b=2^(4t+b), and the independence capacity is a=4t+b. Every irreducible incompatibility in these environments consequently has at most 2^a requirements.

This proves the proposed upper bound for an infinite family containing nonbinary connected components. It does not assert that the bound is attained in each member. In particular, the previously established h(G)=13 is compatible with representation rank 16. The present checker does not repeat the separate maximum-obstruction enumeration proving h(G)=13.

## 8. Why uniform signs and rational cyclic coefficients are insufficient

Every matrix formed by assigning only +1 or −1 to the supported entries reduces modulo two to the unweighted disjointness matrix, whose rank over F_2 is 26. Such an integer signing therefore has real rank at least 26. The successful certificate uses nonuniform algebraic coefficients.

There is a separate exact restriction on cyclically invariant rational matrices. Their twelve nontrivial Fourier blocks are Galois conjugate, so they all have the same rank r. The trivial block has rank r0 between one and three, because the A,C permutation block is nonzero. Thus total rank is r0+12r. Combined with the universal lower bound of 16, this gives rank at least 25 for cyclically invariant rational realizations. It says nothing about arbitrary rational matrices that break cyclic symmetry.

## 9. Reproduction and scope

Run:

    python verify_rank16.py

The checker requires SymPy and writes verification_results.json. It performs exact arithmetic only. The coefficient file contains the cyclic blocks, row/column indexing, the triangular certificate, and both factors.

The numerical discovery process searched cyclic Fourier blocks, refined a candidate at high precision, reconstructed coefficients in Q(t,λ), and then discarded numerical tolerances in favor of exact verification. The result does not depend on rerunning that search.

Remaining unproved: a rank-2^α(G) certificate for every triangle-free graph; the general H(a)=2^a conjecture; and a derivation of these certificates from the proposed r,s path-witness operations. The coefficients here are an algebraic certificate of the existing compatibility relation, not a new admissibility rule.

## Background references

Charles R. Johnson and Joshua A. Link, “The extent to which triangular sub-patterns explain minimum rank,” Discrete Applied Mathematics 156 (2008), 1637–1651. DOI: 10.1016/j.dam.2007.08.040.

Omar Alrabiah and Venkatesan Guruswami, “Visible Rank and Codes with Locality,” APPROX/RANDOM 2021, LIPIcs 207, 57:1–57:18. DOI: 10.4230/LIPIcs.APPROX/RANDOM.2021.57.
