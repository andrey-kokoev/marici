# qRB character-weighted centered Gaussian target

Use the centered character-weighted probe

$$
 h_{t,d}(u)=e^{-tu^2}e^{-idu}.
$$

Its endpoint half-sum is

$$
\frac{h_{t,d}(i/2)+h_{t,d}(-i/2)}2
=e^{t/4}\cosh(d/2).
$$

Unlike the shifted real Gaussian, this probe is the correct spectral representative of a translate Gram entry. Its Fourier transform is a translated centered Gaussian, so the prime terms acquire the character factor associated with the translation difference `d`.

The completed source target must therefore be evaluated by the endpoint, gamma, and prime terms using `h_(t,d)`, not by substituting `xi=d` into the shifted-Gaussian formula. Those two probes are not identical.

Status: correct probe and endpoint normalization derived; full gamma/prime polarization formula remains to be expanded and compared with the relative linking block.
