# Grade `-1` sewn Čech class independent of `q_g2` normalization

## Question

Does the grade `-1` pair formed by the `q_g1` and `q_g3` wall occurrences define a nonzero sewn class without using the missing grade-changing normalization for `q_g2`?

## Construction

Let `C_1` and `C_3` denote the normalized wall components supporting `q_g1` and `q_g3`. Retain the source-oriented leading forms

\[
\omega_1=
-\frac{a+p}{2p(a-p)^2(a+3p)(a^2+(4\kappa-5)p^2)}\,da,
\]

\[
\omega_3=
-\frac{d\xi}{64p^4(\kappa-\xi)(\xi+1)}.
\]

Their common node is represented by `a=-3p` on `C_1` and `xi=-1` on `C_3`. The exact residue census gives

\[
\operatorname*{Res}_{a=-3p}\omega_1
+
\operatorname*{Res}_{\xi=-1}\omega_3=0.
\]

Thus `(omega_1,omega_3)` lies in the kernel of the oriented node-residue boundary map

\[
\Omega^1_{C_1}(*D_1)\oplus\Omega^1_{C_3}(*D_3)
\longrightarrow \mathbb C_{C_1\cap C_3}.
\]

This constructs a sewn grade `-1` Čech cocycle without adding, projecting, or renormalizing the grade `-2` `q_g2` occurrence.

## Nonvanishing

The `q_g3` component has nonzero opposite residues

\[
-\frac{1}{64p^4(\kappa+1)}
\quad\text{at }\xi=-1,
\qquad
\frac{1}{64p^4(\kappa+1)}
\quad\text{at }\xi=\kappa.
\]

Therefore `omega_3` is not a rational derivative. If the sewn pair were exact componentwise, its restriction to `C_3` would be exact, contradicting these residues. The cocycle defines a nonzero logarithmic sewn class for generic `p != 0` and `kappa != -1`.

## Separation from the normalization blocker

The construction is internal to grade `-1`. It does not compare `q_g2` with this class and supplies no map from grade `-2`. Consequently the missing epsilon/conductor normalization blocks completion of the three-occurrence sum but does not block the two-component sewn class.

## Strongest falsification attempt

A node-compatible pair could still be globally exact. The nonzero `q_g3` finite residues obstruct that possibility. A remaining failure mode is physical: the positive-cut cycle may pair trivially with this nonzero cohomology class.

## Disposition

The `q_g1`–`q_g3` occurrences define a nonzero grade `-1` sewn logarithmic class independently of the unresolved `q_g2` normalization. Positive-cut pairing and physical normalization remain separate gates.

## Evidence

- `research/nima/checkers/check_unsplit_wall_leading_residues.py`
- execution `structured_command_execution:e_30844_1788300082167812200_8`
- `research/nima/qG12-unsplit-leading-wall-log-sum.md`
