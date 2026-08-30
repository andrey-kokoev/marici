# Rank-four amplitude to the photon Bell packet

Let

\[
\mathcal A\in
V_1^*\otimes V_2^*\otimes V_3\otimes V_4
\]

be the fixed-kinematics rank-four polarization amplitude.  Once oriented null
kinematics supplies the helicity frames, an incoming preparation \(++\) gives
the canonical contraction

\[
\mu_{h_3h_4}
=
\mathcal A(e_+,e_+;e^{h_3},e^{h_4}).
\]

No primitive section or basis-dependent quotient is chosen: this is evaluation
in the two incoming factors and the helicity decomposition in the outgoing
factors.

For identical parity-symmetric photons, the Sinha--Zahed amplitude table gives

\[
(\mu_{++},\mu_{+-},\mu_{-+},\mu_{--})
=(\Phi_1,\Phi_5,\Phi_5,\Phi_2).
\]

This is the exact symmetry reduction.  Parity, identical-particle symmetry,
and crossing do **not** set \(\Phi_5\) to zero.  The further two-term state

\[
\Phi_1|++\rangle+\Phi_2|--\rangle
\]

uses the source's low-energy dynamical approximation \(\Phi_5\simeq0\).

Applying the CGLMP/MES analyzer packet to the full four-component state gives

\[
I=
\frac{2\sqrt2(\Phi_1\bar\Phi_2+\Phi_2\bar\Phi_1)}
{|\Phi_1|^2+|\Phi_2|^2+2|\Phi_5|^2}.
\]

At \(\Phi_5=0\), this is exactly Equation (13) of Sinha--Zahed.  The checker
also verifies normalization and both no-signalling families directly from the
sixteen joint Born probabilities.

Reproduce with:

```text
uv run --with sympy python research/nima/check_rank_four_photon_bell_map.py
```
