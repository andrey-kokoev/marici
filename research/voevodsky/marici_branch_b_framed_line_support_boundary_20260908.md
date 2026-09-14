# Branch B framed line/support boundary

Date: 2026-09-08

## Decision

**Updated Decision 3:** the eight normalized primitive frames agree in chain degree and in every declared source weight. The derived-support arrow is canonical and has now been constructed from local cohomology. The complete project-specific line arrow remains unspecified. This is a one-map missing-data boundary, not a zero map and not a nonexistence theorem.

## Eight-frame source calculation

For

\[
T\in\{13,15,35,135\},\qquad
I_+=\{1,3,5\},\quad I_-=\{0,2,4\},
\]

write

\[
O=\sum_{i=0}^5e_{X_i},\quad P_T=\sum_{i\in T}e_{t_i},
\quad E_\sigma=\sum_{i\in I_\sigma}e_{t_i},
\quad \lambda_T=\gamma-O-P_T.
\]

On the unique primitive top state, the complete declared physical-source packet has weight

\[
(O+P_T)+\lambda_T-E_\sigma+E_\sigma=\gamma.
\]

The last two terms are respectively the dual endpoint-normal determinant in
\(D_\sigma\) and the independently retained external conormal line. This cancellation is valid in all eight frames and does not evaluate either line. After `[-4]`, the primitive source and conormal target occur in cohomological degree three. The existing first-jet adapter gives coefficient one and ambiguity

\[
C/(t_T,t_i\mid i\in I_\sigma).
\]

Thus degree and primitive scalar normalization are not the failure.

## First unrecoverable line arrow

Let \(W_{\sigma,T,\epsilon}\) denote the complete remaining physical primitive line packet, including the ordered occurrence determinant, product-Cartier duality, long-normal frame, and the separately labelled excess trace frame. The required arrow is

\[
\theta_{\sigma,T,\epsilon}:W_{\sigma,T,\epsilon}
\longrightarrow
\mathcal L_{k_\sigma}\otimes\Pi^\vee
\langle-1\rangle_\beta,
\qquad k_+=35,\quad k_-=04.
\]

No consumed input declares this arrow or gives the degree of the two labelled excess frames relative to the marked conormal/polarity line. The primitive fine-frame adapter explicitly stops before determinant-line identification outside its selected frame. The antipode-mate artifact explicitly records `line_and_support_transport: false`.

Consequently the homogeneous equation

\[
|W_{\sigma,T,\epsilon}|=
|\mathcal L_{k_\sigma}\Pi^\vee\langle-1\rangle_\beta|
\]

cannot be decided from the supplied dictionary. Assigning the absent transition degree zero would be inventing the desired map; assigning it a nonzero mismatch would be inventing an obstruction.

## Derived-support arrow

Put \(I_X=(X_0,\ldots,X_5)\) and
\(J_{\sigma,T}=(t_T,t_i:i\in I_\sigma)\). The actual source support is
\(V(I_X+J_{\sigma,T})\), which is contained in the conductor support
\(V(I_X)\). By `dualizing-lemma-local-cohomology-ss`,

\[
R\Gamma_{I_X+J_{\sigma,T}}
\simeq R\Gamma_{J_{\sigma,T}}R\Gamma_{I_X}.
\]

The counit of the local-cohomology right adjoint therefore gives

\[
\boxed{R\Gamma_{I_X+J_{\sigma,T}}(K)\longrightarrow
R\Gamma_{I_X}(K).}
\]

On extended Čech models this is

\[
1_{\check C(I_X)}\otimes\varepsilon_{\check C(J_{\sigma,T})}.
\]

It retains all four Rees generators and requires no regular-sequence assumption. Restriction and derived base change are supplied by the corresponding Stacks lemmas. The standalone checker verifies the signed tensor-complex map on 1024 basis columns per frame, 8192 total.

## Consequence for the native mate

The established formula

\[
\Phi^0_\sigma(f)=vS(P_\sigma q_\sigma(f))
\]

remains a strict normalized native algebraic mate. A fully framed formula

\[
\Phi_{\sigma,T}(f\otimes\ell)=
(-1)^{|f||\ell|}\chi_{\sigma,T}(\ell)
S(P_\sigma q_\sigma(f))
\]

is not typed until the remaining line arrow above is supplied. Therefore operation and labelled-reflection compatibility cannot be promoted from the normalized model to the physical framed/support model. The known antipode, product-order detector, and decomposable reflection correction remain valid conditional data and are not discarded.

## Reproduction

```sh
python research/voevodsky/check_branch_b_framed_line_support_boundary_20260908.py \
  --root . \
  --output research/voevodsky/branch_b_framed_line_support_boundary_certificate_20260908.json
```

The boundary checker consumes the relevant local source/adapter artifacts, verifies the symbolic source-line cancellation in all eight frames, and verifies their explicit stopping conditions. The support map is independently checked by:

```sh
python research/voevodsky/check_branch_b_derived_support_transition_20260908.py \
  --output research/voevodsky/branch_b_derived_support_transition_certificate_20260908.json
```

It checks 8192 signed Čech basis columns across the eight frames.
