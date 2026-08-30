# The odd incidence has an exact shifted-Hilbert unitarization, but it is only a pullback metric

## Euler-loaded diagonal

Let

\[
Be_p=b_pe_p,
\qquad
b_p
=
2p^{-1/2}\sin\left(\frac{2\pi}{p}\right)
\]

on odd prime labels. The source estimates give

\[
c p^{-3/2}
\le
|b_p|
\le
C p^{-3/2}.
\]

On ordinary \(\ell^2(\mathbb P)\), \(B\) is trace class and not bounded below.

## Exact target metric

Define the weighted target Hilbert space

\[
\mathcal H_B
=
\left\{
y:
\sum_p\frac{|y_p|^2}{|b_p|^2}<\infty
\right\}
\]

with norm

\[
\|y\|_B^2
=
\sum_p\frac{|y_p|^2}{|b_p|^2}.
\]

Then

\[
\|Bx\|_B^2
=
\sum_p
\frac{|b_px_p|^2}{|b_p|^2}
=
\sum_p|x_p|^2.
\]

Therefore

\[
B:
\ell^2(\mathbb P_{\mathrm{odd}})
\longrightarrow
\mathcal H_B
\]

is unitary.

Its inverse is the coordinatewise map \(b_p^{-1}\) from \(\mathcal H_B\) to the ordinary source Hilbert space.

## Physical order of the target

Since

\[
|b_p|^{-2}\asymp p^3,
\]

the target metric is uniformly equivalent to

\[
\ell^2(\mathbb P_{\mathrm{odd}},p^3).
\]

Thus Euler-loaded odd transport is an isometry after a \(3/2\)-order Hilbert shift.

This is the Hilbert-scale counterpart of its exact Köthe automorphism with inverse order loss \(3/2\).

## Metric transport equation

Let \(G_{\mathrm{src}}=I\) and

\[
G_{\mathrm{tgt}}
=
\operatorname{diag}(|b_p|^{-2}).
\]

Then

\[
B^*G_{\mathrm{tgt}}B
=
G_{\mathrm{src}}.
\]

So the simultaneous metric equation is solved exactly for this one arrow.

Reciprocal transport \(B^{-1}\) is unitary in the reverse typed direction.

## Why this does not close passive dilation

The target metric was defined by pulling the source metric through \(B\). Every injective arrow admits such a formal metric on its range.

Therefore this identity proves:

- a precise compatible Hilbert scale exists;
- the required order shift is \(3/2\);
- no additional defect channel is needed for this isolated arrow.

It does not prove that the metric is independently authorized by the Green, wall, seam, or Tate source.

A passive-dilation theorem requires one metric field compatible with all admitted constructors, not a separate pullback metric fitted to each arrow.

## Failure of uniform equivalence

Relative to ordinary target \(\ell^2\),

\[
G_{\mathrm{tgt}}
\asymp
\operatorname{diag}(p^3).
\]

Hence

\[
\|G_{\mathrm{tgt}}\|=\infty
\]

on the unweighted completion, and the two Hilbert metrics are not uniformly equivalent.

This is not a problem if source and target are declared as different typed rungs. It is fatal if the passive network claims one common unweighted energy space.

## Composition gate

Let \(T\) be the next constructor after \(B\). To remain lossless on the shifted target, it must satisfy

\[
T^*G_{\mathrm{next}}T
=
G_{\mathrm{tgt}}.
\]

Choosing a fresh pullback metric for \(T\) always solves this locally, but arbitrary iteration may drift through unbounded order shifts.

The nine-operation domain therefore needs a common invariant order region or bounded intensive order orbit. The single-arrow solution does not provide it.

## Relation to determinant geometry

As an operator

\[
B:\ell^2\to\ell^2,
\]

the map is trace class and determinant-suitable.

As an operator

\[
B:\ell^2\to\mathcal H_B,
\]

it is unitary but no longer compact in the typed operator sense.

These are two realizations of the same source arrow for different purposes. The determinant and energy functors must not silently exchange their target metrics.

## Exact status of the SCC slot

For the formal constructor

\[
\texttt{valuation\_fock\_passive\_dilation},
\]

the current result supplies a candidate typed metric for the odd incidence component.

The slot remains open because the following are not proved:

1. independent source authority for \(G_{\mathrm{tgt}}\);
2. compatibility with seam and endpoint metrics;
3. compatibility with Adams composition;
4. reciprocal and archimedean metric transport;
5. bounded order orbit for arbitrary admitted words.

## Hostiles

1. Treat a pullback metric as independent physical authority.
2. Claim uniform equivalence with unweighted \(\ell^2\).
3. Use the unitary shifted realization to claim trace class in the same category.
4. choose a new target metric after every composition without auditing order drift.
5. close passive dilation from one isolated metric equation.

## Verdict

The Euler-loaded odd incidence admits an exact source-to-target Hilbert unitarization, and the required target is a \(3/2\)-order shifted prime space.

This resolves the local metric equation but not the common passive network. The remaining obstruction is simultaneous source authority and bounded metric-order transport across all constructors.
