# Global iteration 13 (new series 3/10): smooth determinantal witness reduction

## Result

On the same fixed sixfold X, the following existence statements are equivalent:

1. alpha is algebraic.
2. Some rank-two reflexive sheaf F has nonzero P6 kappa3(F).
3. Some smooth codimension-three subvariety D of X has nonzero P6[D].

A smooth D may have several disjoint components; a component with nonzero projection suffices. The equivalence does not assert that any of these objects exists. It follows from a genuine generic-section construction from a **supplied** bundle witness, not from declaring an arbitrary Hodge tensor to be a bundle.

For any rank-two reflexive F there is also the rational Chow identity

    c3(F)=ch3(Ext1(F,O_X))=2 kappa3(F).

The right hand side is half the effective codimension-three singularity cycle, with its generic lengths. Singularities confined to codimension at least four cannot supply third normalized data. This gives a precise geometric target for the singular sheaf route left open previously.

## 1. From a supplied bundle to a rank-two reflexive quotient

The existing resolution argument gives alpha algebraic iff some algebraic bundle G of rank n has w=P6 kappa3(G) nonzero. The preceding locally free rank bound gives n>=3.

Choose m sufficiently large that G(m)=G tensor L0^m is globally generated, where c1(L0)=E_X. This uses standard Serre global generation. Choose n-2 general global sections and consider

    phi:O_X^(n-2) -> G(m),
    F=coker(phi).

At each point, evaluation of the parameter space of sections onto the fiber matrix space is surjective. The first rank-drop stratum, rank at most n-3, has expected codimension

    (n-(n-3))*((n-2)-(n-3))=3.

The next stratum, rank at most n-4, has codimension

    (n-(n-4))*((n-2)-(n-4))=8.

For n=3 the next stratum is absent. Otherwise 8 is greater than dim X=6, so the general map avoids it. Generic determinantal transversality/Bertini in characteristic zero makes the first locus D smooth of pure codimension three, or empty. One can see the needed open parameter set from the smooth universal exact-rank stratum, the deeper-locus incidence dimension bound, and properness of X. This is not an assertion that arbitrary sections are transverse or that a non-globally-generated bundle has this property.

The map is injective as a sheaf map because it is injective generically and its source is locally free on the integral X. Off D its cokernel is a rank-two bundle. Near D invertible row/column operations reduce phi to an identity block and one column of three local functions cutting out D. These functions are a regular sequence. Thus F has local presentation O -> O^3 at D. Koszul exactness embeds its cokernel in a locally free sheaf, giving torsion-freeness. At a point of codimension c>=3 on D it has projective dimension one and depth c-1>=2. Hence F is S2 and reflexive. It is not locally free on D: its fiber requires three generators.

The construction supplies an actual algebraic F and smooth D whenever G is supplied; it supplies neither when the input G is missing. The dimension-six step matters. At dimension eight the second rank-drop stratum is no longer excluded by this argument.

## 2. Cycle class and preserved Weil component

The exact sequence and the triviality of its first term give

    c(F)=c(G(m)).

The Porteous formula at the expected codimension gives

    [D]=c3(G(m))=c3(F).

These characteristic/cycle identities hold in rational Chow. They do not truncate Chern classes above the rank of the singular quotient.

The third-Chern twist formula is

    c3(G(m))=c3(G)+(n-2)m E_X c2(G)
       +binomial(n-1,2)m^2 E_X^2 c1(G)
       +binomial(n,3)m^3 E_X^3.

P6 kills every displayed correction term in cohomology. Also P6 kappa3(G)=P6 c3(G)/2. For a rank-two coherent sheaf Newton's normalized expression is kappa3(F)=c3(F)/2, without assuming c3(F)=0. Consequently

    P6 kappa3(F)=w,
    P6[D]=2w.

If w is nonzero, D cannot be empty. This proves existence of the desired rank-two reflexive sheaf and smooth threefold conditional on a supplied bundle witness. The preservation statement concerns the projected cohomology component, not equality of full kappa3 or of projected Chow classes after twisting.

Conversely, a rank-two reflexive sheaf has algebraic characteristic classes on the smooth projective X, and a smooth D has an algebraic fundamental class. A nonzero Weil projection of either yields alpha by the existing rational inverse. This closes the existence equivalences, without choosing their truth value.

It does **not** show that every prescribed smooth threefold is the singular locus of such a quotient. The construction determines D from G and general sections, not from an arbitrarily imposed target cycle; global presentation/extension requirements cannot be skipped.

## 3. Why codimension-three singularities, rather than isolated ones, matter

Let F be any rank-two reflexive sheaf on the smooth sixfold. On its locally free locus the rank-two pairing gives

    F* = F tensor det(F)^-1.

Both sides are reflexive, so this isomorphism extends across the complement of codimension at least three. The determinant is an algebraic line bundle.

A reflexive sheaf is S2. Local Auslander--Buchsbaum over the regular local rings implies

    codim Supp Ext^i(F,O_X) >= i+2, i>=1.

In particular Ext1 is supported in codimension at least three; higher Ext sheaves begin in codimension four and cannot contribute to ch3. These support bounds, not an assumption that all higher Ext vanish, are sufficient.

In K-theory the derived dual is

    [RHom(F,O_X)]=[F*]-[Ext1]+[Ext2]-... .

Its Chern character changes the sign of each odd component. Normalize by exp(+c1(F)/2). The normalized character of F* is the same as that of F, by the determinant twist above, while the normalized derived-dual degree-three term is -kappa3(F). Lower components of Ext1 vanish and higher Ext have no degree-three part. Thus

    -kappa3(F)=kappa3(F)-ch3(Ext1),
    2 kappa3(F)=ch3(Ext1)=c3(F).

The leading character of a coherent sheaf supported in codimension at least three is its codimension-three fundamental cycle with nonnegative generic lengths. This proves the effective singularity-cycle interpretation. If the singular locus has codimension at least four, the cycle is zero and kappa3(F)=0. Isolated or curve singularities on this sixfold alone are therefore not a rank-two third-Chern witness route.

For the generic quotient in Section 1, Ext1 is a line bundle on the smooth D, locally O_D. Its leading class is exactly [D], with multiplicity one. No generic smoothness or rank-two determinant claim is imposed on an arbitrary higher-rank sheaf.

## 4. Actual determinantal control, and a normalization trap

Choose a sufficiently ample line bundle L, t=c1(L), and take a general map

    O_X^2 -> L^4.

The same codimension calculation gives a smooth nonempty threefold D and rank-two reflexive cokernel F. This is a maximal-minor presentation, not an assumption of three global equations: there are six two-by-two minors, although the smooth locus is locally a codimension-three complete intersection.

Its actual class and characters are

    [D]=c3(F)=4t^3,
    c1(F)=4t, c2(F)=6t^2,
    kappa3(F)=2t^3.

These are nonzero but entirely divisor-generated, so their Weil projections vanish. Nonemptiness follows from the nonzero ample class 4t^3. The existence construction uses generic sections and standard theorems; no numerical coefficients for sections are supplied.

The source L^4 has kappa3=0, whereas its quotient has kappa3=2t^3. Thus full normalized third classes are not preserved by quotienting out trivial sections. Only the projected identity of Section 2 is licensed. This also shows why the locally free Chern truncation is invalid for the rank-two quotient.

## 5. Do not demand a pure effective Weil representative

The fixed Hodge kernel is QE_X^3 plus W6, and E_X W6=0. Write c3(G)=a0 E_X^3+2w and c1(G)=a E_X, c2(G)=b E_X^2. The smooth degeneracy cycle above has class

    [D_m]=a(m) E_X^3+2w,
    a(m)=a0+(n-2)b m+binomial(n-1,2)a m^2+binomial(n,3)m^3.

The coefficient becomes positive and arbitrarily large for sufficiently large m. The Weil component remains fixed; the divisor background is not an error to be normalized away from the actual effective cycle.

Indeed any nonzero effective threefold has strictly positive E_X^3 degree, but every pure Weil class has degree zero. In the chosen normalization integral_X E_X^6=2160. Hence the positive test is a smooth D **not proportional to E_X^3**, not a smooth effective D with a pure nonzero Weil class. Algebraicity of alpha allows rational signed cycle combinations; it does not require an effective representative. The existing rational projector/inverse need not preserve effectivity.

This calculation does not assert effectivity of an arbitrary nonalgebraic Hodge class after adding a divisor power. It says what follows from an existing algebraic bundle source, which is still absent.

## Checks, disposition and next task

Contract: `research/conjecture_net/contracts/hodge-reflexive-rank-reduction.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_reflexive_rank_reduction.py`.
Receipt: `research/voevodsky/results/hodge-reflexive-rank-reduction-v1.json`.

    python research/voevodsky/checkers/check_hodge_reflexive_rank_reduction.py

Exact checks cover the stratum dimensions, rank-two duality polynomial, Chern twisting, preservation of projected third data and its factor two, the actual split-bundle control's class, primitive degree and complex orientation. Nonzero-Weil numerical probes are all labelled formal input only; they are not actual bundles. The general-section, Porteous, depth, reflexive extension and leading-character facts are standard imports justified in the written argument, not proof-assistant certification.

Constructed: the conditional geometric reduction and complete rank-two singularity criterion. Not constructed: a nonzero-Weil reflexive sheaf, smooth threefold or representative of alpha. The next search can focus on a smooth threefold with non-divisor cohomology, or a rank-two reflexive sheaf with a non-divisor codimension-three Ext1 cycle. Split-bundle determinantal controls and singularities confined to higher codimension cannot supply the missing component. No exhaustive literature claim or Hodge verdict is made; all three unrestricted research obligations remain open.
