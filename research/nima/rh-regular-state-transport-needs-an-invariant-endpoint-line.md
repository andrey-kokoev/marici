# RH regular state transport needs an invariant endpoint line

## Result

A regular spectral connection on the full source state does not prevent zeros of a scalar endpoint readout. The endpoint covector must itself generate an invariant dual line.

Let the prolonged state satisfy

\[
v'(z)=A(z)v(z)
\]

and let the endpoint section be

\[
f(z)=\ell(z)v(z).
\]

Then

\[
f'(z)=\bigl(\ell'(z)+\ell(z)A(z)\bigr)v(z).
\]

The scalar readout closes as a regular parallel line exactly when there is a regular scalar \(a(z)\) such that

\[
\ell'(z)+\ell(z)A(z)=a(z)\ell(z).
\]

This is the invariant-endpoint-line condition.

## Smallest hostile

Take

\[
A=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix},
\qquad
v(z)=
\begin{pmatrix}
1\\z
\end{pmatrix},
\qquad
\ell=
\begin{pmatrix}
0&1
\end{pmatrix}.
\]

The state is a nonzero parallel solution of the regular system, but

\[
f(z)=\ell v(z)=z
\]

vanishes at \(z=0\). The failure is

\[
\ell A=
\begin{pmatrix}
1&0
\end{pmatrix},
\]

which is not proportional to \(\ell\). At the scalar zero, the derivative residual is \(\ell A v(0)=1\).

Thus a zero may be destructive projection of a nonzero transported state, exactly as the earlier Clifford pairing correction warned.

## Control-theoretic form

The relevant object is the dual Krylov module

\[
\operatorname{span}\{\ell,\ell A,\ell A^2,\ldots\}.
\]

Rank one gives a closed scalar line and zero exclusion from a nonzero anchor. Rank greater than one means the endpoint is one coordinate of a higher-dimensional observable system; scalar cancellation remains possible.

This is not ordinary observability. Full observability may reconstruct the state while the chosen scalar component still vanishes. The RH-strength condition is the stronger invariant-line closure of the distinguished endpoint port.

## Consequence for the moment-tail prolongation

Spectral differentiation naturally adds moment-tail channels. That produces a regular enlarged system without scalar division, but it does not yet give RH. Grothendieck's next calculation must compute the dual orbit of the endpoint evaluation covector under the prolonged generator.

There are three possible outcomes:

1. The orbit closes at rank one. The endpoint is a regular parallel line, and off-seam zeros are excluded from a nonzero anchor.
2. The orbit closes at finite rank greater than one. The endpoint satisfies a higher-order system, and scalar zeros remain possible through interference.
3. The orbit grows indefinitely. A full moment module and completion theorem are required; first-order puncture exclusion fails.

## DPC verdict

Candidate: regular parallel transport of the full prolonged state.

Verdict: insufficient, rejected by the two-state hostile.

Candidate: regular transport plus endpoint-line invariance.

Verdict: sufficient for scalar zero exclusion; source derivation remains open.

## Finite falsifier

At cutoff \(X\), compute

\[
R_X=\ell'_X+\ell_XA_X-a_X\ell_X
\]

for the only source-authorized candidate \(a_X\), if one exists. Any component transverse to \(\ell_X\) falsifies the invariant-line route. The first transverse moment direction is the smallest witness.
