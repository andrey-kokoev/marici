# The RH scale cut and tail passivity compose to a lossless source cascade

Author: `marici.Nima`

Date: 2026-08-26

Status: exact cascade theorem and localization of the remaining supply defect

## First stage: source cut

Let the source cut be the isometry

\[
C_p:\mathcal S
\longrightarrow
\mathcal F\oplus\mathcal H_{\mathrm{seam}},
\qquad
C_p\Phi=(G_p\Phi,H_p\Phi).
\]

Its source-derived identity is

\[
C_p^*C_p=I_{\mathcal S}.
\]

The tail component $G_p\Phi$ is passed to the spectral-flow node. The seam
component $H_p\Phi$ remains an independently typed external boundary channel.

## Second stage: passive tail dilation

Let the tail node have a contraction

\[
T:\mathcal F\longrightarrow\mathcal P
\]

with defect map

\[
D:\mathcal F\longrightarrow\mathcal G
\]

satisfying

\[
T^*T+D^*D=I_{\mathcal F}.
\]

Here $mathcal G$ is the Green defect-state carrier. This is distinct from
the seam carrier.

The isometric dilation of the tail node is

\[
Nf=(Tf,Df).
\]

## Composite source map

Compose the cut with the dilated tail node while passing the seam through:

\[
W_p\Phi
=
\left(
TG_p\Phi,
DG_p\Phi,
H_p\Phi
\right).
\]

Then

\[
W_p^*W_p
=
G_p^*(T^*T+D^*D)G_p
+H_p^*H_p
=I_{\mathcal S}.
\]

Thus the complete source cascade is lossless.

## Typing consequence

The three output channels have different roles:

- $TG_p\Phi$ is the outgoing scattering port;
- $DG_p\Phi$ is the internal spectral defect state;
- $H_p\Phi$ is the external scale-cut seam state.

Their norms may add in one conservation law, but their authority and future
composition differ. Neither defect state may be substituted for the other.

## Localization theorem

At finite cutoff, the cut and passive stages introduce no unexplained supply
term once their complete defect carriers are retained. Therefore any residual
in the doubled theta construction must first arise from one of the following:

1. mismatch between the actual forcing and the cut tail;
2. failure of the passive factorization on the typed arithmetic source;
3. reciprocal sewing that is not unitary on the complete output packet;
4. a cutoff bonding map that fails to intertwine the cascade;
5. loss of an output carrier during completion.

This localizes the RH-bearing audit. The finite source interior is already a
lossless cascade; the unresolved object is the global cross-sector
interconnection.

## Reciprocal double

Construct one cascade for each causal orientation. Before cross-sewing, their
combined map is the orthogonal direct sum

\[
W_{+,p}\oplus W_{-,p}.
\]

It remains isometric. A unitary sewing of the complete external boundary
packets preserves that identity. A nonunitary sewing contributes the exact
supply residual

\[
J^*J-I.
\]

The internal Green defect states are not sewn away. Their strict positivity
off seam is what drives the zero-confinement contradiction.

## Arithmetic gate

For prime-power displacement $p=k\log\ell$, the cut isometry is already
source-labelled. What remains is to prove that the primitive, square, and
archimedean operations act as intertwiners of $W_p$ rather than changing its
energy signature.

This is the precise composition test for the singular boundary vessel.

## Finite falsifiers

At each cutoff, verify

\[
W_{p,X}^*W_{p,X}=I.
\]

Then test every arithmetic constructor $A_X$ against the cascade:

\[
W_{p,Y}A_X
=
\widetilde A_XW_{p,X}.
\]

Failure of the isometry identifies an omitted carrier. Failure of the
intertwiner identifies the first operation that injects or erases supply.

