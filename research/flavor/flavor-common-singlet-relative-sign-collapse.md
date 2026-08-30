# Common-singlet relative-sign collapse

## Bounded question

Does WP632's abstract relative sign survive the full legal field-rephasing
group and the exact two-stage messenger matching to the faithful flavor
quotient?

## Full rephasing group

The diagonal parity used in WP632 is only one symmetry of the interaction
incidence. Enumerate every independent sign redefinition of

\[
Q,H^u,H^d,\sigma,A^{u,d}_{L,R},B^{u,d}_{L,R},u_R,d_R,S,X
\]

that preserves all six route vertices and four singlet-generated messenger
masses. The projection of this full symmetry group onto the vacuum signs
\((H^d,\sigma)\) contains all four sign changes.

In particular, the down-sector rephasing

\[
H^d,A^d_L,A^d_R,B^d_L,B^d_R,d_R\longmapsto
-(H^d,A^d_L,A^d_R,B^d_L,B^d_R,d_R)
\]

holds \(\sigma\) fixed and preserves every interaction. It flips
\(\operatorname{sgn}(H^d)\operatorname{sgn}(\sigma)\). Therefore the two
WP632 relative classes are isomorphic once the full source-authorized
rephasing groupoid is used.

## Exact messenger matching

Tree elimination of the two messenger stages produces the down-sector
coefficient

\[
C_d=-{y_H^d y_S^d y_X^d\over z_A^d z_B^d\sigma^2}.
\]

The singlet sign cancels because two messenger denominators occur. Changing
the sign of the down entrance expectation value changes the sign of the
resulting down Yukawa matrix, but the legal rephasing \(d_R\mapsto-d_R\)
removes it. Singular values, the left-handed mixing matrix, CP invariants, and
therefore `physical16` are unchanged.

The first nonfaithful arrow is thus the quotient from the selected diagonal
parity groupoid to the full source rephasing groupoid. The later map to
`physical16` preserves that collapse.

## Disposition

WP632 remains a correct restricted-groupoid rigidifier, but its proposed
relative sign is not a physical selector. The existing common singlet does not
provide the independent reference required by WP631 because an additional
legal source symmetry moves between its relative classes.

A progressive reference must reduce the full rephasing group, not merely name
one diagonal subgroup. It needs a source-derived interaction whose incidence
is sensitive to the relative sign and whose matched observable survives all
quark and messenger rephasings. That requires either a closed interference
cycle with a rephasing-invariant phase/sign or an independently prepared
external reference experiment. Neither is present here.

## Reproduction

Run:

    python research/flavor/checkers/wp633_common_singlet_relative_sign_collapse.py

The generated result is
`research/flavor/results/wp633_common_singlet_relative_sign_collapse.json`.

