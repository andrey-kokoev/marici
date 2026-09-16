# The reciprocally doubled theta shift has an exact Krein Green balance and is not passive under diagonal storage

## Doubled generator

On

\[
\mathcal H_\Phi
=
L^2(\mathbb R_+,\Phi(u)\,du),
\]

put

\[
A_+=-\partial_u,
\qquad
A_- =+\partial_u.
\]

The reciprocal doubled generator is

\[
\mathbb A
=
\begin{pmatrix}
A_+&0\\
0&A_-
\end{pmatrix}.
\]

Its spectral sections are

\[
f_+(u)=e^{-su},
\qquad
f_-(u)=e^{su},
\]

and both satisfy

\[
A_+f_+=sf_+,
\qquad
A_-f_-=sf_-.
\]

The superexponential theta weight makes both sections square-integrable for every finite \(s\).

## Two one-sided Green identities

Integration by parts gives

\[
\langle A_+f,g\rangle_
\Phi
+
\langle f,A_+g\rangle_
\Phi
=
\Phi(0)f(0)\overline{g(0)}
+
\int_0^\infty
f\overline g\,\Phi'\,du,
\]

whereas

\[
\langle A_-f,g\rangle_
\Phi
+
\langle f,A_-g\rangle_
\Phi
=
-
\Phi(0)f(0)\overline{g(0)}
-
\int_0^\infty
f\overline g\,\Phi'\,du.
\]

Define

\[
Bf=
\sqrt{\Phi(0)}f(0),
\qquad
Cf=
\sqrt{-\Phi'}f.
\]

Then the doubled diagonal-storage balance is

\[
2\operatorname{Re}
\langle
\mathbb Af,f
\rangle
=
|Bf_+|^2
-
|Bf_-|^2
-
\|Cf_+\|^2
+
\|Cf_-\|^2.
\]

## Control interpretation

This is an exact Krein supply balance. Both the seam ports and the distributed ports have signature

\[
J=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

Consequently, diagonal storage

\[
P_0=I\oplus I
\]

is not a passive Hilbert storage for the reciprocal system. It is a conservative storage relative to an indefinite supply rate.

## Seam matching

The natural seam relation

\[
f_+(0)=f_-(0)
\]

cancels the endpoint contribution, but leaves

\[
2\operatorname{Re}
\langle
\mathbb Af,f
\rangle
=
-
\|Cf_+\|^2
+
\|Cf_-\|^2.
\]

Therefore continuity at the modular seam does not establish passivity. One additionally needs a nonlocal relation that contracts the reflected distributed output:

\[
\|Cf_-\|
\le
\|Cf_+\|.
\]

For the physical reciprocal spectral pair, this is exactly the missing comparison between \(e^{su}\) and \(e^{-su}\) after theta weighting and boundary observation.

## Consequence for cross-storage

The source of the obstruction is now explicit. The negative direction is not an unexplained finite-dimensional coordinate: it is the distributed output of the reflected transport sheet.

Any successful positive storage must do one of the following:

1. impose a source-derived contractive feedback relation between the two distributed outputs;
2. add an off-diagonal storage whose Green derivative converts their signed difference into a positive defect;
3. quotient a maximal neutral graph selected by modular boundary incidence.

A scalar reflection gain cannot perform this operation because it does not alter the distributed signature while retaining both even and odd Clark channels.

## Exact next equation

For an off-diagonal storage

\[
P_K
=
\begin{pmatrix}
I&K^*\\
K&I
\end{pmatrix},
\]

the unknown block must satisfy the cross Sylvester/Green equation

\[
A_-^*K
+
KA_+
=
Q_{-+},
\]

where \(Q_{-+}\) is fixed by the desired Clark seam ports.

Positivity additionally requires

\[
\|K\|\le1.
\]

The doubled boundary calculation therefore reduces the preferred control-theoretic path to deriving \(Q_{-+}\) from the zeroth and first theta moment observations, then testing whether the corresponding Sylvester solution is contractive.

## Disposition

The full diagonal doubled Green form is now explicit. Reciprocal sewing is not automatically passive: it is a Krein interconnection whose reflected distributed output is the precise negative channel.
