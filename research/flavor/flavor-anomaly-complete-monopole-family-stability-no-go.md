# Anomaly-Complete Monopole Family and Stability No-Go

## Question

Can the anomaly-complete six-dimensional matter sector remove WP791's free
charge choice and thereby make the same chiral monopole select three physical
families without sacrificing orientation selection, stability, or the physical
scale?

## Claim boundary

The admitted source is the anomaly-free
\(E_7\times E_6\times U(1)_R\) gauged-supergravity compactification on
\(\operatorname{Minkowski}_4\times S^2\), with an integral monopole of strength
\(n\) embedded in

\[
E_6\supset SO(10)\times U(1).
\]

This is deliberately narrower than all six-dimensional compactifications. It
tests the anomaly-complete successor naturally adjacent to WP791. It does not
grant authority to orbifolds, negative-tension defects, additional fluxes, or
an independently chosen matter charge.

In this source, the charged \(E_6\) gaugino zero modes comprise

\[
N_{\mathrm{fam}}=2|n|
\]

chiral \(SO(10)\) spinor families. Consequently every integral flux sector has
even family multiplicity. The equation \(2|n|=3\) has no integral solution.

The complete charged gauge-fluctuation analysis supplies the independent
source stability gate

\[
|N^I|\leq 1
\]

for every charged gauge direction in the sphere compactification. On the
standard one-parameter \(E_6\) embedding this leaves the nonzero stable sectors
\(n=\pm1\). Each contains exactly two families. The next flux magnitude gives
four families and fails the stability gate:

\[
\begin{array}{c|c|c}
|n| & N_{\mathrm{fam}} & S\\
\hline
1 & 2 & 1\\
2 & 4 & 0
\end{array}
\]

Here \(S=1\) denotes stability and \(S=0\) denotes instability.

There is a second typing obstruction. WP791's BPS orientation selector uses
the monopole in the gauged \(U(1)_R\) direction. The \(E_6\) monopole that
generates the \(SO(10)\) families is a different source embedding and breaks
that supersymmetry. Coordinate compatibility between their flux integers does
not define a constructor joining the two experiments.

This packet therefore does not prove that every anomaly-complete
compactification forbids three generations. It proves that the canonical
anomaly-free successor to Salam--Sezgin cannot supply the desired joint
constructor: the stable branch selects two, the desired odd multiplicity is
absent, and the family-producing embedding does not preserve the BPS
orientation mechanism.

## Exact hostile test

The smallest falsifier is already \(n=1\). It is stable and source-admitted,
but its index yields two families. Increasing to \(n=2\) does not approach
three: it yields four and introduces the charged-vector instability. No tuning
of a continuous coupling changes this parity obstruction.

The apparent escape through large negative-tension branes is not admitted.
It changes the source domain and relaxes the stability condition by adding a
new defect constructor. It would still leave the even index formula and would
require independent authority for the defect tensions, chirality, modulus
lifting, and detector channel.

## Classification

- The anomaly-complete fluctuation family is physically source-authorized.
- It selects a stable two-family subdomain.
- It neither selects three families nor preserves WP791's BPS orientation
  selector in the same embedding.
- It leaves the classical scale modulus and hence the portal magnitude free.
- Its zero-mode count is a topological readout, not a calibrated
  physical16 flavor instrument.

This is a Deutschian negative explanation: representation branching and the
charged-vector spectrum make the stable two-family result hard to vary. For
the observed flavor problem it is a refutation, not the desired explanation.

## Disposition

Close the canonical anomaly-complete \(E_6\) monopole branch as a joint
three-family selector. The positive successor must make an odd index three,
orientation, modulus lifting, and charged-spectrum stability consequences of
one source embedding. Only after that source packet exists is it meaningful to
test its RG basin, finite thresholds, and calibrated descent to physical16.

Verification:

- checker:
  research/flavor/checkers/wp792_anomaly_complete_monopole_family_stability_no_go.py
- generated result:
  research/flavor/results/wp792_anomaly_complete_monopole_family_stability_no_go.json
- exact invocation:
  uv run --with sympy python research/flavor/checkers/wp792_anomaly_complete_monopole_family_stability_no_go.py
- primary stability source:
  [Parameswaran, Randjbar-Daemi, and Salvio](https://arxiv.org/abs/0706.1893)
- original anomaly-free model:
  [Randjbar-Daemi, Salam, Sezgin, and Strathdee](https://doi.org/10.1016/0370-2693(85)91040-3)
