# 1784 — The Five-Site Hessian Multiplicity Is Corrected to One in (x)

## Defect

The authoritative Symbolica elimination in Entry 1777 defines

\[
R=d_{ei}^2-\frac{25}{2}x.
\]

The auxiliary Python saturation and Hessian audits instead used

\[
R_{\rm wrong}=d_{ei}^2+d_{ej}^2-\frac{25}{2}x.
\]

That convention mismatch did not alter the qualitative generic-simplicity
claim, but it made Entry 1780 report the compatible total-energy factor as
(x^2=t^4).

## Repair

The saturation, Hessian, and real-branch checkers now use the exact same
(R) as the source-derived Symbolica elimination. All three were rerun from
their frozen inputs.

For every one of the six labelled representatives:

- the zero-distance and zero-multiplier obstructions remain nonzero;
- the second transverse-Hessian factor still has gcd degree zero;
- the first factor has pairwise resultant gcd degree one;
- same-critical-point compatibility leaves exactly

\[
\boxed{x=t^2.}
\]

## Corrected conclusion

Entry 1780 is superseded only in its multiplicity statement:

\[
x^2=t^4
\quad\longrightarrow\quad
x=t^2.
\]

Its support classification survives unchanged. The only compatible deeper
Hessian locus is still the already frozen total-energy point (t=0), and no
nonzero coefficient divisor or carrier stratum is added.

Entries 1779 and 1782 also survive: every degree-six divisor is generically
Morse, so the six free (C_5)-orbits still assemble thirty local Morse lines.

## Evidence

- `research/benincasa/checkers/five_site_disjoint_mixed_pair_saturation.py`
- `research/benincasa/checkers/five_site_disjoint_mixed_pair_hessian.py`
- `research/benincasa/results/five-site-disjoint-mixed-pair-saturation.json`
- `research/benincasa/results/five-site-disjoint-mixed-pair-hessian.json`
- allocator claim: `seqclaim-80eb92a720460619e8b34935`
