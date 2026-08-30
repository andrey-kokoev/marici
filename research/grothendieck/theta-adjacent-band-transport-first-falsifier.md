# The canonical adjacent-band shift fails on the central labelled fiber

Retain the positive folded theta labels

\[
 \Phi(u)=\sum_{n\ge1}\phi_n(|u|),\qquad \phi_n(r)>0
 \quad(r\ge0).
\]

For an ordered label pair `(n,m)`, the two-copy density in
`S=U+V`, `D=U-V` is

\[
 \rho_{nm}(S,D)
 =\frac12 e^{aS}
 \phi_n\!\left(\left|\frac{S+D}{2}\right|\right)
 \phi_m\!\left(\left|\frac{S-D}{2}\right|\right).       \tag{1}
\]

The Jacobian is `1/2`; the orientation is positive. Freeze the canonical
adjacent-band transport

\[
 T_b(S,D)=(S,D+L),\qquad L=\frac\pi b.                 \tag{2}
\]

It has Jacobian one and preserves the theta labels and midpoint coordinate.
Both trigonometric factors reverse sign. Consequently

\[
 K_{a,b}(S,D+L)
 =-\beta S\cos(bD)-\alpha(D+L)\sin(bD).                \tag{3}
\]

## First local failure

Work in the strict outer region `alpha>0` and restrict to the faithful
labelled fiber `S=0`. For `0<D<L`, sufficiently near zero,

\[
 K(0,D)=\alpha D\sin(bD)>0,
\]

whereas

\[
 K(0,D+L)=-\alpha(D+L)\sin(bD)<0.
\]

Pointwise domination of the transported negative contribution would require

\[
 \frac{\rho_{nm}(0,D+L)}{\rho_{nm}(0,D)}
 \le\frac{D}{D+L}.                                    \tag{4}
\]

But positivity and continuity of every folded theta label give

\[
 \lim_{D\downarrow0}
 \frac{\rho_{nm}(0,D+L)}{\rho_{nm}(0,D)}
 =\frac{\phi_n(L/2)\phi_m(L/2)}{\phi_n(0)\phi_m(0)}>0,
\]

while `D/(D+L)` tends to zero. Hence (4) fails for every ordered label pair
and every `a,b>0` with `alpha>0`.

## Classification

This finitely falsifies the source-normalized **pointwise adjacent-band shift
with fixed `S` and fixed theta labels**. It does not falsify:

- positivity of the integrated two-copy expectation;
- a canonical larger-block transport;
- a transport that moves `S` coherently with `D`; or
- a variation-diminishing theorem formulated after the exact conditional
  `S|D` integration while retaining label multiplicity.

The failed pairing must not be repaired by moving its band boundary or by
discarding the `S=0` fiber. Those would fit the transport to the desired
scalar answer. The next admissible branches are a predeclared larger canonical
block or a source-derived order that transports `(S,D)` jointly.

## Distinct surviving conjecture after conditional integration

The weaker conditional mechanism must be stated as a new conjecture. Define,
with labels retained,

\[
 W_{nm}(D)=\int_{\mathbb R}\rho_{nm}(S,D)\,dS,
 \qquad
 J_{nm}(D)=\int_{\mathbb R}S\rho_{nm}(S,D)\,dS.         \tag{5}
\]

After integrating `S|D`, the labelled contribution is

\[
 H_{nm}(D)=\beta J_{nm}(D)\cos(bD)
 +\alpha D W_{nm}(D)\sin(bD).                          \tag{6}
\]

The same fixed adjacent shift gives the exact paired residual

\[
\begin{aligned}
 R_{nm}(D)={}&H_{nm}(D)+H_{nm}(D+L)\\
 ={}&\beta\cos(bD)[J_{nm}(D)-J_{nm}(D+L)]\\
 &+\alpha\sin(bD)[D W_{nm}(D)-(D+L)W_{nm}(D+L)].       \tag{7}
\end{aligned}
\]

Unlike the pointwise theorem, (7) is not falsified by the `S=0` fiber. Its
first boundary requirement is

\[
 J_{nm}(0)\ge J_{nm}(L).                               \tag{8}
\]

Equation (8), followed by the sign of the full canonical block integral
`integral_0^L R_nm(D)dD`, is the next legitimate hostile test. It may use
monotone likelihood ratio or increasing curvature of the exact labelled
conditional law, but it may not change the shift or labels after inspection.

This result concerns a proposed cancellation mechanism, not the Pick
inequality itself. It neither proves nor disproves RH.

## Durable verification

- Checker: `checkers/theta_adjacent_band_transport_first_falsifier.py`
- Result: `results/theta-adjacent-band-transport-first-falsifier.json`
