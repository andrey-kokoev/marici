# Localized-quartet \(SU(6)\) pole cell: WP1056

## Question

Can the existing minimal anomaly-free \(SU(6)\) family derive \(C=23\) and
\(k=2\) from one representation localization cell?

## Source family

WP775 supplies the minimal anomaly-free chiral \(SU(6)\) family

\[
15+2\overline6,
\qquad
A(15)+2A(\overline6)=2+2(-1)=0.
\]

Under \(SU(4)\times SU(2)\times U(1)\), its dimensional branches are

\[
15\rightarrow6+8+1,
\qquad
\overline6\rightarrow4+2.
\]

Thus the full family has degree

\[
6+8+1+(4+2)+(4+2)=27.
\]

## Joint localization cell

Localize exactly one of the two \(SU(4)\)-quartet branches on a boundary and
keep every other branch in the bulk. The bulk degree is

\[
C=27-4=23.
\]

The two remaining doublet branches, one from each \(\overline6\), provide the
two typed ports:

\[
k=2.
\]

With the \(SU(6)\) vector dimension \(N_V=35\), the bulk spectral index is

\[
\kappa=2+35-23=14>0.
\]

The WP1036 capacity coefficient is exactly

\[
h=\frac{12C\pi^2}{1367k}
 =\frac{138\pi^2}{1367}.
\]

## Exact \(C=23\) hostile

The coefficient \(C=23\) alone is insufficient. There are three exact
localization subsets whose removed dimension is four:

1. boundary \(4_a\), retaining ports \((p_1,p_2)\);
2. boundary \(4_b\), retaining ports \((p_1,p_2)\);
3. boundary both doublets \(2_a+2_b\), leaving \(C=23\) but \(k=0\).

The joint requirement \((C,k)=(23,2)\) rejects the third option. The first
two are exchange-symmetric; this packet does not choose between them.

Adjacent localization classes are exact:

\[
C=27\;(\text{full bulk}),\qquad
C=25\;(\text{one doublet boundary}),\qquad
C=23\;(\text{one quartet boundary}),\qquad
C=19\;(\text{both quartets boundary}).
\]

## Boundary

The remaining source gates are to derive the one-quartet boundary law, resolve
or quotient the symmetric quartet choice, derive the common pole clock and
mass scale, and derive the \(12\pi^2/1367\) interface from the same source.
This packet does not supply the chiral Standard Model embedding or a
`physical16` instrument.

## Classification

Conditional anomaly-localization constructor. It gives the integer-pole branch
an anomaly-complete \(SU(6)\) candidate that derives \(C=23\) and \(k=2\)
jointly from representation branching and localization, with a finite
port-destroying hostile.

Checker: `research/flavor/checkers/wp1056_su6_localized_quartet_pole_cell.py`

Result: `results/wp1056_su6_localized_quartet_pole_cell.json`
