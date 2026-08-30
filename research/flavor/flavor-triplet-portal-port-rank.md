# Messenger-port rank for the adjoint-triplet portal

## Interface problem

WP447 and WP467 use three dynamical adjoints `X_i` and an oriented triplet
symmetry. WP435's minimal renormalizable completion supplies only two direct
one-stage messenger ports, conventionally labelled up and down.

A messenger port coupled to the linear combination

\[
Y_\alpha=\sum_{i=1}^3p_{\alpha i}X_i
\]

generates the WP478 mixed threshold through the positive adjoint-label pairing

\[
W=\sum_\alpha p_\alpha^\dagger p_\alpha.
\]

This is the full matrix typing of the single-channel result. The loop sign and
overall coefficient are carried separately; `W` determines which triplet
directions are seen.

## Exact two-port obstruction

For the minimal up/down port matrix `P`, which is `2 by 3`,

\[
W=P^\dagger P,
\qquad \operatorname{rank}W\leq2,
\qquad \det W=0.
\]

For real port vectors `p` and `q`, the exact blind direction is their cross
product:

\[
W(p\mathbin\times q)=0.
\]

Parallel ports only enlarge the kernel. This is a structural port-count bound,
not a special numerical cancellation.

## Common-clock descent requirement

The WP447 spin-one vacuum obeys

\[
\operatorname{Tr}(J_iJ_j)=2\delta_{ij}.
\]

The common-clock action and its WP475 Hessian use the isotropic pairing

\[
W_{\rm iso}=\kappa I_3,
\qquad \kappa>0.
\]

It has determinant `kappa^3` and rank three. Therefore no two-port messenger
packet can generate this portal or descend under the full oriented triplet
symmetry.

Exactly three ports are necessary. They are algebraically sufficient because
`P=sqrt(kappa) I_3` gives `P^dagger P=kappa I_3`. Generic three ports merely
give a positive rank-three pairing; equal norm and orthogonality still require
a source law. Algebraic span is not executable messenger control.

## Consequences

WP478 remains a valid bounded one-channel threshold theorem. It cannot be
composed with the isotropic WP467 action using only WP435's two ports. WP475 and
WP476 remain conditional on their independently declared isotropic portal;
their poles, residues, and widths have not been derived from the minimal
messenger threshold.

The operation is neither selector nor rigidifier at the full triplet level.
No physical instrument or reference port is involved. The smallest exact
falsifier is the cross-product kernel of the two-port Gram versus the trivial
kernel of `kappa I_3`.

The next constructive gate is an executable three-port messenger action with a
source symmetry enforcing the equal-norm orthogonal Gram. Full threshold
matching and the scalar/vector spectrum must then be recomputed on that action.
