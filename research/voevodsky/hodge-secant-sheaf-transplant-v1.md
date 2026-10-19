# Iteration 8: the retained secant-sheaf theorem cannot be transplanted to this isogeny class

## Result

We investigated an actual published higher-Chern construction, rather than specifying a desired cohomology tensor. The retained Markman source constructs a simple reflexive sheaf with a normalized third Chern component spanning a Weil direction, and proves algebraicity after its semiregularity/deformation argument. Its sixfold algebraicity theorem requires Hermitian discriminant **-1**.

The fixed X has discriminant class **-3** in Q*/Norm(Q(i)*). These are different. More strongly, the new fixed-point End^0(X)=Q(i) and NS(X)_Q=QE certificates imply:

> No polarization, quadratic reembedding or isogeny model of this fixed X can satisfy that discriminant -1 theorem's hypotheses.

Thus `secant-sheaf-transplant` is rejected at that scope. This is not a rejection of all sheaf constructions, an all-cycle annihilation theorem, or nonalgebraicity of alpha.

## 1. What the actual source supplies

Source: Eyal Markman, *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds*, arXiv:2502.03415v2, https://arxiv.org/pdf/2502.03415v2. We use the already retained PDF, not an unverified current revision.

| PDF page | precise role |
|---|---|
| 7 | Theorem 1.4.1: genus-three Jacobian ideal-secant construction; simple reflexive sheaf of rank 8d; normalized third Chern component and K-translates span the Weil directions alongside the divisor cube; specified deformation statements. |
| 9 | Theorem 1.5.1: algebraicity of Weil classes for sixfolds of discriminant -1, for any imaginary quadratic K. |
| 23–24 | Lemma 3.1.3 and proof: the specified oriented-plane construction has determinant class (-1)^n. The proof separates a rational square/field norm from this sign. |
| 88 | Proof of Theorem 1.5.1 uses that discriminant and semiregularity, then spreads within its component. The following Section 10 explicitly says its results are not used in the paper. |
| 89–90 | Igusa quartic and positive-invariant secants; Lemma 10.2.1 identifies the quadratic field and centralizer. |
| 91 | Example 10.2.2: rank-two bundles on a principally polarized threefold with w=2-d theta^2 have J(w)=16d^3 and K=Q(sqrt(-d)). |

The paper's source threefold is **not** our X; the resulting product with its dual is a sixfold, whose marked unitary deformation family is the relevant target of its argument. Simplicity of our X prevents literal product identification, but does not alone rule out deformation from a product. The discriminant argument below is what blocks this particular marked family even after deformation and isogeny workarounds.

The source supplies a genuine positive construction in its stated scope. It is not valid to infer its absence or failure merely because our sixfold is simple, nor to transfer its sheaf to our nonsplit component solely because both Hodge spaces have dimension three.

## 2. The arithmetic mismatch is a norm-class mismatch

In our fixed K-basis the Hermitian form is

    H=diag(1,1,1,-1,-1,-3),   det H=-3.

The ratio between our determinant and the theorem's representative is 3. It is not a norm from Q(i).

For a nonzero Gaussian rational z=(A+iB)/C, factor out the common power of 3 from A,B. If A,B are not both divisible by 3, A^2+B^2 is not divisible by 3: the nonzero squares modulo 3 are 1, and neither 1 nor 1+1 is zero. Hence v_3(A^2+B^2) is even. Subtracting 2v_3(C) shows

    v_3(Norm(z)) is even,
    v_3(3)=1.

So the two determinant classes differ in the quotient, not merely as displayed numbers. The checker runs 320 exact Gaussian rational parity controls; the valuation proof, not the finite list, supplies the universal conclusion.

The older audit already proved that H has K-Witt index two rather than three. We retain that result; it is not presented as a new achievement here. The new work is the rigidity under **all** the following target-changing workarounds, using the fixed-point endomorphism and Picard results established since that audit.

## 3. Why changing the polarization cannot repair it

Every polarization class on X is qE with q a positive rational, because NS_Q has rank one. Keeping the K action, the Hermitian form scales by q. Since its K-dimension is six,

    det(qH)=q^6 det(H),
    q^6=Norm(q^3).

Thus every polarization has the same determinant class. Changing elementary divisors or the integral polarization degree does not change this rational invariant.

Likewise a K-basis change S in GL_6(K) gives

    det(S* H S)=Norm(det S) det H.

The checker verifies 24 exact combinations of positive rational rescaling and genuinely Gaussian basis changes, including complex shears and non-real determinants. Resulting numerical determinants need not equal -3, but all keep odd 3-adic valuation relative to -1.

## 4. Why changing the K action or isogeny model cannot repair it

End^0(X)=Q(i), proved in iteration 6. An embedding of an imaginary quadratic field into this degree-two field must identify it with Q(i). The only embeddings of Q(i) are i->i and i->-i. There is no hidden second imaginary quadratic field available on this X.

Conjugating the action conjugates the Hermitian form, possibly with a global minus sign depending on the chosen imaginary-trace convention. Its rational determinant is unchanged by conjugation; a global sign changes the determinant by (-1)^6=1. Hence neither embedding changes the class.

Now let f:X->Y be any isogeny, without initially requiring K-linearity, and give Y any polarized Weil structure. The rational isogeny inverse transports End^0(Y) to End^0(X). Therefore its quadratic field and action become one of the two just discussed. Pull back its polarization: f*E_Y=qE for a positive rational q. These facts put the pulled-back Hermitian structure in the same determinant class. A choice of K-bases contributes only Norm(det S).

Thus **no such Y can have discriminant -1**. This treats arbitrary isogenies, not only the explicit endomorphisms already used in our projector. Finite-translation quotients of the type used in the source's sheaf descent are isogenies and cannot evade the obstruction. Twisting or normalizing a sheaf changes neither the base's rational endomorphism algebra nor the pulled-back polarization determinant.

A connected deformation with transported K action and polarization keeps this rational Hermitian local system and hence its determinant class. The source theorem's split marked component therefore cannot acquire our generic point by its stated deformation argument. We do not exclude paths in unmarked moduli, changing structures at special fibers, or a new deformation theorem with additional input; those would require new hypotheses and proofs.

## 5. The Igusa parameter is not the missing discriminant parameter

Example 10.2.2 uses

    ch(F)=2-d theta^2,   J(ch(F))=16d^3,
    K=Q(sqrt(-d)).

Setting d=3 does **not** address our discriminant -3: it changes the field to Q(sqrt(-3)), which cannot act on our generic X. To retain Q(i), positive integer d must be a square. For example d=4 gives K=Q(i), J=1024 and source secant-sheaf rank 32 (8d); d=9 and 16 give further same-field controls. None changes the discriminant -1 hypothesis of Theorem 1.5.1. The checker evaluates the Igusa value using the Pfaffian term of (10.1.1), not just the displayed 16d^3 formula: for these classes x0=2, all x_ij=y0=0 and y_14=y_25=y_36=2d. The paper normalizes the six-by-six Pfaffian of the standard symplectic matrix to +1, so it is the negative of the usual recursive Pfaffian in this size.

We do not assert that Lemma 3.1.3, whose oriented-plane hypothesis is explicit, classifies every conceivable positive-Igusa construction. Nor does Section 10 state an unconditional semiregularity/algebraicity theorem for every nonsplit sixfold. It does not license applying the retained -1 theorem here. A different construction would need its own range and deformation checks.

## 6. What this does not show

- It does not show alpha nonalgebraic. The earlier Z=0 elliptic-product fiber has the same nonsplit Hermitian form and algebraic Weil classes. Its larger endomorphism and Picard algebras also prevent use of our generic-point rigidity hypotheses there.
- It does not prove every algebraic cycle class tau=i invariant. The unrestricted anti-i higher-Chern/cycle search remains open.
- It does not exclude every reflexive or twisted sheaf, every secant construction, or every isogeny-based cycle argument. It rejects this retained theorem's applicability to our fixed isogeny class.
- A sheaf's normalized third Chern class being Hodge under some deformation is not a supplied sheaf or algebraic representative at our X.
- No publication, proof-assistant admission or global Hodge verdict follows from passing source/control checks.

## 7. Executable continuation and artifacts

The next search must either supply genuinely nonsplit hypotheses for an actual construction, or explicitly change dimension/ambient variety and prove a cycle-class transfer. One nonredundant calculation is to investigate stabilization by a CM elliptic surface to a split eightfold and an explicit reverse correspondence. A sixfold theorem cannot be applied to an eightfold; such a reduction would not itself prove algebraicity. No stabilization theorem or transfer is claimed here.

Contract: `research/conjecture_net/contracts/hodge-secant-sheaf-transplant.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_secant_sheaf_transplant.py`.
Receipt: `research/voevodsky/results/hodge-secant-sheaf-transplant-v1.json`.
Pinned page snapshot: `research/voevodsky/inputs/hodge-secant-transplant-v1/sources.json`.

    python research/voevodsky/checkers/check_hodge_secant_sheaf_transplant.py

All PDF searches used `pnpm pdf:search`. The existing local index reports repository-wide additions/removals, and the literal search `kappa` has no hit because of text encoding; neither absence is evidence of nonexistence. We extracted the cited pages directly from the retained, hashed PDF with pdftotext and read them. No exhaustive current-literature claim is made.

The old pins and source pages are not edited. This successor adds a bounded research rejection and preserves the same X, alpha and candidate map O. The genuine remaining positive criterion is still an actual algebraic middle class not fixed by i, with nonzero cohomology, not merely nonzero Chow.
