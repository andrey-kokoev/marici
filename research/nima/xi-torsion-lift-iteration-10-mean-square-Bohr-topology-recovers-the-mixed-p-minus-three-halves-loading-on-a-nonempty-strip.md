# Xi-torsion lift iteration 10: mean-square Bohr topology recovers the mixed p-minus-three-halves loading on a nonempty strip

## Replace sup recovery by Besicovitch recovery

For an exponential sum with distinct real frequencies,

\[
G(R+it)=\sum_\nu d_\nu e^{R\lambda_\nu}e^{it\lambda_\nu},
\]

define the mean-square Bohr seminorm

\[
M_R(G)^2
=
\lim_{T\to\infty}
\frac1{2T}\int_{-T}^T|G(R+it)|^2dt.
\]

Orthogonality of distinct characters gives the exact Parseval identity

\[
M_R(G)^2
=
\sum_\nu|d_\nu|^2e^{2R\lambda_\nu}.
\]

Unlike the sup-norm coefficient estimate, this has no extra summation loss.
Shrinking gaps between logarithmic frequencies are irrelevant in the infinite
Bohr mean.

## Apply to the endpoint frequencies

Iteration 4 proved that the outgoing and reflected shell frequencies

\[
k\log q(p),
\qquad
k\log(p^2/q(p))
\]

are jointly distinct. Therefore the atomic endpoint coordinate satisfies exact
mean-square coefficient recovery after the opposite-chart inversion of
iteration 6.

For the outgoing part, Bertrand's bound `p<q(p)<2p` gives

\[
p^{2Rk}
\le q(p)^{2Rk}
\le 2^{2Rk}p^{2Rk}.
\]

At each fixed grade, the mean-square observer is equivalent to the weighted
`ell^2` coefficient norm. The grade attenuation handles summation in `k` under
the declared prime-power majorant.

## Mixed loading at the seam

For

\[
d_p=\frac12p^{-3/2-\sigma},
\]

the weighted square sum is

\[
\sum_p|d_p|^2p^{2\delta}
=\frac14\sum_pp^{-3-2\sigma+2\delta}.
\]

It converges whenever

\[
\delta<1+\sigma.
\]

In particular, at the seam `sigma=0` there is a nonempty recovery strip

\[
0\le\delta<1.
\]

This repairs the failed `ell^1` budget from iteration 9. No observer height
larger than the absolute-convergence width is required: the observer norm is
itself the weighted square coefficient norm.

## Strict horizontal topology

Equip the endpoint channel with the family `M_R` for `R` in compact
substrips of `R<1+sigma`, together with the bordered Green graph seminorms.
Parseval makes the labelled synthesis an isometry up to the explicit outgoing
and reflected normalization matrix. Hence its range is closed and the map is
strict.

Spectral differentiation multiplies coefficients by the frequency. For
`R<R'<1+sigma`,

\[
\lambda^n e^{R\lambda}
\le C_{n,R'-R}e^{R'\lambda},
\]

so every finite derivative is continuous with strip loss. The synthesis is
horizontal in the resulting analytic Silva scale.

## H-border membership

Under the mixed loading, the frozen coefficient packet belongs to every
weighted `ell^2` rung with `delta<1+sigma`. Since `H_border` is assembled from
that packet and the four-chart inverse exposes its endpoint characters,
`H_border` belongs to the mean-square Fourier-recoverable bordered range.

Under the superexponential loading it belongs a fortiori. Thus the previous
coefficient-selection fork no longer blocks recoverability, provided the
target retains the mean-square Bohr observer.

## Remaining qualifications

1. The infinite-time Bohr mean must be admitted as a continuous target
   observer, not inferred from a finite spectral window.
2. The exact grade-`k` loading must give the asserted square-summable majorant;
   the existing completion claims this qualitatively but does not display one
   formula for all grades.
3. The Xi-normal germ disk must lie inside the recovered strip. In the centered
   critical strip this has positive room, but the normalization must be stated.

## Next step

Construct the quotient in this mean-square bordered Silva topology and run the
Weyl--Cauchy torsion argument with explicit substrip radii. This should exclude
Xi torsion for every zero lying in the interior recovered strip.