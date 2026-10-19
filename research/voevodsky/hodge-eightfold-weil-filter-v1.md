# Iteration 10: full eightfold Weil filter and the order of reverse transfer

## Result

Keep the same sixfold X, alpha=R6 and auxiliary A=X x B constructed previously. This turn constructs the explicit rational projector P8 on **all** H^8(A,Q), of dimension 12870, onto its two-dimensional determinant Weil plane W8. It supplies the cycle-preserving test

    T=D P8:H^8(A,Q)->W6.

For an actual codimension-four algebraic cycle beta on A, T(cl(beta)) nonzero would yield an algebraic representative of the original alpha by the already proved 2x2 inverse. No such beta has been supplied.

The construction is not an all-cycle annihilator and does not decide algebraicity. It is a correct filter with exact scope, not a new counterexample. A bounded search through 15 actual factor-divisor cycles gives no nonzero Weil projection.

## 1. Complete spectrum and explicit polynomial

Let F_A=(2+i)*. Splitting H^1(A,Q(i)) into its two eight-dimensional K-character spaces, the degree-eight character with a factors from the first and 8-a from the second has eigenvalue

    lambda_a=(2+i)^a(2-i)^(8-a), a=0,...,8,
    multiplicity=binomial(8,a)^2.

All nine values are distinct. The multiplicities are

    (1,64,784,3136,4900,3136,784,64,1), sum 12870.

Their rational minimal factors, indexed by conjugate pairs, are

    m0=t^2+1054t+390625,       a=0,8,
    m1=t^2+1170t+390625,       a=1,7,
    m2=t^2+350t+390625,        a=2,6,
    m3=t^2-750t+390625,        a=3,5,
    m4=t-625,                a=4.

The endpoint eigenvalues are -527 +/-336i. Put q=m1 m2 m3 m4. Then

    P8(t)=(302035039681+797649839 t) q(t)
           /12644736328125000000000000000000.

Exact rational division verifies P8=1 modulo m0, P8=0 modulo the other four factors, and P8^2=P8 modulo their product. Therefore P8(F_A) is the rank-two full-cohomology Weil projector. The polynomial is defined from the supplied endomorphism, not from an unknown quotient by algebraic classes.

Since A is balanced Weil type, W8 is of type (4,4). This does not compute the entire Hodge space of A; its special product structure has other rational Hodge sectors.

## 2. An independently derived fast coordinate implementation

Set u_j=dx_j+i dy_j. In each native pair,

    dx_j=(u_j+conjugate(u_j))/2,
    dy_j=(u_j-conjugate(u_j))/(2i).

A degree-eight native monomial containing both coordinates of some pair has both K characters and hence no endpoint component. A monomial with one coordinate from each pair and k y-indices has all-u coefficient (-i)^k/256. Adding its conjugate gives

    P8(monomial)=(-1)^(k/2) R8/128,                k even,
    P8(monomial)=(-1)^((k-1)/2) I8/128,            k odd.

This formula is the same spectral projector: it is identity on the endpoint lines and zero on every other character. It is not a fitted period reader on a few chosen classes. The checker examines all 12870 real basis columns: 256 have nonzero images, the trace is two, and R8,I8 are fixed. The analogous n=6 formula is cross-checked against the original sixfold CRT polynomial.

Native (2+i) pullback is tensorized exactly: a complete dx_j dy_j pair contributes determinant five, a single coordinate transforms by its two-by-two matrix, and missing pairs contribute one. This avoids constructing a dense 12870-square matrix. It is cross-checked with the old exterior pullback and used for the full source intertwining calculation.

The coordinate formula depends on the marking only as a presentation. The spectral definition is intrinsic relative to the specified K action and conjugates correctly under a marking change. Functorial cohomology pullback gives class-level descent, not dependence on a chosen cocycle history.

## 3. Algebraic preservation is the license for testing cycles

F_A is the pullback of an algebraic finite etale isogeny. The rational combination of its iterated flat pullbacks given by P8 defines an operator P8_CH on CH^4(A)_Q. Cycle-class functoriality gives

    cl(P8_CH beta)=P8(F_A) cl(beta).

Composing with the already constructed D_CH therefore gives a genuine algebraic map CH^4(A)_Q->CH^3(X)_Q inducing T. Its image in cohomology lies in W6, because P8 first lands in W8 and D identifies the two Weil planes.

We do **not** assert P8_CH^2=P8_CH. The annihilating minimal polynomial and idempotence above are cohomological statements. Nor do we assert the old sixfold P6_CH equals D_CH P8_CH S_CH on Chow. The verified identity below concerns cohomology. The actual Chow identity D_CH S_CH=Id from iteration 9 remains valid but cannot by itself justify the new assertions.

The filtered image preserves algebraic classes rather than annihilating them. All-cycle vanishing of T on A is equivalent to alpha nonalgebraic: any nonzero T-image yields alpha, while if alpha were algebraic, S_CH would give a pure W8 representative detected by P8. This equivalence isolates the unsolved geometric question; it is not a proof of either side.

## 4. The correct intertwining identities

On the entire source H^6(X,Q),

    P8 S=S P6,
    D P8 S=P6.

The checker verifies both identities on all 924 native source basis vectors, not only R6,I6. The conceptual proof is also direct. S uses an endomorphism polynomial on X and r,s on B. The latter carry only the two determinant characters of the surface. A non-endpoint sixfold character cannot reach an eightfold endpoint after adding two characters; the endpoint sixfold plane is mapped exactly to W8. This proves the first identity, and D S=Id proves the second.

On all H^8(A,Q), S D P8=P8, since S D is identity on W8. The reverse ordering is different.

### Counterexample to commuting the filters

Define rational Hodge tensors

    R_op=R6 r+I6 s,
    I_op=I6 r-R6 s.

They are not supplied algebraic cycles. Their characters are the a=2,6 pair, not the eightfold endpoints. Accordingly,

    P8(R_op)=P8(I_op)=0,
    D(R_op)=R6, D(I_op)=I6.

Thus D P8 is **not** P6 D on arbitrary target cohomology. Also

    P8 S D(R_op)=R8,
    S D P8(R_op)=0.

The genuine rank-924 Chow image projector S_CH D_CH and the rank-two cohomological projector P8 therefore do not even commute on cohomology. Containment of images does not justify commuting nonorthogonal projections.

This matters when testing proposed cycles. The filter T is an exact sufficient positive test and has the correct existence equivalence, but it can discard an individual opposite-sector class. If such a class were algebraic, D followed by the sixfold filter would instead recover a Weil witness. One cannot reorder the maps without keeping their domains and kernels.

## 5. Actual bounded cycle search and coarse-projector hostiles

Use the four explicit B-divisors D1,D2,r,s from iteration 9. Enumerate all 15 rational algebraic factor-divisor monomials

    E_X^(4-k) external (a degree-k monomial in D1,D2,r,s), k=0,1,2.

Eight have nonzero cohomology. Every Weil projection is zero. The receipt lists every monomial and whether its class is zero; this is a bounded actual-cycle control, not a complete codimension-four cycle enumeration.

In particular E_A^4 is a nonzero algebraic class with F_A eigenvalue 625, killed by P8. The nonzero actual cycle S_CH(E_X^3) also has zero filtered reverse, despite its unfiltered reverse being E_X^3. This prevents a divisor cube from being called an alpha witness.

Two coarser substitutes are wrong:

- With B_A=(1+i)*, the rational polynomial (t+16)(t^2+256)/16384 selects a=0,4,8, of total rank **4902**, not two. It even fixes the known algebraic E_A^4, whose B_A eigenvalue is 16.
- The diagonal-i invariant sector has rank **6470**, not two. Diagonal i fixes W8 but also many other classes.

The full spectrum, correct polynomial and explicit divisor controls are needed. Neither full-cohomology hostile is erased by the fact that the desired Weil space is Hodge; the whole Hodge space of this special eightfold has not been identified with the desired two-plane.

## 6. Net disposition and remaining task

Constructed: `eightfold-weil-filter`, at its stated class-level/cycle-preserving scope. The same sixfold, original alpha, candidate O=P6 and three unresolved research obligations are retained. No nonzero algebraic W8 class, alpha representative, all-cycle annihilation theorem or Hodge verdict has been produced.

The next substantive step requires actual geometry: supply a non-tautological algebraic A-cycle or higher-Chern/sheaf construction with verified dimension-eight hypotheses and compute T, checking the opposite sector if maps are reordered. Alternatively seek a genuinely nonsplit construction directly on X. The retained sixfold split theorem still has the wrong dimension for A and the wrong discriminant for X; the filter does not repair its hypotheses.

Contract: `research/conjecture_net/contracts/hodge-eightfold-weil-filter.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_eightfold_weil_filter.py`.
Receipt: `research/voevodsky/results/hodge-eightfold-weil-filter-v1.json`.

    python research/voevodsky/checkers/check_hodge_eightfold_weil_filter.py

The polynomial, basis and finite-cycle controls are exact regressions for the written arguments. Torus exterior cohomology and algebraic cycle functoriality are standard imported facts, not proof-assistant certification. All-cycle nonexistence and algebraicity remain undecided by these artifacts.
