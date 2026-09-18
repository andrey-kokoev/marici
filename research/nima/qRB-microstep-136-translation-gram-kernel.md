# qRB microstep 136: translation-Gram kernel

For fixed-width translated source Gaussians, the spectral product is a centered Gaussian multiplied by a character depending on the translation difference. Therefore the correct Gram kernel has the form

$$
K_t(a,b)=\mathcal K(t,a-b),
$$

where `mathcal K(t,d)` is the endpoint–gamma–prime target for the centered character probe.

Ordinary Gaussian-translate positivity requires every finite Toeplitz matrix

$$
\bigl[\mathcal K(t,a_i-a_j)\bigr]_{i,j=1}^r
$$

to be positive semidefinite.

The two-point condition is

$$
\mathcal K(t,0)\ge|\mathcal K(t,a-b)|.
$$

This is different from midpoint positivity for shifted spectral Gaussians. The two tests must not be conflated.

Status: correct translation-Gram kernel identified; all finite Toeplitz positivity remains open and is the genuine spectral observer gate.
