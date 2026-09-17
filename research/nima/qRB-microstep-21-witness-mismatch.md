# qRB microstep 21: one-witness mismatch certificate

For `f_0(x)=exp(-pi x^2)`, the residual is

$$
(UT_b-\tau_LU)f_0(u)
=e^{u/2}e^{-\pi(e^u-b)^2}-e^{(u+L)/2}e^{-\pi e^{2(u+L)}}.
$$

At `u=log b`,

$$
(UT_b-\tau_LU)f_0(\log b)
=b^{1/2}\left(1-e^{L/2}e^{-\pi b^2e^{2L}}\right),
$$

which is generically nonzero.

Thus the failure of strict identification is witnessed by one Gaussian evaluation, not merely by an abstract representation argument.

Status: strict window-to-theta identification rejected. The comparison packet must retain both affine actions.
