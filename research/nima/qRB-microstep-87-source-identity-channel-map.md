# qRB microstep 87: source-identity channel map

The recovered compact source identity maps directly to the three qRB channels:

- `E(f)`: endpoint channel `B_end`;
- `G(f)`: regular archimedean channel `R_reg`;
- `P_L(f)`: finite prime translation channel `B_prime`.

Thus

$$
Q_L=E+G+P_L
$$

is an explicit finite regulated boundary observation, with the prime contribution written through translated source correlations.

The map preserves the required order: form the complete source expression first, then apply the finite-support Fourier/observer representation. It does not split the prime and gamma terms into independently positive pieces.

Status: internal channel identification closed; extending `P_L` to the full prime family and matching the relative wall Wronskian remains the next comparison.
