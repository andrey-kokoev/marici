# Consolidated Branch C theorem: strict targets and formal P24 class

Date: 2026-09-08

## Category and scope

Everything below is asserted in the algebraic continuous-formal category, using the GR `IndCoh` formal vector prestack and its distribution coalgebra. No reconstruction of Bruce's smooth Q-manifold is required or claimed. Bruce/P24 supplies only the algebraic derived-product and deformation-cocycle formulas.

## Theorem

Let

\[
B=A/(I_EI_O),\qquad C=A/(I_E+I_O),
\]

and let `omega` be the ordered 50-state dualizing model obtained from the complete node resolution. For `k=35,04`, define

\[
D_k^n=\omega[2]^n\oplus(E_{\beta,k}\Pi^\vee[3])^n
\oplus(C\Pi^\vee[3])^{n-1}
\]

with

\[
d(z,e,h)=(d_\omega z,d_Ee,qz-\pi_ke-d_Ch).
\]

Then:

1. **Strict conductor map.** In the ordered top frame,
   \[
   q(p_{E,O}^{\vee})=-1,
   \qquad q=0\text{ on the other 49 states},
   \qquad q(\kappa)=1.
   \]
   The chain equation holds strictly after `A -> C`.

2. **Strict pullbacks.** Both `D35` and `D04` are square-zero strict homotopy-pullback models. For every
   \[
   T\in\{13,15,35,135\}
   \]
   and both endpoint signs,
   \[
   b_{\sigma,T}=(0,j_{k_\sigma}\kappa_{\sigma,T},0)
   \]
   is a strict chain map with primitive framed coefficient one.

3. **Normalization descent.** The two smooth normalization branches and their common conductor descend to the singular native target through
   \[
   \operatorname{fib}(K_E\oplus K_O\to K_6).
   \]
   The coherence is
   \[
   H(p_{U,V})=(-1)^{|U|}e_U\wedge e_V.
   \]
   The complete comparison cone contracts by 65 integral unit cancellations. Dual descent retains the row `(1,-1)` and top coefficient `-1`.

4. **Formal Q-object and trace.** The strict complex determines
   \[
   \mathfrak X_k=\operatorname{Vect}_{\operatorname{Spec}B}(D_k)
   \]
   in GR formal geometry, with
   \[
   \operatorname{Distr}^{\mathrm{Cocom}}_{\mathrm{aug}}(\mathfrak X_k)
   \simeq\operatorname{Sym}^{c}_{!}(D_k).
   \]
   Its weight-zero distribution counit followed by the normalized sixfold conductor residue is Q-closed.

5. **Outer translation and P24 cocycle.** For an odd cubic or quintic primitive endpoint cycle `v=b_sigma,T`, constant translation
   \[
   X_v=\partial_v
   \]
   lowers symmetric weight and satisfies
   \[
   [Q,X_v]=\partial_{Qv}=0.
   \]
   If `lambda_v` is the closed framed coordinate with `lambda_v(v)=1`, the P24 cochain satisfies
   \[
   \phi_v(\lambda_v,1)=-1.
   \]

6. **Nonboundary.** Since
   \[
   Q\lambda_v=Q1=0,
   \]
   both `lambda_v star 1` and `1 star lambda_v` vanish. Hence every degree-zero Hochschild boundary vanishes on `(lambda_v,1)`, while `phi_v` evaluates to `-1`. Therefore
   \[
   \boxed{[\phi_v]\ne0}.
   \]

The construction is compatible with all eight frames and with marked reflection `D35 <-> D04`.

## Important distinction

The original weight-preserving linear operation fields produce zero under the vacuum trace. The nonzero P24 class uses the constant translation field attached to the strict endpoint cycle. These two kinds of outer action must not be conflated.

## Dependency ledger

| Component | Certificate |
|---|---|
| strict `q` | `marici_strict_conductor_truncation_q_certificate_20260908.json` |
| strict targets and eight maps | `marici_strict_d35_d04_spatial_comparison_certificate_20260908.json` |
| GR distribution counit | `marici_gr_distribution_counit_certificate_20260908.json` |
| formal pairing and linear no-go | `marici_formal_function_distribution_pairing_certificate_20260908.json` |
| translation cocycle | `marici_p24_translation_cocycle_certificate_20260908.json` |
| nonboundary detector | `marici_p24_nonboundary_detector_certificate_20260908.json` |
| normalization descent | `marici_normalization_q_descent_certificate_20260908.json` |

## Reproduction

```sh
python research/voevodsky/check_marici_branch_c_consolidated_20260908.py \
  --root . \
  --output research/voevodsky/marici_branch_c_consolidated_certificate_20260908.json
```

The consolidation checker validates seven input certificates by SHA-256 and performs 49 cross-certificate assertions.

## Final status

Branch C is complete in the intended algebraic/formal category. Compact smooth realization, nuclear-Frechet topology, and reconstruction of Bruce's geometry are explicitly outside the claim.
