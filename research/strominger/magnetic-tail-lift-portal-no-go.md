# The known magnetic tail lift is transparent to the portal relation

The transfer from Kitaev's forcing-plus-endpoint theorem can be stated directly
for the magnetic Schur system.

For every integral collision block, write the tail equations and boundary jet as

\[
A x + Bc=0,
\qquad
j=Ec+Cx.
\]

Here \(c\) is the collision-core packet, \(x\) is the tail packet, \(A\) is a
square full-rank tail observation matrix, and \(E\) is the raw boundary block.
The forcing equation determines the unique tail lift

\[
x=-A^{-1}Bc.
\]

Substitution gives the effective boundary map

\[
j=\left(E-CA^{-1}B\right)c.
\]

The existing magnetic boundary-compatibility theorem proves, on all 345 exact
blocks with \(2\le g\le16\) and \(2\le d\le24\),

\[
CA^{-1}B=0.
\]

This is not because \(B\) or \(C\) vanishes. Reconstruction uses tail depths on
the left of the collision gap, while boundary visibility uses depths on the
right. Their supports are disjoint.

Consequently the known tail lift is uniquely reconstructible but portal
transparent:

\[
E-CA^{-1}B=E.
\]

It neither creates nor removes a collision relation.

The same conclusion holds for a minimal fractional extension if transport
preserves each affine exponent sector. A block-diagonal family

\[
F=\bigoplus_{\lambda}F_\lambda
\]

has

\[
\ker F=\bigoplus_{\lambda}\ker F_\lambda.
\]

Independent injective sector blocks cannot produce a cross-sector cancellation,
even after an invertible charge relabelling.

Therefore the missing portal tail cannot be a blockwise continuation of the
known magnetic tail. It must introduce a source-authorized off-diagonal term

\[
D_{\lambda\mu}:\mathcal G_\lambda\longrightarrow\mathcal T_\mu,
\qquad
\lambda\ne\mu,
\]

or a non-flat/nonfaithful construction with equivalent relational force.

This yields a precise contract for the next lift:

- forcing incidence between distinct affine sectors;
- an endpoint anchor fixing the homogeneous tail torsor;
- a charged line or bimodule typing the off-diagonal map;
- retention of both adjacent Tor grades on any defect support;
- a protected-readout descent test annihilating residual lift ambiguity.

The new constructor is not “fractional tail continuation.” It is
cross-sector tail sewing.

Replay:

\`python research/strominger/checkers/magnetic_tail_lift_portal_checks.py\`
