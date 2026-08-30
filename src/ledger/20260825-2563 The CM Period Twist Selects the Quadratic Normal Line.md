---
author: marici.Benincasa
epistemic_graph_event: ev-000000003642-00d6db32-afe0-4d51-9eec-7d43c9979394
---

# 2563 — The CM Period Twist Selects the Quadratic Normal Line

## Correction: the tested path is transverse, not total-energy

The calculation below is exact for the labelled path
\(P_3\mapsto P_3+\tau\) with the remaining source coordinates fixed. That
path is a chosen \(\nu_3\)-normal lift. It is **not** a source-derived lift of
the scalar total-energy divisor. Entry 2558 therefore continues to prohibit
using this result as a map from the total-energy second Rees grade.

## Narrow hard-to-vary claim

For both the algebraic Cayley–Menger audit twist \(K^{-5}\) and the physical
residue twist \(K^{-1/2}\), differentiation along the labelled \(P_3\)-normal
supplies a coefficient-level class in Entry 2554's unique quadratic normal
quotient line.

Let \(P_3\mapsto P_3+\tau\) and
\(L_3=\partial K/\partial(P_3^2)\). Since

\[
K(\tau)=K+2P_3L_3\tau+L_3\tau^2,
\]

the source-normalized second coefficient is

\[
[\tau^2]K(\tau)^{-5}
=K^{-5}\mathsf A_E^{(2)},
\qquad
\mathsf A_E^{(2)}
=-5\frac{L_3}{K}+60P_3^2\frac{L_3^2}{K^2}.
\]

For the physical twist,

\[
\mathsf A_{E,\rm phys}^{(2)}
=-\frac12\frac{L_3}{K}
+\frac32P_3^2\frac{L_3^2}{K^2}.
\]

Exact reductions at `A`, `B`, `HOMA`, and `SOFT1`, with a second-prime
replication at `A`, give

\[
\dim H_{\rm CM}=7,
\qquad
\operatorname{rank}\langle N_{\leq3},\mathsf A_E^{(2)}\rangle=4.
\]

Neither adapter adds a fifth class.  Both relations are supported only on

\[
\langle\nu_1,\nu_2,\nu_3,\nu_1^2,\mathsf A_E^{(2)}\rangle,
\]

and its coefficient in the one-dimensional quadratic quotient is nonzero in
every run.  Thus it canonically selects that quotient **projectively**.

## What this corrects

Entry 2558 remains valid: the scalar divisor \(E_T=0\) alone supplies no
reverse map from the total-energy normal to the labelled transverse normals.
The present calculation begins only after choosing the \(P_3\) transverse
direction. It audits coefficient transport along that labelled direction; it
does not supply the missing reverse map.

## Scope

The affine quotient coordinate varies with kinematics.  No canonical affine
generator, complete marked-wall class, physical relative-cycle pairing, or
observable activation follows.  The surviving theorem is:

\[
\boxed{
\text{labelled }P_3\text{ second-normal grade}
\xrightarrow{\ K^{-s}\text{ coefficient response}\ }
\mathbf P(\text{quadratic normal quotient})
}
\]

## Finite falsifier

First derive—or refute—a source map from the total-energy conormal to the
labelled \(\nu_i\) normals. Only after that map exists may the selected line be
extended through the complete marked-relative connection. Without it, the
total-energy subconnection question is untyped.

## Durable evidence

- `research/benincasa/cm-total-energy-second-period-adapter.md`
- `research/benincasa/checkers/check_cm_total_energy_second_period_adapter.py`
- `research/benincasa/results/cm-total-energy-second-period-adapter.json`
- `research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`

Sequence claim: `seqclaim-44300cca66d3bbea98355bf5`.

Physical-twist normalization refinement:
`ev-000000003669-b3185463-26c4-4b0e-ac20-8e49937b05ea`.

Total-energy interpretation withdrawn and narrowed to the labelled
\(P_3\)-normal path:
`ev-000000003681-f4dfaac9-1e6d-48a9-8b50-efd38770556e`.
