# Derived Gysin Class and the Weighted Route Cube

## Record

Date: 2026-08-13

Status: exact eight-point derived-selector theorem and exact formal localized
route-cube equations; global occurrence-decorated Pochhammer/Cousin
naturality remains conditional. Entry 75 computes the complete local
derived-Hom groups, proves the normalized degree-zero class is unique and
torsion-free, and identifies the remaining degree-one belt extension.

Entry 73 isolated forty strict cellular lifts from a nontransverse route
pentagon to a fixed-core square.  The apparent ambiguity is now resolved at
the correct categorical level:

\[
\boxed{
\text{no canonical strict map from existing data}
\quad\text{but}\quad
\text{one canonical oriented relative/Borel--Moore class}.
}
\]

At the same time, the fixed-core target has acquired its correct loaded chain
model.  It is not a rank-eight coefficient module copied over every cell of a
cube.  It is the tensor product of three weighted interval complexes.  The
eight occurrence terms are its degree-zero vertices, while the twelve edges,
six faces, and one cube are the homotopies and higher coherence relations
among them.

These two corrections fit together.  A physical Gysin operation should be a
derived correspondence whose class is canonical even when its strict
cellular representatives are not.

## Strict representatives versus the derived class

Let \(P\) be one of the eight nontransverse route pentagons and \(S\) its
fixed-core target square.  Support-compatible cellular maps \(P\to S\) have
the exact census

\[
40=20_{+}+20_{-},
\]

where the sign is the degree on

\[
H_2(P,\partial P)\longrightarrow H_2(S,\partial S).
\]

Requiring nonzero support on all four physical core-changing edges forces the
unique same-core scalar edge to collapse.  This removes most maps, but still
leaves four cyclic target origins for each normal orientation.  All four
origins rotate covariantly and close after the eight-step deck orbit.
Therefore neither physical support nor deck covariance chooses a strict
representative.

The relative statement is different.  Both open faces are oriented disks,
so

\[
C_*^{\mathrm{BM}}(P^\circ)
\simeq C_*(P,\partial P)
\simeq \mathbf Z[-2],
\]

\[
C_*^{\mathrm{BM}}(S^\circ)
\simeq C_*(S,\partial S)
\simeq \mathbf Z[-2].
\]

Every one of the twenty positive representatives induces the same map of
relative fundamental classes, and every negative representative induces its
negative.  The audit constructs chain homotopies for all

\[
2\cdot20\cdot20=800
\]

ordered pairs of equal degree.  The ordered normal line selects the positive
degree.  Hence

\[
\boxed{
[G_{P\to S}]
\in
\operatorname{Hom}_{D(\mathbf Z)}
\bigl(C_*(P,\partial P),C_*(S,\partial S)\bigr)
}
\]

is canonical even though a point-set map is not.

This is the precise sense in which the forty-fold ambiguity was a
presentation ambiguity rather than a physical ambiguity.

## The conditional Boolean representative

If the target square is additionally labelled by the partial-core word

\[
\varnothing,\quad D,\quad DE,\quad E,
\]

then the pentagon word

\[
\varnothing,\quad\varnothing,\quad D,\quad DE,\quad E
\]

has a unique positive quotient map: collapse the first, same-core edge and
preserve the remaining four labels.  In index notation the representative is

\[
[0,0,1,2,3].
\]

This is a useful bare carrier, but the qualification is essential.  The
present target occurrence facet has not yet been constructed as a
Boolean-labelled partial-core object.  Existing physical-edge data alone
leave four cyclic origins.

There is also a coefficient obstruction to treating the bare contraction as
the loaded map.  Along the scalar edge, the constructible coefficient span is

\[
\mathbf Z^5
\longleftarrow
\mathbf Z^4
\longrightarrow
\mathbf Z^5.
\]

Its cosheaf pushout has rank

\[
5+5-4=6,
\]

whereas a target-square vertex has rank five.  The extra rank-one direction
is the difference of the two exchanged endpoint labels.  Thus the contraction
requires one loaded Cousin counit or lower-face relation.

## The corrected fixed-core target

Fix a rank-two core \(Q=\{D,E\}\).  It cuts the octagon into three
quadrilateral regions.  For region \(r\), let its two scalar refinements be
\(d_{r0}\) and \(d_{r1}\), and define the weighted interval complex

\[
K_r^{\mathrm w}
=
\left[
R h_r
\xrightarrow{\,d\,}
R e_{r0}\oplus R e_{r1}
\right],
\]

\[
d h_r
=
X_{d_{r1}}e_{r1}
-
X_{d_{r0}}e_{r0}.
\]

The fixed-core loaded target is

\[
\boxed{
K_Q^{\mathrm w}
=
K_0^{\mathrm w}
\otimes_R
K_1^{\mathrm w}
\otimes_R
K_2^{\mathrm w}.
}
\]

Its degree ranks are

\[
(8,12,6,1),
\]

and it has twenty-seven generators in total.  The differential is the tensor
Koszul differential and satisfies

\[
d^2=0
\]

on every generator.

This forward-corrects the deliberately formal target in entry 73:

\[
\boxed{
\mathcal L_Q\otimes C_*(I^3)
\quad\text{is overlarge, while}\quad
K_Q^{\mathrm w}
\quad\text{is support-compatible}.
}
\]

The rank-eight occurrence module is the degree-zero vertex space of
\(K_Q^{\mathrm w}\), not a constant rank-eight stalk repeated over all
twenty-seven cube cells.

## One decomposable occurrence tensor

Set

\[
c_r
=
X_{d_{r0}}e_{r0}
+
X_{d_{r1}}e_{r1}.
\]

Over the localized symbolic ring, write

\[
u_d=q_d-1,
\qquad
\kappa_d=\frac{\beta}{u_d},
\qquad
\beta=2\pi i\alpha'.
\]

The rank-eight full-core occurrence coefficient is the polarization of one
decomposable tensor,

\[
\Omega_Q
=
-\kappa_D\kappa_E\,
c_0\otimes c_1\otimes c_2.
\]

For the representative core \(Q=\{03,05\}\), the four physical charts are
exactly the restrictions to

\[
P_+:x_2=1,\qquad
P_-:x_0=1,\qquad
S_+:x_2=0,\qquad
S_-:x_0=0.
\]

Each restriction has four occurrence terms.  Across the eight relevant
cores the audit checks 128 weighted terms and 32 deck-rotated chart
identities.

The remaining coordinate facets are not arbitrary additions.  They are the
two other restrictions of the same tensor:

\[
x_1=0,
\qquad
x_1=1.
\]

Thus the four physical sides, two caps, and top cube are parts of a single
weighted cubical object.

## The loaded scalar-edge counit

Let \(x=15\) and \(y=37\) be the two exchanged scalar labels on the
representative pentagon.  In the localized endpoint-tube complexes,

\[
d\ell_x=u_xe_x,
\qquad
d\ell_y=u_ye_y.
\]

The unique typed localized lower term is

\[
\boxed{
H_s
=
\frac{X_x}{u_x}\ell_x
-
\frac{X_y}{u_y}\ell_y.
}
\]

Its boundary is

\[
dH_s
=
X_xe_x-X_ye_y.
\]

This is exactly the one rank-one relation needed to turn the rank-six
cosheaf pushout into the rank-five target coefficient.  The supported
physical double-Gysin map kills both exchanged endpoint quotient lines, so

\[
G_{D,E}(dH_s)=0=d\,G_{D,E}(H_s).
\]

Thus \(H_s=X_xh_x^{\rm PC}-X_yh_y^{\rm PC}\) in the notation
\(h_e^{\rm PC}=\ell_e/u_e\) of entry 38.  These normal contractions must not
be confused with the regional weighted-cube edges \(h_r\).

This solves the coefficient equation formally after localization.  It does
not yet prove that \(H_s\) is a component of one natural transformation of
the complete occurrence-decorated constructible complex.  Entry 38 already
makes literal collars auxiliary and proves their independence for the
underlying undecorated Pochhammer/Cousin class; no preferred collar should be
requested here.

## Caps and cube are forced

Let \(B_Q\) be the weighted sum of the four physical side facets.  Solving the
weighted cubical boundary equations forces the two cap coefficients to be

\[
(1,1),
\]

and then forces the cube coherence coefficient to be

\[
1.
\]

Equivalently,

\[
B_Q+K_Q^-+K_Q^+
=
d\!\left(
-\kappa_D\kappa_E\,
h_0\otimes h_1\otimes h_2
\right).
\]

All six facets inherit their signs from the cubical boundary, and the two
orders of physical normal contraction differ by the expected Koszul sign:

\[
\iota_E\iota_D(D\wedge E)=+1,
\qquad
\iota_D\iota_E(D\wedge E)=-1.
\]

The cap and cube data therefore cease to be discretionary once the weighted
interval target is used.

## What is proved

Promote:

1. Existing support data determine one positive relative/Borel--Moore Gysin
   class, not a unique strict route map.
2. The four strict origins in the selected orientation are mutually
   chain-homotopic as maps of pairs and are deck covariant.
3. The correct target is the twenty-seven-generator weighted interval cube
   \(K_Q^{\mathrm w}\).
4. Every physical chart is a weighted coordinate-facet restriction of one
   decomposable full-core tensor.
5. The formal localized scalar-edge counit \(H_s\) supplies exactly the
   missing rank-one relation.
6. The two cap coefficients and the cube coherence coefficient are uniquely
   \(+1\).

Retain as conditional:

> A Boolean-labelled partial-core cofiber supplies a preferred strict
> cellular representative.

Retain as open:

> The formal localized equations assemble with the existing facewise
> Pochhammer/Cousin class to a global bivariant natural transformation on the
> occurrence-decorated constructible complex.

Reject:

> Occurrence support, physical-edge incidence, normal orientation, and deck
> covariance already select a unique point-set pentagon-to-square map.

Also reject:

> The fixed-core target is a constant rank-eight coefficient tensored with
> the full cube cell complex.

## Formula objective

The next theorem should not ask for a preferred cellular map.  It should
construct a derived bivariant kernel

\[
\boxed{
\mathscr G_Q^{\alpha'}
\in
\operatorname{RHom}\!\left(
\operatorname{PC}_{\alpha'}(\mathcal R_Q;\mathcal L),
K_Q^{\mathrm w}[-2]
\right),
}
\]

where \(\mathcal R_Q\) is the complete route-face envelope containing
\(P_\pm\), \(S_\pm\), their lower faces, and the source coherences
corresponding to both caps and the cube.

It must satisfy:

\[
d\,\mathscr G_Q^{\alpha'}
=
\mathscr G_Q^{\alpha'}d,
\]

\[
\operatorname{Res}_{D,E}\mathscr G_Q^{\alpha'}
=
-\kappa_D\kappa_E\,\operatorname{pol}_Q,
\]

\[
\mathscr G_{\rho Q}^{\alpha'}\rho
=
\rho\,\mathscr G_Q^{\alpha'}
\]

for the deck rotation \(\rho\), and its scalar-edge component must realize
the counit \(H_s\) above.

The point-set choices of collars, subdivisions, and strict face maps may vary.
The required invariant is the derived class of \(\mathscr G_Q^{\alpha'}\).

## Why this matters for \(\mathsf J\)

The eight-point obstruction was not nonzero curvature.  It was a category
error: asking a constructible, bivariant operation to be an edgewise
automorphism or a preferred strict cellular map.

The corrected object has:

- extension-by-zero scalar coefficients;
- relative/Borel--Moore face classes;
- weighted interval mapping cones;
- Gysin degree shifts and ordered normal lines;
- cap homotopies and a cube higher homotopy.

This is the first explicit local model of the homotopy-coherent
factorization data that an intrinsic scalar-derived half-object must carry.
If the global kernel \(\mathscr G_Q^{\alpha'}\) exists, the nontransverse
eight-point factorization square closes before applying the inverse scalar
pairing.  That is precisely the missing pre-pairing naturality required for
\(\mathsf J\) to be a genuine half-object rather than an amplitude
reconstruction device.

## Reproducible certificates

Run:

    rustfmt --check research/nima/check_filtered_gysin_selector.rs
    rustc --edition=2021 -D warnings -O research/nima/check_filtered_gysin_selector.rs -o "$env:TEMP\\marici-filtered-gysin.exe"
    & "$env:TEMP\\marici-filtered-gysin.exe"

    rustfmt --check research/nima/check_loaded_route_cube_gysin.rs
    rustc --edition=2021 -D warnings -O research/nima/check_loaded_route_cube_gysin.rs -o "$env:TEMP\\marici-loaded-route-cube.exe"
    & "$env:TEMP\\marici-loaded-route-cube.exe"

Certificate SHA-256 values:

    check_filtered_gysin_selector.rs
    1da3140e3b8d560d72766f64aba296f149b2bd38cb279dc5bab24524ee116229

    check_loaded_route_cube_gysin.rs
    f3489edc4e5017e4f39ecfcb9fc982e7af8c6234094ec22e219343d6661288ad

## Decision

The n=8 local result is now:

\[
\boxed{
\text{canonical oriented derived Gysin class}
+
\text{canonical weighted target cube}
+
\text{one formal localized Cousin counit}.
}
\]

What remains is a categorical comparison theorem rather than another
point-set choice: assemble the coefficient counit, chart maps, and higher
fillers into a global occurrence-decorated Pochhammer/Cousin natural
transformation.  The underlying face-tube class is already independent of
collars by entry 38.

## Internal dependencies

- Entry 38: facewise Pochhammer/Cousin symbols and the transverse comparison.
- Entries 70--72: coefficient Gysin, strict transport no-go, and constructible
  descent.
- Entry 73: occurrence-support cosheaf and the exact target cube.
- research/nima/check_filtered_gysin_selector.rs.
- research/nima/check_loaded_route_cube_gysin.rs.
