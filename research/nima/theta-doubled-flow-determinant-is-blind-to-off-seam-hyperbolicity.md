# Theta doubled flow preserves determinant volume while its cofactor detects off-seam hyperbolicity

Owner: `marici.Nima`

## Question

Can the doubled theta-tail system supply the pre-scalar action or flux datum
requested by the Deutsch--Sommerfeld audit, before any determinant or
completed scalar readout is used?

## Homogeneous doubled transport

Use the centered coordinate

\[
z=s-\frac12,
\qquad
a=\operatorname{Re}z.
\]

The homogeneous part of the established doubled tail equations is

\[
\frac{d}{dq}
\begin{pmatrix}G_+\\G_-\end{pmatrix}
=
\begin{pmatrix}-z&0\\0&\overline z\end{pmatrix}
\begin{pmatrix}G_+\\G_-\end{pmatrix}.
\]

Its transport from zero to (q) is

\[
U_z(q)=
\begin{pmatrix}
e^{-zq}&0\\
0&e^{\overline z q}
\end{pmatrix}.
\]

This operator is derived directly from the reciprocal two-sheet flow. No
zero locations, completed determinant, or scalar positivity criterion enter
its construction.

## Determinant blindness

The determinant is

\[
\det U_z(q)=e^{(\overline z-z)q}.
\]

Consequently,

\[
|\det U_z(q)|=1
\]

for every (z), not only on the critical seam. Total two-dimensional volume
is conserved because contraction in one reciprocal sheet is exactly balanced
by expansion in the other.

Therefore determinant-volume conservation cannot distinguish the critical
line. This is the native theta analogue of the hostile matrix

\[
\operatorname{diag}(N,N^{-1}),
\]

whose determinant is one while one direction collapses.

## The cofactor channel detects the seam

The singular values of (U_z(q)) are

\[
e^{|a|q},
\qquad
e^{-|a|q}.
\]

Thus

\[
\|U_z(q)\|=e^{|a|q},
\qquad
\sigma_{\min}(U_z(q))=e^{-|a|q}.
\]

In rank two, the codimension-one exterior power is the operator itself, so

\[
\|\Lambda^1U_z(q)\|=e^{|a|q}.
\]

The following conditions are therefore equivalent:

1. (a=0);
2. (U_z(q)) is unitary for every (q\ge0);
3. (U_z(q)) is uniformly bounded on the half-line;
4. its cofactor channel is uniformly bounded on the half-line;
5. its least singular value is bounded away from zero on the half-line.

This supplies a source-local explanation of the seam: it is the unique locus
where reciprocal transport is lossless in every direction, rather than only
volume preserving in aggregate.

## Exact indefinite current

For the forced system, write

\[
\Psi=\begin{pmatrix}G_+\\G_-\end{pmatrix},
\qquad
\eta=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

The established current and norm are

\[
J=\Psi^*\eta\Psi=|G_+|^2-|G_-|^2,
\qquad
\mathcal N=|G_+|^2+|G_-|^2.
\]

With source forcing retained, direct differentiation gives

\[
\partial_qJ=-2a\mathcal N-2\mathcal F,
\]

where

\[
\mathcal F=operatorname{Re}
\left(f_+c_+\overline{G_+}-f_-c_-\overline{G_-}\right).
\]

The homogeneous cofactor growth and the indefinite Green current are two
views of the same reciprocal hyperbolicity. The former identifies the seam;
the latter states exactly what the source forcing must cancel or convert into
boundary flux.

## Growing-rank typing correction

The arithmetic completion is not presently a fixed-rank matrix system. Each
finite prime cutoff adds labelled prime-power boundary directions. Moreover,
the primitive current is distributional, the square current is Hilbert but
not trace class, and only the connected tail beginning at the third level is
trace class.

Hence a finite-rank determinant--cofactor theorem cannot be applied globally
by assigning one stable rank to all cutoffs. If

\[
D_T=D_S\oplus E_{T\setminus S},
\]

then the degree of the cofactor space changes from

\[
\Lambda^{r_S-1}D_S
\]

to

\[
\Lambda^{r_T-1}D_T.
\]

Comparing them requires a volume element or determinant trivialization for
the newly adjoined complement. That extra choice is precisely where the
nonconvergent target cocycle can be hidden. It is not source-authorized by the
finite scalar Euler detector.

The primary global object must therefore be the conserved current of the
full boundary-bearing system. A Fredholm determinant or regularized exterior
theory may be derived afterward only if it retains the primitive and square
currents as typed boundary data.

## Remaining RH gate

The homogeneous calculation explains why the critical seam is the unique
unitary locus. It does not prove that an off-seam two-endpoint zero-state is
impossible. The unresolved question is whether the complete source forcing
can connect the stable and unstable reciprocal directions while satisfying
both endpoint conditions.

Equivalently, one must derive source-locally a decomposition of the form

\[
2\mathcal F
=
\partial_qJ_{\mathrm{boundary}}+2a\mathcal M
\]

with finite positive completed energy

\[
\int_0^\infty(\mathcal N+\mathcal M)\,dq
\]

on every nonzero admissible zero-state, and with vanishing total endpoint
flux. That would force (a=0). An uncancelled bulk residual, an undefined
primitive pairing, or an escaping boundary direction falsifies the route.

## Decisive outcome

The determinant is not the Sommerfeld invariant: it preserves only total
reciprocal volume and is blind to off-seam hyperbolicity. The independently
meaningful pre-scalar datum is the directional cofactor or, globally, the
full indefinite boundary current. The critical line is already selected as
the unique unitary seam by the source-derived homogeneous transport. RH
content remains entirely in the forced boundary-incidence and completion
theorem.
