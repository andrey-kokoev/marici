# External research report: Schoen and corrected secant candidate

Advisory follow-up to the operator-supplied external literature report. Not a new validated net iteration. Contracts, immutable pins and research verdicts are unchanged.

## Independently checked here

Freshly downloaded primary PDFs:

- Schoen, https://www.numdam.org/article/CM_1988__65_1_3_0.pdf
- Markman survey v2, https://arxiv.org/pdf/2509.23403v2

Scratch PDFs and extracted text: `temp/hodge-external-leads/`.

### Schoen really has an eightfold cycle mechanism

Read Theorem 2.0, printed p11, and Corollary 3.1, printed p24, in the fresh Schoen text. The theorem assumes even primitive-character multiplicity h and a simple branch tuple (branch characters paired with their negatives). The unramified case satisfies simplicity. The corollary transfers the resulting algebraic determinant-character classes from a power of the curve to the primitive abelian factor.

Consequently an appropriate cyclic-quartic curve cover with primitive multiplicity eight supplies algebraic codimension-four determinant classes on its eight-dimensional primitive Prym. The source theorem is not restricted to dimension six. This licenses pursuing the construction after the full target identification and transfer hypotheses are checked; it does not identify our target with such a Prym.

For the balanced ramified example in the external report, a genus-four bottom with two fully ramified branch monodromies 1 and 3 gives:

    2g(C)-2 = 4*(2*4-2) + 2*(4-1) = 30,
    g(C)=16, g(C/<rho^2>)=8, primitive Prym dimension=8.

The top double cover has two ramification points. This is a concrete presentation problem different from the existing etale genus17/9/5 route. Actual period/lattice/K-equivariant isogeny matching and the polarization/cycle transfer must be supplied; matching dimensions and signatures is insufficient.

### The proposed secant twist correction passes an independent calculation

Markman v2, section12, PDF pp21-22, displays the twist by O(Theta), and claims membership in span(exp(sqrt(-d)*t), exp(-sqrt(-d)*t)). The extracted primary text agrees with the external report. This is an apparent discrepancy, not a verified author-issued erratum.

Let n=(d+9)/2, t=[Theta], and N=(d+9)(2d-1) be the stated number of partially normalized isolated nodes. Assume the stated generic incidence and partial-normalization geometry. On the ppav fourfold, t^4=24[point]. Inclusion-exclusion for the union of the n surface intersections uses:

- n surfaces, each with character (1-exp(-t))^2;
- n adjacent curve intersections, each with character (1-exp(-t))^3;
- n(n-3)/2 nonadjacent pair intersections of four divisors;
- n triple intersections of three consecutive surfaces, also intersections of four divisors.

Thus, before partial normalization,

    ch(O_Z)=n*t^2 - 2n*t^3 + n*(55-6n)*t^4/12.

Normalizing the N isolated ordinary double points adds N*t^4/24, so

    ch(nu_*O_Ztilde)=n*t^2 - 2n*t^3 + n*(18-n)*t^4/6.

For F_a=[O -> nu_*O_Ztilde] tensor O(a*Theta), with the rank-one K-class convention [O]-[nu_*O_Ztilde],

    ch_2(F_1)=(1/2-n)*t^2=-(d+8)*t^2/2.

That disagrees with the claimed secant plane's rank-one degree-two coefficient -d*t^2/2. Twisting instead by O(3*Theta) gives

    ch(F_3)=1+3t-d*t^2/2-d*t^3/2+d^2*t^4/24.

Indeed, if s=sqrt(-d), this equals

    ((1+3/s)/2)*exp(s*t) + ((1-3/s)/2)*exp(-s*t)

through degree four. An exact Fraction-arithmetic scratch calculation also checked d=3,5,9,13. These calculations check Chern-character arithmetic, not existence/deformation of the resulting secant transform.

For the Gaussian choice d=9: n=9, N=306, and

    ch(F_3)=1+3t-(9/2)t^2-(9/2)t^3+(27/8)t^4.

The candidate is a derived object; this calculation does not turn it into a locally free sheaf, establish properties of its Orlov transform, or prove semiregularity. Section12 explicitly leaves the proposed weaker criterion unchecked; Question11.4 is a question, not an available deformation theorem. A corrected character alone does not close either gap.

## Important already-resolved prerequisite

The suggestion to check integral Gaussian automorphisms is sound in general, but this is already addressed for our explicit Y2. The principal-model construction explicitly makes the enlarged lattice Gaussian-stable and keeps the polarization invariant. Its native i is an actual integral polarized order-four automorphism, not merely a rational field embedding. This does not construct a covering curve or identify a hypothetical deck action with it.

## External report leads still awaiting primary verification here

- Schoen's 1998 addendum: its precise correction and transfer hypotheses.
- Lange-Ortega arXiv:1902.00251: the stated ramified trigonal construction and branch-position hypotheses. If verified, its genus-eight trigonal curve must not be confused with the previously excluded genus-nine trigonal intermediate. Preservation of a polarized Prym does not automatically supply an order-four curve action.
- Donagi's tetragonal preservation theorem and any extra-action compatibility.
- The reported quartic-CM and quaternionic alternatives and their full theorem hypotheses.

The elementary endomorphism-algebra warning is independently clear under our recorded simplicity/End assumptions: End^0(X x E^2)=K x M_2(K), since X and E have no homomorphisms between them. A unital field embedding projects injectively into K, excluding a quartic field; similarly a unital embedding of a simple noncommutative quaternion algebra cannot project into K. This blocks retaining those larger actions on the target, not every possible correspondence through varieties with larger endomorphism algebras.

## Recommended execution

1. Verify and freeze the corrected d=9 secant construction's geometry and Chern character, then determine the actual obstruction maps. Do not invoke Question11.4 as a theorem.
2. Open a separate ramified genus16/8/4 cyclic-cover search with a precisely specified K-equivariant target-matching criterion.
3. Verify Lange-Ortega and its extra-action compatibility before using it to reparameterize that search.

No matched cover, new exceptional algebraic cycle, all-cycle obstruction or Hodge verdict has been obtained in this follow-up.
