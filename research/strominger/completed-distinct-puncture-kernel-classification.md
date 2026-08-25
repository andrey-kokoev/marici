# Distinct puncture magnetic jets have no local grade-three kernel

> Scope refinement: `p^4-q^4` is the principal symbol of the local scalar
> magnetic projection after identifying opposite spin frames. It proves the
> finite point-jet statement below. It is not the symbol of the unprojected
> global paired spin-four bundle map; the latter and its smooth low-mode kernel
> are classified in `global-grade-three-spin-spectrum.md`.

## Theorem

Fix finitely many distinct labelled punctures and any finite source-jet bound
`J`. Retain the complete local principal-part and delta-jet target. Then the
grade-three map restricted to the magnetic parity sector is injective:

\[
 \boxed{\ker(\widetilde{\mathfrak M}_3|_{\mathcal H_{P,Q=-1}^J})=0.}
\]

Consequently the full completed source kernel before gauge/period quotient is
exactly the electric parity sector:

\[
 \boxed{\ker\mathfrak M_3=\mathcal H_{P,Q=+1}^J.}
\]

The statement persists under the strict LF union over finite `J`.

## Principal-symbol proof

Near one puncture, encode a finite point-supported source jet by

\[
 T(p,q)=\sum_{r+s\leq J}c_{rs}p^rq^s,
\]

where `p` and `q` represent holomorphic and antiholomorphic derivatives of a
delta function. At highest filtration order:

- the Green inverse contributes `(pq)^(-1)`;
- `D_z^2` and its conjugate produce the two helicity shears;
- the magnetic grade-three curl contributes
  `q p^5-p q^5`.

The composed principal symbol is therefore

\[
 \boxed{P(p,q)=p^4-q^4.}
\]

If a nonzero source jet were killed, take its highest homogeneous part
`T_top`. The highest output filtration would be

\[
 (p^4-q^4)T_{\rm top}=0.
\]

But `C[p,q]` is an integral domain and `p^4-q^4` is nonzero. Hence
`T_top=0`, a contradiction. Sphere-connection and Green-background terms
have lower filtration order and cannot alter this leading argument.

This proof is stronger than ellipticity: `p^4-q^4` has characteristic lines,
but no nonzero finite polynomial jet can be supported on them algebraically.
Characteristic-wave solutions may exist in larger function spaces; they are
not finite point-supported source jets.

## Several distinct punctures

Point-supported distributions at different punctures form a direct sum. A
distribution supported at `xi_i` cannot cancel one supported at `xi_j` for
`i!=j`. The one-puncture injectivity theorem therefore applies blockwise for
arbitrary finite labelled configurations.

Conservation restriction cannot create a kernel because restriction of an
injective map remains injective. Antipodal matching also preserves the result
because its adapter is invertible. Gauge and contour quotients can create
later aliases, already classified as exact-form and higher-jet losses.

## Kernel taxonomy at this stage

| source/readout stage | kernel |
|---|---|
| completed two-chart transport | `0` |
| joint electric-magnetic port | `0` |
| magnetic projector | electric `Q=+1` sector |
| grade-three map on magnetic finite jets | `0` |
| distinct-support direct sum | `0` additional |
| period-only quotient | exact/higher-pole classes |

Thus there is no distinct-puncture interior circuit analogous to `E_2`.

## Evidence

`checkers/completed_distinct_puncture_kernel_checks.py` constructs the sparse
integer multiplication matrix for `p^4-q^4`, verifies full column rank through
jet bound 20 and puncture multiplicity 10, checks the Hilbert-filtration
dimension law, and tests that characteristic factors do not become finite
polynomial annihilators.
