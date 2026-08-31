# Unbounded characteristic-zero quotient-class system for the marked K residual

## Theorem

For every even ambient degree A at least 12, every K-pole and every monomial exponent admitted at levels `(1,1,2,1,1)`, the K-derivative target has an exact rational `T+S_K+Q` contraction.

Start from the complete 90-target A12 exact family. Every later target is reached by a sequence of unchanged ambient inclusions and multiplication by either axis-square monomial. These maps commute with all source constructors for arbitrary admissible exponents.

For a target r, quotient the nonempty contraction fiber d^{-1}(r) by ker(d). The quotient is a singleton. Any two transition paths produce contractions of the same target and therefore the same quotient class. The two square maps commute, and their overlap differences are exact syzygies.

The transition category splits into eight directed components: two K poles times four exponent-parity classes. Each component has a singleton colimit class.

## Disposition

P5d3c2, P5d3, and P5d are completed for the marked K-residual family. The mechanism extends to all even A at least 12 as a source-natural, representative-independent characteristic-zero absorption-certificate system.

What survives is the canonical quotient class of contractions. What does not survive is a canonical coefficient word: the contraction torsor is nontrivial.

This theorem is restricted to the marked K-residual stratum. It does not by itself promote every rank-26 p-normal source family to characteristic zero. More importantly, it proves absorption rather than a surviving p-normal quotient line, so it cannot supply the required horn column or relative Bockstein.

The next programme leaf is P6a: determine whether any sourced quotient line remains outside the absorbed family.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_unbounded_quotient_colimit_gate.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_unbounded_quotient_colimit_gate.json`
