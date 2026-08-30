# The odd Adams ray has a bounded intensive order profile and is trace class at every grade

## Grade-\(k\) odd coefficient

Combine three source factors:

1. the Euler grade coefficient
   \[
   \frac1k p^{-k/2};
   \]
2. the canonical finite odd phase conversion
   \[
   a_p=2\sin\left(\frac{2\pi}{p}\right);
   \]
3. the prime-labelled parity port.

The resulting diagonal grade-\(k\) coefficient is

\[
b_{p,k}
=
\frac1k p^{-k/2}a_p.
\]

Since

\[
a_p\asymp p^{-1},
\]

we have

\[
|b_{p,k}|
\asymp
\frac1k p^{-(k/2+1)}.
\]

## Trace class at every positive grade

For every \(k\ge1\),

\[
\sum_p|b_{p,k}|
\le
\frac{C}{k}
\sum_p p^{-(k/2+1)}
<
\infty.
\]

Thus each odd grade operator

\[
D_k^{\mathrm{odd}}e_p=b_{p,k}e_p
\]

is trace class, including the primitive grade \(k=1\).

The odd phase conversion contributes one full prime-decay order and removes the primitive trace-class obstruction within this auxiliary channel.

This does not alter the ordinary even Euler primitive current, which remains distributional.

## Köthe inverse order

The inverse coefficient grows as

\[
|b_{p,k}^{-1}|
\asymp
k\,p^{k/2+1}.
\]

Hence the grade-\(k\) odd map is an automorphism of the projective exponential Köthe source with inverse order shift

\[
r_k=\frac{k}{2}+1.
\]

The scalar factor \(k\) does not change the prime order.

## Adams doubling law

Under the grade-doubling Adams arrow \(k\mapsto2k\),

\[
r_{2k}=k+1.
\]

But

\[
2r_k=k+2.
\]

Therefore

\[
r_{2k}=2r_k-1.
\]

The odd phase order is paid once per prime, not once per copied grade. Adams doubling improves the naive doubled budget by one order.

## Intensive order

Define

\[
\eta_k=\frac{r_k}{k}.
\]

Then

\[
\eta_k
=
\frac12+\frac1k.
\]

Along the doubling ray,

\[
\eta_{2^nk}
=
\frac12+\frac1{2^nk}
\longrightarrow
\frac12.
\]

Hence

\[
\sup_{n\ge0}\eta_{2^nk}
=
\frac12+\frac1k
<
\infty.
\]

The odd Adams ray has no topology-at-infinity runaway in intensive order.

## Consequence for constructor iteration

The earlier generic hostile

\[
\rho_{S^n}(\delta)=\delta+n
\]

does not occur for this source channel after grade normalization.

Raw inverse order grows linearly with grade because the physical Mellin scale grows linearly with grade. Relative to grade, the order remains bounded and converges to the half-density value \(1/2\).

This closes the order-profile component of completion for repeated Adams doubling on the odd channel.

## What remains open

Bounded intensive order does not prove:

- a source-authorized type-fiber Adams map;
- compatibility of the finite character conductor under \(k\mapsto2k\);
- operator-norm control of the Adams intertwiners;
- seam and endpoint naturality;
- convergence to an actual Adams-end object;
- a Green lower margin.

In particular, every \(D_k^{\mathrm{odd}}\) remains compact on the unweighted prime Hilbert space.

## Conductor typing

The parity coefficient \(a_p\) was derived from a conductor parameter \(\eta\) and its paired displacement \(h_\eta\). Adams grade changes the multiplicative valuation grade, not automatically the additive conductor.

The formula above assumes the odd conductor frame is transported unchanged along the Adams grade ray.

That assumption must be proved by a type-fiber law. If Adams also changes conductor, the sine coefficient and order profile must be recomputed.

## Determinant-line implication

Because every odd grade is trace class, the odd auxiliary determinant may be formed without the primitive–square–connected regularization split required by the even Euler carrier.

Therefore the odd port should remain a separate determinant line. Merging it with the even Euler logarithm before sewing would erase the distinction between:

\[
\text{distributional even primitive current}
\]

and

\[
\text{trace-class odd primitive incidence}.
\]

## Hostiles

1. Transfer the even primitive divergence to the odd channel despite its extra \(p^{-1}\) decay.
2. Treat raw order \(r_k\to\infty\) as topology runaway without dividing by grade.
3. assume conductor invariance under Adams without a type-fiber map.
4. infer Hilbert coercivity from trace class at every grade.
5. merge the odd determinant line into the even Euler scalar before reciprocal sewing.

## Verdict

The canonical odd phase improves every Euler grade by one prime-decay order. Consequently all odd grades are trace class.

Its Köthe inverse order is

\[
r_k=\frac{k}{2}+1,
\]

with bounded intensive profile

\[
\eta_k=\frac12+\frac1k.
\]

Thus repeated Adams doubling is topologically stable on the odd channel, conditional only on source-authorized transport of the additive conductor frame.
