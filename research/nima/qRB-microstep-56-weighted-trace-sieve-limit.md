# qRB microstep 56: weighted trace of the sieve limit

The prime half-density estimate gives a continuous sampling map on the wall carrier:

$$
\|\bigl(p^{-1/2}f(\log p)_{\rm avg}\bigr)_p\|_{\ell^2}
\le C\|f\|_{\rm wall}.
$$

Therefore, if the sieve differences satisfy

$$
\|S_S-\phi_1\|_{\rm wall}\to0,
$$

then their weighted prime traces converge in `ell2`:

$$
\bigl(p^{-1/2}S_S(\log p)_{\rm avg}\bigr)_p
\longrightarrow
\bigl(p^{-1/2}\phi_1(\log p)_{\rm avg}\bigr)_p.
$$

This is the exact bridge from prime-sieve convergence to a spectral boundary observer. The missing input is wall-norm convergence, stronger than source `L1` or finite derivative `L1` convergence.

Status: trace upgrade reduced to one wall-norm estimate; not yet claimed proved.
