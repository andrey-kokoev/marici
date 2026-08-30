# The Positive-Mode Wronskian Is a Uniformly Oriented Pair-Separation Current

## Labelled exponential source

Consider a finite positive mode packet

\[
f(q)=\sum_n c_ne^{-\alpha_nq},
\qquad
c_n>0,
\qquad
0<\alpha_1<\cdots<\alpha_N.
\]

For the second-order homotopy sector,

\[
K_z(q)
=
\sum_n
\frac{c_n}{\alpha_n^2-z^2}e^{-\alpha_nq}.
\]

Write

\[
b_n(z)=\frac{c_n}{\alpha_n^2-z^2}.
\]

## Pair expansion of the Wronskian

The diagonal modes make no contribution to

\[
J(K)=\operatorname{Im}\langle DK,K\rangle.
\]

Combining the two orientations of every unordered pair gives

\[
J(K)
=
\sum_{m<n}
\frac{\alpha_m-\alpha_n}{\alpha_m+\alpha_n}
\operatorname{Im}
\left(b_m\overline{b_n}\right).
\]

For real positive `c_n`, this simplifies exactly to

\[
J(K)
=
-\operatorname{Im}(z^2)
\sum_{m<n}
\frac{
c_mc_n(\alpha_m-\alpha_n)^2
}
{
|\alpha_m^2-z^2|^2
|\alpha_n^2-z^2|^2
}.
\]

Since

\[
\operatorname{Im}(z^2)
=
2\operatorname{Re}(z)\operatorname{Im}(z),
\]

every pair carries the same orientation.  The current vanishes for one mode
and becomes strictly nonzero as soon as two distinct positive modes are
present away from either coordinate axis.

## Meaning

The odd PV/Wronskian port is a labelled pair-separation current.  It measures
neither individual mode mass nor an arbitrary phase.  Its numerator is the
squared separation

\[
(\alpha_m-\alpha_n)^2.
\]

This is the same structural pattern previously found in the theta curvature
measure: diagonal source data are neutral, while relational separation creates
the order-two current.

Thus the orientation instrument is not merely present in the five-cell.  On a
positive exponential cone, the source labels orient it coherently before
aggregation.

## Remaining inequality

Substitution into the face difference yields

\[
\Delta_{\mathrm{face}}
=
2\operatorname{Re}(z)
\left(
|K_z(0)|^2
-4\operatorname{Im}(z)^2S_z
\right),
\]

where `S_z` is the nonnegative pair-separation sum displayed above without
the factor `Im(z^2)`.

The RH-shaped burden on this cone is therefore the single explicit inequality

\[
|K_z(0)|^2
\mathrel{?\ge}
4\operatorname{Im}(z)^2S_z.
\]

This is now finitely falsifiable at any mode count.  It must not be assumed
from the uniform sign of `J`; endpoint amplitude and pair separation are
independent quantities.

## Scope boundary for theta

The actual completed theta forcing is superexponentially decaying but is not
yet proved to be a positive mixture of the modes used here.  Polynomial
prefactors can introduce signed derivative modes.  Therefore this theorem is
a candidate positive cone and an exact explanation of its orientation, not
yet a theorem about the full theta source.

The next attack is to determine whether theta forcing belongs to the closure
of this positive cone under the source-authorized differential operations, or
to exhibit the first signed mode that violates it.

## Result

For positive exponential packets, the Wronskian/PV current is a uniformly
oriented sum of squared label separations.  This is the first source-level sign
law for the missing orientation port.  The remaining work is an explicit
endpoint-dominance inequality and a cone-membership audit for the theta
forcing.

