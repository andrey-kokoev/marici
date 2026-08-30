# Hidden-port sign groupoid: WP693

## The WP692 sign pair is contextual

On the reduced radial two-point domain, define

\[
S=\operatorname{diag}(1,-1).
\]

The inverse propagators with opposite mixing satisfy

\[
K(-\kappa)=S K(\kappa)S.
\]

The ordinary Higgs source vector \(e_h=(1,0)^T\) is fixed by \(S\). Therefore
every visible Higgs resolvent agrees:

\[
e_h^T K(-\kappa)^{-1}e_h
=e_h^T K(\kappa)^{-1}e_h.
\]

The pole polynomial is also invariant. Thus the pair found in WP692 is one
operational equivalence class under the stabilizer groupoid of the admitted
visible port. It must not yet be described as two physically inequivalent
`physical16` points.

## What an exit reference changes

For the hidden-port vector \(e_x=(0,1)^T\), the cross resolvent is odd:

\[
e_h^T K(-\kappa)^{-1}e_x
=-e_h^T K(\kappa)^{-1}e_x.
\]

A calibrated exit-sensitive port would therefore distinguish the two
representatives. It would also shrink the stabilizer and define a new
relational experiment. It would not reveal an absolute sign already present
in the original visible-only experiment.

## Authority boundary

WP693 classifies the reduced two-point groupoid only. The full scalar source
may contain invariants, vacuum relations, or odd exit interactions that do not
descend to this reduction. The remaining gate is a covariant map from the
complete flavor source to the radial propagator packet, followed by a test of
whether any full-source invariant distinguishes the portal-sign branches
before detector projection.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp693_hidden_port_sign_groupoid.py

Generated result: results/wp693_hidden_port_sign_groupoid.json.
