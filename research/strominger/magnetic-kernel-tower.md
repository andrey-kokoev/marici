# The magnetic kernel forms three pole-depth towers

Companion to `checkers/magnetic_kernel_tower_checks.py` (42/42, exit 0)
and `results/magnetic_kernel_tower.json`. This packet expands the smaller
grid of `magnetic-kernel.md` and supersedes only dimension interpretations
made outside that earlier packet's explicitly declared cutoff.

## Typed source space

The comparison is performed before reduction on the labelled 42-dimensional
Laurent space

\[
V=\operatorname{span}_{\mathbb Q}\{z^{-a}\bar z^m:
a\in\{0,2,4\},\ -9\le m\le4\}.
\]

The grades are \(g=2,3,4,5\). This is an engine-side finite-cutoff theorem;
no source-to-engine map or physical quotient is supplied.

## Three towers

For every tested grade and every admitted pole depth \(a=0,2,4\), define

\[
D_{g,a}=z^{-a}\bar z^{-(g+a-1)}.
\]

Exact symbolic computation gives

\[
\boxed{M_g(D_{g,a})=0,
\qquad g=2,3,4,5,\quad a=0,2,4.}
\]

The full expanded-grid kernels are

\[
\ker M_2=\operatorname{span}\{D_{2,0},D_{2,2},D_{2,4},
1-\bar z^{-2}\},
\]

\[
\ker M_g=\operatorname{span}\{D_{g,0},D_{g,2},D_{g,4}\},
\qquad g=3,4,5.
\]

Thus the exact kernel dimensions on this fixed source space are
\((4,3,3,3)\). Neighboring-exponent controls
\(z^{-2}\bar z^{-g}\) have nonzero magnetic readout at every tested grade.

## Rational line and two residue lines

The \(a=0\) tower is rational-exact. Verified potentials are

\[
\Phi_{g,0}=-\frac{c_g}{(1+u)^{g-1}},\qquad
(c_2,c_3,c_4,c_5)=(20,60,280,1680).
\]

The \(a=2\) and \(a=4\) towers are closed but not rational-exact. Their
\(z\)-components have nonzero opposite residues at
\(z=0,-1/\bar z\):

| grade | \(a=2\) residues | \(a=4\) residues |
|---|---:|---:|
| 2 | \((-60,60)\) | \((-120,120)\) |
| 3 | \((-1008,1008)\) | \((-3360,3360)\) |
| 4 | \((-20160,20160)\) | \((-100800,100800)\) |
| 5 | \((-475200,475200)\) | \((-3326400,3326400)\) |

The grade-2 exceptional line \(1-\bar z^{-2}\) is rational-exact with

\[
\Phi=-\frac{20(z+\bar z)}{1+u}.
\]

The individual residue test does **not** make these two directions independent
in rational cohomology: both residue pairs lie on the same two divisors.  Their
weighted difference is rational-exact at every audited grade.  Consequently
the rational-exact dimensions are \((3,2,2,2)\), and the ordinary quotient of
the closed kernel by rational-exact directions has dimension one at every
tested grade.

The earlier `(2,1,1,1)` inference is superseded.  One line per positive depth
exists only in a depth-labelled associated grade that forbids cross-depth
cancellation; it is not the ordinary rational de Rham quotient.

## What changed from the first census

The first packet used \(-4\le m\le4\). That cutoff included the \(a=2\)
residue line at grades 2 and 3 but excluded the \(a=4\) continuations
\(m=-(g+3)\). The expanded grid exposes them. The earlier ranks and kernels
remain correct on their named 27-dimensional source; they must not be
silently promoted to the larger source. This packet supplies the properly
typed comparison.

## Scope and open mechanism

The repeated formula strongly suggests an all-grade tower law, but grades
2 through 5 do not prove it. No symbolic-grade induction, global de Rham
classification, source descent, or physical gauge interpretation is claimed.
The symbolic theorem is now supplied by
`magnetic-tower-logarithmic-normal-form-proof.md`: all positive-depth towers
are rational representatives of one universal logarithmic class.

## Verification

`uv run --with sympy python -u research/strominger/checkers/magnetic_kernel_tower_checks.py`
passes 42/42. Groups: GRID (8), TOWER (12), RAT (4), RES (8), RATCOMB (4),
FAIL (4), EXC (2). All arithmetic, ranks, potentials, and residues are exact.
