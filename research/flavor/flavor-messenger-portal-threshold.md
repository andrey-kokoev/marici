# Messenger-generated Higgs–flavon portal threshold

## Bounded source calculation

WP478 tests one color-degenerate singular channel of the renormalizable WP435
messenger chain. On constant real Higgs and flavon backgrounds, its chiral mass
matrix is

\[
\mathcal M=\begin{pmatrix}
0&y_Qh\\
y_\Phi\phi&M
\end{pmatrix}.
\]

Write `x=y_Q^2 h^2` and `z=y_Phi^2 phi^2`. The two squared singular values
have exact trace and determinant

\[
S=M^2+x+z,
\qquad D=xz.
\]

This is a source-derived threshold calculation. No flavor target, pole mass,
or detector record enters it.

## Exact finite mixed threshold

For the heavy squared singular value `lambda_+`, differentiate the fermionic
Coleman–Weinberg kernel

\[
F(\lambda)=\lambda^2
\left(\log{\lambda\over Q^2}-{3\over2}\right).
\]

At zero backgrounds the exact mixed derivative is

\[
{\partial^2F(\lambda_+)\over\partial x\partial z}=2.
\]

The light eigenvalue begins as `xz/M^2`, so its kernel starts beyond the local
`xz` order. Meanwhile

\[
\lambda_+^2+\lambda_-^2=S^2-2D
\]

has zero mixed derivative. Hence the mixed dimension-four threshold is finite:
there is no mixed ultraviolet counterterm in this bounded chain. Including
three colors gives

\[
\Delta V_{h^2\phi^2}
=-{3y_Q^2y_\Phi^2\over8\pi^2}h^2\phi^2.
\]

The sign is exactly the negative mixed sign in
`eta*(HdaggerH-a*sigma^2)^2`.

## Map to the selector coordinate

Let the full background/group normalization be
`phi^2=k_Phi sigma^2`. Matching the mixed term gives

\[
a_{\rm ind}={3k_\Phi y_Q^2y_\Phi^2\over16\pi^2\eta},
\]

and therefore

\[
c_{\rm ind}
={3k_\Phi y_Q^2y_\Phi^2
\over16\pi^2\eta g_F^2y^2}.
\]

The messengers thus generate the correct functional portal and its sign, but
they do not select the WP477 coordinate. The coefficient still depends on two
messenger Yukawas, the Higgs-square coefficient, the flavor gauge coupling,
the vacuum-geometry coefficient, and the full matrix normalization.

## Hostile pair and disposition

The admitted replacement `y_Q -> 2 y_Q` preserves all fields, gauge
representations, renormalizability, anomaly cancellation, and the messenger
matching grammar. It multiplies `c_ind` by four and divides the predicted
`g_F f/v` by two. This is the smallest exact falsifier of numerical selection
by the one-loop threshold alone.

WP478 is therefore a source-generated interaction rigidifier, not a numerical
selector. It has no detector instrument and adds no reference port. The next
constructor must derive the messenger Yukawas and scalar/gauge coefficients on
one complete fixed trajectory, perform the full matrix-valued threshold
matching, and prove the WP477 `beta_c=0` condition across decoupling.
