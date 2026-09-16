# The global Adams-to-Weil crossing must be arity-graded before any Gram factorization

## Typing correction

The proposed global target

\[
L(q^*p)=\langle\iota(q),\iota(p)\rangle
\]

is already a Gram factorization of the Weil kernel. Its existence is equivalent
to positivity of that kernel and therefore cannot serve as the noncircular map
used to prove positivity.

Primitive and primitive-square observations have different source arities.
The correct pre-positivity crossing is

\[
J_1:\mathcal A\to\mathcal B_1,
\]

\[
\widetilde J_2:
\operatorname{Sym}^2\mathcal A\to\mathcal B_2,
\]

with

\[
\boxed{
\widetilde J_2(q^*\odot p)
=L(q^*p).}
\]

This is a linear identity on the polarized two-copy source. It does not assume
that \(L(q^*p)\) is a positive Gram.

## Local CP lift

For each prime-labelled primitive arrow \(A_r\), the square-phase map

\[
\mathcal E_r(X)=A_r^*XA_r
\]

is completely positive and satisfies

\[
\mathcal E_r\mathcal E_s=\mathcal E_{sr}.
\]

Thus the local target \(\mathcal B_2\) already carries a coherent positive
square law. The crossing problem is to identify the arity-two Weil map
\(\widetilde J_2\) with the arity-two matrix coefficient of this CP law, after
including gamma, endpoint, and the connected prime-power tail.

## Global graded source

The source must retain

\[
\operatorname{Sym}^{\le2}\mathcal A
\oplus
\mathcal A_{\ge3}^{connected},
\]

rather than treating primitive, square, and connected coordinates as parallel
linear ports on one additive copy.

The available projective exponential Kothe construction supplies:

- continuous labelled prime/grade synthesis;
- finite-packet density and cutoff convergence;
- local primitive/square joint graphs;
- a nuclear connected \(k\ge3\) return;
- a closed global retained graph when the source coordinate is kept.

These results construct the codomain in which an arity-graded comparison may
land.

## Exact noncircular comparison diagram

The required diagram is

\[
\begin{CD}
\operatorname{Sym}^2\mathcal A
@>{\operatorname{Sym}^2(\mathrm{Poisson/Mellin})}>>
\operatorname{Sym}^2\mathscr E_S\\
@V{\widetilde J_2^{Weil}}VV
@VV{\widetilde J_2^{Adams\,CP}}V\\
\mathcal B_2
@=\mathcal B_2.
\end{CD}
\]

The desired crossing is the linear equality

\[
\boxed{
\widetilde J_2^{Weil}
=
\widetilde J_2^{Adams\,CP}
\circ
\operatorname{Sym}^2(\mathrm{Poisson/Mellin}).}
\]

Only after proving this identity may one restrict to diagonal tensors
\(p^*\odot p\). Complete positivity then gives

\[
L(p^*p)\ge0.
\]

## Why this breaks the earlier circle

The comparison is tested on arbitrary polarized tensors
\(q^*\odot p\), where no positivity is assumed. Positivity enters only after:

1. the linear arity-two comparison has been established;
2. the input is specialized to the diagonal;
3. the already-constructed Adams CP law is applied.

Thus the next analytic theorem is a polarized two-copy source identity, not a
Hilbert Gram embedding of the Weil form.

## Remaining term

The local prime-labelled primitive/square cells satisfy this architecture. The
unproved part is equality with the **fully coupled** endpoint--gamma--prime
arity-two Weil map on every finite composite Gaussian tensor, followed by
continuity on the projective completion.
