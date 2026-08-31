# Residue obstruction for the logarithmic denominator primitive

## Question

Does the negative denominator-gate result persist beyond the bounded rational ansatz?

## Claim boundary

This packet proves a local punctured-bidisc obstruction. It does not exclude relative Čech boundary maps, resolved/Rees exceptional generators, or a full Cayley--Menger face mapping cone whose face residue changes the target complex. It does not construct a physical period.

## Disposition

Work at the normal crossing

\[
u=q_1=0,
\qquad
v=q_2=0,
\qquad
q_3=p+u+v,
\]

with \(p\) a unit. The denominator target is

\[
p\eta=\frac{p\,du\wedge dv}{uv(p+u+v)}.
\]

Its double residue along \(u=v=0\) is the constant term of

\[
\frac{p}{p+u+v},
\]

hence equals \(1\). Over \(\mathbb F_{101}\) and \(\mathbb F_{103}\), setting \(p=1\) gives the same residue.

For any Laurent one-form

\[
A\,du+B\,dv,
\]

one has

\[
d(A\,du+B\,dv)=(\partial_uB-\partial_vA)du\wedge dv.
\]

The coefficient of \(u^{-1}v^{-1}\) in a Laurent derivative is always zero: a \(B\)-term would need an exponent \(u^0v^{-1}\), but differentiating in \(u\) multiplies it by zero; an \(A\)-term would need \(u^{-1}v^0\), but differentiating in \(v\) multiplies it by zero. The checker verifies this termwise on a symmetric Laurent support window over both finite fields; the argument is exponent-local and therefore not bounded by that window.

Therefore \(p\eta\) is not exact in the punctured-bidisc logarithmic denominator carrier. This independently strengthens the previous denominator-gate no-go: the failure is a residue obstruction, not just a failed low-depth ansatz.

The remaining possible enlargements must alter the complex, not merely enlarge ordinary Laurent pole depth: a relative Čech boundary map, a resolved/Rees exceptional generator, or a full Cayley--Menger face mapping cone with compensating face residue.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_log_denominator_residue_obstruction.py`

Result:

- `research/voevodsky/results/cosmology_log_denominator_residue_obstruction.json`

Command:

- `python research/voevodsky/check_cosmology_log_denominator_residue_obstruction.py`
