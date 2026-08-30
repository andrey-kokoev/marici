# The Actual Theta Source Enters the Local Two-Point Krein Negative Cone

## Exact root collapse

For two positive source samples at (0<u_1<u_2), choose the cross phase

\[
x(u_2-u_1)=\pi.
\]

The preceding two-atom Krein gate is negative exactly when the amplitude ratio (r=w_2/w_1) lies between

\[
r_-=
\frac{\sinh(yu_1)}{\sinh(yu_2)}
\qquad < \qquad
r_+=
\frac{\cosh(yu_1)}{\cosh(yu_2)}.
\]

These formulas follow from

\[
\sinh^2(y(u_1+u_2))
-\sinh(2yu_1)\sinh(2yu_2)
=\sinh^2(y(u_2-u_1)).
\]

## Infinitesimal slope corridor

Let (u_1=u), (u_2=u+d), and let the amplitude be a positive differentiable source (w(u)). Put

\[
k(u)=-\frac{d}{du}\log w(u).
\]

As (d) tends to zero, the forbidden amplitude interval becomes the exact local corridor

\[
y\tanh(yu)<k(u)<y\coth(yu).
\]

Thus pairwise Krein orientation is a comparison between source logarithmic decay and two hyperbolic connection slopes.

## Near-seam obstruction

For the completed theta source (w=\Phi), evenness gives (\Phi'(0)=0). Its strict decrease on the positive chart gives (k(u)>0) for sufficiently small positive (u), while continuity gives

\[
u k(u)\longrightarrow0.
\]

For any such (u) with (0<uk(u)<1), sufficiently small positive (y) satisfies

\[
y\tanh(yu)<k(u)<y\coth(yu).
\]

The reason is that the lower endpoint tends to zero and the upper endpoint tends to (1/u) as (y) tends to zero.

Therefore the actual theta source itself has arbitrarily narrow positive-chart two-point packets whose Krein contribution is negative at the matching high frequency (x=\pi/d).

## Consequence

This closes a stronger route than the amplitude hostile did. The exact theta coefficient law does not orient every adjacent pair separately. Any proof by source-normalized adjacent-pair domination, local acute-cone preservation, or coefficientwise positive crossing fails near the modular seam at high frequency.

The remaining mechanism must be nonlocal in at least one of these senses:

1. combine more than one adjacent source pair;
2. couple the positive and negative modular charts before taking signs;
3. use an all-label conservation law whose positive and negative local packets cancel only after global sewing;
4. retain a frequency-dependent boundary current that is invisible to a pairwise amplitude comparison.

This is not a counterexample to RH or to the global de Branges orientation. It proves that the global orientation, if true, cannot be assembled from independently nonnegative local two-point contributions.

## Verification

The checker `research/grothendieck/checkers/theta_local_krein_slope_corridor.py` evaluates the exact theta summands and their analytic derivatives. At (u=0.1), (y=0.2), and (d=10^{-4}), both the infinitesimal slope and the finite theta amplitude ratio lie strictly inside the forbidden interval.
