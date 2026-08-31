# The bi-bounded comparison is only at the differentiated-front level

## Carrier correction

The recent labelled comparison

\[
q_{kL}
\longmapsto
u_{p,k}
\]

is bi-bounded after retaining prime-grade fibers and wall ports.  However,

\[
q_t=DW_t
\]

is the differentiated boundary front, while the selected resolved positive
form is carried by the primitive windows

\[
W_t.
\]

Therefore the bi-bounded front theorem does **not** yet establish a bi-bounded
comparison for the resolved first-Adams window Gram.

## Primitive norm growth

The closed ordinary window formula gives

\[
\|W_t\|_2^2
=2\bigl(R(2t)-R(0)\bigr)
=2t-\frac{\sqrt2}{\pi}+O(e^{-2\pi t^2}).
\]

Thus

\[
\|W_t\|_2\sim\sqrt{2t}.
\]

By contrast,

\[
\|q_t\|_2^2
=\sqrt2(1-e^{-2\pi t^2})
\]

is uniformly bounded above and below for \(t\ge\log2\), and the wall-extended
cut-atom norm is exactly constant in \(t\).

Hence the ordered primitive map

\[
D^{-1}_{\mathrm{ord}}:q_t\mapsto W_t
\]

introduces a genuine \(\sqrt t\) norm growth.  It is not uniformly bounded
from the labelled front norm to the ordinary window norm across all
prime-power labels.

## Resolved norm does not remove the growth

The selected resolved form satisfies

\[
\|W_t\|_{\mathrm{res}}^2
=(1+M_\Phi^2)\|W_t\|_2^2+\|BW_t\|_2^2
\ge(1+M_\Phi^2)\|W_t\|_2^2.
\]

Therefore

\[
\|W_t\|_{\mathrm{res}}\gtrsim\sqrt t.
\]

The bounded tail operator \(B\) cannot cancel this base growth because its
contribution is positive.  Consequently the resolved primitive carrier is
not uniformly equivalent to the differentiated front carrier with its
unweighted labelled norm.

## What remains valid

The following differentiated-level statements remain correct:

- finite front independence;
- algebraic source-generated comparison with theta cut atoms;
- labelled Hilbert bi-boundedness for \(q_{kL}\leftrightarrow u_{p,k}\);
- wall-extended cut norm constancy;
- closed range and zero radical on that differentiated labelled carrier;
- literal Euler sampling through the cut-side normal derivative.

What must be retracted is the claim that these facts already close the
resolved **window** Green comparison.

## Required weight

To compare primitive windows with constant-norm cut atoms, the source side must
carry a primitive scale weight comparable to

\[
\omega_{p,k}^2
\asymp k\log p.
\]

Equivalently, one may normalize

\[
\widetilde W_{p,k}
=\frac{W_{k\log p}}{
\|W_{k\log p}\|_{\mathrm{res}}}.
\]

But this weight or normalization must be derived from the source ordered-port
Green form.  It cannot be inserted merely to restore boundedness.

The Euler coefficient \(k^{-1}p^{-k/2}\) does not by itself remove the issue
when comparing normalized source fibers: it multiplies both analytic images
and cancels in the norm ratio.

## Revised completion gate

The earliest completion theorem is now:

> Prove that the source-authorized primitive/ordered-port metric on the
> arithmetic scale atom contains exactly the \(k\log p\) window-energy weight,
> and that this weighted metric is compatible with the constant cut-atom
> Green norm through the full source graph.

Only after this weighted primitive comparison is established may the ordered
linking polarization be tested for common-domain continuity and radical
descent on the resolved window carrier.

The differentiated front comparison remains useful as the boundary graph of
this missing primitive theorem.  Global closed range and the connected tail
remain open.  No RH conclusion is authorized.
