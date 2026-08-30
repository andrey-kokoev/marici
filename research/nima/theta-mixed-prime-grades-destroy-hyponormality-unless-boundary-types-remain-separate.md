# Mixed prime grades destroy hyponormality unless their boundary types remain separate

## Two-grade unilateral current

Fix one prime \(p\), write

\[
r=\Re(z)\log p,
\]

and suppress the removable vertical phase by diagonal unitary conjugation.

The first two source grades on the unilateral valuation cone are

\[
T_1=aS-bS^*,
\qquad
T_2=cS^2-dS^{*2},
\]

with

\[
a=p^{-1/2}e^r,
\qquad
b=p^{-1/2}e^{-r},
\]

and

\[
c=\frac{p^{-1}}2e^{2r},
\qquad
d=\frac{p^{-1}}2e^{-2r}.
\]

Each grade separately has a signed positive self-commutator for \(r>0\).

## Exact mixed self-commutator

Set

\[
T=T_1+T_2.
\]

The self-commutator

\[
C=T^*T-TT^*
\]

is supported on the first two valuation states. In the basis \(e_0,e_1\),
its nonzero block is

\[
C_{\partial}
=
\begin{pmatrix}
a^2-b^2+c^2-d^2&ac-bd\\
ac-bd&c^2-d^2
\end{pmatrix}.
\]

The off-diagonal entry is the mixed \(k=1\)-by-\(k=2\) boundary term.

Its determinant is

\[
\det C_{\partial}
=
(c^2-d^2)^2-(ad-bc)^2.
\]

Substituting the source coefficients gives

\[
\det C_{\partial}
=
4A_2^2
\left(
A_2^2\sinh^2(4r)
-
A_1^2\sinh^2(r)
\right),
\]

where

\[
A_1=p^{-1/2},
\qquad
A_2=\frac{p^{-1}}2.
\]

For \(r>0\), positivity requires

\[
\frac{2}{\sqrt p}\cosh(r)\cosh(2r)\ge1.
\]

## Immediate falsifier

As \(r\) tends to zero from the right,

\[
\cosh(r)\cosh(2r)\longrightarrow1.
\]

Hence for every prime \(p\ge5\),

\[
\frac{2}{\sqrt p}<1,
\]

and the determinant is strictly negative in an open neighborhood of the
critical seam.

Therefore the naive sum \(T_1+T_2\) is not hyponormal there, even though each
source edge is individually hyponormal.

Prime \(2\) and prime \(3\) do not expose the near-seam failure, which explains
why a smallest-prime test alone would be misleading.

## Structural meaning

The failure is not caused by hostile signs. It occurs for the actual positive
prime-power coefficients. The obstruction is untyped addition of two
analytically different boundary grades on one carrier.

This independently confirms the three-grade architecture:

- the primitive current is distributional in a Laplace rigging;
- the square current is Hilbert or tempered but not absolutely summable;
- the connected tail is trace-class near the seam.

If the primitive and square currents remain in orthogonally typed boundary
ports, their individual self-commutators form a positive block direct sum for
\(r>0\). The negative mixed minor appears only when an undeclared constructor
identifies the two ports and adds their operators.

Thus typing can preserve the local signed index. It does not yet prove that
the later source-authorized sewing between grades preserves it.

## Exact coherence question

Let

\[
\mathcal E_1\oplus\mathcal E_2
\]

be the primitive and square boundary ports. Any coupling map \(K_{12}\) that
eventually combines their readouts must carry its own self-commutator
correction.

The required finite law is

\[
C_1\oplus C_2+C_{\mathrm{sew}}\ge0
\]

on the right half-strip, with the reversed inequality on the left. The term
\(C_{\mathrm{sew}}\) must cancel or dominate the explicit mixed block above
and must be derived from endpoint, gamma, or reciprocal incidence.

Choosing it by taking the negative part of \(C_{\partial}\) would fit the
answer and is rejected.

## Finite test suite

For every proposed grade-sewing constructor:

1. reproduce the exact \(2\times2\) block above;
2. test primes \(2,3,5,7\);
3. test the limit \(r\to0^+\);
4. type every off-diagonal correction;
5. delete the sewing constructor and recover the negative mixed minor;
6. apply reciprocal reflection and verify reversal of the signed law.

Prime \(5\) near the seam is the smallest arithmetic falsifier.

## Disposition

The source-derived signed boundary index survives each individual valuation
edge but fails under naive mixed-grade addition. This is a sharp negative
result and a durable architectural gain.

Any surviving orientation theorem must keep primitive and square currents
separate until a source-authorized sewing operation supplies the exact mixed
boundary correction.
