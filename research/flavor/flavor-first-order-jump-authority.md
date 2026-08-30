# First-order jump authority (WP357)

## Bounded question

Can a source-derived first-order transition select a finite nonzero flavor
geometry deformation without the near-critical control required by WP356?

Take the minimal stable even sextic grammar

\[
V(t)=\frac r2t^2+\frac u4t^4+\frac w6t^6,
\qquad u<0,\quad w>0.
\]

Writing \(q=t^2\), a nonzero stationary vacuum satisfies

\[
r+uq+wq^2=0.
\]

At coexistence with the symmetric vacuum, \(V(q)=V(0)=0\). Solving the two
conditions gives

\[
q_\star=-\frac{3u}{4w},
\qquad
r_\star=\frac{3u^2}{16w}.
\]

The transition therefore produces a discontinuous nonzero jump. It also
selects an exact coexistence relation among the coefficients.

## Residual authority

The jump magnitude retains the dimensionless source ratio \(u/w\):

\[
\frac{\partial q_\star}{\partial u}=-\frac{3}{4w},
\qquad
\frac{\partial q_\star}{\partial w}=\frac{3u}{4w^2}.
\]

Coexistence fixes \(r\) after \(u,w\) are supplied; it does not fix their
ratio. The hostile packets

\[
(r,u,w)=(1,-4,3),
\qquad
(r,u,w)=(2,-8,6)
\]

both satisfy coexistence and give \(q_\star=1\). They differ as normalized
source actions even though their classical vacuum readout agrees. Treating an
overall action rescaling as invisible would require an independently declared
zero-temperature classical quotient; it is not licensed for fluctuation or
thermal instruments.

## Disposition

Within the declared sextic grammar, coexistence is a source-derived phase
selector and the broken vacuum is rigidified to a sign pair. The finite jump
avoids critical susceptibility, but it is not a numerical selector: the jump
is carried by \(-u/w\). Nor is this a full `physical16` selector; it constrains
only the CP-geometry magnitude inherited from WP353.

The smallest exact falsifier is
\(\partial q_\star/\partial u=-3/(4w)\ne0\). The remaining instrument gate is
a normalized flavor action and threshold experiment that independently fixes
the quartic-to-sextic ratio and maps the jump into calibrated `physical16`
coordinates.

Run `uv run --with sympy python
research/flavor/checkers/wp357_first_order_jump_authority.py` to regenerate the
exact result.
