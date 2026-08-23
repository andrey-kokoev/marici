# Source sewing is internal-boundary cancellation in a relative cycle

Date: 2026-08-23

## Sharpening

The common theta/cosmology phenomenon is better typed as relative-cycle
boundary cancellation than as an abstract kernel projection.

For a transported relative period, differentiation has the schematic form

\[
d\int_{\Gamma_b}\omega_b
=
\int_{\Gamma_b}\nabla\omega_b
+
\operatorname{ev}_{\partial\Gamma_b}(\iota_v\omega_b).
\]

If a source presentation decomposes

\[
\Gamma=\sum_i n_i\gamma_i,
\]

the labelled pieces can carry internal endpoint terms.  Sewing is the
source-defined reconstruction of \(\Gamma\); paired internal boundaries then
cancel.  The remaining Gauss--Manin defect is the evaluation on the genuine
external relative boundary.

## Theta realization

Grothendieck's oriented thimble packet proves that the physical observable is
a functional of the total relative class, not of a chosen thimble basis.
Under a Picard--Lefschetz mutation

\[
\gamma'=A\gamma,
\qquad n'=A^{-T}n,
\]

the total periods and quadratic cone readout are invariant.  Within a Stokes
chamber the thimble endpoints are decaying sectors or zeros of the completed
source.  Endpoint evaluation therefore vanishes and

\[
\partial_bM_{j,k}=\frac{i}{2}M_{j,k+1}
\]

is an exact Gauss--Manin identity.

The earlier modular cancellation of odd folded-label jets is another
presentation of the same discipline: sum to the completed source before
performing an operation that exposes artificial internal boundaries.

## Cosmology realization

The two lower occurrences are canonical as meromorphic de Rham and
endpoint-jet data, but their individual physical periods are not
source-canonical.  Their finite endpoint primitives are nonzero, so the
endpoint term cannot be discarded occurrence by occurrence.

The unsplit source combination supplies the canonical relative object.  Its
endpoint jets sew coefficientwise.  Existing exact data further suggest that
the two coordinate derivatives of the sewn class have identical transverse
residue, so their antisymmetric difference has no transverse boundary class.

## Shared calculus, sector-specific boundary condition

The shared structure is:

\[
\boxed{
\text{labelled chains}
\xrightarrow{\text{source sewing}}
\text{total relative class}
\xrightarrow{\text{Gauss--Manin}}
\text{period/readout},
}
\]

with the boundary term retained until source sewing.

The coefficient distinction is:

- theta: genuine endpoints kill the integrand, so the boundary defect is zero;
- cosmology: finite endpoint primitives are nonzero, so a sewn relative
  extension is required before the defect can cancel or descend.

Thus sewing does not generically erase information.  It removes internal
boundary artifacts while retaining any genuine external boundary class.

## Sharp falsifier

For each sector construct the chain map and verify

\[
\partial S=S\partial,
\qquad
\nabla S-S\nabla
=
\operatorname{ev}_{\partial_{\rm ext}}.
\]

The proposal fails if a supposedly internal boundary survives the
source-defined total cycle, or if a genuine external boundary is cancelled
without an independently supplied relative trivialization.

For the active cosmology branch, prove symbolically that the antisymmetric
sewn derivative has zero transverse endpoint class and separately compute its
remaining line-valued Gauss--Manin coefficient.

