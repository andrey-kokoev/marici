# Directed bound for the angular quadratic IMS window

## Question

What rigorous localization constant follows from the angular normalization of the septic profile?

## Claim boundary

This packet gives a conservative composition bound. It does not certify the sharper numerical scout.

## Construction

For the septic smoothstep \(s\), define

\[
\rho_1(t)=\sin\left(\frac{\pi s(t)}2\right),
\qquad
\rho_2(t)=\cos\left(\frac{\pi s(t)}2\right).
\]

Then \(\rho_1^2+\rho_2^2=1\). Because the first three derivatives of \(s\) vanish at each endpoint, both windows extend as proper subordinate \(C^3\) cutoffs.

For \(f(u)=\sin(\pi u/2)\),

\[
\lVert f'\rVert_\infty\le\frac\pi2,
\quad
\lVert f''\rVert_\infty\le\frac{\pi^2}4,
\quad
\lVert f'''\rVert_\infty\le\frac{\pi^3}8.
\]

Combining these with

\[
\lVert s'\rVert_\infty=\frac{35}{16},
\quad
\lVert s''\rVert_\infty=\frac{84\sqrt5}{25},
\quad
\lVert s'''\rVert_\infty\le210
\]

gives

\[
B_{\rm ang}
=
\frac{\pi^3}{8}\left(\frac{35}{16}\right)^3
+
\frac{3\pi^2}{4}\left(\frac{35}{16}\right)
\left(\frac{84\sqrt5}{25}\right)
+
105\pi
\]

with \(\lVert\rho_1'''\rVert_1\le B_{\rm ang}\).

For two windows and two transitions of angular width \(h_\theta\),

\[
C_{\rm loc}^{\rm ang}(h_\theta)
\le
\frac{2\pi}{3h_\theta^2}B_{\rm ang}.
\]

Under \(\theta=\pi(x+L)/L\) and physical overlap \(h_x=L\), one has \(h_\theta=\pi\), so

\[
C_{\rm loc}^{\rm ang,norm}
\le
\frac{2}{3\pi}B_{\rm ang}.
\]

## Disposition

The angular quadratic profile supplies a convention-correct, denominator-free, directed IMS constant. Its certified bound must be compared with the finite low-block margin. The numerical scout \(9.84825790\) remains separate and non-directed.

## Verification

- `research/voevodsky/checkers/check_angular_quadratic_ims_bound.py`
- `research/voevodsky/results/angular_quadratic_ims_bound.json`
- `research/grothendieck/angular-septic-windows-reduce-the-quadratic-localization-budget.md`
