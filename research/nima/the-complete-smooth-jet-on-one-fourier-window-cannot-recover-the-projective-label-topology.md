# The complete smooth jet on one Fourier window cannot recover the projective label topology

## Question

Does observing every derivative of the deconvolved exponential sum on the fixed low-frequency window continuously recover the projective source coefficients?

## Claim boundary

No for the ordinary smooth compact-window topology. A single prime label escaping to infinity has unit size in one chosen projective coefficient seminorm while its deconvolved Fourier exponential and every fixed derivative tend uniformly to zero on the window. Algebraic faithfulness therefore does not become continuous recovery merely by retaining the full smooth jet.

## Escaping-label packet

Fix one projective source seminorm \(q_\delta\), with \(\delta>0\). Choose primes \(p_n\to\infty\), set

\[
L_n=\log p_n,
\qquad
a_n=e^{-L_n/2},
\]

and retain only the positive orientation and primitive grade. Define

\[
c_n=e^{-\delta L_n}.
\]

The packet has exactly one nonzero coefficient, so

\[
q_\delta(c^{(n)})
=e^{\delta L_n}|c_n|
=1.
\]

It does not converge to zero in the projective source topology.

## Deconvolved observation

After division by the nonvanishing theta factor on the source-fixed window, the observed exponential sum is

\[
F_n(\xi)
=a_nc_ne^{i\xi L_n}
=e^{-(\delta+1/2)L_n}e^{i\xi L_n}.
\]

For every fixed derivative order \(j\ge0\),

\[
\sup_{|\xi|\le r_0}|F_n^{(j)}(\xi)|
=e^{-(\delta+1/2)L_n}L_n^j
\longrightarrow0.
\]

Thus

\[
F_n\longrightarrow0
\quad\text{in }C^\infty([-r_0,r_0]).
\]

The same conclusion holds on every fixed real compact interval. Multiplication or division by the smooth theta factor on the protected window does not change it.

## Consequence

If a continuous recovery map

\[
\mathcal R_{\rm win}:
C^\infty([-r_0,r_0])
\supset\operatorname{ran}(C\mathcal I)
\longrightarrow\mathcal A_{\exp}
\]

existed with \(\mathcal R_{\rm win}F_c=c\), then continuity would force

\[
q_\delta(c^{(n)})
=q_\delta(\mathcal R_{\rm win}F_n)
\longrightarrow0,
\]

contradicting \(q_\delta(c^{(n)})=1\). Therefore no such continuous inverse exists.

This hostile uses neither prime-gap clustering nor cancellation between labels. The Euler half-density coefficient itself hides labels escaping to large logarithmic displacement from every fixed-order derivative probe.

## Required observer strength

A continuous post-codiagonal recovery topology must include displacement-sensitive growth. Candidate seminorms must see at least the exponential cost of translating a label, for example through:

- full-history exponential weights in the physical displacement variable;
- Fourier observation on complex horizontal lines whose height varies with the requested source seminorm;
- a Wiener-type coefficient norm authorized independently of the desired inverse;
- retention of the original label projections.

The ordinary compact-open entire topology also needs care. On a complex strip \(|\operatorname{Im}z|\le R\), the same packet has size

\[
e^{-(\delta+1/2-R)L_n}.
\]

Strips with \(R>\delta+1/2\) detect it, whereas bounded real-window jets do not. This identifies the missing datum as vertical exponential growth, not derivative order alone.

## Direction rescore

- Recovery from a complete smooth jet on one real window: disproved, 0/10.
- Recovery from arbitrary fixed real compact windows: disproved, 0/10.
- Recovery from an all-strip entire-growth topology: 8/10; topology comparison remains.
- Recovery from the existing exponentially weighted full-history topology: 9/10; requires proving that codiagonal synthesis reflects those weights.
- Retaining the labelled recovery port: already completed and remains the safest G4 architecture.

## Disposition

The depth-first window-jet route fails continuously despite algebraic uniqueness. The productive successor is to compare the common-history exponential-weight seminorms with complex-strip growth of the deconvolved Fourier sum. If that comparison fails, G4 must retain the labelled port or add an independently authorized observer norm. No RH or closed-range conclusion is authorized.
