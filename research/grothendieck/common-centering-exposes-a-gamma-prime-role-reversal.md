# Common centering exposes a gamma--prime role reversal

## Question

Does the common-center rank-two chart isolate a uniformly positive sector contribution across the gamma sign crossing?

## Common-center identity

For total localizer moments `A_k=g_k+p_k` and a real center `r`, define

\[
C_r=A_2-2rA_1+r^2A_0,
\qquad
B_r=A_1-rA_0.
\]

Then

\[
D_2=A_0C_r-B_r^2.
\]

The centered quadratic splits linearly:

\[
C_r=C_r^\Gamma+C_r^{\mathbb P}.
\]

Choosing a rational `r` near `A_1/A_0` makes `B_r` small without dividing intervals.

## Intermediate box

At `(t,h)=(0.01,0.005)`, choose `r=0.342`. The scan gives

\[
C_r^\Gamma\approx-2.0536\times10^{-3},
\qquad
C_r^{\mathbb P}\approx+3.4120\times10^{-3},
\]

so

\[
C_r\approx1.3584\times10^{-3}.
\]

The centered linear residual is only

\[
B_r\approx1.11\times10^{-6}.
\]

Prime curvature repairs negative gamma curvature.

## Larger-heat box

At `(t,h)=(0.05,0.01)`, choose `r=0.989`. The signs reverse:

\[
C_r^\Gamma\approx+3.8003\times10^{-4},
\qquad
C_r^{\mathbb P}\approx-3.5068\times10^{-4},
\]

leaving

\[
C_r\approx2.9342\times10^{-5}.
\]

Here

\[
B_r\approx3.83\times10^{-7}.
\]

Gamma curvature repairs negative prime curvature even though the uncentered gamma initial difference is itself negative.

## Consequence

Common centering gives a stable polynomial certificate across the scalar gamma sign crossing, but it does not reveal one uniformly positive sector. The sector supplying positive centered curvature changes with heat scale.

A uniform proof must therefore control the sum `C_r^Gamma+C_r^P` as one source object. Fixed assignments such as “gamma background, prime correction” or “prime background, gamma correction” fail across the sampled regimes.

## Exact certificate target

For rational centers selected on parameter boxes, certify

\[
A_0>0,
\qquad
A_0(C_r^\Gamma+C_r^{\mathbb P})>B_r^2.
\]

This avoids sector slope divisions and remains valid when `g_0` changes sign. The center may vary by declared parameter box; it is a proof coordinate, not a source decomposition.

## Boundary

The values are uncertified. The common-center identity residual was below `10^-52`, but finite gamma and prime evaluations still require outward rounding.

## Disposition

Use common-centered total curvature for rank-two certification. Record the observed gamma--prime role reversal as a falsifier of every uniform one-sector-background argument.