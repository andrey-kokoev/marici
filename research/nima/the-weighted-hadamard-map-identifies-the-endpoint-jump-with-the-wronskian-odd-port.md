# The weighted Hadamard map identifies the endpoint jump with the Wronskian odd port

## Raw endpoint characters

In the two-trace endpoint plane with Euclidean metric, define

\[
v_w
=
\frac1{\sqrt2}
\begin{pmatrix}
1\\
1
\end{pmatrix},
\qquad
v_j
=
\frac1{\sqrt2}
\begin{pmatrix}
-1\\
1
\end{pmatrix}.
\]

These are the normalized reciprocal-even wall and reciprocal-odd jump
directions.

The complete endpoint pushforward is the Hadamard coordinate map, so it
retains both characters isometrically.

## Completed Wronskian frame

The completed theta endpoint columns are

\[
w_\theta
=
\begin{pmatrix}
\frac12\\
\frac12
\end{pmatrix},
\qquad
j_\theta
=
\begin{pmatrix}
\frac14\\
-\frac14
\end{pmatrix}.
\]

With endpoint metric \(2I\),

\[
\|w_\theta\|_{2I}=1.
\]

The normalized odd column is

\[
\widehat j_\theta
=
2j_\theta
=
\begin{pmatrix}
\frac12\\
-\frac12
\end{pmatrix},
\]

and

\[
\|\widehat j_\theta\|_{2I}=1.
\]

Moreover,

\[
w_\theta
=
\frac1{\sqrt2}v_w,
\qquad
\widehat j_\theta
=
-\frac1{\sqrt2}v_j.
\]

The factor \(1/\sqrt2\) is exactly compensated by the metric change from
\(I\) to \(2I\).

## Weighted Hadamard isometry

Define

\[
U_\partial v_w=w_\theta,
\qquad
U_\partial v_j=-\widehat j_\theta.
\]

Then

\[
\langle
U_\partial x,
U_\partial y
\rangle_{2I}
=
\langle x,y\rangle_I
\]

on the entire endpoint character plane.

Thus the complete endpoint pushforward and the completed Wronskian frame are
not merely rank-equivalent. They are exactly isometric after the source-fixed
metric transport.

## Odd normalization used by the Schur cell

The Schur incidence uses the unnormalized quarter-column

\[
j_\theta
=
\frac12\widehat j_\theta.
\]

Therefore the endpoint odd coordinate acquires the fixed amplitude \(1/2\)
before entering the auxiliary return, and its rank-one Schur projector carries
the factor

\[
|j_\theta\rangle\langle j_\theta|
=
\frac14
|\widehat j_\theta\rangle
\langle\widehat j_\theta|.
\]

In raw coordinate entries this is the previously derived factor \(1/16\).
No normalization remains adjustable.

## Ordered-history linking

The source identity

\[
j_\theta
=
\frac14S_{\mathrm{ord}}
\]

and the endpoint Stokes difference show that the Hadamard jump and Wronskian
odd column are two frames for the same reciprocal-odd history.

The additional identities

\[
j_\theta\Omega=A,
\qquad
Bj_\theta=-\frac12H_K
\]

transport that odd endpoint coordinate through curvature and completed tail
propagation.

Hence the linking triangle is closed:

\[
\text{endpoint jump}
\longrightarrow
\text{Wronskian quarter-column}
\longrightarrow
\text{ordered/tail odd history}.
\]

## Pushforward consequence

Primewise complete pushforward

\[
(t_-,t_+)
\longmapsto
(w,j)
\]

is faithful, and the retained \(j\) coordinate maps isometrically to the
normalized Wronskian odd line. The Schur constructor then applies its
source-fixed half-amplitude.

Therefore scalar Euler projection loses orientation only if it intentionally
discards \(j\). The typed two-port pushforward has no kernel and no
completion-frame decay on the incidence plane.

## Prime assembly

Apply \(U_\partial\) independently inside each valuation-prime fiber.
Because its singular values are exactly one in the transported metrics,

\[
\bigoplus_pU_{\partial,p}
\]

is an isometry with cutoff-independent inverse. Prime aggregation introduces
no new pushforward margin before scalar Euler observation.

## Remaining global gate

The pushforward-linking problem is now closed. The next unresolved issue is
terminal use of the two ports:

- whether the global evaluator retains both;
- whether coherent and disagreement outputs can cancel;
- whether the five global Green margins stay uniformly positive;
- whether the resulting spectral defect is exactly the completed zeta zero
  condition.

## Verdict

The endpoint jump, normalized Wronskian odd column, and ordered-history port
are one source-derived reciprocal-odd coordinate in three compatible frames.
The weighted Hadamard map identifies them isometrically.

Thus the complete prime pushforward is exactly faithful on the first Adams
incidence plane, with the Schur quarter-amplitude fixed rather than fitted.
