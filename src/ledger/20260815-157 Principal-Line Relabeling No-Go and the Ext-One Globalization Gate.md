---
authors:
  - marici.Nima
---
# Principal-Line Relabeling No-Go and the Ext-One Globalization Gate

## Record

Date: 2026-08-15

Status: proved variance correction. Principal occurrence lines repair the
internal divisibility of the mixed block, but they do not turn the missing
global trace into an ordinary degree-zero map. The required local operation
is the Cartier \(\operatorname{Ext}^1\) fundamental class; its global
normalization-sheet/\(Q\) coupling remains unconstructed.

## The tempting relabeling

Entry 156 proved that an ordinary scalar trace would require

\[
x_iT(b_i\otimes n_{D(i)})
=\epsilon_{D(i)}T(\mathbf q_i\otimes p_{D(i)}),
\]

and therefore \(x_i a=\pm1\). A natural attempted repair is to retain the
principal occurrence ideal

\[
I_i=(x_i)
\]

as a labelled line. The unique normalized relabeling of one mixed sector is

\[
R\langle m_i\rangle
\longrightarrow
R\langle\mathbf q_i\rangle\oplus
I_i\langle\bar\xi_i\rangle
\longrightarrow
I_i\langle\bar b_i\rangle,
\]

\[
dm_i=\mathbf q_i-\bar\xi_i,
\qquad d\mathbf q_i=\bar b_i,
\qquad d\bar\xi_i=\bar b_i,
\]

where \(\bar b_i=x_ib_i\) and \(\bar\xi_i=x_i\xi_i\). This is integral and
square-zero. Its labelled dual line has the canonical evaluation

\[
I_i^\vee\otimes I_i\longrightarrow R,
\qquad x_i^\vee(x_i)=1.
\]

This construction does not invert \(x_i\).

## Why relabeling is not yet the trace

Let \(j_i:I_i\hookrightarrow R\) be the inclusion and let
\(B_i=R/I_i\). Derived pullback gives

\[
L i_i^*I_i=I_i/I_i^2,
\]

but the pulled-back inclusion is

\[
L i_i^*(j_i):I_i/I_i^2\longrightarrow B_i,
\qquad [x_i]\longmapsto0.
\]

Thus ideal labeling preserves the conormal line while ordinary conductor
restriction still gives zero. The nonzero normalized operation is shifted:

\[
\boxed{
\operatorname{Ext}^1_R(B_i,R)
\simeq(I_i/I_i^2)^\vee.
}
\]

Indeed the free resolution

\[
0\to R\xrightarrow{x_i}R\to B_i\to0
\]

gives

\[
\operatorname{Ext}^0_R(B_i,R)=0,
\qquad
\operatorname{Ext}^1_R(B_i,R)=R/(x_i).
\]

The minimal honest local formula is therefore

\[
\boxed{
\operatorname{Tr}_i^!
=\operatorname{ev}_{I_i}\circ(g_i^!\otimes\mathrm{id}),
\qquad
g_i^!\in\operatorname{Ext}^1_R(B_i,I_i),
}
\]

with the Cartier coorientation shift. This is precisely the kind of
operation constructed locally by entries 129--131: the full Koszul--Cech
Gysin, both Tor grades, graph Bockstein, and scoped \(D03\) edge purity.

The target generators \(n_D,p_D\) must remain those of entry 143's fixed
seven-generator \(Q\) quotient. Relabeling them by occurrence ideals would
change that quotient rather than construct a map into it. Likewise the
generic classes \(\mathbf q_i\) are not ideal-supported terms to which the
special evaluation can be extended.

## The actual globalization gate

The first missing datum is no longer a local principal line. It is a global,
two-sheet-compatible, mixed-variance kernel

\[
\boxed{
\alpha_{\rm sh}^{!,\check C}
}
\]

whose local \(x_i\)-restrictions are the proved Cartier classes and whose
generic restriction retains

\[
q_\Sigma=q_{14}+q_{03}+q_{25}\ne0.
\]

It must be a morphism of the normalization/conductor and endpoint/\(Q\)
localization triangles, not a map of their ordinary coefficient shadows. It
must also provide the two endpoint comparison cells. Once it exists, the
honest pointed mapping space is

\[
\operatorname{hofib}_{(\tau_+,\tau_-,\tau_Q)}
\left[
R\!\operatorname{Hom}^{\rm fr}_{D_3}
(\mathcal S_{\rm sh}\otimes^L
 \mathcal E_{\partial,Q}^{\rm BM,\check C},
 \mathbf1_{\chi_N})
\longrightarrow
B_+\oplus B_-\oplus B_Q
\right].
\]

A point is a trace together with the two endpoint cells and the based
\(Q\)-comparison. Reflection parity is defined only after this fibre is
nonempty.

## Mandatory controls

- Forgetting endpoint/\(Q\) framing must restore entry 133's contraction.
- Forgetting the Tate window must kill the candidate class.
- Both Tor grades and every lower Cech term must remain present.
- No target \(Q\) generator may be relabelled to force the ideal pairing.
- Neither \(x_i\), \(t_i\), nor an integer may be inverted.

## Evidence

- entries 129--131: local principal line, Cartier Gysin, and scoped edge
  purity;
- entry 133: ordinary-derived contraction;
- entry 143: fixed primal endpoint/\(Q\) target;
- entries 154 and 156: primal trace typing and zero-section no-go;
- `research/voevodsky/check_principal_line_trace_variance.rs`.

## Outcome contract

```json
{
  "claim": "Principal occurrence-line relabeling repairs internal divisibility but does not produce the primitive conductor scalar as an ordinary degree-zero map. The scalar is the shifted Cartier Ext1 fundamental class. Entries 129-131 construct it locally; the remaining datum is its global two-sheet normalization-Cech coupling to the nonzero q_Sigma leg and endpoint cells.",
  "status": "proved",
  "assumptions": [
    "The occurrence ring is integral and x_i is a non-zero-divisor.",
    "The principal ideal is pulled back as a labelled line before evaluation.",
    "Entry 143's Q quotient and its generator types remain fixed."
  ],
  "evidence_refs": [
    "research/voevodsky/check_principal_line_trace_variance.rs",
    "src/ledger/20260814-129 Cox Principal-Line Trace and the Extraordinary Cousin Boundary.md",
    "src/ledger/20260814-131 D03 Cartier Edge Purity and the Scoped PC Promotion.md",
    "src/ledger/20260814-133 Ordinary-Derived Ablation and the Framed Off-Diagonal Objective.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-156 Zero-Section Trace No-Go and the Principal-Dual-Line Gate.md"
  ],
  "factorization_test": {
    "principal_line_relabeling": "square-zero and integral",
    "ordinary_conductor_map": "zero",
    "Cartier_Ext0": "zero",
    "Cartier_Ext1": "one primitive R/(x_i) line",
    "local_D03_Gysin": "proved by entries 129-131",
    "global_qSigma_coupling": "unconstructed",
    "endpoint_fixed_mapping_fibre": "not yet instantiated",
    "physical_parity": "undefined"
  },
  "counterevidence": [
    "Generator-dual evaluation is defined on the ideal-valued special term, not on generic free terms.",
    "Derived conductor pullback retains I/I^2 but sends I->R to zero in degree zero.",
    "Relabeling the target road/Q generators changes the fixed target instead of constructing the missing trace."
  ],
  "next_experiment": "Construct alpha_sh^{!,Cech} as a D3-equivariant morphism of the two-sheet normalization and endpoint/Q localization triangles, require its local restrictions to be the entry-131 Cartier purities and its generic restriction to retain q_Sigma, then compute the endpoint-fixed mapping fibre before evaluating parity."
}
```
