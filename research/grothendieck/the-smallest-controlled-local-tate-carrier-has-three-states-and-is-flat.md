# The smallest controlled local Tate carrier has three states and is flat

## Source normalization

Fix one finite place `p`. Use the standard additive character of
`Q_p` with conductor `Z_p` and the self-dual Haar measure normalized by

\[
\operatorname{vol}(\mathbb Z_p)=1.
\]

For an integer `k`, define the normalized ball state

\[
b_k(x)=p^{k/2}\mathbf 1_{p^k\mathbb Z_p}(x).
\]

Its `L^2` norm is one. The local Fourier transform satisfies

\[
\mathcal F_p\mathbf 1_{p^k\mathbb Z_p}
=p^{-k}\mathbf 1_{p^{-k}\mathbb Z_p},
\]

and therefore

\[
\mathcal F_p b_k=b_{-k}.
\]

No finite Fourier matrix has been inserted. This matrix follows directly
from the local Tate source normalization.

## Smallest controlled carrier

The outer pair

\[
V_p^{\mathrm{outer}}=\operatorname{span}\{b_{-1},b_1\}
\]

is Fourier closed, but it contains no source-fixed reference state with which
to calibrate the exchange phase. The distinguished unramified vector `b_0`
supplies that control.

Hence the smallest Fourier-closed carrier containing one reciprocal pair and
one native common mode is

\[
V_p^{(3)}
=
\operatorname{span}\{b_{-1},b_0,b_1\}.
\]

In this ordered basis the Fourier–Tate transport is

\[
J_p=
\begin{pmatrix}
0&0&1\\
0&1&0\\
1&0&0
\end{pmatrix}.
\]

It is source-typed, real, unitary, self-adjoint, and involutive:

\[
J_p^*=J_p,
\qquad
J_p^2=I.
\]

## Representation decomposition

The carrier splits into two Fourier-even channels and one Fourier-odd
channel:

\[
b_0,
\qquad
\frac{b_{-1}+b_1}{\sqrt2},
\qquad
\frac{b_{-1}-b_1}{\sqrt2}.
\]

The first two have eigenvalue `+1`; the last has eigenvalue `-1`. Thus the
local object has the exact architecture

```text
reciprocal input state
+ unramified common-mode control
+ reciprocal output state.
```

The control is not an external phase standard. It is the Fourier-fixed local
vacuum required by the restricted product itself.

## Flatness result

The reciprocal route and its reverse have transport

\[
J_p^{-1}J_p=I.
\]

Therefore this smallest phase-framed local coefficient system has trivial
backtracking holonomy. Its normalized two-chart cycle carries no irreducible
local residue once the inverse route is an authorized filling.

This is a useful negative theorem: phase framing and a native control solve
the local typing problem, but they do not create an RH-bearing class. Any
surviving class must use structure absent from one place:

- incompatibility among several placewise transports;
- primitive and square boundary currents under restricted-product
  completion;
- archimedean coupling;
- a nonfillable global route cycle;
- or failure of the local homotopies to assemble continuously.

## Relation to the three-tower intuition

The local carrier is not merely two opposing states. It is a reciprocal pair
plus a fixed control. This realizes a minimal `2+1` pattern inside one place.
The global interface tower must retain these controls coherently across
places; deleting them returns to an unframed projective comparison.

## Next finite test

Take two primes `p` and `q`. Form

\[
V_p^{(3)}\otimes V_q^{(3)}
\]

with transports `J_p` and `J_q`. The independent tensor transports commute,
so the untwisted two-prime square remains flat. The first informative test
must therefore include a source coupling that is not the tensor product of
the two local reversals—most naturally the global archimedean or restricted-
product boundary map.

The falsifier is sharp: if the proposed global coupling also conjugates the
product transport without changing domains, the homotopy transports and the
route closes again. Only a nonexact interface map can produce the class.

## Scope

This proves the smallest source-derived finite phase-framed carrier at one
finite place and its flatness. It does not construct the global coupled
interface, its archimedean boundary map, a nonfillable cycle, or RH.
