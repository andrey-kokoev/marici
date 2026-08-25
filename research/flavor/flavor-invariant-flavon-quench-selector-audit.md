# Invariant flavon-quench selector audit (WP123)

Owner: `marici.Figueiredo`.

## Bounded question

Does the smallest weak-basis-invariant symmetry-breaking completion of WP122
provide a genuine selector on the faithful flavor quotient, or only stabilize
an undetermined family of physical points?

Pre-objective process report: excitement `8/10`, confidence `5/10` that a
proper but incomplete selector exists, expected information gain `8/10`.
Confounds are the simplicity of polynomial potentials and the absence of a
validated microscopic flavon sector. These observations are non-evidential.

Frozen optionality snapshot: test one radial potential, two inequivalent
vacua on its minimum shell, the lowest invariant hierarchy deformation, and
the lowest invariant alignment deformation. A selector must descend under the
full weak-basis group and its coefficients must be fixed before flavor data.

## Admitted state domain and quotient

The candidate domain is the pair of complex matrix fields `(Phi_u,Phi_d)`.
Write

\[
R^2=\operatorname{Tr}(\Phi_u\Phi_u^\dagger)
   +\operatorname{Tr}(\Phi_d\Phi_d^\dagger).
\]

The faithful comparison is made after the full weak-basis groupoid, using
`physical16`; the measured-ten projection is not used for uniqueness. All
functionals below are trace words and therefore descend to the quotient.

## Minimal radial quench

Take a source action containing

\[
V_0=\frac{\lambda}{4}(R^2-v^2)^2,
\qquad \lambda>0,quad v^2>0,
\]

and suppose a source-timed quench makes this the post-quench potential. Its
minimum set is the proper shell `R^2=v^2`. The operation is therefore a
genuine **radial selector**, conditional on the action and quench: it removes
all other norms and stabilizes a nonzero matrix amplitude.

It does not select a physical flavor point. At `v^2=1`, consider squared
singular-value packets

\[
A:(1,0,0;0,0,0),
\qquad
B:(1/3,1/3,1/3;0,0,0).
\]

Both minimize `V_0`, but the weak-basis invariant

\[
Q_u=\operatorname{Tr}[(\Phi_u\Phi_u^\dagger)^2]
\]

equals `1` on `A` and `1/3` on `B`. They are physically inequivalent and are
separated already on the faithful quotient. Thus the radial shell has a
non-singleton physical fiber. This is not a measured-ten argument.

At a shell point the Hessian of `V_0` is `2 lambda X X^T`: it has one radial
massive direction and all tangent directions remain flat before additional
invariants are supplied. Gauge quotienting removes only authorized orbit
directions; it cannot identify the displayed pair because `Q_u` differs.

## Lowest invariant deformations

The source-authorized probe family available from a polynomial local action is
larger than the radial norm. At quartic order it includes

\[
Q_u=\operatorname{Tr}(H_u^2),\quad
Q_d=\operatorname{Tr}(H_d^2),\quad
C=\operatorname{Tr}(H_uH_d),
\qquad H_a=\Phi_a\Phi_a^\dagger .
\]

For fixed `Tr(H_u)=s`, positivity gives

\[
\frac{s^2}{3}\le Q_u\le s^2.
\]

A positive coefficient of `Q_u` favors equal singular values; a negative
coefficient favors the rank-one boundary, subject to global stability. Hence
this invariant can select hierarchy *extremes*, but neither sign generically
selects the observed intermediate hierarchy.

Likewise `C` is a genuine alignment functional. With fixed spectra, its
extrema favor ordered alignment or anti-alignment of eigenspaces. It is not a
texture phase and needs no reference port, but an observed CKM interior point
requires further invariant terms and independently fixed coefficients.

Therefore invariant polynomial geometry can supply real quotient selectors;
the earlier negative result applies to the isotropic radial source, not to all
flavon actions. What remains absent is source authority for the particular
invariant content and coefficients that would select the observed interior
point.

## Contextual partition and instrument gate

For the radial family, contextual equivalence is equality of `R^2`; its
minimum class is the whole shell and does not separate physical points. Adding
`Q_u,Q_d,C` refines the partition by hierarchy and relative alignment, but
the finite family is not asserted faithful on `physical16`.

Classification:

- radial quench: **selector and stabilizer**, but only of total norm;
- quartic trace probes: **physical separators and conditional selectors**;
- texture rigidifier: **no**;
- reference port: **not required**;
- physical instrument: **not established** beyond a hypothetical flavon
  potential, quench, and vacuum-to-Yukawa matching.

The smallest exact falsifier of point selection is the pair `A,B`: equal
`R^2`, zero radial potential, unequal `Q_u`.

## Descent and failure conditions

Every displayed trace word is invariant under the full weak-basis groupoid.
The construction fails descent if coefficients are attached to matrix entries,
texture zeros, or a preferred basis rather than invariant contractions. It
fails source authority if `lambda`, `v`, or quartic coefficients are obtained
from the flavor targets. It fails physical realization if no local field,
quench trigger, stable vacuum, and equivariant matching map are supplied.

## Disposition

WP123 finds the first proper selector in the WP120--WP123 chain: a radial
symmetry-breaking quench selects a nonzero norm shell on the physical quotient.
It does not select a distinguished physical point, hierarchy, or mixing
pattern. Additional trace invariants can refine the shell without reverting
to chart data, but their source and coefficients remain unvalidated. The
programme has therefore advanced from “no selector” to “conditional coarse
selector with an unresolved coefficient-and-instrument gate.”

Post-objective process report: excitement `8/10`, confidence `7/10` in the
bounded classification, realized information gain `9/10`. Raw delta: one
proper radial subfamily selected; one false point-selection claim eliminated;
two physically inequivalent minima exhibited; three invariant refinements
opened; no reference port introduced; the physical-instrument gate remains.
These ratings are non-evidential.

