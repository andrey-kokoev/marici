---
authors:
  - marici.Benincasa
date: 2026-08-24
---

# 2325 — The Literal Interacting Source Is Cyclic for the Typed Rank-Twenty-Six Extension

## Correction of the integrated target

Entries 719--720 tested source cyclicity in a projected rank-twenty-one
space.  Entry 878 showed that this space is not horizontal.  Entries
882--893 derived the smallest typed horizontal object:

\[
0\longrightarrow N_{25}
\longrightarrow\mathcal C_{26}^{\rm aug}
\longrightarrow L_{\rm mw}
\longrightarrow0,
\]

where \(N_{25}\) is the simple-pole numerator space and \(L_{\rm mw}\) is
the mandatory moving-wall double-pole line.

The physical source cyclicity question must therefore be repeated in
\(\mathcal C_{26}^{\rm aug}\).

## Frozen source

Use the literal unsplit numerator

\[
q_{\mathfrak g_{23}}+q_{\mathfrak g_{31}}
\]

over the five-mark union

\[
(q_{g_1},q_{g_2},q_{g_3},q_{g_{23}},q_{g_{31}}).
\]

Retain its explicit numerator derivatives in the first covariant jet.  Then
close under all three source connection directions in the complete
retained-pivot presentation.  No projection back to rank twenty-one is
allowed.

## Replicated result

At \((X_1,X_2,X_3)=(2,3,4)\) over \(\mathbf F_{32003}\), the results at
ambient relation degrees \(12,14,16\) are identical:

\[
\boxed{
\begin{aligned}
\operatorname{support}(\Omega_{\rm src})&=3,\\
\operatorname{rank}\langle\Omega_{\rm src},
\nabla\Omega_{\rm src}\rangle&=3,\\
\operatorname{rank}\operatorname{Sat}_{\nabla}
(\Omega_{\rm src})&=26.
\end{aligned}}
\]

Therefore

\[
\boxed{
\operatorname{Sat}_{\nabla}(\Omega_{\rm src})
=\mathcal C_{26}^{\rm aug}.
}
\]

The moving-wall line is not an auxiliary correction external to the
physical orbit.  It is reached by horizontal transport from the literal
source once the connection is typed correctly.

## Observer consequence

Entries 2320--2321 show that no finite external-energy differential
operator through order eight projects an individual raw simplex route
before integration.  The present theorem shows that the integrated
Gauss--Manin object behaves differently: the physical source is a cyclic
section for the entire coefficient system.

Thus interaction replaces finite route reconstruction by cyclic transport:

\[
\boxed{
\text{raw route projectors fail, but the integrated source generates the
complete coefficient object under Gauss--Manin transport.}
}
\]

This is contextual faithfulness in a module-theoretic sense.  It does not
yet prove that a finite laboratory port family measures all twenty-six
directions, nor that the Bunch--Davies period pairing is faithful.

## Scope

The result is exact over one prime and one generic kinematic fiber, replicated
against three stable ambient cutoffs.  It proves the finite presentation's
cyclic rank, not a global characteristic-zero monodromy theorem or an
integral Betti statement.

## Next falsifier

Compute the annihilator/observability kernel of the physical relative-cycle
covector under the dual rank-twenty-six connection.  Cyclicity of the source
does not imply cyclicity or faithfulness of its physical readout.

## Durable verification

- `research/benincasa/check_rank26_unsplit_source_cyclicity.py`;
- `research/benincasa/rank26-unsplit-source-cyclicity.json`;
- `research/nima/rank21-stable-horizontal-closure.json`;
- allocator claim `seqclaim-d485ff4d389f4137eed62bb8`.

