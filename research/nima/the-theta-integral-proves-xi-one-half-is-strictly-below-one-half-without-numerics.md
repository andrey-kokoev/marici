# The theta integral proves xi one-half is strictly below one-half without numerics

## Completed-xi integral

Let

\[
\psi(x)
=
\sum_{n\ge1}e^{-\pi n^2x},
\qquad
x\ge1.
\]

The standard completed-xi splitting at the theta fixed point gives

\[
\xi(s)
=
\frac12
+
\frac{s(s-1)}{2}
\int_1^\infty
\psi(x)
\left(
x^{s/2}+x^{(1-s)/2}
\right)
\frac{dx}{x}.
\]

This is the source theta representation of the completed mass; it does not
use RH or any zero information.

## Central value

At

\[
s=\frac12,
\]

one has

\[
s(s-1)=-\frac14
\]

and

\[
x^{s/2}+x^{(1-s)/2}
=
2x^{1/4}.
\]

Therefore

\[
\xi\!\left(\frac12\right)
=
\frac12
-
\frac14
\int_1^\infty
\psi(x)x^{-3/4}\,dx.
\]

Every summand of \(\psi(x)\) is positive, and the integral is finite and
strictly positive. Hence

\[
\xi\!\left(\frac12\right)
<
\frac12.
\]

No decimal evaluation is needed.

## Strictness and finiteness

Strictness follows already from the \(n=1\) term:

\[
\int_1^\infty
\psi(x)x^{-3/4}\,dx
>
\int_1^\infty
e^{-\pi x}x^{-3/4}\,dx
>0.
\]

Finiteness follows from

\[
\psi(x)
\le
\sum_{n\ge1}e^{-\pi nx}
=
\frac{e^{-\pi x}}{1-e^{-\pi x}},
\qquad
x\ge1.
\]

Thus the central theta mass is rigorously separated from \(1/2\).

## Exact role in the shifted-history square

With the frozen source normalization,

\[
M_\Phi
=
\xi\!\left(\frac12\right).
\]

The integral identity therefore proves

\[
1-M_\Phi>\frac12.
\]

For the reciprocal shifted-history blocks,

\[
D_\pm
=
\frac12(I\pm iH_\Phi)^*(I\pm iH_\Phi),
\]

the mass estimate yields

\[
D_\pm
>
\frac18I
\]

as a quadratic-form inequality on the completed translation carrier.

Consequently,

\[
\|D_\pm^{-1}\|<8.
\]

The strict constants can be weakened to the rational bounds
\(D_\pm\ge1/8\) and \(\|D_\pm^{-1}\|\le8\) whenever a non-strict
closed estimate is more convenient.

## Completing the prime-two certificate

The rational Gaussian bounds gave

\[
a_2>0.6,
\qquad
d_2^2<0.1.
\]

Since

\[
1-M_\Phi>\frac12,
\]

one has

\[
8(1-M_\Phi)^2a_2
>
8\left(\frac12\right)^2(0.6)
=
1.2.
\]

Therefore

\[
d_2^2
<
8(1-M_\Phi)^2a_2
\]

with margin greater than \(1.1\).

Together with the monotone Gaussian envelope for \(p\ge3\), the
theta-mass Schur inequality holds for every prime.

## Logical qualification

This closes the analytic loading estimate conditional on the previously
isolated constructor statements:

- the source odd incidence equals the Stieltjes disagreement;
- reciprocal equivariance forces Wronskian rank one;
- the auxiliary block is the normalized completed-theta shifted square.

The theta integral proves the scalar bound inside that constructor. It does
not prove the constructor identifications themselves.

## Verdict

The last scalar residue required no numerical checker. The fixed-point theta
integral gives the exact sign

\[
\xi\!\left(\frac12\right)-\frac12<0.
\]

Accordingly, the local primewise Schur-loading margin is analytically closed
once the window-to-completed-history constructor identity is established.
The earliest first-Adams obstruction has returned entirely to source
functoriality.
