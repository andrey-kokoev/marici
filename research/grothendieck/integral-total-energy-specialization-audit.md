# Integral total-energy specialization audit

## Question

Do the supplied conductor Čech data and marked localization matrices determine the integral image of `g111_top` in the Picard lattice of the smooth degree-two del Pezzo surface?

## Claim boundary

The supplied data determine the primitive kernel

\[
\ker\begin{pmatrix}1&0&0\\0&1&0\end{pmatrix}=\mathbb Z g_{111,\mathrm{top}}
\]

and the primitive Picard class

\[
d_\infty=(3,-1,-1,-1,-1,-1,-1,-3)
\]

in the basis \((H,E_1,\ldots,E_7)\). They verify

\[
d_\infty^2=-6,\qquad K\mathbin{\cdot}d_\infty=0,
\qquad d_\infty\equiv-K\pmod 2.
\]

They do not supply a chain map from the normalization–conductor specialization complex to an integral Betti or Picard complex. Consequently the integer in

\[
g_{111,\mathrm{top}}\longmapsto n d_\infty
\]

is undetermined. In particular, the maps with \(n=1\) and \(n=2\) both satisfy every supplied lattice, kernel, orientation-up-to-global-sign, and rational-column statement once no Betti comparison identifies the rational coordinate `e6` with a fixed integral dual coordinate.

The coefficient \(1/[8(x+y)]\) belongs to the rational de Rham/connection presentation. It cannot determine \(n\) without an integral comparison map and its normalization. The rank-nine diagonal residue is a different block and has zero `e6` residue; it does not provide the missing marked rank-twelve top column.

## Strongest falsification attempt

The executable audit serializes the known specialization matrix, Picard intersection form, canonical class, conductor half-boundary, and the two rival integral maps \(n=1,2\). It verifies all stated identities and shows their distinguishing Smith factors are respectively 1 and 2. Thus the requested Smith form is itself contingent on the absent map.

The first missing typed object is an integral chain-level comparison

\[
C_{\mathrm{norm/conductor}}\longrightarrow C_{\mathrm{Betti}}(S_E\setminus D_\infty)
\]

that sends the ordered marked top generator to the chosen Picard marking and is compatible with specialization. Acceptance requires serialized chain groups and differentials for this map, verification of every comparison square, and a primitive integral basis comparison whose rationalization recovers the displayed de Rham column.

## Disposition

The requested determination `±d_infinity` versus `±2d_infinity` is blocked, not computed. No cusp parity follows from the supplied comparison. Independently, every split-bitangent component difference satisfies the geometric congruence \(d\equiv-K\pmod2\); this does not identify the marked source generator with that difference. Adjacent-cusp and symmetry transport are deferred because transporting an undetermined map cannot determine its divisibility.

Evidence: `research/grothendieck/checkers/check_integral_total_energy_specialization_audit.py` and `research/grothendieck/results/integral_total_energy_specialization_audit.json`.
