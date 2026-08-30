# 2882 — The Complete Soft Pushforward Meets an Internal Marked Collision

## Frozen dimensionless kernel

Set

\[
x=\frac ap.
\]

The exceptional Cayley–Menger kernel is

\[
k(x,\kappa,\xi)
=
x^4-(8\kappa\xi+10)x^2
+16\kappa^2+40\kappa\xi+16\xi^2+9.
\]

The complete marked density contains

\[
\frac{x+1}
{2p^4(x-1)^2(x+3)(\xi+1)\sqrt{k}}
\,dx\,d\xi.
\]

Writing

\[
\alpha_\pm
=
5+4\kappa\xi
\pm
4\sqrt{(1-\kappa^2)(1-\xi^2)},
\]

one has

\[
k=(x^2-\alpha_-)(x^2-\alpha_+).
\]

The complete positive-occurrence pushforward is therefore the marked elliptic
period

\[
I(\xi)
=
\frac1{2p^4(\xi+1)}
\int_{\sqrt{\alpha_-}}^{\sqrt{\alpha_+}}
\frac{(x+1)\,dx}
{(x-1)^2(x+3)\sqrt{k(x,\kappa,\xi)}}.
\]

This formula retains the actual moving endpoints and all marked rational
factors; it is not an endpoint interpolation.

## Exact collision identities

Direct coefficient reduction gives

\[
k(1,\kappa,\xi)=16(\kappa+\xi)^2,
\]

and

\[
k(-3,\kappa,\xi)=16(\kappa-\xi)^2.
\]

Therefore the physical positive occurrence meets the marked pole \(a=p\) at

\[
\xi=-\kappa,
\qquad
t=1-\kappa.
\]

For generic \(-1<\kappa<1\), this lies strictly inside

\[
0<t<2.
\]

The deck-partner collision at \(a=-3p\) occurs at \(t=1+\kappa\).

## Local Newton order

Let

\[
u=x-1,
\qquad
\delta=\xi+\kappa.
\]

At the positive collision,

\[
\left.\partial_x k\right|_{x=1,\xi=-\kappa}
=
-16(1-\kappa^2),
\]

which is generically nonzero. The Newton balance is

\[
u\sim\delta^2.
\]

Since the marked density contains

\[
\frac{du}{u^2\sqrt{k}},
\]

its moving-cycle pushforward has local scaling

\[
I(\xi)\sim\delta^{-3}
\]

before the source-prescribed contour continuation or subtraction is applied.

## Correction to the endpoint-only picture

The complete pushed-forward one-form does not live on the unpunctured real
interval from \(t=2\) to \(t=0\). The physical route crosses an independently
existing marked collision. Thus the expression

\[
P(t)=\int_2^t I(s)\,ds
\]

is globally typed only after the full source \(i\epsilon\) continuation around
the internal support is retained.

Entries 2871–2875 remain valid as local endpoint statements in their generic
transverse patches. They do not by themselves construct the complete global
primitive between the endpoints.

## Classification

- Existing carrier support: the marked divisor \(a=p\) meeting the
  Cayley–Menger branch.
- New carrier datum: none.
- Missing global datum: the source-normalized continuation and connection
  across the internally punctured base.
- Next falsifier: derive the complete Gauss–Manin system on
  \(\mathbf P^1_t\setminus\{0,2,1-\kappa,1+\kappa,\ldots\}\) and test whether
  the published boundary-value germ fixes its connection matrix and finite
  transport.

## Durable artifacts

- `research/benincasa/check_soft_pushforward_internal_marked_collision.py`
- `research/benincasa/soft-pushforward-internal-marked-collision.json`
