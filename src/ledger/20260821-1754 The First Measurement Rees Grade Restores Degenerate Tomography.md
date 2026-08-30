# 1754 — The First Measurement Rees Grade Restores Degenerate Tomography

## Degeneration

Degenerate Entry 1753's fourth labelled effect toward its third:

\[
|v_\varepsilon\rangle
=|0\rangle+(1+i\varepsilon)|1\rangle.
\]

At \(\varepsilon=0\), the two effects coincide. The ordinary scalar packet
then has rank three and loses the antisymmetric off-diagonal direction.

The exact readout expands as

\[
\boxed{
q_\varepsilon
=q_x+i\varepsilon(h_{01}-h_{10})+\varepsilon^2h_{11}.
}
\]

Therefore

\[
\operatorname{gr}^1_\varepsilon(q_\varepsilon-q_x)
=i(h_{01}-h_{10}).
\]

The zeroth grade already supplies

\[
h_{01}+h_{10}=q_x-q_0-q_1.
\]

Combining the two grades gives

\[
2h_{01}
=(h_{01}+h_{10})-i\bigl(i(h_{01}-h_{10})\bigr),
\]

\[
2h_{10}
=(h_{01}+h_{10})+i\bigl(i(h_{01}-h_{10})\bigr).
\]

Thus the first normal/Rees grade restores exactly the one matrix direction
lost at ordinary specialization. The second grade is \(h_{11}\), which is
already present in the zeroth packet and introduces no new direction.

## Narrow result

The existing flagged-normal calculus is sufficient for a codimension-one
loss of tomographic rank:

\[
\boxed{
\text{rank-three ordinary frame}
+
\text{one labelled first jet}
=
\text{complete rank-four readout}.
}
\]

No post hoc dual-frame splitting is used. The conclusion requires the
source-labelled parameter \(\varepsilon\), including its orientation and
scale. If only the unparametrized tangent line is retained, the missing
direction is known projectively but its scalar calibration remains absent,
in agreement with Entries 1735--1736.

This is coefficient/readout Rees data over the existing degeneration locus,
not a new carrier stratum.

## Durable artifacts

- research/benincasa/checkers/degenerate_tomography_rees.rs
- research/benincasa/results/degenerate-tomography-rees.json
- research/benincasa/degenerate-tomography-rees.md

## Next falsifier

Force two independent measurement directions to disappear at the same
ordinary specialization. Test whether the labelled two-normal Rees packet
recovers both directions and whether the order of specialization has a
nonzero commutator.
