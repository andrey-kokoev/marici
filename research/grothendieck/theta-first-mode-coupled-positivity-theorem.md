# First-mode coupled positivity theorem

## Universal theorem

Let \((X,\mu)\) be a measure space, let \(K:X\times X\to\mathbb R\) be
measurable, and let

\[
\Phi(x)=\sum_{n\geq1}\phi_n(x),\qquad \phi_n(x)\geq0.
\]

Assume that the higher-mode tail obeys the pointwise source bound

\[
0\leq R(x):=\frac{\sum_{n\geq2}\phi_n(x)}{\phi_1(x)}\leq\rho
\]

wherever \(\phi_1>0\).  Define

\[
I_1=\iint K(x,y)\phi_1(x)\phi_1(y)\,d\mu(x)d\mu(y),
\]

and

\[
A_1=\iint |K(x,y)|\phi_1(x)\phi_1(y)\,d\mu(x)d\mu(y).
\]

Then

\[
\boxed{
\iint K(x,y)\Phi(x)\Phi(y)\,d\mu(x)d\mu(y)
\geq I_1-(2\rho+\rho^2)A_1.
}
\]

Consequently,

\[
I_1>(2\rho+\rho^2)A_1
\]

implies strict positivity of the full coupled source expectation.

### Proof

Write \(\Phi=\phi_1(1+R)\).  The product perturbation is

\[
\Delta(x,y)=(1+R(x))(1+R(y))-1
            =R(x)+R(y)+R(x)R(y),
\]

so \(0\leq\Delta\leq2\rho+\rho^2\).  Therefore

\[
\begin{aligned}
\iint K\Phi\Phi
&=I_1+\iint K\phi_1\phi_1\Delta\\
&\geq I_1-\iint |K|\phi_1\phi_1\Delta\\
&\geq I_1-(2\rho+\rho^2)A_1.
\end{aligned}
\]

No sign assumption on an individual higher-label orbit is used.  This is why
the theorem survives the negative \(\{(1,2),(2,1)\}\) falsifier.

## Theta-source tail order

For the labelled theta source used here, put \(y=\pi e^{2r}\).  Directly from
the source formula,

\[
\frac{\phi_n(r)}{\phi_1(r)}
=n^2\frac{2n^2y-3}{2y-3}e^{-(n^2-1)y}.
\]

For every \(n\geq2\) and \(y\geq\pi\), its logarithmic derivative is

\[
\frac{2n^2}{2n^2y-3}-\frac{2}{2y-3}-(n^2-1)<0.
\]

Indeed,

\[
\frac{n^2}{n^2y-3/2}<\frac1{y-3/2}.
\]

Thus every higher-to-first mode ratio decreases with \(r\geq0\), and the
tail-ratio supremum is source-forced to occur at \(r=0\).  This turns the
functional domination problem into a one-dimensional rapidly convergent
theta tail.

## Hostile-point diagnostic

At \((a,b)=(1,11)\), integrating through six canonical bands gives

\[
I_1\approx2.0709409897502165\times10^{-3},
\]

\[
A_1\approx4.6779629630142566\times10^{-1},
\]

and the source ratio through labels \(2\) to \(19\) is

\[
\rho\approx2.176061157485408\times10^{-3}.
\]

Hence

\[
(2\rho+\rho^2)A_1
\approx2.038121828739195\times10^{-3}<I_1.
\]

The remaining margin is approximately \(3.28\times10^{-5}\).  This explains
how the full source can remain positive while its first asymmetric exchange
orbit is negative: lowest-mode positivity dominates the entire coupled theta
tail, but only narrowly under this deliberately absolute perturbation norm.

These hostile-point values are converged quadrature, not interval-certified.
A proof application requires certified enclosures for \(I_1\), \(A_1\), and
the infinite tail \(\rho\).  The theorem itself is algebraic and unconditional.

## Falsifier and next gate

For any proposed parameter region, the theorem fails to certify positivity at
the first point where

\[
I_1-(2\rho+\rho^2)A_1\leq0.
\]

This is a fixed, source-normalized falsifier.  The next global question is
whether the normalized first-mode margin \(I_1/A_1\) admits a uniform lower
bound exceeding the source constant \(2\rho+\rho^2\) throughout the remaining
outer quadrant.

## Global scan: the absolute-norm route is not uniform

A fixed-physical-domain scan answers that question negatively.  The integration
range was chosen as

\[
0\leq d\leq \lceil3b/\pi\rceil\pi/b,
\]

so it does not shrink as frequency increases.  Representative normalized
margins are

\[
\begin{array}{c|rrrr}
 &b=8&b=11&b=16&b=24\\ \hline
a=0.1&6.83\!\times10^{-3}&4.49\!\times10^{-4}&1.39\!\times10^{-6}&6.40\!\times10^{-10}\\
a=1&6.48\!\times10^{-2}&4.43\!\times10^{-3}&1.47\!\times10^{-5}&7.35\!\times10^{-9}\\
a=4&1.84\!\times10^{-1}&1.78\!\times10^{-2}&1.16\!\times10^{-4}&3.85\!\times10^{-8}.
\end{array}
\]

The source threshold is approximately
\(2\rho+\rho^2=4.35686\times10^{-3}\).  Hence no positive uniform lower bound
of the required size survives large \(b\).  The signed first-mode transform
oscillates toward zero while its absolute-kernel norm does not.

This does not falsify coupled positivity.  It falsifies the information-losing
step that replaces the perturbation transform by its absolute norm.  The live
large-frequency theorem must retain phase and compare the signed oscillatory
transform of each higher source mode directly with the first-mode transform.

The scan is diagnostic; very small large-frequency values require certified
oscillatory quadrature before their numerical scale is used quantitatively.

## Phase-aware scan: the privileged first mode also eventually fails

Direct signed-orbit comparison at \(a=1\) gives

\[
\begin{array}{c|rr}
b&I_{12+21}/I_{11}&I_{22}/I_{11}\\ \hline
8&-3.80\!\times10^{-4}&9.66\!\times10^{-8}\\
11&-7.82\!\times10^{-3}&1.10\!\times10^{-6}\\
16&-1.02\!\times10^{-1}&1.85\!\times10^{-4}\\
24&-1.055&1.079\!\times10^{-1}.
\end{array}
\]

At \(b=24\), the negative first exchange orbit is already larger in magnitude
than the first diagonal.  The second diagonal restores a small positive
two-mode partial sum.  Thus the fixed-first-mode phase-aware conjecture is also
falsified.

An interim scale-adaptive candidate was to define

\[
\Phi_N=\sum_{n=1}^N\phi_n.
\]

and let frequency choose a cutoff. The subsequent one-copy factorization and
boundary-jet audit show that this is not the canonical high-frequency
mechanism. The full infinite label sum cancels every odd folding jet by the
theta modular identity. Truncating before this sewing manufactures algebraic
Fourier tails that the completed source does not possess. See
`theta-modular-jet-sewing-mechanism.md`.

The earlier two-dimensional \(b=32\) binary64 sign is retracted as cancellation
error. Stable one-dimensional factorized quadrature keeps the completed
partial-source values positive through \(b=40\), while revealing cancellations
of nine decimal orders.

Artifacts:

- `checkers/theta_cross_label_orbit_compensation.py`
- `results/theta-cross-label-orbit-compensation.json`
- `checkers/theta_first_mode_margin_scan.py`
- `results/theta-first-mode-margin-scan.json`
- `checkers/theta_phase_aware_orbit_ratio_scan.py`
- `results/theta-phase-aware-orbit-ratio-scan.json`
