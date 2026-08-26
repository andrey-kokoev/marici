# Boolean coincidence selector hierarchy (WP292)

## Pairwise closure fails

Let $F_i$ be the Boolean event that local selector margin $i$ fails. On
three labelled domains, compare the uniform even-parity and odd-parity laws.
Both give

\[
P(F_i)=\frac12,
\qquad
P(F_i\cap F_j)=\frac14
\]

for every label and pair. Thus all single and pairwise failure probes place
the packets in one contextual equivalence class.

Their triple coincidences differ:

\[
P_{\mathrm{even}}(F_1\cap F_2\cap F_3)=0,
\qquad
P_{\mathrm{odd}}(F_1\cap F_2\cap F_3)=\frac14.
\]

Consequently, global failure is $3/4$ for the even packet and 1 for the odd
packet. Pairwise covariance and pairwise coincidence are therefore
nonfaithful.

## Complete Boolean tower

For a finite labelled domain packet, inclusion-exclusion reconstructs global
failure from the complete coincidence tower:

\[
P\left(\bigcup_iF_i\right)
=\sum_{\varnothing\neq T}(-1)^{|T|+1}
P\left(\bigcap_{i\in T}F_i\right).
\]

This is the direct flavor transfer of the Boolean route-tower lesson: context
closure is not automatically faithful, but the complete finite labelled tower
is faithful for this declared Boolean packet.

## Instrument gate

Algebraic reconstructibility does not establish executable coincidence
control. A physical flavor implementation needs source-derived labels, common
clocks, finite detector resolution, and calibrated subtraction of accidental
coincidences at every required order. Without those, the tower remains a
mathematical distinguishing family rather than an admitted instrument.

Run `uv run --with sympy python
research/flavor/checkers/wp292_boolean_coincidence_selector.py` to regenerate
the exact tower audit.
