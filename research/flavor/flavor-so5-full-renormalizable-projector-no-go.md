# SO(5) full renormalizable projector no-go: WP741

## Question

Does the cubic invariant omitted in WP740 allow one symmetric-traceless
breaking field to produce a stable, isolated (3+1+1) vacuum and thereby
select the two singlet projectors?

## Admitted source domain

Let (Phi) be one real symmetric-traceless (5\times5) field. Its complete
renormalizable (SO(5))-invariant potential is

\[
V(\Phi)=-\frac{m^2}{2}\operatorname{tr}\Phi^2
+\frac{\mu}{3}\operatorname{tr}\Phi^3
+\frac{\lambda_1}{4}(\operatorname{tr}\Phi^2)^2
+\frac{\lambda_2}{4}\operatorname{tr}\Phi^4.
\]

No discrete symmetry is imposed. Thus this packet tests the full
renormalizable one-(14) source rather than the (Z_2)-even subfamily of
WP740.

## Complete stationary family

A candidate with stabilizer (SO(3)) has three repeated eigenvalues and two
distinct singlet eigenvalues. After a nonzero rescaling and an (SO(5))
rotation, write it as

\[
\Phi_* = \operatorname{diag}(1,1,1,t,-3-t).
\]

The three distinct eigenvalues are roots of the same cubic stationarity
polynomial. Comparing its root sum and pair sum fixes

\[
\mu=2\lambda_2,
\qquad
m^2=\lambda_1 S_2+\lambda_2(t^2+3t+3),
\]

where

\[
S_2=3+t^2+(t+3)^2.
\]

Restoring the repeated eigenvalue scale restores the corresponding powers of
that scale. The cubic coefficient therefore moves the candidate along a
continuous (t)-family; it does not by itself select one eigenvalue ratio.

## Exact Hessian obstruction

Define

\[
A=(t-1)(t+4),
\qquad
D=\lambda_2+2\lambda_1.
\]

The five symmetric-traceless shape modes in the repeated three-dimensional
eigenspace have quadratic coefficient

\[
c_{\mathrm{shape}}=-\lambda_2 A.
\]

The two remaining (SO(3))-invariant diagonal fluctuations are represented by

\[
H=\operatorname{diag}(x,x,x,y,-3x-y).
\]

Their Hessian has determinant

\[
\det M=6\lambda_2 D A(2t+3)^2,
\]

and leading principal minor

\[
M_{11}=6\lambda_2 A+9D(t+4)^2.
\]

For a strict local minimum, shape stability requires

\[
\lambda_2 A<0.
\]

If the two singlet modes were also positive, their determinant would be
positive. Away from the eigenvalue-degenerate point (t=-3/2), the determinant
formula and (lambda_2 A<0) then require

\[
D<0.
\]

Both terms in (M_{11}) are consequently negative. This contradicts the
positive leading-minor condition. The contradiction is global: it does not
depend on a scan, an interval choice, or the sign of (m^2).

The excluded boundaries do not repair the construction. At (t=1) or
(t=-4), a shape coefficient vanishes. At (t=-3/2), the two singlet
eigenvalues coincide and the singlet determinant vanishes. At
(lambda_2=0), the shape sector is flat.

## Smallest exact falsifier

The attempted point

\[
t=2,
\qquad
\lambda_1=0,
\qquad
\lambda_2=-1
\]

has positive shape coefficient (6) and positive singlet determinant (1764),
but its leading singlet minor is (-360). It is therefore a saddle despite
passing the two coarser tests.

## Disposition

The cubic invariant does not repair WP740. One renormalizable
symmetric-traceless (14) supplies neither a stable projector rigidifier nor
a selector. Every distinct (3+1+1) stationary orbit is unstable or
non-isolated.

This removes the smallest simple-group source before the portal magnitude,
RG-basin, threshold, and detector gates open. A successor must introduce a
source object independently required by dynamics or geometry and must change
the Hessian obstruction. Adding a coefficient solely because it stabilizes
the desired answer would be a degenerating shift, not a Deutschian
explanation.

The claim does not exclude multiple breaking fields, higher operators,
radiative effective potentials, or different representations. Any such
successor must still transport a labelled projector through thresholds into
independently calibrated physical16 readout channels.

Reproduce with
`uv run --with sympy python research/flavor/checkers/wp741_so5_full_renormalizable_projector_no_go.py`.

Generated result:
`results/wp741_so5_full_renormalizable_projector_no_go.json`.
