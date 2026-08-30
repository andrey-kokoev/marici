# 2293 — The Finite-\(q\) Tensor Transfer Induces a Logarithmic Detector Connection with Trivial Gram Monodromy

## Connection convention

Use

\[
\nabla=d-A.
\]

The occurrence source bundle is constant.  Away from rank-loss support, the
derived tensor transfer \(T\) therefore induces the unique detector connection

\[
\boxed{
A_D=dT\,T^{-1}
}

for which

\[
\nabla_DT=dT-A_DT=0.
\]

No connection is fitted independently of the source map.

## Gram-wall local form

Entry 2288 gives Smith gauge

\[
T\sim\operatorname{diag}(1,1,c)
\]

for the resolved Gram normal \(c\).  Hence

\[
A_D
\sim
\operatorname{diag}\left(0,0,\frac{dc}{c}\right)
+\text{regular terms}.
\]

The residue is

\[
R_{\rm Gram}=\operatorname{diag}(0,0,1).
\]

Thus the tensor channel has one logarithmic transport direction, matching the
single Cartier costalk of Entry 2288.  Its local monodromy is

\[
\exp(2\pi iR_{\rm Gram})=I_3.
\]

The Gram class is supported but carries no nontrivial local-system character.

## Gauss--Manin tensor compatibility

For either sector-specific Gauss--Manin system \((\mathbb V,A_{\mathbb V})\),
put

\[
A_{\mathbb V\otimes D}
=A_{\mathbb V}\otimes I_3+I_{\mathbb V}\otimes A_D.
\]

Then

\[
1_{\mathbb V}\otimes T
\]

is horizontal by the Leibniz rule.  The direct Gaussian score block has
constant connection and is horizontal by Entry 2289.  Therefore the complete
score-plus-tensor observer map is a typed morphism of connections, not merely
an invertible map of generic fibers.

## Classification

The Gram wall contributes:

- a simple logarithmic detector residue;
- identity monodromy;
- one recoverable Cartier costalk;
- no new elliptic or marked-relative coefficient character.

This completes the connection-level compatibility omitted from Entry 2289.

## Verification

`research/benincasa/checkers/finite_q_detector_connection.rs` verifies the
Smith-gauge connection, residue, monodromy character, and tensor-product rule.
