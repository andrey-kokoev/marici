# Reciprocal Wiener–Hopf factorization still needs the Green orientation sign ledger

The scalar identity

$$
R(z)+R(-z)=\Xi(z)^2
$$

is exact. It does not by itself identify the resulting boundary with a positive sum of two Green energies.

The two terms correspond to opposite spectral resolvents:

$$
R(z)\leftrightarrow(\partial_q+z)^{-1},
\qquad
R(-z)\leftrightarrow(\partial_q-z)^{-1},
$$

up to the chosen reflection of the spatial orientation. Their polarized Green coefficients may therefore be

$$
z+\overline w
\quad\text{and}\quad
-(z+\overline w),
$$

rather than two copies with the same sign.

Spatial reflection changes the boundary concomitant sign, while spectral reflection changes the bulk coefficient sign. These two changes can cancel or reinforce depending on the declared reciprocal port convention. Consequently the required typed calculation is:

| sector | differential pencil | stable endpoint | forcing transform | boundary sign | bulk coefficient |
|---|---|---|---|---|---|
| `+` | declared `D_+(z)` | declared wall | `-R(z)` | to compute | to compute |
| `-` | declared `D_-(z)` | declared wall | `-R(-z)` | to compute | to compute |

Only if the completed port metric converts the doubled bulk into

$$
(z+\overline w)
\left(
\langle G_w^+,G_z^+\rangle+
\langle G_w^-,G_z^-\rangle
\right)
$$

does Xi-square boundary vanishing imply seam confinement by positivity.

If instead the result is the difference of the two tail Grams, cancellation can occur off seam and no confinement follows. Abstract reciprocal symmetry cannot decide this sign.

Thus the newly proved Xi-square factorization closes the scalar boundary divisor gate, but the decisive remaining computation is the signed integration-by-parts table for the two actual stable-history pencils and their endpoint port metrics.

Status: scalar boundary factorization closed; positive doubled Green orientation not yet established.
