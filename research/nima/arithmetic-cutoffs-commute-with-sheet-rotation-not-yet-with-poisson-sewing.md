# Arithmetic cutoffs commute with sheet rotation, not yet with Poisson sewing

## Question

Does the arithmetic pro-Gram topology escape the norm-one log-window Fourier
hostile and thereby solve the completed-sewing descent problem?

## Exact arithmetic result

The arithmetic test carrier is the rapidly decaying prime-labelled space

\[
\mathcal S_{\mathbb P}
=\bigcap_{delta>0}\ell^2(\mathbb P,p^{2\delta}),
\]

duplicated over direct and reciprocal sheets. Its declared finite sheet action
is

\[
J_X=
\begin{pmatrix}
0&-I\\
I&0
\end{pmatrix}.
\]

If \(P_X\) cuts off the same prime labels on both sheets, then

\[
[P_X,J_X]=0
\]

exactly at every cutoff. Every saturated primitive and square seminorm is also
preserved by \(J_X\).

Thus the arithmetic reciprocal-sheet action passes the authorized
quasidiagonality gate with zero defect.

## Why this does not contradict the log-window no-go

The continuous hostile lives in \(L^2(\mathbb R,dq)\). It uses arbitrarily
long interval packets translated beyond a spatial log cutoff. Such packets
are not elements of the prime-labelled rapid-decay test carrier merely by
sharing a logarithmic coordinate.

More importantly, \(J_X\) is a local rotation between two copies of the same
prime-label space. The analytic Fourier–Poisson operator transforms a
continuous source presentation and crosses every interval cutoff with norm
one. These are differently typed operators.

Exact commutation of \(J_X\) therefore cannot be transported into a claim
about analytic Fourier–Poisson sewing.

## The interface is now the whole problem

Let \(I\) denote the still-missing source correspondence from the arithmetic
test rigging into the completed analytic boundary carrier. The required
naturality cell is

\[
I J\Longrightarrow\mathcal F I.
\]

If it is strict, its image must reconcile exact arithmetic cutoff commutation
with maximal analytic interval leakage. That is possible only if arithmetic
cutoff does not map to analytic interval cutoff, or if the image retains an
additional boundary component carrying the discrepancy.

The seam is the canonical candidate for that component. But the incidence and
its topology must be constructed; naming the seam does not supply the cell.

## DPC verdict

Resolved: exact cutoff compatibility of the reciprocal-sheet rotation on the
arithmetic pro-Gram carrier.

Rejected: inference of completed Fourier–Poisson descent from that exact
finite commutation.

Open: the operator-valued comparison cell between arithmetic sheet rotation
and analytic Fourier–Poisson sewing, including its seam-valued defect.

This is now the unique place where the two prior theorems can coexist without
contradiction.

## Finite falsifier

Any proposed interface that identifies arithmetic prime cutoff with analytic
log-window cutoff and also declares strict sewing naturality is impossible:
the arithmetic commutator is zero while the analytic incoming leakage norm is
one.

## Verification

The checker `check_arithmetic_vs_analytic_sewing_types.py` verifies exact
commutation of duplicated label cutoff with reciprocal-sheet rotation and
records the incompatible analytic norm-one gate established by the translated
interval certificate.

