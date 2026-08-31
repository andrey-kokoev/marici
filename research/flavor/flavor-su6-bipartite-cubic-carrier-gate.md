# \(SU(6)\) bipartite cubic-carrier gate: WP1080

## Question

Does the \(SU(6)\) anomaly family supply Nima's bipartite alignment and
alternating cubic carrier signature?

## Branching

Use

\[
SU(6)\to SU(3)_A\times SU(3)_B\times U(1),
\qquad
6=(3,1)_1+(1,3)_{-1}.
\]

Then

\[
15=(3,3)_0+(\overline3,1)_2+(1,\overline3)_{-2},
\]

and each

\[
\overline6=(\overline3,1)_{-1}+(1,\overline3)_1.
\]

The seven branches have total dimension \(27\). The cubic anomalies vanish
separately on both \(SU(3)\) factors, and the dimension-weighted \(U(1)\)
anomaly vanishes.

## Carrier signature

The \(15\) contains the bifundamental

\[
(3,3)_0.
\]

In an aligned frame its coefficient matrix is the rank-three identity, so it
supplies a nondegenerate \(A\)-\(B\) pairing and directed cross-block.

Each \(SU(3)\) factor carries its invariant alternating cubic tensor
\(\epsilon_3\), with

\[
\epsilon_{123}=1,
\qquad
\epsilon_{213}=-1.
\]

Thus the group theory supplies the first four items in Nima's microscopic
search signature:

1. two three-state families;
2. a nondegenerate pairing;
3. alternating cubic carriers;
4. a directed cross-block.

## Remaining fiber

The exchange \(A\leftrightarrow B\) preserves the full branch multiset but
swaps the two carrier lines and reverses the \(U(1)\) charges. Separate
orientation of \(A\) versus \(B\) remains a discrete structure to fix.

The representation candidate still lacks:

- a temporal coherence process;
- ordered detector ports;
- a production/decay kernel;
- calibrated descent to physical16.

## Classification

Conditional \(SU(3)\times SU(3)\) bipartite carrier constructor. It gives
Nima's search signature an exact \(SU(6)\) representation candidate, but it
is not yet a mediator or physical16 channel.

Checker: `research/flavor/checkers/wp1080_su6_bipartite_cubic_carrier_gate.py`

Result: `results/wp1080_su6_bipartite_cubic_carrier_gate.json`
