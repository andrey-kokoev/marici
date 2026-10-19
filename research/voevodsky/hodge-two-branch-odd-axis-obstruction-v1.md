# Global iteration 38 (fourth series 7/10): two ramification points do not repair the odd-axis obstruction

## Result

The fixed (Y2,theta2) is not the **natural principally polarized Prym** of a smooth cyclic-quartic tower whose top double cover has exactly two branch points. No trigonal hypothesis is needed. In dimension8 this is necessarily the genus16/8/4 case with the two full order-four ramification points carrying opposite tangent characters.

The proof does not reuse the etale free-orbit argument without modification. It includes the fixed points and their local ramification indices. The same degree-three elliptic axis would give an equivariant degree-six map, but its fixed-fibre residues are impossible. Combined with iteration37, exact principal cyclic-quartic presentations with zero or two top-double branch points are excluded for this Y2.

This does not exclude arbitrary unpolarized K-isogenies, polarized isogenies with nonunit multiplier, higher-branch/differently polarized or generalized sources, or double-cover Pryms without the specified order-four curve lift. The actual auxiliary family still exists and its Schoen algebraicity result is unchanged.

## 1. Freshly verify the principal normalization in the ramified case

Mumford, *Prym Varieties I*, Corollary2 on printed p333/PDF p9 says that for zero or two branch points the restricted Jacobian polarization is twice the principal Prym polarization. The display was checked in a fresh rendering: it reads rho=2 lambda_Xi. The OCR omits that display, so we do not infer the multiplier from missing text.

The old complete primary PDF remains immutable. The new rendering and page extraction, with a source manifest pointing to that same PDF, are retained under `inputs/hodge-two-branch-odd-axis-v1/`. Thus for I:P->J(C),

    I*Theta_J=2Xi,

in the two-branch case as well as the etale one. This exact normalization is required for the adjoint degree below; no arbitrary repolarization is being identified with it.

Let rho have order4, h=rho^2, and f:C->D=C/<h> have exactly two branch points. If dim P(C/D)=8, Riemann-Hurwitz and dim P=g(C)-g(D) give g(C)=16, g(D)=8.

## 2. Exhaust the short curve orbits

The fixed locus of h consists of exactly two points. Let F be the number fixed by rho, and T the number of size-two orbits with stabilizer<h>. Then

    F+2T=2.

Every other point has a full orbit of length4. The only candidates are(F,T)=(2,0) or(0,1). Riemann-Hurwitz for C->B=C/<rho> gives

    30=4(2g(B)-2)+3F+2T.

For(2,0) this gives g(B)=4. For(0,1) it gives g(B)=9/2, impossible. Thus rho itself fixes both branch points p,q, and there are no size-two source orbits.

The cyclic-quartic local monodromies at p,q are each1 or3; their sum must vanish modulo4. They are therefore(1,3), up to reversing labels or generator. In characteristic zero a finite-order stabilizer acts faithfully on the local parameter. The tangent eigenvalues of rho at p,q are i and-i, in some order. In particular neither has tangent character-1 or+1.

This analysis is independent of a trigonal pencil or any existence construction. It applies to every smooth tower satisfying these branch and dimension hypotheses.

## 3. The actual target still forces a degree-six elliptic map

Iteration37 computed the entire elliptic-isotypic lattice of Y2. Its physical positive CM polarization is the actual product diag(2,3). Every polarized automorphism of Y2 preserves both axes, not just its native Gaussian automorphism. This proof is consumed freshly; no preservation assumption about a selected curve map is added.

Suppose the natural principal P(C/D) were Y2. The induced polarized automorphism rho_P has square minus identity, so its restriction u to the degree-three elliptic axis E is i or-i. The norm-adjoint construction, using I*Theta_J=2Xi just verified, gives

    phi:C->E, deg(phi)=2*3=6,
    phi(rho x)=A(phi(x)),  A(z)=u z+c.

The constant c accounts for the Abel-Prym basepoint. The affine automorphism A has order4 and exactly two fixed points t0,t1, since 1-u is a degree-two surjective elliptic isogeny. Its tangent eigenvalue is u at both fixed points.

We now analyze these two fibre divisors with the two actual source fixed points included.

## 4. Tangent compatibility supplies the missing local constraint

More generally let m=deg(phi)>0 for any nonconstant equivariant map of this type. Both p and q map to fixed points of A. At a source fixed point let e be the ramification index of phi, let rho act on its parameter by i^a, and let u=i^b. Here a,b are1 or3 modulo4. Comparing the first nonzero term of phi in local coordinates gives

    a*e = b mod4.

Choose labels with a_p=1, a_q=3. Then

    e_p=b mod4, e_q=3b mod4.

The two residues are odd and distinct. All other support points in either fixed target fibre occur in source orbits of length4, with equal multiplicities within each orbit. Therefore:

- If p and q map to different fixed target points, the equal fibre degree m would have to be b modulo4 at one fibre and3b modulo4 at the other. This is impossible.
- If they map to the same fixed target point, their total contribution is b+3b=0 modulo4. The other fixed target fibre contains no source fixed points and has only full length-four orbits. Both fibre degrees must be0 modulo4.

Consequently every such equivariant map must have degree divisible by4, and the two curve fixed points must map to the **same** elliptic fixed point. Degree6 is impossible. This gives the required principal-match contradiction.

Merely counting the two source fixed points is not sufficient. If tangent compatibility is omitted, a spurious degree-six profile puts one fixed point of multiplicity2 in each target fibre and fills each remaining degree4 by a free orbit. The local equation forbids those even ramification indices. The checker explicitly retains this hostile countercontrol.

Degree4 does pass the local residue test: the two fixed points may contribute1 and3 in one fibre, with one length-four orbit in the other. This is only a local control, not a constructed equivariant map or a matched cover. Repeated or ramified points elsewhere do not invalidate the argument, since multiplicity is constant along each orbit.

## 5. Consequences and still-executable research

Exact natural principal realizations of fixed Y2 by smooth cyclic-quartic towers in the standard zero- or two-top-double-branch cases are now excluded. The two-branch exclusion includes nontrigonal genus-eight intermediates; dropping the trigonal assumption does not repair this particular principal comparison.

It is not an assertion that all ramified Pryms or arbitrary isogenies are excluded. In higher-branch situations there can be additional short orbits and other polarization types; this proof does not admit those without a separate analysis. An etale or ramified double-cover Prym without a curve order-four lift is also outside the conclusion. No stronger theta-singularity statement has been proved.

For a hypothetical **K-equivariant isogeny** from a natural two-branch cyclic-quartic Prym to Y2, connected inverse-image elliptic axes are invariant under the source deck action. The same argument says their curve-map degrees2d are divisible by4, so their source theta degrees must both be even. They need not equal the target degrees2,3. This is a necessary isogeny-source gate, not a supplied pair of axes or a contradiction to every isogeny. In the specific auxiliary ramified-trigonal family the previous degree>=4 refinement still applies via its etale realization.

Next obtain actual K-isogeny/period/factor data with the correct source polarization; test a differently polarized or higher-branch/generalized source with explicit cycle transfers; change the auxiliary principal model transparently; or pursue direct cycles and justified deformation methods. Do not repeat exact principal matching of this Y2 in either standard cyclic-quartic case. The unrestricted research obligations remain open.

## Verification and trust

Contract: `research/conjecture_net/contracts/hodge-two-branch-odd-axis-obstruction.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_two_branch_odd_axis_obstruction.py`.
Receipt: `research/voevodsky/results/hodge-two-branch-odd-axis-obstruction-v1.json`.

The checker consumes the actual target/axis and auxiliary-family receipts freshly, verifies the retained Mumford primary bytes and new page rendering/extraction, exhausts the two short-orbit RH cases, and checks weighted fixed-fibre residues for both primitive tangent/target characters. Degree controls1..24 illustrate the universal residue proof; they are not an enumeration of actual maps or the basis of a universal inference. Written imports include normalization, Riemann-Hurwitz, cyclic monodromy, faithful tangent actions, polarized adjoints and equivariant local expansions. These are not proof-assistant-certified or independently reviewed by the arithmetic checker.

Iteration37 and immutable pins v1-v39 are preserved. Fixed X, alpha, Y2, determinant/denominator48 data, all four cycle-transfer channels and prior target censuses are unchanged. No exceptional target cycle, all-cycle theorem, alpha nonalgebraicity or Hodge verdict follows.
