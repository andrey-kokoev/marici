# The exact half-density columns fix the source incidence and give tau minus theta L2 mass

## Reconciliation of the two frames

The half-density endpoint columns are not an abstract frame waiting to be
identified with the theta plane.  The existing twisted-history theorem derives
them directly from the unnormalized source vectors \(\Phi\) and \(\Phi'\):

\[
\operatorname{Tr}_{1/2}(\Phi)
=\begin{pmatrix}1/2\\1/2\end{pmatrix},
\]

\[
\operatorname{Tr}_{1/2}(\Phi')
=\begin{pmatrix}1/4\\-1/4\end{pmatrix}.
\]

Therefore the source incidence selected by that theorem is

\[
{
V_{\rm src}(e_0)=\Phi,
\qquad
V_{\rm src}(e_1)=\Phi'.
}
\]

Normalizing \(\Phi\) and \(\Phi'\) before compression changes the coefficient
metric and produces the different candidate
\(-\|\Phi\|_2/\|\Phi'\|_2\).  That normalized value is useful as a
unit-vector scout, but it is not the scalar in the frozen unnormalized
half-density trace frame.

## Exact compression

Let

\[
T=\frac{H-H^*}{2}.
\]

The relative Volterra identity gives

\[
\langle\Phi',T\Phi\rangle=-\|\Phi\|_2^2.
\]

Skew-adjointness gives

\[
\langle\Phi,T\Phi'\rangle=\|\Phi\|_2^2.
\]

Parity kills the diagonal entries.  Hence

\[
V_{\rm src}^*iTV_{\rm src}
=
\begin{pmatrix}
0&i\|\Phi\|_2^2\\
-i\|\Phi\|_2^2&0
\end{pmatrix}.
\]

Comparing with the ledger convention

\[
V^*iTV
=i\tau
\begin{pmatrix}0&-1\\1&0\end{pmatrix}
\]

gives

\[
{
\tau_{\rm src}=-\|\Phi\|_2^2.
}
\]

No unknown incidence scales \(\alpha,\beta\) remain in the exact twisted-theta
source frame.

## Numerical scout

The independent theta-series checker reports

\[
\|\Phi\|_2^2\approx0.31975181196.
\]

Thus

\[
\tau_{\rm src}\approx-0.31975181196.
\]

This numerical value is not needed for the symbolic identity and is not an
interval-certified estimate.

## Metric qualification

The source coefficient metric pulled back from the theta-history plane is

\[
G_{\rm src}
=V_{\rm src}^*V_{\rm src}
=
\begin{pmatrix}
\|\Phi\|_2^2&0\\
0&\|\Phi'\|_2^2
\end{pmatrix}.
\]

The endpoint trace Gram is

\[
G_{\rm end}
=
\begin{pmatrix}1/2&0\\0&1/8\end{pmatrix}.
\]

These need not be equal.  The trace is a bounded observation of the source
history plane, not an isometry in the standard endpoint Euclidean norm.
Demanding equality of these two Grams would impose an extra normalization not
present in the twisted-history theorem.

## G1.1 status

This closes incidence compression to a finite coefficient on the exact
source-derived theta frame:

\[
\tau=-\|\Phi\|_2^2<0.
\]

Together with the retained graph factorization and theta-mass lower bound, the
three analytic clauses of G1.1 now have explicit formulas on one relative
history carrier.

The remaining caution is arithmetic identification: prove that the ledger's
coefficient basis is indeed the twisted-theta source basis above through the
first-Adams/Euler incidence, with no additional prime loading before
compression.  If the ledger defines \(\tau\) before Euler loading, the formula
above is final; if it defines a loaded coefficient, that loading must be
applied explicitly afterward.

G1.1 should therefore not yet be marked closed in the publication ledger
without that basis-order check.  No RH conclusion is authorized.
