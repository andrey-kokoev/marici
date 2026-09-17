# Fixed-width Gaussian translates are jointly faithful

Fix

$$
g_\sigma(x)=e^{-\sigma x^2},\qquad \sigma>0.
$$

Use all translated observations

$$
B_a(T)=\langle T,g_\sigma(\,\cdot-a)\rangle,
\qquad a\in\mathbb R.
$$

If every observation vanishes, then

$$
B_a(T)=0
$$

for every `a`, equivalently

$$
T*\check g_\sigma=0.
$$

Fourier transformation gives

$$
\widehat T\,\widehat g_\sigma=0.
$$

The Gaussian transform is

$$
\widehat g_\sigma(\xi)
=
\sqrt{\frac{\pi}{\sigma}}
 e^{-\xi^2/(4\sigma)},
$$

which is nonzero at every real `xi`. Local division by this smooth nonvanishing function gives

$$
\widehat T=0,
$$

and therefore

$$
T=0.
$$

Thus one fixed Gaussian width, with all translates retained, is jointly faithful on tempered distributions. Equivalently, its translates have dense linear span in `L2(R)`.

For the `qRB` tower this closes the abstract observer-separation requirement: two continuous completed coherencers that agree under every translated Gaussian observer are equal.

It does not prove that the source-derived Weil form is positive on this family. The remaining arithmetic condition is positivity of every finite translate Gram matrix

$$
\bigl[Q(T_{a_i}g_\sigma,T_{a_j}g_\sigma)\bigr]_{i,j}.
$$

It also does not by itself verify the external normalization identifying the coded form `Q` with the authoritative completed Weil form.
