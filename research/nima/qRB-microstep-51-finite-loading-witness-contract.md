# qRB microstep 51: finite loading witness contract

Canonical loading selection can begin with a finite prime set `F` and one regular source point `s_0`. For each candidate `omega`, compute

$$
\Delta_F^{(\omega)}
=
\sum_{p\in F}\omega_p(s_0)C_pX_p(s_0)
-
\mathcal B_{\rm declared}(s_0).
$$

A candidate survives the finite witness only if its wall, reciprocal, and completion components match the declared normalization on that packet. The infinite majorant then controls passage from `F` to all primes.

The witness is diagnostic: finite agreement cannot prove global canonicity, but finite disagreement rejects a candidate immediately.

Status: finite selection protocol specified; numerical execution awaits explicit normalized source values for `C_pX_p` and the declared target readout.
