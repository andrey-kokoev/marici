# The shape-derivative coherence face is parity reversing

## Question

Does the sourced exchange-odd shape intervention transport the canonical mixed residue into the simple exchange-odd class that detects the second primitive physical coordinate?

## Claim boundary

This packet computes the parity of the existing differentiation map. It corrects the earlier treatment of that map as exchange-equivariant. It does not construct the separate Gauss–Manin/IBP and integral Betti comparison required for a scalar detector.

## Exact derivative matrix

Use the ordered simple-pole basis

\[
s_1=(b-x)^{-1},\qquad s_2=(a-y)^{-1},
\]

and doubled-pole basis

\[
p_1=(b-x)^{-2},\qquad p_2=(a-y)^{-2}.
\]

For

\[
D_{\rm shape}=\partial_x-\partial_y,
\]

direct differentiation gives

\[
D_{\rm shape}s_1=p_1,
\qquad
D_{\rm shape}s_2=-p_2.
\]

Hence

\[
N_D=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

If \(S\) swaps the two wall labels, then

\[
N_DS=-SN_D.
\]

The minus sign is forced because wall exchange reverses the tangent \(D_{\rm shape}\). The comparison is therefore anti-equivariant, not equivariant.

## Parity exchange

Let

\[
s_+=s_1+s_2,\qquad s_-=s_1-s_2,
\]

and similarly \(p_\pm=p_1\pm p_2\). Then

\[
N_Ds_+=p_-,
\qquad
N_Ds_-=p_+.
\]

The sourced principal response \(p_-=(1,-1)\) is the derivative of the canonical symmetric residue \(s_+\). Applying the inverse derivative comparison on its image returns \(s_+\), whose marked algebraic extension has zero \(v_{\rm alg}\) coordinate. It does not return the antisymmetric class \(s_-\).

## Consequence for the four-vertex flow

The earlier proposed route

\[
p_-\longmapsto g_{101}-g_{110}\longmapsto v_{\rm alg}
\]

is parity-incompatible with the actual shape derivative. The existing flow is

\[
s_+\longmapsto p_-,
\]

whereas the simple class with nonzero \(v_{\rm alg}\) projection satisfies

\[
s_-\longmapsto p_+.
\]

Thus the two candidate paths cross characters rather than preserving them. A valid coherence pyramid must retain the tangent character as an additional tensor factor:

\[
\chi_{\rm output}=\chi_{D_{\rm shape}}\chi_{\rm input}.
\]

Since \(\chi_{D_{\rm shape}}=-1\), symmetric input yields antisymmetric principal response and antisymmetric input yields symmetric principal response.

## Disposition

The sourced exchange-odd intervention constructs a nonzero primitive vector response, but that fact alone does not construct the second \(v_{\rm alg}\) detector. To use the same intervention for that detector, one must source the antisymmetric simple mixed input \(s_-\); its differentiated principal response is the symmetric doubled-wall vector \(p_+\). Any comparison sending the already constructed \(p_-\) directly to \(g_{101}-g_{110}\) would erase the tangent character and fail covariance.

Verification:

- `research/voevodsky/checkers/check_exchange_odd_coherence_eigenvalue_reduction.py`
