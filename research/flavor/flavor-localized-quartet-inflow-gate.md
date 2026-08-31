# Localized-quartet inflow gate: WP1057

## Question

What anomaly-inflow class does WP1056's one-quartet localization law require,
and can linear \(U(1)\) inflow select it?

## Branch charges

For

\[
SU(6)\rightarrow SU(4)\times SU(2)\times U(1),
\]

tracelessness fixes

\[
6=(4,1)_1+(1,2)_{-2},
\qquad
15=(6,1)_2+(4,2)_{-1}+(1,1)_{-4}.
\]

The WP1056 family branches therefore have dimension-weighted \(U(1)\) anomaly
contributions

\[
(6,8,1,4,2,4,2)
\;\longrightarrow\;
(12,-8,-4,-4,4,-4,4),
\]

whose total is zero.

## Inflow equation

For boundary anomaly \(b_0\) at endpoint \(0\), bulk anomaly \(B\), and
Chern–Simons level \(k_{\rm CS}\), WP755 gives

\[
A_0=b_0+\frac B2+k_{\rm CS},
\qquad
A_\pi=\frac B2-k_{\rm CS}.
\]

For WP1056's one-quartet cell, the boundary \(4\) has weighted anomaly
\(-4\), so the bulk has \(B=4\). Hence

\[
k_{\rm CS}=2.
\]

At the reflected endpoint the required class is \(-2\).

## Exact \(C=23\) cofiber

The three WP1056 subsets that leave \(C=23\) now separate by inflow and
ports:

| boundary | \(k_{\rm CS}\) | retained ports |
|---|---:|---:|
| \(4_a\) | \(2\) | \(2\) |
| \(4_b\) | \(2\) | \(2\) |
| \(2_a+2_b\) | \(-4\) | \(0\) |

All levels are integral. Thus linear \(U(1)\) inflow does not obstruct the
quartet law, but it also does not select it. A UV-fixed class \(k_{\rm CS}=2\),
together with the joint requirement \((C,k)=(23,2)\), would retain the
quartet cells and reject the doublet-pair hostile. A UV-fixed class
\(-4\) would instead retain the port-destroying hostile.

Adjacent localizations are exact:

\[
\begin{array}{c|c|c}
\text{boundary} & C & k_{\rm CS}\\
\hline
2 & 25 & -2\\
8 & 19 & 4\\
1 & 26 & 2
\end{array}
\]

The one-singlet cell shares the quartet's inflow level \(2\), but has
\(C=26\), so it fails the WP1036 capacity point.

## Boundary

This checker computes only the linear \(U(1)\) anomaly. The complete
non-Abelian, mixed, and gravitational anomaly lattice remains open. The next
source must derive the complete Chern–Simons level vector and endpoint
orientation from the compactification. The common pole clock, mass scale, and
WP802 interface also remain open.

## Classification

Conditional anomaly-inflow cofiber. It sharpens the missing one-quartet law
into a fixed-level requirement and rejects the false claim that branch
dimensions alone are a localization selector.

Checker: `research/flavor/checkers/wp1057_localized_quartet_inflow_gate.py`

Result: `results/wp1057_localized_quartet_inflow_gate.json`
