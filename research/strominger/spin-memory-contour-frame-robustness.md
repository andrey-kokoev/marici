# Spin-memory contour frame robustness

## Typed norm

Use the standard orthonormal complex spherical-harmonic norm on

\[
V=\bigoplus_{l=2}^{4}\mathcal H_l
\]

and normalize the 45 physical contour delays by

\[
\|y\|_{\mathrm{port}}^2=\frac1\pi\sum_{p=1}^{45}|y_p|^2.
\]

The factor \(1/\pi\) only fixes units. It does not alter rank, condition
number, leverage, or the erasure conclusion.

Let \(T:V\to\mathbb C^{45}\) be the common-radius cap-contour map from the
finite apparatus. The nine-longitude Fourier transform splits its Gram
operator into five latitude blocks, indexed by \(|m|=0,\ldots,4\). Every
entry is algebraic and the block sizes are at most three.

## Exact frame theorem

Exact principal-minor checks give

\[
\frac{14875}{64}\|v\|^2
\leq \|Tv\|_{\mathrm{port}}^2
\leq \frac{49809375}{2048}\|v\|^2.
\]

Both bounds are attained. Hence

\[
\kappa(T)^2=\frac{56925}{544},
\qquad
\kappa(T)\approx10.229445.
\]

Thus timing noise \(e\) reconstructed by the canonical least-squares left
inverse obeys

\[
\|T^\dagger e\|
\leq \sqrt{\frac{64}{14875}}\,\|e\|_{\mathrm{port}}.
\]

This is a frame statement, not an inference from a preferred determinant.

## Two-erasure theorem

For a contour row \(t_p\), define its leverage relative to the full frame by

\[
h_p=t_p(T^*T)^{-1}t_p^*.
\]

Longitude symmetry makes leverage constant around each latitude ring. The
largest value occurs on the outer rings and is

\[
h_{\max}=
\frac{2596492565939373204341}{5394794373190978300116}
\approx0.481296<\frac12.
\]

If \(D\) is a deleted set, the whitened lost-frame operator is positive and
has trace \(\sum_{p\in D}h_p\). Therefore for \(|D|\leq2\),

\[
\left\|(T^*T)^{-1/2}T_D^*T_D(T^*T)^{-1/2}\right\|
\leq 2h_{\max}<1.
\]

Consequently every possible deletion of zero, one, or two contours preserves
rank 21. Uniformly over all such deletions,

\[
\|T_{D^c}v\|_{\mathrm{port}}^2
\geq
\frac{88291543074101452502375}
     {10154907055418312094336}\|v\|^2
>8.69\|v\|^2.
\]

This conclusion does not select particular healthy ports after seeing a
failure. It is universal over all pairs.

## Hostile boundary

The same trace certificate cannot be promoted to three erasures because

\[
3h_{\max}>1.
\]

That inequality is not evidence that some triple destroys faithfulness. It
only marks the exact boundary of the present proof constructor. A three-port
theorem requires either exact subset analysis or a sharper restricted frame
bound. Likewise, center displacement and unequal-radius errors require a
separate perturbation norm for the physical geometry; discrete erasure
robustness does not authorize those claims.

## Interpretation

The 45-port product geometry buys a definite operational resource: two
arbitrary contour failures can occur without losing any of the 21 magnetic
low modes. The redundancy is therefore not merely excess row count. It is a
certified distinction-preserving margin.
