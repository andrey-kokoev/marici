# The all-prime odd incidence is Hilbert–Schmidt and the Euler-weighted version is trace class, but neither is coercive

## Primewise diagonal assembly

For each odd prime, the canonical parity-changing incidence has coefficient

\[
a_p
=
2\sin\left(\frac{2\pi}{p}\right).
\]

On the orthonormal prime-labelled odd and even port spaces, assemble

\[
D_{\mathrm{odd}}e_p=a_pe_p.
\]

Every \(a_p\) is nonzero, so \(D_{\mathrm{odd}}\) is injective on finite packets and on its natural Hilbert domain.

## Exact ideal class

The elementary bound

\[
|a_p|
\le
\frac{4\pi}{p}
\]

gives

\[
\sum_p|a_p|^2
\le
16\pi^2\sum_p\frac1{p^2}
<
\infty.
\]

Hence

\[
D_{\mathrm{odd}}\in\mathcal S_2.
\]

On the other hand,

\[
a_p\sim\frac{4\pi}{p},
\]

and Euler's divergence of the prime harmonic series gives

\[
\sum_p|a_p|=\infty.
\]

Therefore

\[
D_{\mathrm{odd}}\notin\mathcal S_1.
\]

The unweighted odd incidence is exactly Hilbert–Schmidt but not trace class.

## Primitive Euler loading

The primitive half-density multiplies the coefficient by \(p^{-1/2}\):

\[
b_p
=
p^{-1/2}a_p.
\]

Then

\[
|b_p|
\le
4\pi p^{-3/2},
\]

so

\[
\sum_p|b_p|<\infty.
\]

Thus the Euler-loaded odd incidence

\[
D_{\mathrm{Euler,odd}}e_p=b_pe_p
\]

is trace class.

This is a genuine analytic gain: the finite odd port can enter an ordinary determinant-class mixed block after Euler loading.

## Compactness no-go for observability

Both diagonal operators are compact because their coefficients tend to zero. An injective compact operator on an infinite-dimensional Hilbert space cannot be bounded below.

Explicitly,

\[
\|D_{\mathrm{odd}}e_p\|
=
|a_p|\longrightarrow0,
\]

and

\[
\|D_{\mathrm{Euler,odd}}e_p\|
=
|b_p|\longrightarrow0.
\]

Therefore neither operator supplies a completion-stable observer margin on the full prime-labelled odd carrier.

Trace-class improvement strengthens determinant typing while worsening any attempt to use the same geometry for coercivity.

## Range structure

Since every coefficient is nonzero, the range is dense in the diagonal coordinate closure. But it is not closed.

Indeed, a diagonal operator on \(\ell^2(\mathbb P)\) has closed range only when its nonzero coefficients are uniformly separated from zero. Here

\[
\inf_p|a_p|=0.
\]

Thus the odd incidence has:

- zero kernel;
- dense range;
- nonclosed range;
- compact completion;
- no bounded inverse on its range.

This is the precise completion defect.

## Collective compression cannot restore labels

A scalar or finite-rank collective observer may detect one coherent combination of odd prime ports. It cannot be bounded below on the full infinite-dimensional labelled carrier.

If the constructor family includes prime-support idempotents, the orthogonal prime directions remain declared source distinctions and cannot be quotiented merely because a collective observer ignores them.

A one-dimensional quotient is authorized only if every declared target operation annihilates its complement. Prime-labelled operations prevent that condition.

## Placement in the coefficient lenses

The odd incidence belongs naturally to the determinant lens:

\[
D_{\mathrm{Euler,odd}}\in\mathcal S_1.
\]

It does not belong to the coercive Green lens:

\[
\inf_{\|x\|=1}
\|D_{\mathrm{Euler,odd}}x\|
=
0.
\]

Therefore the same odd port can legitimately orient a determinant return while being unusable as one of the uniform global observability margins.

This separation mirrors the adelic vacuum sandwich: nuclear smoothing authorizes determinants but cannot prove lower-frame estimates.

## Consequence for the RH architecture

The primewise parity-flip programme has now closed three local questions:

1. the divisor-free odd source port exists;
2. the parity-changing incidence exists;
3. the Euler-loaded assembly is trace class.

What remains impossible in the raw prime Hilbert topology is uniform labelwise observability.

Any RH coercivity theorem must obtain its lower margin from the unsmoothed Green/incidence geometry or from a finite defect-space reduction proved independently. It cannot obtain that margin from the compact odd determinant channel.

## Hostiles

1. Infer a lower frame bound from injectivity.
2. Infer coercivity from trace class.
3. Replace the infinite labelled carrier by one collective scalar without a target-relative quotient theorem.
4. Use the inverse diagonal weights and ignore their unbounded growth.
5. Count the compact odd channel as one of the five global Green margins.

## Verdict

The all-prime odd parity flip has an exact operator-ideal classification:

\[
D_{\mathrm{odd}}\in\mathcal S_2\setminus\mathcal S_1,
\qquad
D_{\mathrm{Euler,odd}}\in\mathcal S_1.
\]

This makes it a strong determinant-construction channel and a provably inadequate coercive observer on the full prime-labelled completion.
