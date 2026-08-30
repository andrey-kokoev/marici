# The completed boundary resolution is linear except for one odd-port metric identification

## Correction after source rehydration

The odd incidence magnitude is already fixed. The source endpoint and ordered
history identities give

\[
j_\theta=\frac14S_{\mathrm{ord}},
\qquad
j_\theta\Omega=A,
\qquad
Bj_\theta=-\frac12H_K.
\]

Therefore there is no free scalar \(\eta\). Every statement below describing
its magnitude as unresolved should be read as a statement about the still
unproved quadratic representation theorem: the fixed operator
\(\frac14S_{\mathrm{ord}}\) must intertwine the Stieltjes Green form with the
completed theta-history form.

## Resolved wall channel

The relative constant wall and the completed theta Wronskian wall are related
by the source amplitude law

\[
-\mathbf1_{\partial}
=
-2w_\theta,
\qquad
w_\theta=
\begin{pmatrix}
\frac12\\
\frac12
\end{pmatrix}.
\]

With endpoint metric \(2I\), the theta wall has unit energy:

\[
\|w_\theta\|_{2I}^2=1.
\]

Thus the wall part of the completed-boundary resolution is fixed both
linearly and metrically. The coefficient \(M_\Phi\) in the theta convolution
acts only after this calibration.

## Resolved derivative-tail channel

The completed causal theta history factors exactly as

\[
H_\Phi
=
M_\Phi I+H_KD,
\]

where

\[
K(r)=\int_r^\infty\Phi(s)\,ds.
\]

On the zero-mode-reduced rapid core, the ordered port satisfies

\[
DS_{\mathrm{ord}}
=
S_{\mathrm{ord}}D
=
-2I.
\]

Consequently,

\[
(H_\Phi-M_\Phi I)S_{\mathrm{ord}}
=
-2H_K.
\]

The unbounded derivative tail is therefore converted into a bounded tail
convolution by a source-native ordered constructor.

This closes the linear odd kernel-synthesis arrow.

## Exact two-column frame

The completed theta traces are

\[
w_\theta=
\begin{pmatrix}
\frac12\\
\frac12
\end{pmatrix},
\qquad
j_\theta=
\begin{pmatrix}
\frac14\\
-\frac14
\end{pmatrix}.
\]

In the endpoint metric \(2I\),

\[
\langle w_\theta,j_\theta\rangle_{2I}=0,
\]

\[
\|w_\theta\|_{2I}^2=1,
\qquad
\|j_\theta\|_{2I}^2=\frac14.
\]

Therefore the completed boundary frame has no finite rank or radical defect.
Its only unequal scale is the quarter-energy odd column.

## Remaining incidence scalar

To compare the odd Wronskian column with the ordered derivative port, one
needs a source scalar or operator

\[
\eta:
\mathbb C j_\theta
\longrightarrow
\operatorname{ran}D
\]

such that the odd Green energy pulled back from the resolved tail agrees with
the endpoint energy.

In a rank-one reduction, the required equality has the form

\[
\frac14|\alpha|^2
=
\left\langle
\eta(\alpha j_\theta),
D_{\mathrm{tail}}
\eta(\alpha j_\theta)
\right\rangle.
\]

The sign of \(\eta\) is already fixed by the Wronskian orientation and
reflection. Its magnitude is not free: it must be derived from the
source connection/curvature identity.

This is the one surviving local metric identification.

## Why linear closure is insufficient

The identities

\[
-\mathbf1_{\partial}=-2w_\theta
\]

and

\[
(H_\Phi-M_\Phi I)S_{\mathrm{ord}}=-2H_K
\]

prove that the wall and odd histories belong to one linear constructor
system. They do not prove that the quadratic Green form on the bivariate
window boundary equals the completed theta-history form.

A rescaling of the odd incidence preserves every linear diagram while
changing the Schur return and its contraction margin.

Therefore the remaining theorem must be polarized.

## Polarized comparison target

Let \(Q_p^{\mathrm{pre}}\) be the already constructed bivariate-to-completed
linear comparison through ray transport, theta summation, and \(P_u\).
Let \(R_{\mathrm{lin}}\) apply the fixed wall map and the ordered tail
resolution.

The candidate full comparison is

\[
Q_p(\eta)=R_{\mathrm{lin}}\circ\eta\circ Q_p^{\mathrm{pre}}
\]

on the odd channel, together with the fixed wall map on the even channel.

The required theorem is

\[
\mathfrak G_{\mathrm{bi},p}(x,y)
=
\mathfrak G_{\mathrm{comp},p}
\bigl(Q_p(\eta)x,Q_p(\eta)y\bigr)
\]

for all \(x,y\) in the rapid finite-prime core.

Full polarization determines both the magnitude and the reciprocal adjoint
orientation of \(\eta\).

## Completion margin

If \(\eta_p\) is prime-dependent, finite nonzero values are insufficient.
Completion requires a frame bound

\[
0<c_-
\le
\eta_p^*D_{\mathrm{tail},p}\eta_p
\le
c_+<\infty
\]

in the source-normalized odd coordinate, uniformly over primes and compact
off-seam parameters.

The existing trace-class disagreement incidence and bounded tail resolvent
then make the global odd return trace class.

## Hostiles

1. Set \(\eta=2\) merely to compensate for the quarter-energy odd column.
2. Match the odd scalar energy but reverse the Wronskian sign.
3. Preserve all linear diagrams while rescaling \(\eta_p\to0\).
4. Prove the polarized identity only after scalar endpoint aggregation.
5. Absorb the wall mass into the ordered inverse and lose the zero mode.
6. Use the same metric on wall and odd columns without the source factor-two
   calibration.

## Verdict

The final completed-boundary resolution is almost entirely explicit:

- wall amplitude and metric are fixed;
- theta convolution splits into wall mass and derivative tail;
- the ordered port resolves the derivative tail exactly;
- the two Wronskian columns are orthogonal and nondegenerate.

The sole remaining local datum is the source-derived odd incidence magnitude
\(\eta\), determined by one fully polarized Green identity between the
bivariate window boundary and the resolved theta tail.
