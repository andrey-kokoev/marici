# Prior research closes autocorrelation faithfulness but not polarization

Date: 2026-09-08

## Completed faithful detector

Grothendieck's prior research constructs the continuous autocorrelation of a real completed source `f`:

\[
C(d)=\int_{\mathbb R}f(u)f(u+d)\,du
\]

and the analytic half-form

\[
A(z)=\frac{C(0)}2+
\int_0^\infty C(d)e^{zd}\,dd.
\]

On the boundary,

\[
2\operatorname{Re}A(it)=|X(it)|^2,
\]

so the positive-real theorem gives `Re A(z)>0` in the left half-plane.  Define the oriented current

\[
J(z)=A(z)-A(-z).
\]

Since

\[
X(z)X(-z)=A(z)+A(-z),
\]

at every zero of `X` one obtains

\[
\operatorname{Re}z<0
\Longrightarrow
\operatorname{Re}J(z)>0,
\]

\[
\operatorname{Re}z>0
\Longrightarrow
\operatorname{Re}J(z)<0.
\]

Thus the completed current is strictly faithful to radial displacement.  This does not require a uniform finite Gram lower bound.

## Relation to the DAG boundary proposal

The current `J` is precisely a transverse observable that survives scalar cancellation.  It supplies the target of a boundary map but not the map from the Xi zero-state.  The missing implication remains

\[
X(z)=0
\Longrightarrow
\operatorname{Re}J(z)=0.
\]

Without an independent modular/adelic polarization law, an off-seam zero produces a nonzero current rather than a contradiction.

The two-atom moving-seam calculation gives the same distinction algebraically: the relative current survives in the quotient by the scalar value ideal and detects imbalance, but no universal scalar-zero law kills it.

## Disposition

Prior research closes the positive detector and its infinite-source completion.  It leaves exactly the same boundary-map problem isolated by the DAG search: derive a source boundary law sending every completed theta zero-state to the zero normal-current class.  The detector cannot provide its own vanishing without circularity.

## Evidence

- `research/grothendieck/the-autocorrelation-half-form-is-strictly-radially-faithful-at-every-finite-source-zero.md`
- `research/grothendieck/the-continuous-autocorrelation-half-form-preserves-strict-radial-faithfulness-after-completion.md`
- `research/grothendieck/the-moving-seam-current-is-the-first-transverse-cokernel-port.md`
