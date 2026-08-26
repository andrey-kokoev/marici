# Common-clock CP normalization migration

Work package: WP591  
Owner: marici.Figueiredo

## Candidate architecture

WP590 isolates the freely variable CP scale in FDM-1. The strongest existing
normalization mechanism is WP467's common dilaton clock, which already removes
an independent electroweak/flavor relevant-scale fiber. Couple the CP modulus
to the same singlet through the positive source term

\[
V_L
={\kappa\over4}(s^2-\chi\sigma^2)^2,
\qquad \kappa>0,\quad\chi>0.
\]

This term is CP even, weak-basis scalar, and nonnegative. Its zero-energy shell
fixes \(s^2=\chi\sigma^2\). WP467 independently gives

\[
f^2=6y^2\sigma^2.
\]

Consequently the common dilation cancels:

\[
{s^2\over f^2}={\chi\over6y^2}.
\]

The architecture genuinely removes the independent dimensionful CP scale and
ties CP breaking to the flavor clock.

## Exact hostile deformation

The same declared symmetries, positivity, and source grammar allow every
positive \(\chi\) and \(y\). The selected dimensionless relation has

\[
{\partial\over\partial\chi}{s^2\over f^2}
={1\over6y^2},
\qquad
{\partial\over\partial y}{s^2\over f^2}
=-{\chi\over3y^3}.
\]

At \(y=1\), the equally typed choices \(\chi=1\) and \(\chi=4\) give
\(s^2/f^2=1/6\) and \(2/3\). Both preserve the common-clock mechanism,
CP symmetry, broken vacua, and the qualitative prediction \(J\ne0\).

Thus the free normalization has migrated from a dimensionful scale to the
dimensionless Wilson ratio \(\chi/y^2\). It has not been explained.

## Deutschian disposition

The coupled architecture improves FDM-1 in one real way: CP breaking and the
flavor scale are now relational outputs of one source clock. But its numerical
prediction remains easy to vary because changing \(\chi/y^2\) leaves the
explanatory mechanism intact.

The inherited qualitative prediction still passes all 1,210 fitted sheets.
No numerical ensemble test is authorized until a source theorem fixes
\(\chi/y^2\) independently of those sheets.

A progressive successor must derive that ratio from a load-bearing structure,
such as:

- a gauge or discrete symmetry fixing the operator normalization;
- an anomaly coefficient derived from an explicit UV charge packet;
- an isolated coupled fixed point with no relevant ratio deformation;
- a microscopic threshold matching theorem with frozen representation data.

Changing the derived ratio would then require changing or destroying that
structure, satisfying the hard-to-vary demand.

## Experimental criticism

After the ratio is fixed, the clean falsifier is a joint calibrated readout of
the CP invariant and the flavor clock in the same source model. The existing
CP readout and common-clock spectral calculations are separate objects and do
not yet constitute that instrument. A fit of \(\chi\) to the observed CP
magnitude would test nothing and is prohibited.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp591_common_clock_cp_normalization_migration.py

The generated result is
research/flavor/results/wp591_common_clock_cp_normalization_migration.json.
