# Modular forcing may renormalize the bulk norm

## Correction from the exact mixed-sheet theorem

Packet 145 isolated the doubled forcing difference `F` and proposed the
singular gate

\[
 2\mathcal F=\partial_qJ_{\rm boundary}.
\]

That condition is sufficient but unnecessarily strong. The earlier exact
mixed-sheet calculation already proves that the physical alternating cross
polarization is a reflection coboundary:

\[
 \mathcal X(z,w)=(z+\bar w)\mathcal R(z,w).
\]

On the ordinary kernel diagonal `w=z`, the factor is

\[
 z+\bar z=2\Re z.
\]

Hence a source-local mixed term may legitimately survive in the bulk while
carrying the same horizontal spectral factor as the norm term. It should then
be moved to the left side as a correction of the completed energy, not forced
artificially into an endpoint antiderivative.

## Revised exact target

The admissible decomposition is

\[
 \boxed{
 2\mathcal F
 =\partial_qJ_{\rm boundary}
 +2\Re(z)\,\mathcal M,}
\]

where both `J_boundary` and the horizontal bulk correction `M` must be derived
from labelled Fourier--Tate sewing before assuming a zero.

Substitution into the doubled identity gives

\[
 2\Re(z)\bigl(\mathcal N+\mathcal M\bigr)
 =-\partial_q\bigl(J+J_{\rm boundary}\bigr)
\]

up to the sign convention used when defining `M`. The sign must be frozen by
the exact source expansion rather than chosen to make the corrected energy
positive.

Thus the RH-bearing object is the **completed bulk form**

\[
 \mathcal N_{\rm comp}=\mathcal N+\mathcal M,
\]

not the bare sum of tail norms.

## Why this is not a retreat to a fitted inequality

The horizontal divisibility is independently source-derived from the full
alternating sheet polarization. It is not obtained by dividing an arbitrary
residual by `Re(z)` after inspection. A valid construction must exhibit the
analytic two-variable coboundary before restriction to `w=z`:

\[
 \mathcal X(z,w)=(z+\bar w)\mathcal R(z,w).
\]

Only this stronger identity authorizes `R` as a bulk correction. An arbitrary
term vanishing on `Re(z)=0` does not.

## Correct residual

At finite cutoff, the hostile residual is now

\[
 \boxed{
 R_X
 =2\mathcal F_X
 -\partial_qJ_{{\rm boundary},X}
 -2\Re(z)\mathcal M_X.}
\]

The conservation route survives only if `R_X=0` as a labelled distribution,
not merely after scalar integration.

There are then two independent theorem gates:

1. **Exact modular decomposition:** `R_X=0` at every finite source cutoff and
   compatibly under completion.
2. **Orientation of the completed energy:** for every nonzero admissible
   zero-state,

\[
 0<\int_0^\infty\mathcal N_{\rm comp}\,dq<\infty.
\]

The second gate is not local primewise positivity. Prime two's negative
contribution belongs inside `M_X` and must be retained exactly.

## Relation to the earlier no-go theorem

The exact mixed-sheet result also proved that no constant local two-sheet
metric converts every cross term into the desired positive Green bulk. The
completed correction `M` must therefore arise from one of:

1. reflection-coboundary cancellation;
2. seam localization;
3. a source-derived coupled evolution.

An invented constant Clifford metric is already falsified.

## New singular question

The programme has not returned to vague positivity. It now asks:

\[
 \boxed{
 \text{Does the source-derived reflection quotient }\mathcal R
 \text{ complete the bare tail norm into a positive finite global energy?}}
\]

The forcing-current identity and the curvature programme meet at this exact
quotient. Earlier work identifies the transverse reflection jet with the
order-two logarithmic-curvature numerator, so the two routes are not
independent evidence.

## Present boundary

The two-variable coboundary factor is proved in the earlier packet. Its
identification with the forcing correction in the new rank-two boundary
system, its finite-cutoff label decomposition, and positivity of the completed
energy remain unproved.

