# The equal Bunch--Davies node pair has odd e6 component

The split infinity fiber at \(E=0\) has two components

\[
C_+:W=xt^2+y,
\qquad
C_-:W=-(xt^2+y),
\]

meeting at the two nodes \(t=\pm i\sqrt{y/x}\). Their component difference

\[
d_\infty=[C_+]-[C_-]
\]

is an integral primitive class in the saturated invariant lattice. This supplies a geometric Betti normalization of the source \(e_6\)-line:

\[
e_{6,\mathrm B}:=d_\infty.
\]

At either individual node, the local sheet-difference co-core represents the half-class

\[
\frac12e_{6,\mathrm B}.
\]

This is the geometric content of the source de Rham coefficient \(-1/2\); its sign depends on orientation conventions, but its denominator records that one node sees half of the global component difference.

The Bunch--Davies based-path calculation proved that the two exchanged node arcs carry the same orientation. Therefore their global sum is

\[
\frac12e_{6,\mathrm B}
+rac12e_{6,\mathrm B}
=e_{6,\mathrm B},
\]

not zero. Consequently the paired cusp thimble has odd coefficient along the geometrically normalized \(e_6\)-line:

\[
\langle 2m,e_6^\vee\rangle\equiv1\pmod2.
\]

This is the first direct mod-two intersection calculation. It does not follow from choosing among four labels: it follows from three geometric facts—two nodes on one split fiber, primitive component difference, and equal Bunch--Davies orientation.

The conclusion fixes only the first bit. In the ordered geometric/source convention where the first coordinate is the component-difference \(e_6\)-line,

\[
a=1.
\]

The second pairing with \(v_{\rm alg}^\vee\) remains to be constructed. Its natural geometric support is the two-component divisor

\[
E^4-X_1^2X_2^2
=(E^2-X_1X_2)(E^2+X_1X_2)
\]

that defines the \(v_{\rm alg}\) quotient connection.

Certificate:

- `research/voevodsky/checkers/paired_nodes_fix_e6_parity.py`;
- `research/voevodsky/results/paired_nodes_fix_e6_parity.json`.
