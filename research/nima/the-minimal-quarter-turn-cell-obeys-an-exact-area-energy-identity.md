# The minimal quarter-turn cell obeys an exact area-energy identity

## Setup

Take the minimal real \(K\)-\(V\) carrier

\[
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
\]

and the positive Hermitian auxiliary block

\[
D=sI+i\tau J,
\qquad
s>|\tau|.
\]

Let the two real endpoint incidence rows be \(u,v\in\mathbb R^2\), so

\[
C=
\begin{pmatrix}
u\\
v
\end{pmatrix}.
\]

The inverse is

\[
D^{-1}=aI-ibJ,
\qquad
a=\frac{s}{s^2-\tau^2},
\qquad
b=\frac{\tau}{s^2-\tau^2}.
\]

## Even and odd returns

Define

\[
Q=CD^{-1}C^T.
\]

Its even real part is

\[
E=\operatorname{Re}Q
=
a
\begin{pmatrix}
\|u\|^2&u\cdot v\\
u\cdot v&\|v\|^2
\end{pmatrix}.
\]

Its oriented coordinate is

\[
h_Q=\operatorname{Im}Q_{12}
=
-b\,uJv^T.
\]

The effective Schur form is \(G^{\mathrm{eff}}=A-Q\), so its odd coordinate has the opposite sign.

In two real dimensions,

\[
(uJv^T)^2
=
\|u\|^2\|v\|^2-(u\cdot v)^2.
\]

Consequently,

\[
h_Q^2
=
\frac{b^2}{a^2}\det E
=
\frac{\tau^2}{s^2}\det E.
\]

This is an exact identity, not merely an estimate.

## Consequences

Because \(D>0\),

\[
\frac{|\tau|}{s}<1,
\]

and therefore

\[
h_Q^2<\det E
\]

whenever the incidence has rank two. The Fourier odd magnitude is bounded by the even eliminated energy. It cannot be chosen independently after the endpoint energies have been frozen.

Equality can occur only at the auxiliary radical threshold \(s=|\tau|\), where \(D^{-1}\) ceases to be controlled. Thus saturation of the area bound is a completion obstruction, not a valid positive cell.

The odd coordinate is nonzero exactly when all three conditions hold:

- \(\tau\ne0\): the auxiliary Fourier orientation is active;
- \(\det C\ne0\): the endpoint incidences span oriented area;
- the relevant auxiliary direction survives radical reduction.

A rank-one incidence cannot generate an odd endpoint orientation even with the correct quarter-turn.

## Reconstruction data

If the source determines both \(E\) and the Euler odd target \(h_p\), then the minimal model forces

\[
\left|\frac{\tau_p}{s_p}\right|
=
\frac{|h_p|}{\sqrt{\det E_p}}.
\]

The ordered source convention fixes the sign of \(\tau_p\det C_p\), while additive data determine \(E_p\). Hence a necessary existence condition is

\[
|h_p|<\sqrt{\det E_p}.
\]

This supplies a direct finite falsifier before any global completion: if the scoped Euler odd current exceeds the source-derived even area budget, no positive minimal \(K\)-\(V\) Schur cell can realize it.

## Uniform completion margin

The correct quantitative margin is

\[
\delta_{KV}
=
1-
\frac{h_p^2}{\det E_p}
=
1-\frac{\tau_p^2}{s_p^2}.
\]

Completion requires a positive lower bound for \(\delta_{KV}\) over the admitted primes, cutoffs, and compact off-seam parameter sets, together with bounds on the overall scale of \(D_p\) and the incidence maps. A lower bound on \(\delta_{KV}\) alone does not control scalar amplification.

This is a new local coercivity margin upstream of the previously identified five global margins. It certifies that the source-authorized phase remains strictly inside the positive auxiliary cone.

## Hostiles

1. **Rank-one incidence:** \(u\) and \(v\) are parallel. The Fourier quarter-turn exists, but \(uJv^T=0\).
2. **Overlarge Euler target:** \(|h_p|\ge\sqrt{\det E_p}\). Scalar orientation is prescribed, but no positive minimal cell realizes it.
3. **Near-radical realization:** \(|h_p|/\sqrt{\det E_p}\to1\). Every finite cell is positive, while its auxiliary inverse loses uniform control.
4. **Orientation flip:** \(J\mapsto-J\) or \(\det C\mapsto-\det C\). Even return and determinant magnitude are unchanged, but the reciprocal character reverses.

## Next source calculation

Compute the real incidence rows \(u_p,v_p\) and the even tail/PV return \(E_p\) from the source cell. Then compare the exact area budget \(\sqrt{\det E_p}\) with the scoped Euler odd current. This decides finite existence of the minimal positive quarter-turn realization before attempting closability or primewise completion.
