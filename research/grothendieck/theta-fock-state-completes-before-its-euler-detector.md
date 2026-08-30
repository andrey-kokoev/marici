# Theta Fock state completes before its Euler detector

## Local Euler detector is distributional

In the local occupation Hilbert space with orthonormal basis `e_(p,k)`, the
Euler readout is the coefficient-sum functional

\[
 \ell_p(e_{p,k})=1
 \qquad(k\ge0).
\]

If `ell_p` were represented by a Hilbert vector, that vector would have
coordinates `(1,1,1,...)`, whose squared norm diverges. Therefore

\[
 \boxed{
 \ell_p\notin\mathcal H_p^*.}
\]

It is a rigged/distributional covector.  This failure occurs already at one
prime and cannot be repaired by global tensor convergence.

On the raw geometric state

\[
 \Omega_{p,s}^{\rm raw}=\sum_{k\ge0}p^{-ks}e_{p,k},
\]

the distributional pairing is nevertheless defined for `Re(s)>0` and equals

\[
 \ell_p(\Omega_{p,s}^{\rm raw})={1\over1-p^{-s}}.
\]

## Pairing with the normalized Fock state

Packet 185 uses

\[
 \omega_{p,s}
 =\sqrt{1-p^{-2\sigma}}\Omega_{p,s}^{\rm raw},
 \qquad \sigma=\Re s.
\]

Its local detector amplitude is

\[
 \boxed{
 a_p(s)
 =\ell_p(\omega_{p,s})
 ={\sqrt{1-p^{-2\sigma}}\over1-p^{-s}}.}
\]

Every local amplitude is nonzero where finite.

## Global scalar threshold

The logarithmic modulus has expansion

\[
\begin{aligned}
 \log|a_p(s)|
 &={1\over2}\log(1-p^{-2\sigma})
 -\log|1-p^{-s}|\\
 &=p^{-\sigma}\cos(t\log p)+O(p^{-2\sigma}),
\end{aligned}
\]

with the error summable for every `sigma>1/2`.

Absolute convergence of the leading prime sum requires `sigma>1`. Thus:

\[
 \boxed{
 \begin{array}{c|c}
 \text{object}&\text{canonical ordinary completion threshold}\\
 \hline
 \text{normalized Fock state}&\sigma>1/2\\
 \text{raw Euler detector product}&\sigma>1
 \end{array}}
\]

The state exists throughout the open RH half-sector before its scalar Euler
detector admits an ordinary product pairing.

## Meaning of Poisson completion

Poisson/Tate sewing is therefore not needed to create the state.  It is needed
to extend its distributional detector pairing from the Euler chamber into the
larger Fock representation sector.

This refines the current architecture:

\[
 \boxed{
 \text{Fock completion supplies the state at }\Re s>1/2;
 \quad
 \text{Poisson completion transports the detector across }\Re s=1.}
\]

The two thresholds have different meanings:

- `Re(s)=1/2` is the representation boundary of the normalized prime state;
- `Re(s)=1` is the absolute-convergence boundary of the scalar Euler detector.

Conflating them obscures where RH difficulty lives.

## The remaining transversality theorem

The completed Poisson detector `ell_s^Pois` must be a continuous covector on a
rigging containing `Omega_s`, even though the raw tensor product of the local
`ell_p` is not a Hilbert covector.  RH becomes

\[
 \boxed{
 \ell_s^{\rm Pois}(\Omega_s)\ne0
 \qquad(\Re s>1/2),}
\]

plus the reciprocal statement.

The construction must reproduce the ordinary product pairing in `Re(s)>1`,
retain primitive and square anomaly currents during continuation, and avoid
defining the covector backward from `Xi`.

## Smallest falsifiers

1. A proposed detector represented by a bounded local Hilbert vector cannot
   reproduce `ell_p(e_(p,k))=1` for all `k`.
2. A global detector obtained by the ordinary product of `a_p(s)` is undefined
   in general in `1/2<Re(s)<=1`.
3. A regularized detector whose finite-cutoff changes do not match the Tate
   anomaly-line cocycle is not source compatible.
4. A detector defined solely by the desired scalar completed section is
   circular even if continuous.

## Scope

This packet proves the local unboundedness of the Euler covector and separates
the exact state and detector convergence thresholds. It does not construct the
Poisson-completed covector on the Fock rigging or prove its transversality.
