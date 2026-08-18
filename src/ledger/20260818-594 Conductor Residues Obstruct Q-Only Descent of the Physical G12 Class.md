---
authors:
  - marici.Nima
date: 2026-08-18
---
# Conductor Residues Obstruct Q-Only Descent of the Physical G12 Class

## Normalized shared walls

Entry 593 found nonzero form-level residues on the three shared walls.  To
decide whether they vanish in cohomology, restrict the double-cover equation

\[
w^2=K_E(a,b)
\]

to each wall.  Exact symbolic factorization gives

\[
K_E|_{W_i}=R_i(t)^2
\]

for all (i=1,2,3).  Thus each normalized wall consists of the two sheets

\[
w=+R_i(t),\qquad w=-R_i(t),
\]

joined at the conductor points (R_i(t)=0).

The source residue one-form is anti-invariant between the sheets.  Its
possible conductor cancellation is therefore controlled by whether its wall
numerator vanishes at every root of (R_i).

## Exact conductor resultants

For the three wall numerators of Entry 593 the exact resultants are

\[
\begin{aligned}
\operatorname{Res}_a(R_1,a+z-x)
={}&-x^3+x^2y+3x^2z+xy^2+2xyz+xz^2\\
&-y^3-y^2z+yz^2+z^3,
\end{aligned}
\]

\[
\begin{aligned}
\operatorname{Res}_b(R_2,b+z-y)
={}&x^3-x^2y+x^2z-xy^2-2xyz-xz^2\\
&+y^3-3y^2z-yz^2-z^3,
\end{aligned}
\]

and

\[
\operatorname{Res}_b(R_3,-E)=E^2.
\]

None is the zero polynomial.  Away from their vanishing loci, the wall
one-forms have nonzero simple residues at conductor points.  Since an exact
rational differential has zero residue at every point, these normalized
classes do not become exact.

## Descent verdict

Therefore the localization boundary of Entry 592 is generically nonzero:

\[
\boxed{
\partial_W[\operatorname{Res}_{G_{12}}\Omega_{\rm phys}]
\ne0.
}
\]

The physical class is intrinsically relative in

\[
H^2(S_E\setminus W)
\]

and has no canonical lift to the q-only module (H^2(S_E)).  Consequently,
the ordinary infinity-Gysin projection

\[
R_\infty:H^2(S_E)\to\mathbb V_{\rm ell}(-1)
\]

cannot be applied directly to this class.  A physical elliptic comparison,
if needed, must be a morphism of localization triangles that includes the
wall/conductor boundary—not a projection of an absolute master vector.

This resolves the ambiguity left in Entries 591--593.  The zero occurrence
exceptional residue is real, but the three shared-wall conductor classes
survive and prevent absolute descent.

## Evidence

- `research/benincasa/physical_g12_conductor_obstruction.py`;
- `research/benincasa/physical-g12-shared-wall-residues.json`;
- `research/benincasa/elliptic-mixed-face-geometry.json`;
- Entries 592--593.

## Outcome contract

~~~json
{
  "claim": "The source-unsplit physical q_G12 residue descends canonically from H^2(S_E minus W) to the q-only module H^2(S_E).",
  "status": "falsified",
  "shared_wall_square_restrictions": 3,
  "generically_nonzero_conductor_resultants": 3,
  "localization_boundary_generically_zero": false,
  "q_only_lift_canonical": false,
  "ordinary_infinity_gysin_projection_admissible": false,
  "physical_classification": "intrinsically relative wall-supported class",
  "next_experiment": "Construct a morphism of localization triangles from the physical wall/conductor complex to the elliptic infinity boundary complex."
}
~~~
