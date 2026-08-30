# Full-source visible-port hostile pair: WP694

## Lift from the reduced propagator

WP693 showed that opposite mixing signs are equivalent within the reduced
visible-only two-point groupoid. They need not be equivalent as complete
source potentials. Consider the radial potential of WP685 and fix positive
target vacuum norms \(H^2,X^2\). Define two source branches by

\[
\begin{aligned}
\lambda_p^{(+)}&=p,&
\mu_{h,+}^2&=\lambda_hH^2+pX^2,&
\mu_{x,+}^2&=\lambda_xX^2+pH^2,\\
\lambda_p^{(-)}&=-p,&
\mu_{h,-}^2&=\lambda_hH^2-pX^2,&
\mu_{x,-}^2&=\lambda_xX^2-pH^2.
\end{aligned}
\]

Both branches have the same vacuum norms. Their radial Hessians obey

\[
M_-^2=S M_+^2S,
\qquad S=\operatorname{diag}(1,-1),
\]

so they have identical poles and every visible Higgs two-point resolvent.

## Source inequivalence

The mixed fourth derivative is

\[
\frac{\partial^4V}{\partial h^2\partial x^2}=2\lambda_p.
\]

It is unchanged by independent sign changes of the radial fields. The two
branches therefore differ as full source potentials even though the visible
two-point packet collapses them.

The exact rational witness

\[
\lambda_h=\lambda_x=3,
\quad p=1,
\quad H^2=X^2=1
\]

has positive quadratic masses on both branches and radial Hessian determinant
thirty-two. It is the smallest current hostile pair: identical visible
two-point data, inequivalent mixed quartic source coupling.

## Pipeline diagnosis

The first nonfaithful arrow is

complete radial source -> visible two-point propagator packet.

The visible Higgs port is a contextual readout and rigidifier, not a faithful
identifier of full source constructors. Repair requires a calibrated
observable sensitive to mixed-quartic or mixed-cubic interference, derived
from the same source and evaluated jointly with the two-point bins.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp694_full_source_visible_port_hostile_pair.py

Generated result: results/wp694_full_source_visible_port_hostile_pair.json.
