# Entry 1230 — Orbit Discriminant Is Larger Than Five-Site Singular Support

## Reason for the audit

Entry 1226 computed discriminants of marked-wall orbit norms. Before assembling higher intersections, distinguish the discriminant of the polynomial family from the singular support of its total divisor.

## One-cut norm

For

\[
N_1=X^2-4R,
\]

one has

\[
\partial_RN_1=-4.
\]

Therefore the total orbit-norm divisor is smooth, including over the polynomial discriminant $R=0$. That locus describes ramification/nonreduced specialization of the orbit polynomial, not a singular total divisor.

## Two-cut norm

For

\[
N_2
=
X^4-2(R+S)X^2+(R-S)^2,
\]

the exact derivatives satisfy

\[
\partial_RN_2+partial_SN_2=-4X^2,
\]

\[
\partial_RN_2-partial_SN_2=4(R-S).
\]

Consequently the reduced Jacobian locus is

\[
\boxed{X=0,qquad R=S.}
\]

With $R_i=F_i/\det H$, the physical reduced singular support away from the Gram divisor is

\[
\boxed{X_A=0,qquad F_i=F_j.}
\]

## Typing correction

The larger polynomial discriminant

\[
R_iR_j(R_i-R_j)=0
\]

records ramified or nonreduced fibers under the orbit-forgetting projection. It is not by itself the support of a singular marked divisor.

Entries 1226–1227 remain valid with their stated projection/labelled-local meanings, but the higher-overlap frontier must be narrowed:

\[
\boxed{
\text{pair collision support}
=
\text{signed-energy wall }X_A=0
\cap
\text{root equality }F_i=F_j.
}
\]

Thus triple Čech overlaps cannot be inferred merely from $F_i=F_j=F_k$. The relevant source-labelled energy walls must intersect simultaneously.

## Classification

This refinement further weakens any carrier claim. The actual singular locus already includes a frozen marked/signed-energy section. No new carrier datum is introduced.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_orbit_norm_singular_support.rs`
- `research/benincasa/results/five-site-orbit-norm-singular-support.json`

## Next falsifier

Use the 20 source-labelled two-cut sections to enumerate actual simultaneous loci

\[
X_A=X_B=0,
\qquad
F_i=F_j=F_k,
\]

with the correct incidence labels. Compute only the nonempty strata and their higher Čech maps. Do not assemble the complete root-equality braid arrangement without the energy-wall incidence conditions.
