# Unit-panel Bernstein bound closes the two-prime finite gamma matrix

Split `[0,250]` into 250 unit panels. On each panel choose the Bernstein
ellipse with semiminor `0.2`, hence

\[
\rho=1.477032961426901.
\]

The ellipse remains in `|Im u|<=0.2`, so for

\[
z=1/4+iu/2
\]

one has `Re z>=0.15`. The Binet integral bound

\[
|\psi(z)-\log z|\le(\Re z)^{-1}
\]

and `|u|<=250.3` bound the normalized gamma multiplier. Cauchy--Schwarz on
the normalized compactly supported Legendre functions gives

\[
|\widehat\phi_n(u)|\le\sqrt{2L}e^{L|\Im u|}.
\]

At `L=.55`, the product of two amplitudes times the normalized multiplier is
bounded by `3` uniformly in the basis orders. The standard analytic
Gauss--Legendre remainder bound, summed over 250 panels at order 48, is

\[
2.544\times10^{-13}.
\]

Arb node evaluation contributes radius at most

\[
1.092\times10^{-17}.
\]

Thus every finite-gamma entry has total radius below

\[
2.545\times10^{-13}<2\times10^{-11}.
\]
