# The extra `q_g2` soft grade is a nonexact logarithmic class

## Question

Does the grade `-2` leading `q_g2` wall form vanish under rational or relative exactness, or does it survive as a supported logarithmic class?

## Leading form

Using the positive exceptional square-root branch only to fix an overall sign, the grade `-2` coefficient is

\[
\omega_{g2}^{(-2)}=
-\frac{d\xi}
{16p^3(\kappa-1)(\xi+1)(\kappa+\xi)}.
\]

Changing the square-root branch multiplies the form and both residues by `-1`; it does not affect nonvanishing.

## Exact residue test

Execution `structured_command_execution:e_30844_1788299889702602400_7` gives

\[
\operatorname*{Res}_{\xi=-1}\omega_{g2}^{(-2)}
=-\frac{1}{16p^3(\kappa-1)^2},
\]

\[
\operatorname*{Res}_{\xi=-\kappa}\omega_{g2}^{(-2)}
=\frac{1}{16p^3(\kappa-1)^2},
\qquad
\operatorname*{Res}_{\infty}\omega_{g2}^{(-2)}=0.
\]

A derivative of a rational function has zero residue at every finite pole. Hence this one-form is not rationally exact for generic nonzero `p` and `kappa != 1`. Any compatible relative class maps to this nonzero meromorphic de Rham class under forgetting relative boundary data, so relative reduction cannot make it zero.

## Support typing

The two opposite residues connect distinct divisors:

- `xi=-1` is the soft endpoint `q_g1=0`;
- `xi=-kappa` is the reduced exceptional Cayley–Menger/conductor divisor on `q_g2`.

Thus the grade is a logarithmic endpoint-to-conductor class, not a bulk holomorphic class and not merely a higher-order exact pole.

## Strongest falsification attempt

The proposed failure mode was that the extra grade is an artifact of the rational presentation and disappears after relative reduction. The nonzero finite residues falsify rational exactness and any relative exactness compatible with the forgetful map. The surviving limitation is that this does not identify the class with the positive-cut cycle or determine analytic epsilon normalization.

## Collision locus

At `kappa=1` the two marked structures responsible for the coefficient collide and the generic residue formula diverges. That locus requires a separate rescaled normal chart; it is excluded rather than inferred by continuity.

## Disposition

The `q_g2` grade `-2` coefficient survives algebraic relative reduction as a nonzero logarithmic class, generically. Its physical normalization and pairing with the positive-cut generator remain unverified.

## Evidence

- `research/nima/checkers/check_qg2_extra_soft_log_class.py`
- `research/nima/qG12-exceptional-k-wall-valuations.md`
- `research/nima/qG12-sewn-wall-x1-soft-specialization.md`
