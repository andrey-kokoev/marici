# Soft-channel degeneracy gate: WP1074

## Question

Does the common clock select a unique soft ratio-one physical16 production
channel?

## Branch candidates

WP1056's localized bulk branches are

\[
6+8+1+4+2_a+2_b,
\qquad
6+8+1+4+2+2=23.
\]

Under WP1060's common-twist admission, every branch has the same unit clock

\[
M^2=1.
\]

At each branch's own threshold,

\[
\frac{p^2}{M^2}=1,
\qquad
\frac{R(p^2)}{R(0)}=\frac{1}{1+p^2/M^2}=\frac12.
\]

Thus all six localized branches have the same ratio-one soft signature.

## Vector comparison

The first same-frame vector-KK port instead has

\[
\frac{p_1^2}{M^2}=4,
\qquad
\frac{R(p_1^2)}{R(0)}=\frac15.
\]

A two-port ratio instrument can therefore distinguish “soft branch” from
“vector branch,” but it cannot distinguish one soft branch from another.

## Exact hostiles

Without a source-to-physical16 coupling matrix, the current data do not
select:

- the localized quartet branch \(4\);
- the two doublet ports \(2_a+2_b\);
- the largest branch \(8\).

Choosing any of these from its dimension, localization history, or port count
would be transport rather than a production law.

## Boundary

The next source must derive production/decay couplings from the localized
brane system to physical16, including the gain and channel reweighting law.

## Classification

Soft-channel degeneracy gate. C1 is narrowed from a missing soft channel to a
missing coupling matrix among six exact degenerate soft candidates.

Checker: `research/flavor/checkers/wp1074_soft_channel_degeneracy_gate.py`

Result: `results/wp1074_soft_channel_degeneracy_gate.json`
