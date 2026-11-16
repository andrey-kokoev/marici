# Ramsey two-bite matrix generator: exact projection-rectangle obstruction

Date: 2026-11-09

## Scope

This note tests the *coordinate carrier* from the previous parabolic quarter-turn construction against Lemma 4.1 of Harris–Hefty–Horn–King–Pfender, *A short proof that R(3,k)=Theta(k²/log k)*, arXiv:2609.01782v1 (2026), §4. The lemma states that, with high probability in their random construction, every K-set of final vertices has at least one coordinate projection of size at least `(1/2-epsilon) K`. The deterministic quarter-turn models previously checked only local-overlap bounds. This note derives an exact equivalent matrix property for the projection lemma and proves that the **previous source-generated carriers cannot satisfy it asymptotically**, independent of the choice of the source adjacency matrices.

The note proves no new Ramsey-number bound.

## 1. Exact rectangle criterion

Let W be a finite additive group of order m, let T be a set of s shifts, and define

    V_T = {(a,b) in W x W : b-a in T},      n = m*s.

The m-by-m bipartite incidence matrix is

    B_T[a,b] = 1[b-a in T].

Every row and column has s entries equal to one. Choose K<=n, theta in (0,1), and set t=ceil(theta*K)-1. Assume t<=m. Then the following are equivalent:

(A) Every K-element subset I of V_T satisfies

    max(|pi_R(I)|, |pi_B(I)|) >= theta*K.

(B) Every t-by-t submatrix of B_T contains fewer than K ones:

    max_{U,V subset W, |U|=|V|=t} 1_U^T B_T 1_V < K.

Proof: an offending I has both coordinate projections of cardinality <=t and lies entirely in U x V, where U and V can be padded to size t. Conversely, K different incidences in a t-by-t rectangle constitute an offending I. This equivalence is completely independent of which source graphs are lifted onto the two coordinate spaces.

An average over uniformly selected U,V of cardinality t gives

    E[# of incidences in U x V] = s*t^2/m.

Hence a necessary condition for (A) is

    s*t^2/m < K.

If this fails, no s-regular carrier with the same (m,s,K) can satisfy the projection lemma. This averaged bound is a necessary condition only, not sufficient.

## 2. Source-generated axis-cross carrier fails at arbitrary scale

The previous checker selected the first `r=floor(log(q)^2)` nonzero orbits of the quarter-turn `-rho(x,y)=(y,-x)` in lexicographic order on `W=F_q^2`. For q>2r this is exactly

    T_cross = {(0,0)} union {(±j,0),(0,±j): 1<=j<=r}.

It has s=4r+1 shifts and is invariant under the quarter-turn. Take

    n=q^2*s,
    K=floor(10 sqrt(n log n)),
    a=ceil(sqrt(K/s)),
    U={0,...,a-1}^2 subset W.

There are at least K incidence vertices `(u,u+t)` with u in U and t in T_cross. Choose any K of them as I. For all sufficiently large q (so the shifted intervals do not wrap),

    |pi_R(I)| <= a^2,
    |pi_B(I)| <= |U+T_cross| = a^2 + 4*r*a.

Now `s ~ 4(log q)^2`, `K ~ 10q sqrt(s log n)`, and `a^2 ~ K/s`. In particular, `a` tends to infinity, `r/a` tends to zero, and

    a^2/K = o(1),      4*r*a/K = o(1).

Therefore both coordinate projections have size `o(K)` and violate the paper's required lower bound of approximately `K/2`. This is a **general asymptotic impossibility theorem for the axis-cross carrier**, independent of the source graph edge differences H.

## 3. The interval-parabola carrier has the same asymptotic defect

The alternative shift set

    T_par = {0} union ⋃_{j=1}^r orbit_{-rho}(j,j²)

contains at most `4r+1` shifts. Its representatives are in the integer square of coordinate radius `r²`; assume `q` large enough that reduction mod q does not wrap the relevant box. Using the same U and I,

    |pi_B(I)| <= |U+T_par| <= (a+2*r²)^2.

Since `r²/a -> 0` and `a²/K -> 0`, this is also `o(K)`. The issue is the concentrated location of the selected shifts, not the parabola source's triangle-free or bounded-codegree properties.

## 4. Finite exact checks

Use q=1013 (prime, 1013=2 mod 3), r=47, s=189, m=1,026,169, n=193,945,941 and K=608,365. With epsilon=0.001, t=303,574.

- Average incidence count of a t-by-t rectangle: 16,973,525.5956, already above K. Thus **every** 189-regular carrier with these parameters fails the projection lemma; this q is still pre-asymptotic for this particular proof criterion.
- A concrete K-element set drawn from the 57-by-57 source square has 3,219 red-coordinate values.
- Exact blue-coordinate projection cardinality for `T_cross`: **13,905**.
- Exact blue-coordinate projection cardinality for `T_par`: **246,516**.

The latter two are strictly less than t but do not, on their own, distinguish a defective carrier from a good one at these parameters, because the averaging obstruction defeats all carriers.

To separate the carrier defect from the pre-asymptotic averaging obstruction, choose q=1,000,037, r=190, s=761, m=1,000,074,001,369, n=761,056,315,041,809, K=1,614,873,030, t=805,821,641.

- Average t-by-t rectangle incidences: about 494,117,656, below K, so averaging alone no longer prohibits success.
- The explicit axis-cross source square has only a²=2,122,849 red-coordinate values and at most a²+4ra=3,230,169 blue-coordinate values, where a=1457. Both are far below t.

This demonstrates an explicit intrinsic failure of the axis-cross geometry in a parameter range where the universal averaging obstruction has gone away. The large graph is not materialized; these are exact cardinality bounds.

## 5. Correct next target

Before changing the source-graph difference set H or optimizing the pair-loss expression, replace the carrier T. The necessary property is the **no-dense-small-rectangles condition** for B_T in §1. In additive language, full-fiber selections already require roughly linear sumset growth:

    |U+T| >= theta*K

whenever `s|U| >= K` and `|U| < theta*K`, though this condition by itself is only necessary, not sufficient for all K-edge selections.

An algebraic candidate is to select the quarter-turn orbits of parabola parameters dispersed throughout F_q, rather than the first consecutive parameter values. Initial finite tests show that changing the parameter distribution materially changes source-square projection growth, but they do not certify the all-submatrix condition; at q=1013 the averaging obstruction makes certification impossible for **any** T.

The next mathematical question is to construct a quarter-turn-invariant T with provably small densest t-by-t submatrix, then independently derive the paper's global pair-loss bound for the lifted source matrices. Passing the local common-neighbor checks alone does not address either requirement.

## Reproduction

    python /mnt/data/check_ramsey_coordinate_rectangle_obstruction.py

Sources: uploaded arXiv:2609.01782v1, §4, Lemma 4.1; preceding research note `ramsey_parabolic_quarter_turn_transverse_sources_2026-11-09.md` and checker `check_ramsey_parabolic_quarter_turn.py`.

## 6. Stronger necessary geometry: no three collinear shifts

**Three-shift line obstruction.** Suppose W=F_q² and T contains three distinct points t0,t1,t2 on one affine line t0+L, where L is a one-dimensional vector subspace. Let t=ceil(theta*K)-1. Put ℓ=floor(t/q). If `3 ℓ q >= K`, take U to be the union of ℓ distinct cosets of L, and take V=U+t0. Then |U|=|V|=ℓq<=t, but **every u in U gives three distinct incidences into V**:

    (u,u+t0), (u,u+t1), (u,u+t2).

Hence `1_U^T B_T 1_V >= 3ℓq >= K`, violating the projection lemma. This obstruction is independent of the source graphs and their triangle deletion.

The earlier shift sets, including the versions with dispersed parabola parameters, were constructed as `T={0} union a collection of complete quarter-turn orbits`. If a nonzero v is present, so is -v, because a half-turn is negation. Therefore **0,v,-v always form a collinear triple**. No choice of parameter distribution in that construction can satisfy the projection lemma at the paper's eventual scales. This is an unconditional failure of that *carrier family*, not an impossibility result for all quarter-turn carriers.

Exact instances:

| q | t | floor(t/q)*q | guaranteed incidences from a three-shift line | K |
|---:|---:|---:|---:|---:|
| 1,013 | 303,574 | 302,887 | 908,661 | 608,365 |
| 1,000,037 | 805,821,641 | 805,029,785 | 2,415,089,355 | 1,614,873,030 |

The second row is already beyond the trivial averaging obstruction, yet its line submatrix still violates the bound.

## 7. Source-defined conic replacement, with no collinear triples

For odd prime q, the nondegenerate affine conic

    C_q = {(x,y) in F_q² : x²+y²=1}

contains no three collinear points and is preserved by the quarter-turn `rho(x,y)=(-y,x)`. It excludes zero. Thus selecting only complete four-orbits in `C_q` produces a quarter-turn-invariant shift set T that avoids the fatal line obstruction.

For q=1013, choose a primitive root g of F_q^× and a square root i of -1. Parametrize the conic by nonzero z in F_q:

    x=(z+z^-1)/2,    y=(z-z^-1)/(2i).

The quarter-turn acts as multiplication by a fourth root of unity on z. Choosing representatives z=g^j, j=0,...,46, and completing their quarter-turn orbits produces exactly 188 shifts on the conic. There are no collinear triples in this shift set by the line/conic intersection theorem.

For a source square U of 3,227 coordinates, the exact projected sumset size is 461,373; the paper's target at the corresponding K=606,669 and epsilon=0.001 is 302,727. Thus this particular concentrated U does **not** violate the projection lemma. Five other simple low-dimensional source-set templates were also screened in an exploratory run and did not reveal a violation for this conic carrier.

This is only a **candidate primitive**. At q=1013 the averaged rectangle bound itself shows that the *full* projection lemma still cannot hold, so passing one or several structured test sets is not a proof of sufficient dispersion. The conic removes the identified universal three-collinear obstruction and is appropriate for attempting a nontrivial all-rectangle theorem at asymptotic parameters.

The absence of the zero shift here is a condition on the *coordinate-pair incidence carrier*. It does not remove or reinterpret the two empty markers in the original R/G/0 symbolic row.

## Revised research target

Prove or disprove the *densest-small-rectangle condition* for a source-generated, quarter-turn-invariant cap-like shift carrier with no zero shift. A conic-orbit family provides the first explicit candidate satisfying the necessary no-three-collinear condition. Independently require the paper's global pair-loss estimate for the source adjacency graphs. Neither property follows merely from quarter-turn invariance or low pairwise neighborhood overlap.
