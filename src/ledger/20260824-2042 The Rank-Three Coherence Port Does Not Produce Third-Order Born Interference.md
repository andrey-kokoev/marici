# The Rank-Three Coherence Port Does Not Produce Third-Order Born Interference

Entry 2039's nontrivial Bargmann/exterior port does not become an independent
cubic screen term.

For a common unnormalized quadratic readout

\[
p(S)=\left|\sum_{i\in S}\psi_i\right|^2,
\]

all Boolean-lattice Möbius coefficients above order two vanish.  In
particular,

\[
I_3
=p(123)-p(12)-p(13)-p(23)+p(1)+p(2)+p(3)-p(\varnothing)
=0.
\]

The same holds with path-record correlations because record overlaps only
modify pairwise coefficients.  The rank-three exterior port instead enforces
the positivity and consistency of the complete oriented pairwise coherence
packet.

Independent subset normalization can fake a nonzero \(I_3\).  The exact
checker exhibits this using

\[
\bar p(S)=\frac{p(S)}{2+p(S)}.
\]

Therefore Sorkin comparisons require one common unnormalized support/measure;
a projectively normalized statistic diagnoses a different physical object.

The checker verifies symbolic Möbius vanishing through order seven and passes
5/5 gates.

Artifacts:

- `research/nima/three-path-sorkin-readout-gate.md`
- `research/nima/checkers/check_born_mobius_interference_order.py`
- `research/nima/results/born-mobius-interference-order.json`

Sequence claim: `seqclaim-201a954cffdf25fccc672564`.

