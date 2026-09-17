# qRB microstep 50: canonical-loading selection test

For each candidate loading `omega_p`, define the assembled local readout

$$
\mathcal B_{\omega}(s)=\sum_p\omega_p(s)\,C_pX_p(s).
$$

The canonical loading must satisfy all three source identities:

1. **wall normalization:** its wall coefficient equals the declared half-density boundary term;
2. **mixed sewing:** its reciprocal difference equals `d log gamma_p` after summation;
3. **completion normalization:** its archimedean limit agrees with the fixed completed source form.

A candidate that merely converges but fails any one of these identities is an admissible analytic assembly, not the canonical spectral observer.

This gives a finite-to-infinite selection procedure: test the identities on finite prime packets, then pass to the limit using the established majorant.

Status: selection criterion isolated; no candidate has yet been source-identified as canonical.
