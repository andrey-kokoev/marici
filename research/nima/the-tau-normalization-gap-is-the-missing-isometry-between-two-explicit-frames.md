# The tau normalization gap is the missing isometry between two explicit frames

## Two explicit two-channel frames

The remaining G1.1 normalization problem is not a lack of finite-dimensional
data.  Two exact frames already exist.

### Theta history frame

The normalized reciprocal theta plane is

\[
V_\theta=(e,o),
\qquad
e=\frac{\Phi}{\|\Phi\|_2},
\qquad
o=\frac{\Phi'}{\|\Phi'\|_2}.
\]

Its odd Volterra compression is

\[
V_\theta^*iTV_\theta
=i\tau_\theta
\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
\tau_\theta=-\frac{\|\Phi\|_2}{\|\Phi'\|_2}.
\]

### Half-density endpoint frame

The closed reciprocal traces have columns

\[
v_0=\begin{pmatrix}1/2\\1/2\end{pmatrix},
\qquad
v_1=\begin{pmatrix}1/4\\-1/4\end{pmatrix},
\]

with matrix

\[
T_{1/2}=\begin{pmatrix}1/2&1/4\\1/2&-1/4\end{pmatrix}
\]

and Gram

\[
T_{1/2}^*T_{1/2}
=\begin{pmatrix}1/2&0\\0&1/8\end{pmatrix}.
\]

Both frames are faithful and have fixed reciprocal orientation.

## Why their scalars cannot be equated directly

The theta columns are orthonormal in the relative history metric.  The
endpoint columns are orthogonal but have squared norms \(1/2\) and \(1/8\).
Thus the coordinate change between them is not unitary in the standard
coefficient norm.

The positive diagonal normalization that turns the endpoint frame into an
orthonormal frame is

\[
N=\operatorname{diag}(\sqrt2,2\sqrt2),
\]

because

\[
(T_{1/2}N)^*(T_{1/2}N)=I.
\]

However, inserting \(N\) is source-authorized only if the coefficient wall
metric is exactly the pullback endpoint metric.  If the coefficient basis has
another frozen Green normalization, the required isometry differs.

## Exact missing intertwiner

Let \(U\) denote the sought representation from the normalized coefficient
wall module into the theta history plane.  The endpoint trace theorem and theta
compression compose correctly only if

\[
\operatorname{Tr}_{1/2}U=T_{1/2}
\]

in the frozen coefficient basis and

\[
U^*U=G_{\rm coeff}
\]

for the source coefficient metric.

Equivalently, after choosing the endpoint pullback metric, one seeks a unitary
\(\widetilde U\) satisfying

\[
\operatorname{Tr}_{1/2}\widetilde U=T_{1/2}N.
\]

Then the ledger coefficient is

\[
\tau
\begin{pmatrix}0&-1\\1&0\end{pmatrix}
=
-i\,U^*iTU,
\]

and its scale is determined rather than fitted.

## Conditional endpoint-pullback value

If the source coefficient metric is declared to be exactly the endpoint
pullback and the normalized endpoint columns map respectively to \(e,o\), then
\(U=V_\theta\) in normalized coordinates and

\[
{\tau=\tau_\theta
=-\frac{\|\Phi\|_2}{\|\Phi'\|_2}.}
\]

The numerical scout gives approximately

\[
\tau\approx-0.312996101.
\]

This value is conditional on the metric identification, not merely on matching
parity and dimensions.

## Revised G1.1 frontier

The incidence-compression problem has reduced to one representation theorem:

> Prove that the exact half-density endpoint frame and the normalized theta
> history frame are related by the source coefficient Green isometry, with the
> frozen Fourier/reciprocal signs.

Once this is proved, \(\tau\) is the explicit norm ratio above (or its
source-scaled conjugate if a different coefficient metric is declared).  The
operator lower bound \(1/8\) is already independent of this finite frame
choice.

Until that isometry is constructed, G1.1 remains open at incidence
compression.  No RH conclusion is authorized.
