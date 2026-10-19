# Global iteration48, fifth series7/10: two primes, native CM type and a completed local chart

## Result

The actual off-reflection control(lambda,a,b)=(2,6,2), which passed the necessary CM test at13, FAILS at17: its sevenfold complement has no geometric E_i factor there. Faithful Hom specialization excludes this control even up to complex Y3 isogeny. Its smooth source and primitive theta-four axis remain valid.

The new work also gives a native-character veto where an extra CM factor DOES exist in reduction. This is not mislabelled a CM-absence result, and does not assume a hypothetical unpolarized isogeny respects the native K action. The target's retained End-field and signature are essential.

A transverse Weierstrass chart admits two earlier uncertified cases. Combining full certificates at13 and17 then leaves the two necessary survivor classes a=197,214 mod221 inside the two-good-chart domain. A further22 classes remain uncertified, not excluded. The least-absolute lift of those TWO-GOOD-CHART survivors is a=-7. It gives a new actual theta-four source and passes both necessary opposite-type tests; no complex second axis is lifted.

## 1. Transverse special fibres at Weierstrass points

Keep W:y^2=P=x(x-1)(x-2), D=x^2-a*x+2, N=2(x^2-2), g=(y+N)/D and F_c=P-(cD-N)^2 for c=0,+1,-1. The preceding sufficient chart required gcd(F_c,P)=1. That condition is unnecessary when a special fibre meets a Weierstrass point transversely.

Suppose P(r)=0, cD(r)-N(r)=0, D(r) nonzero, and P'(r) nonzero in odd characteristic. On W, y is a local parameter, x-r has order2, and

    g-c = y/D(r) + O(y^2).

Thus g-c has order ONE, not two. Also F'_c(r)=P'(r) is a unit. A squarefree quartic F_c accounts for simple g-fibre points both here and away from P=0, where its derivative divides by2yD. The double cover V:w^2=g^3-g has a simple branch point, with its usual single normalized w=0 point. No point multiplicity is changed in the enumerator.

The new cases are(a,p)=(5,13) and(1,17). Their c=+1,-1 intersections are respectively x=(1,2) and x=(2,1). All four D(r), P'(r) and local slopes are recorded and verified. D still has two distinct roots disjoint from P, gcd(D,F_0)=1, and all F_c remain degree4 and squarefree. Four simple poles and twelve simple finite special-value points give branch degree16 and genus(V)=9; g(infinity)=2 is not special. The same argument works relatively over a DVR, so this is a GOOD reduction certificate, not just a singular affine equation with guessed genus. The cyclic-four lift T and its free translation extend at13,17, which are prime to the cover degrees.

The extended chart residues are:

    p13 regular: 0,2,5,6,7,8,10,11,12; uncertified:1,3,4,9;
    p17 regular: 0,1,2,4,6,7,8,9,10,11,13,14,15,16;
                uncertified:3,5,12.

An uncertified reduction is not a characteristic-zero exclusion. This extends the earlier sufficient chart; it does not reverse any earlier negative certificate.

## 2. Fresh counts and full polynomials

The new Rust program includes the historical generic field kernel unchanged. It enumerates all fourteen regular a cases at17 and the new a5 case at13 through ordinary degree5 and rho-Frobenius degree4:75 ordinary and60 twisted rows. The inherited eight F13 cases are separately rerun by the fresh predecessor checker, giving a total23 regular cases,115 ordinary and92 twisted rows in the combined certificate. At17, the generalized a4 specialization is cross-checked directly against the old denominator routines in every extension. Its full rational polynomial independently recovers the earlier p17 obstruction polynomial.

Independent digitwise Python arithmetic checks ordinary degrees1,2 and direct rho Frob_p fixed points in F_(p^4) for every new case. Poles use the exact identity P-(a-3)x^2=xD: all four are defined over F_(p^2), and are rational in odd degrees iff both a^2-8 and a-3 are nonzero squares. Infinity contributes the root count of6. No pole profile is copied from another a.

The native first-axis eigenvalues are beta13=3+2i at i=5 and beta17=1+4i at i=4. Four Gaussian moments reconstruct a1,...,a4, with a3 nonzero in every case. Full unitary reciprocity, Gaussian integrality and rational reciprocity are verified, and the unused fifth ordinary trace checks each reconstructed degree14 polynomial. Complete exact cyclotomic divisions and modular residual certificates cover all55 possible root-of-unity ratio orders, including1. All positive factors are accounted for by exact Gaussian linear division; no positive CM factor is inferred merely from a norm value.

For literal a6 at17 the Gaussian coefficients descending are

    [(1,0),(-1,0),(19,-12),(-51,4),(67,-200),
     (-1139,1088),(289,-1156),(-4913,19652)].

The rational coefficients descending are

    [1,-2,39,-140,741,-4446,12819,-88232,217923,-1284894,
     3640533,-11692940,55374423,-48275138,410338673].

Power traces through degree5 are2,-74,194,590,4002. The cyclotomic part is empty. This contradicts the second complex E_i factor required by Y3, by the same one-way faithful Hom specialization argument as before. The reduction's p13 extra factor did NOT lift.

## 3. Native-type specialization, not just rational CM multiplicity

At17 only a7 and a10 have an extra geometric E_i in the sevenfold complement; each has exactly one. Their complete positive norm parts are Phi_1^2 and Phi_4 respectively. In the native i-character polynomial their roots are

    a7: beta17, once (same type as the known first axis);
    a10: i*conjugate(beta17), once (opposite type).

All other regular cases have no extra CM factor, including the new transverse case a1. At13 the new transverse case a5 also has none; the only survivors remain a2 and a6, of opposite type as previously certified.

In the source i-character, an opposite-action CM elliptic curve has eigenvalue conjugate(beta_p), up to a root of unity after descent. An equivariant complex Hom would specialize faithfully after a finite field extension. Consequently its eigenvalue must satisfy alpha^m=conjugate(beta_p)^m. The exhaustive rational CM certificate leaves only the displayed same-type root for a7; beta_p/conjugate(beta_p) is in Q(i) but is NOT one of its roots of unity{1,-1,i,-i}. Therefore no opposite-action elliptic Hom exists over the geometric special fibre, or over C. The first known axis is same type and supplies no such Hom either. This argument is stronger than a finite-field multiplicity count and does not assert that the same-type positive factor lifts.

### Why this forbids even a non-K-linear Y3 isogeny

Use the retained fixed target data, not an End computation of the new source:

* Y3 is unpolarized-isogenous to X6 x E_i^2;
* X6 is simple, End^0(X6)=Q(i), and its K signature is(3,3);
* the actual source's native K signature is(4,4).

Suppose an unpolarized isogeny from the source to Y3 exists. Transport the SOURCE's native K action through it. Since there are no cross Homs between X6 and E_i, End^0(Y3)=Q(i) x M_2(Q(i)). On the simple sixfold the transported unital embedding K->End^0(X6)=Q(i) is identity or conjugation; either has signature(3,3). On the elliptic-isotypic surface, a K action has signatures(r,2-r), r=0,1,2. Adding to(3,3) must give(4,4), forcing(r,2-r)=(1,1). Hence a complex opposite-action elliptic subvariety MUST exist in the source. The specialization above forbids it for a7. Contradiction.

This does NOT assume that the hypothesized isogeny preserves the target's preselected K action; it constrains any transported action using the SIMPLE factor's exact End field. It would not be valid for an arbitrary sixfold End algebra or an unbalanced sixfold signature. Nor does it transfer a polarization norm obstruction from Y2 to Y3. The elementary signature enumeration is checked, while the isogeny-block and equivariant specialization implications are written mathematics using the fixed target data.

## 4. Algebraic residue boxes and a fully scoped CRT partition

At17, all regular residues except a10 are now excluded even up to complex Y3 isogeny: twelve by CM absence and a7 by the native-type/End-field argument. The theorem applies to algebraic integral(lambda,a,b) reducing to lambda2, those a residues, and b=2 or15=-2. These26 boxes have good models at that place. The new a5 box at13 likewise gives two additional exclusions(b=2 or11), beyond the predecessor's twelve. The sign-pair V isomorphism(p,w)->(-p,i*w) commutes with the native Gaussian action; it preserves the type statements, not merely the rational polynomial. As before arbitrary transcendental coefficients are outside this arithmetic specialization assertion.

On the fixed lambda2,b2 integral a-line, exhaust all221 residues. A negative certificate at either prime excludes the class even if the other prime's model is uncertified. The raw CM-absence rules exclude191 classes and leave four jointly regular CM-only survivors:

    41,58,197,214 mod221.

The same-type-only rule at17 removes an additional SIX classes that were not already CM-excluded, including joint survivors41,58. The final partition is

    197 excluded classes;
      2 jointly regular necessary survivors:197,214;
     22 classes not certified at both primes and not excluded by either rule.

The full disjoint arrays and their decision rule are retained. There are9*14=126 jointly regular classes;124 of these are excluded. The22 remaining uncertified classes are NOT folded into the exclusion count. Exact reflection geometry is never applied merely from a congruence. In particular the two survivor classes do NOT exhaust the complex source search. A positive CM/type test at two primes cannot lift an elliptic map or identify a fixed complex sixfold.

## 5. Next actual source and open gate

Among centered representatives of the two jointly certified survivor classes,197 gives a=-24 and214 gives a=-7. This is a height choice only inside that domain, not a global minimum over all sources. Exact Q-gcd tests for a=-7 verify the branch construction and four genuine simple poles. The retained T/translation, scalar tower and genus/primitivity argument give an actual smooth C17/D9/B5 and primitive theta-four axis, outside a=2lambda, a=2 and b=0. Its residues are a6 at13 and a10 at17, both of opposite arithmetic type.

Next either construct an actual opposite-character elliptic map on this source and compute its primitive theta degree/joint kernel, or use another certified good split prime to test a=-7 and the surviving parameter classes. No second complex axis, theta-six degree, End/simplicity of a residual sixfold, fixed-X6 periods or correspondence has been constructed. The fixed target, denominator768/four-channel transfer, other scalar parameters, uncertified charts, compactified sources, birational genus-five-image branch and direct cycles remain open.

Contract: `research/conjecture_net/contracts/hodge-off-reflection-joint-screen.v1.json`.
Checker/counter: `research/voevodsky/checkers/check_hodge_off_reflection_joint_screen.py`, `count_hodge_off_reflection_joint_screen.rs`.
Counts: `research/voevodsky/inputs/hodge-off-reflection-joint-screen-v1/counts.json`.

Trust: fresh finite-field enumeration with independent small counts; exact full polynomial, CM and native-type certificates; written relative smoothness, faithful equivariant-Hom specialization and End-field signature arguments; retained actual-source primitivity and fixed-target End data. Finite-field factor interpretation uses standard Tate semisimplicity. Not proof-assistant certification or independent review. Iteration47 and pins v1-v50 remain immutable. No target cycle, global family exclusion or Hodge verdict is supplied.
