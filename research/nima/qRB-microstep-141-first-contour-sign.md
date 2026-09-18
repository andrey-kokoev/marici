# qRB microstep 141: first contour-crossing sign

For an upward contour shift crossing `u=i/2`, the rectangular residue theorem gives

$$
\int_{\mathbb R}F(u)\,du
-
\int_{\mathbb R+i\eta}F(u)\,du
=2\pi i\operatorname{Res}_{u=i/2}F,
$$

with `0<eta` beyond the pole. Using the residue `2i` and the explicit gamma prefactor `1/(4 pi)`, the correction to the shifted contour is

$$
-\frac{2\pi i}{4\pi}(2i)e^{-t(i/2-\xi)^2}
=+e^{-t(i/2-\xi)^2}.
$$

Thus the first upward crossing contributes a positive endpoint-shaped Gaussian term; downward crossing contributes its reflected counterpart with the opposite contour orientation.

The complete continuation must combine this residue with the polar endpoint term before any positivity interpretation.

Status: first contour sign fixed under the stated contour convention.
