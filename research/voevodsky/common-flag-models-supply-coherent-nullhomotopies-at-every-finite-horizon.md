# Common flag models supply coherent nullhomotopies at every finite horizon

## Result

The vertical coherence gate can be closed without assuming projectivity of completed ideals or choosing equivariant splittings.

For every finite flag of the actual strict source/observer modules, there are simultaneous two-term models for ALL its graded layers. The adjacent connecting classes lift to closed degree-one maps whose consecutive composites are STRICTLY ZERO. Zero nullhomotopies then give a coherent defining system at every finite length, including four-stage comparisons.

These models are natural under actual filtration-preserving maps. Horizon refinement has the already familiar bounded identity-complex kernel, and all refinement routes commute strictly. Corrected frame changes preserve the system. The horizontal consistency contraction is compatible after the required total-complex sign is inserted.

This constructs a coherent system, not a uniqueness theorem for nullhomotopies or all possible secondary operations. In particular it supplies a zero defining system; it does not assert that every Toda/Massey value or its indeterminacy vanishes.

Inputs:
- `adjacent-attachments-are-degree-one-transports-not-higher-yoneda-products.md`
- `consistency-complexes-retract-to-corrected-observers-while-discrepancies-kill-synchronized-classes.md`
- the admitted strict filtered source and corrected observer towers.

## 1. Correctly type the vertical compositions

For a surjective observer tower p_m:O_(m+1)->O_m, write K_m=ker(p_m). Its transition class has type

    tau_m:O_m -> K_m[1].

It cannot be composed directly with tau_(m+1), whose domain is O_(m+1). The intervening class comes instead from

    0 -> K_(m+1)
      -> ker(O_(m+2)->O_m)
      -> K_m -> 0.

Call it kappa_m:K_m->K_(m+1)[1]. The typed degree-two product is

    kappa_m[1] tau_m:O_m -> K_(m+1)[2].

Longer coherent comparisons use the analogous consecutive kernel extensions. Source ideal filtrations have the same structure, with their own actual graded modules. The following common flag construction handles both.

## 2. One common model for a finite flag

Take a finite decreasing strict flag

    T=F_0 superset F_1 superset ... superset F_(N+1)=0,
    G_i=F_i/F_(i+1).

All inclusions and quotients are the declared bounded strict maps. Put

    P_i=[F_(i+1) -> F_i], degrees -1,0,
    q_i:P_i -> G_i.

Each q_i is a strict quasi-isomorphism. Let e_i be the connecting class of

    0 -> G_(i+1) -> F_i/F_(i+2) -> G_i -> 0.

Define a closed degree-one map a_i:P_i->P_(i+1) by the SINGLE nonzero component

    a_i^(-1):F_(i+1) -> F_(i+1), identity.

Equivalently it is a chain map P_i->P_(i+1)[1]. The shifted target has differential minus the inclusion. Closure is direct: both terms of d a_i+a_i d vanish.

This map represents e_i. Indeed the quotient

    P_i -> [G_(i+1) -> F_i/F_(i+2)]

has kernel [F_(i+2) --identity--> F_(i+2)], with its bounded contraction. Following a_i by q_(i+1)[1] gives precisely the degree-minus-one quotient F_(i+1)->G_(i+1) of the usual extension roof.

Thus the representatives are derived connecting classes, not arbitrary maps between unrelated resolutions.

## 3. Strict zero products and all higher coherence choices

Every a_i maps degree -1 to degree zero. The next a_(i+1) is zero on degree zero. Therefore

    a_(i+1) a_i=0

as an actual degree-two map. No homotopy is needed to make this composite zero in the common models.

Choose the nullhomotopy of every consecutive pair to be zero. The four-stage coherence expression, consisting of a degree-one map composed with a chosen pair nullhomotopy minus the opposite such composite, is then literally zero. Choose its filling homotopy to be zero as well. The same statement holds inductively at every finite length: all defining equations have zero right-hand side.

Equivalently, on the direct sum of the P_i let A have a_i on its first off-diagonal and zero elsewhere. Then

    dA+Ad=0, A^2=0.

Taking all higher off-diagonal defining maps to be zero solves the full triangular defining-system equations. This describes the chosen coherent nullhomotopies without an ambiguous assertion about composing the raw tau_m.

The individual e_i can remain nonzero. Strictly zero pair composites do not make the individual identity-component maps nullhomotopic.

## 4. The models still reconstruct the actual filtered object

To check that this construction has not erased the extension data, form the finite complex

    L=direct_sum_i P_i, with differential D=d-A.

The minus sign is chosen so that its augmentation is the SUM of the actual inclusions:

    epsilon:L^0=direct_sum_i F_i -> F_0,
    epsilon((x_i))=sum_i inclusion_(F_i,F_0)(x_i).

On an element of F_(i+1) in degree -1, D has the inclusion into component i and minus the identity into component i+1. Hence epsilon D=0.

D is injective and its image is ker(epsilon). One can solve for a preimage starting at the last component and moving upwards: if y is in ker(epsilon), set x_(N-1)=-y_N and recursively x_(i-1)=inclusion(x_i)-y_i. The remaining first-component equation is exactly epsilon(y)=0. These are finite sums of the given bounded inclusions.

Thus L is strictly quasi-isomorphic to F_0. More importantly, the subcomplex with indices i>=k is strictly quasi-isomorphic to F_k by the same construction. The augmentation is therefore an actual filtered comparison; it recovers the entire given flag, not merely its abstract associated graded.

This finite reconstruction does not identify the original filtration with a split graded module. The internal differentials and off-diagonal identity components retain its nonsplit extensions. No filtered section of F_i->G_i is chosen.

## 5. Horizon refinements and their contractions are compatible

For a tower segment beginning at O_m and ending at O_H, take

    F_0^(H)=O_H,
    F_i^(H)=ker(O_H -> O_(m+i-1)), i>=1,

through F_(H-m+1)^(H)=0. Its grades are O_m, K_m, K_(m+1), and so forth. Its first adjacent class is tau_m, followed by the correctly typed kernel-extension classes.

Increase the horizon from H to H'>H while keeping any fixed earlier grade i. The actual restriction O_H'->O_H induces

    R_i:P_i^(H') -> P_i^(H).

Its kernel in BOTH degrees is Z=ker(O_H'->O_H), and the kernel differential is the identity. The contraction is bounded and canonical. Moreover

    R_(i+1)[1] a_i^(H')=a_i^(H) R_i.

Successive R maps compose exactly as the original tower restrictions. Maps between their identity-complex kernels have the same component in each degree, so the identity contractions commute with those maps as well.

All zero higher homotopies are consequently preserved by refinement. There is no residual four-stage comparison defect and no choice of an equivariant section hidden in this argument.

More generally, every actual filtration-preserving map induces a morphism of these models, commuting with a_i. This covers the supplied quotient/refinement diagrams in the source filtration as well as corrected frame isomorphisms in the observer tower.

The assertion is a compatible system at ALL FINITE horizons. It does not by itself identify a single norm-bounded infinite resolution or justify exchanging derived constructions with an unspecified completion or inverse limit.

## 6. Corrected frames and horizontal consistency

Corrected frame transports commute with tower restrictions. They therefore preserve the kernel flags in section 5 and induce isomorphisms of the P_i models. They commute with a_i, the refinements and the zero defining system. Raw uncorrected original/private observers are not inserted into this statement: their source-marked towers differ.

For the consistency complex, the reference projection r, synchronized inclusion i, and horizontal homotopy h=s all commute with tower restrictions. They restrict to every F_i and hence to every P_i. This proves compatibility before totalization.

There is an essential sign when both complex directions are retained. Write a for the vertical degree in P_i (a=-1 or 0), and b for horizontal consistency degree (b=0 or 1). Use

    D_tot=d_vertical+(-1)^a d_horizontal,
    H_tot=(-1)^a h_horizontal.

Then

    D_tot H_tot+H_tot D_tot=id-i r.

The mixed terms cancel because the ungraded source maps commute. The lifted a_i is a closed total degree-one map, and the compatibility with the contraction is the GRADED identity

    H_tot a_i+a_i H_tot=0,

not an unsigned commutation assertion. The synchronized inclusion and reference projection commute with a_i as degree-zero maps. Consecutive total a_i still compose to zero.

Thus the horizontal deformation retraction transports the chosen vertical defining system without adding hidden correction homotopies. In particular expressions a_(i+1) H_tot a_i vanish as well, by the anticommutation identity and the strict zero pair product.

## 7. What is now closed, and what remains outside the claim

Closed for the declared strict flags and corrected towers:
- typed representatives of consecutive connecting classes;
- compatible pair nullhomotopies;
- all finite higher coherence fillings in one defining system;
- strict compatibility with finite-horizon refinement and its contractions;
- corrected-frame naturality;
- compatibility with the horizontal consistency deformation retraction, including signs;
- recovery of the actual finite filtered object by the common models.

Not claimed:
- uniqueness of nullhomotopies or disappearance of Toda/Massey indeterminacy;
- vanishing of all conceivable secondary invariants of the source;
- new nonzero higher Ext degrees from the number of seams or frames;
- projectivity of completed ideals;
- a uniform all-depth norm or automatic summable-source realization.

There is therefore no missing higher homotopy required for this particular finite-horizon filtered comparison: an explicit coherent choice is supplied. A proposed different secondary invariant must specify its own defining data and distinguish it from this zero defining system.

## Verification

    uv run --with sympy python research/voevodsky/checkers/check_coherent_filtration_nullhomotopies.py

The exact checker verifies horizon composition, the identity-complex refinement kernels, four simultaneous graded models, strict zero adjacent products, five filtered-tail reconstructions, the total-complex differential and contraction signs, and graded anticommutation with the connecting representatives.

The all-horizon result is the natural common-flag construction above, not an extrapolation from the matrix sizes.
