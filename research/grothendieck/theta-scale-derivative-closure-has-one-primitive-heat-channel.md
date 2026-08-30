# Scale-derivative closure has exactly one primitive heat channel

## Bounded question

How much information is missing when the source seam-moment tower is replaced
by derivatives of the single completed scalar kernel?

## Raw and completed moments

Let

\[
 H_k(t)=\sum_{n\ge1}n^{2k}e^{-\pi tn^2}
\]

and let the completed seam moments be

\[
 M_k(t)
 =\pi t^{5/4}\bigl(2\pi tH_{k+2}(t)-3H_{k+1}(t)\bigr).
\]

The Riemann Fourier kernel is `Phi=M_0`, up to the fixed convention already
used in packet 107.  With `D=t partial_t`, the raw tower obeys

\[
 DH_k=-\pi tH_{k+1}.
\]

## Exact one-channel closure

Direct differentiation gives

\[
 DM_k
 =\frac54M_k-\pi tM_{k+1}
 +2\pi^2t^{9/4}H_{k+2}.
\]

The defining relation for `M_k` gives the recursion

\[
 H_{k+2}
 =\frac{M_k}{2\pi^2t^{9/4}}
 +\frac{3}{2\pi t}H_{k+1}.
\]

Iterating downward expresses every `H_(k+2)` uniquely in

\[
 H_1,M_0,M_1,\ldots,M_k.
\]

Therefore

\[
 D\,\operatorname{span}\{H_1,M_0,\ldots,M_k\}
 \subseteq
 \operatorname{span}\{H_1,M_0,\ldots,M_{k+1}\}.
\]

No new primitive channel appears at higher order.  For example,

\[
 DM_0
 =\frac94M_0-\pi tM_1+3\pi t^{5/4}H_1.
\]

Thus the complete scale-derivative closure of `Phi` is the oriented seam jet
plus one source-fixed raw heat line.

## Minimality of the primitive line

The line `H_1` cannot be removed algebraically from `M_0` alone.  The relation

\[
 M_0=2\pi^2t^{9/4}H_2-3\pi t^{5/4}H_1
\]

contains two independent raw moments.  Solving for both from one scalar would
be an unfaithful inverse.  Once `H_1` is retained, however, every higher raw
moment is recovered recursively from the corresponding `M_k`.

So the closure is minimal in the typed sense:

In ordinary language, the scalar completed jet equals the oriented seam-moment
tower together with one primitive heat channel.

## Cross-programme meaning

This is the same algebraic shape previously encountered as:

- positive Green bulk plus a primitive seam line;
- one unstable even mode plus one rank-one repair at prime-two level 44;
- a completed kernel plus a source-fixed endpoint channel.

Here the recurrence proves the rank statement exactly: the apparent growing
derivative defect tower is repeated presentation of one primitive source line.

## RH boundary and next gate

The new result removes an infinite-dimensional ambiguity but does not orient
the primitive line after Fourier/Mellin transport.  The sharp next question is
whether modular reflection supplies the conjugate copy of `H_1` with an exact
boundary pairing, so that eliminating the two primitive representatives is a
positive Schur complement rather than an arbitrary subtraction.

The falsifier is local: compute the first generalized Laguerre form using the
augmented packet `(H_1,M_0,M_1,...)`. If its primitive-channel Schur complement
has the wrong sign for a source-admissible scale, this closure does not bridge
to RH.
