# The minimal Green completion of the theta forcing is the skew-adjoint source pair

> **Compatibility obstruction.** The successor packet
> `the-natural-forced-history-cannot-satisfy-the-adjoint-source-equation-off-the-seam.md`
> shows that the natural Mellin-history lift does not automatically satisfy
> \(V^*u=0\). Off the seam, endpoint closure plus that adjoint equation already
> forces the desired confinement. The paired block is therefore a valid Green
> completion but not yet a noncircular Xi-to-kernel bridge.

## Forcing column

Let

\[
V:\mathbb C\to H,
\qquad
Vc=c\Phi.
\]

Its source-metric adjoint is

\[
V^*:H	o\mathbb C,
\qquad
V^*u=\langle\Phi,u\rangle.
\]

The augmented history equation using only the column \(-V\) leaves the Green
residual

\[
2\operatorname{Re}\langle u,Vc\rangle.
\]

## Minimal paired block

The unique adjoint completion with no additional diagonal source dynamics is

\[
\mathcal D_a^{\rm pair}
=
\begin{pmatrix}
\partial_q-a&-V\\
V^*&0
\end{pmatrix}.
\]

Its off-diagonal coupling

\[
\begin{pmatrix}0&-V\\V^*&0\end{pmatrix}
\]

is skew-adjoint.  Therefore its real quadratic pairing vanishes identically:

\[
2\operatorname{Re}
\left(
-\langle u,Vc\rangle
+
\overline c\,V^*u
\right)=0.
\]

The forcing term is cancelled at the vector level, before scalar readout.

## Kernel Green identity

For a kernel state \((u,c)\), the equations are

\[
(\partial_q-a)u=Vc,
\]

\[
V^*u=0.
\]

Pairing the first equation with \(u\), and using the second equation, gives

\[
2a\|u\|^2
=
\left[|u(q)|^2\right]_{-\infty}^{+\infty}.
\]

After replacing the raw endpoint difference by the complete Green boundary
form, maximal-isotropic sewing yields

\[
2a\|u\|^2=0.
\]

Thus the minimal paired block supplies the exact cancellation missing from
the column-only augmentation.

## Uniqueness boundary

Suppose the lower-left block is \(W:H\to\mathbb C\).  Cancellation of the
forcing pairing for every \((u,c)\) requires

\[
\operatorname{Re}
\left(-\langle u,Vc\rangle+
\overline c\,Wu\right)=0
\]

for all \(u,c\).  Polarization forces

\[
W=V^*
\]

up to an additional purely imaginary source-diagonal term, which contributes
no real Green energy.  The adjoint return is therefore fixed by the source
metric.

## New compatibility condition

The paired completion changes the kernel problem.  A state derived from the
Xi Koszul residue must satisfy not only the forced history equation but also

\[
\langle\Phi,u\rangle=0.
\]

A scalar Xi zero does not automatically imply this orthogonality.  The
required divisor-to-state map must prove it from the retained arithmetic and
boundary construction.

Installing \(V^*u=0\) after locating a zero would be circular boundary fitting.
It must be one of the source equations defining the pencil for every
parameter.

## Relation to the retained joint graph

The source-authorized joint graph already retains an incidence together with
its metric adjoint in positive Green energy.  To use it here, one must identify
its forcing column with \(V\) and its return row with this exact \(V^*\) on the
same half-density history metric.  Equality of Gram norms is insufficient.

## G4 consequence

The Green-readback residual has a canonical algebraic repair: retain the full
skew-adjoint source pair \((-V,V^*)\).  This closes forcing cancellation for
the resulting paired pencil.

The remaining G4 question becomes sharper:

\[
\tau_s=0
\Longrightarrow
\exists\,(u,c)\ne0
\text{ satisfying both }
(\partial_q-a)u=Vc
\text{ and }V^*u=0,
\]

with all reciprocal, prime, grade, and endpoint components retained.  No RH
conclusion is authorized.
