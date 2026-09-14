# Branch B fully framed line/support variance adapter

Date: 2026-09-08

## Result

**Decision 1.** The missing adapter exists in all eight labelled frames. It is the tensor product of the canonical nested-support counit with the marked column of the polarity-loaded normalization--conductor primitive map.

Put

\[
I_X=(X_0,\ldots,X_5),\qquad
J_{\sigma,T}=(t_T,t_i:i\in I_\sigma),
\qquad k_+=35,\quad k_-=04.
\]

## Support component

The inclusion \(V(I_X+J_{\sigma,T})\subset V(I_X)\) induces

\[
s_{\sigma,T}:R\Gamma_{I_X+J_{\sigma,T}}(K)
\longrightarrow R\Gamma_{I_X}(K).
\]

By the Stacks local-cohomology composition lemma,

\[
R\Gamma_{I_X+J_{\sigma,T}}
\simeq R\Gamma_{J_{\sigma,T}}R\Gamma_{I_X},
\]

and \(s_{\sigma,T}\) is the counit of the first factor. On extended Čech complexes it is

\[
1_{\check C(I_X)}\otimes\varepsilon_{\check C(J_{\sigma,T})}.
\]

This retains the complete four-generator Rees support. The standalone checker verifies all 8192 signed basis equations.

## Line component

Entry 93 identifies the polarity line \(L_{\rm pol}\) intrinsically from the normalization--conductor Čech difference; this is the line denoted \(\Pi\) in the conormal target. Entry 94 gives

\[
K_{\rm alt}=
\begin{pmatrix}
0&0&-1&0&0&1\\
-1&0&0&1&0&0\\
0&1&0&0&-1&0
\end{pmatrix},
\qquad \Delta^\vee=(1,1,1).
\]

Hence

\[
\Delta^\vee K_{\rm alt}=(-1,+1,-1,+1,-1,+1).
\]

The polarity character in the ordered occurrence basis is the same row, so

\[
(\Delta^\vee\otimes L_{\rm pol})K_{\rm alt}
=(1,1,1,1,1,1).
\]

Projecting to column 5 on the plus endpoint and column 4 on the minus endpoint gives coefficient one in respectively \(\mathcal L_{35}\Pi^\vee\) and \(\mathcal L_{04}\Pi^\vee\).

Compose this marked-column projection with the already constructed complete physical top detector. The resulting line map is

\[
\chi_{\sigma,T,\epsilon}=
\operatorname{pr}_{k_\sigma}
(\Delta^\vee\otimes L_{\rm pol})K_{\rm alt}
\circ\operatorname{det}_{\sigma,T,\epsilon}.
\]

Here \(\operatorname{det}_{\sigma,T,\epsilon}\) is the complete endpoint detector of the existing 1024-state cocycle, not a newly postulated scalar map. Its endpoint-normal dual and external conormal factors pair canonically. Its ordered occurrence and product-Cartier factors are retained by the detector; its long-normal coefficient remains \(U_L\). The two excess labels are transported separately by identity. No Euler section, long-normal evaluation, or parameter inversion occurs.

The prior fine-frame checker establishes degree displacement zero. Thus

\[
\chi_{\sigma,T,\epsilon}:\mathcal L_{\sigma,T,\epsilon}
\longrightarrow C v_{k_\sigma}\otimes\Pi^\vee[3]
\]

has cohomological degree zero, internal degree zero, and primitive coefficient one.

## Fully framed mate

Tensoring with the established normalized native mate gives

\[
\Phi_{\sigma,T,\epsilon}(f\otimes\ell)=
(-1)^{|f||\ell|}\chi_{\sigma,T,\epsilon}(\ell)
S(P_\sigma q_\sigma(f)).
\]

The support counit and line map are scalar with respect to the native operation factor. Therefore the established antipode identity transports unchanged:

\[
\Phi_{\sigma,T,\epsilon}(r\smile(f\otimes\ell))
=(-1)^{|r|(|f|+|\ell|)}
\Phi_{\sigma,T,\epsilon}(f\otimes\ell)S(r).
\]

This covers the established nine quadratic, 18 cubic, 15 quartic, six quintic and one sextic primitives, and all 81 ordered quadratic products. The decomposable correction under reflection remains in \(S\) and is not discarded.

Rotation permutes the six loaded unit columns. Endpoint-exchanging reflection sends the labelled 35 column to the labelled 04 column. Raw determinant sign and polarity sign reverse together, so the loaded coefficient stays +1. This is covariance of the `D35/D04` family, not an automorphism of fixed `D35`.

## Reproduction

```sh
python research/voevodsky/check_branch_b_derived_support_transition_20260908.py \
  --output research/voevodsky/branch_b_derived_support_transition_certificate_20260908.json

python research/voevodsky/check_branch_b_framed_line_adapter_20260908.py \
  --root . \
  --output research/voevodsky/branch_b_framed_line_adapter_certificate_20260908.json
```

The first checker verifies 8192 new signed Čech equations. The second independently reconstructs the polarity-loaded six-column primitive row and checks its eight marked-frame projections. Prior operation assertions are consumed, not recounted as new checks.

## Scope

This is the requested Branch B algebraic framed/support interface. It does not assert a physical Q-manifold, outer vector fields, or the P24 deformation class.
