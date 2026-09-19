# The Sokhotski half-jump has the Wronskian quarter-column normalization

## Convention

Use

\[
\frac1{x+i0}=
\operatorname{pv}\frac1x-i\pi\delta_0,
\qquad
\frac1{x-i0}=
\operatorname{pv}\frac1x+i\pi\delta_0,
\]

and retain the `C34` prefactor `1/(2 pi i)`. For a smooth diagonal coefficient
`f`, the two ordered boundary values are

\[
q_+=\frac1{2\pi i}
\operatorname{pv}\!\int\frac{f(t)}{t-t_0}\,dt
-\frac12f(t_0),
\]

\[
q_-=\frac1{2\pi i}
\operatorname{pv}\!\int\frac{f(t)}{t-t_0}\,dt
+\frac12f(t_0).
\]

Hence

\[
q_+-q_-=-f(t_0),
\qquad
\frac12(q_+-q_-)=-\frac12f(t_0).
\]

## Comparison with the retained odd column

The ordered-history port has opposite endpoint values. Its jump is twice its
single oriented endpoint amplitude. The retained Wronskian column is

\[
j_\theta=\frac14S_{\rm ord}.
\]

Therefore applying the quarter-column to the full ordered-history jump gives
exactly one half of the residue amplitude, with the sign determined by whether
`q_+-q_-` or `q_--q_+` is declared positive.

With the convention above and positive jump `q_+-q_-`, the real odd coordinate
is

\[
j_{C34}=-\frac12f(t_0),
\]

which matches the retained Wronskian half-amplitude. The skew-Hermitian
coordinate

\[
\frac1{2i}(q_+-q_-)
\]

is the same real odd line after the standard multiplication by `-i`; it is not
an additional normalization.

## Consequence

The pole anomaly and retained Wronskian odd port agree in magnitude. Their sign
is fixed by the declared ordering of the two boundary placements and cannot be
fitted after evaluation. Reversing placement reverses both signs.

Thus the local wall/jump packet, including the Schur half-amplitude, is sewn.
The remaining comparison is global and Hermitian: equality between the
polarized signed Tate wall current and the independently retained positive
Green bulk current.