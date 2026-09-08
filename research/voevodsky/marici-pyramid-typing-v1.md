# Marici conductor–Morse pyramid: typing pass v1

## Objective

Identify the actual vertices, edges, faces, and top coherence needed to interpret the conductor primitive as part of a Marici tetrahedron/pyramid. This is a typing manifest, not a claim that the pyramid is complete.

## 1. Fixed dg convention

Work in a dg enhancement with cohomological Hom differential

\[
\delta f=d_Yf-(-1)^{|f|}fd_X.
\]

Composition obeys

\[
\delta(gf)=(\delta g)f+(-1)^{|g|}g\delta f.
\]

All objects below must be realized in this one enhancement before subtraction or tetrahedral composition is defined. Derived roofs may be used as edges only after choosing a compatible dg localization/model; equality of their scalar readouts is not such a realization.

## 2. The coefficient-level degenerate pyramid now available

Fresh inputs:

- `research/chatgpt/physical_source_comparison.md` constructs the derived roof
  \(a:J\to T[1]\), induced by the unique road augmentation \(a_C:J\to C_{\rm cond}[1]\).
- `research/chatgpt/proof.md` constructs \(k_\nu:T[1]\to V\) and \(e_\nu:T[1]\to V\) in the stated shifted degrees with
  \(\delta k_\nu=e_\nu\).
- Given a cochain \(h:J\to T[1]\) with \(\delta h=a\), it gives the composite primitive \(-k_\nu h\).

The meaningful cell table is therefore a *degenerate/nullhomotopy tetrahedron in a mapping complex*, not yet a four-object physical tetrahedron:

| Cell | Typed datum | Status |
|---|---|---|
| base edge | \(a:J\to T[1]\) | constructed as a derived roof; no strict inverse to \(\rho[1]\) chosen |
| conductor edge/homotopy | \(k_\nu:T[1]\to V\) | constructed after endpoint Cech promotion |
| conductor boundary | \(e_\nu=\delta k_\nu\) | constructed in the coefficient target |
| source nullhomotopy | \(h:J\to T[1]\), \(\delta h=a\) | conditional; the corrected Morse source has not been identified with this J/T model |
| first composite face | \(H_C^\nu=k_\nu a\) | constructible from the roof in a common dg model |
| second composite face | \(e_\nu h\) | conditional on h |
| face-to-face filler | \(P=-k_\nu h\) | conditional on h |

The checked formal boundary is

\[
\delta P=k_\nu a-e_\nu h.
\]

This is the Leibniz face equation. It supplies a candidate 2-cell between two degree-shifted composite faces. It is not yet the top 3-cell of the physical pyramid.

## 3. Why this is not yet the physical four-face boundary

The physical expression in Entry 109 requires

\[
q_J:J_{\rm phys}\to Q_{\rm phys},\qquad
h_M:J_{\rm phys}\to Q_{\rm phys},\quad \delta h_M=q_J,
\]

\[
e_F:Q_{\rm phys}\to F_0[2],\qquad
H_C:J_{\rm phys}\to F_0[2],\quad \delta H_C=e_Fq_J.
\]

Then

\[
\Delta_J=H_C-e_Fh_M
\]

is a closed face discrepancy. The four triangular equations required around the physical pyramid are:

1. \(\delta h_M=q_J\) (Morse face);
2. \(\delta e_F=0\) (closed supported/Gysin edge);
3. \(\delta H_C=e_Fq_J\) (conductor face);
4. \(\delta\Delta_J=0\), derived from 1–3 with the graded composition sign (boundary compatibility).

A top filler would be an admissible cochain \(K\) in the *same framed relative Hom object* satisfying

\[
\delta K=\Delta_J
\]

(or the conventionally shifted equivalent). The equation alone is not sufficient: K must retain support, Q framing, endpoint connectors, Rees/Cartier degrees, and transport.

## 4. Actual edges and missing identifications

The present packets do not define one four-vertex diagram with all six edges. They define pieces in different dg targets:

| Required physical datum | Closest constructed datum | Gap |
|---|---|---|
| physical source \(J_{\rm phys}\) | six-point complex J | corrected seven-triangle Morse source not compared to J |
| physical generic target \(Q_{\rm phys}\) | normalization conductor \(T[1]\), and separately actual Q targets | no support-typed equivalence/arrow identifies them |
| physical endpoint target \(F_0[2]\) | endpoint Cech target V | no admissible identification preserving Q and endpoint frames |
| \(q_J\) | road augmentation roof a | same coefficient +1 does not identify target or map |
| \(h_M\) | corrected \(\widehat h_M=H\otimes p-\widetilde\xi\otimes h_{occ}\) | its source/target is not T[1] and the occurrence term must remain |
| \(e_F\) | \(e_\nu\), supported Gysin classes | no common-complex comparison |
| \(H_C\) | \(k_\nu a\) | endpoint-valued and zero in generic Q; physical admissibility not proved |
| top filler | \(-k_\nu h\) | conditional h and admissibility absent |

Therefore naming four abstract vertices now would conceal, rather than solve, the central typing problem.

## 5. New obstruction from the mutable tree

`research/chatgpt/physical_delta_result.md` proves that the existing native first-jet readout \(\Xi_{jet}\) is zero on the entire literal endpoint-valued Hom complex. Hence

\[
\Xi_{jet}(j^1(i_0\Delta_Ja))=0
\]

for every literal endpoint inclusion route. The nonzero native class \(\tau\) is not in the endpoint-valued image. Thus the receiving first-jet object cannot be attached as a face of this pyramid via ordinary endpoint inclusion. A support-changing extraordinary comparison would be a new edge and must be constructed explicitly.

The same packet supplies an actual corrected Morse face equation

\[
\delta\widehat h_M=\widehat q_J,
\]

with the occurrence-Koszul correction retained. This upgrades the Morse face from a scalar claim to a constructed face, but it remains in a different source/target model.

## 6. First executable next move

Construct one comparison roof

\[
c_Q:(J,T[1],a)\longrightarrow
(J_{\rm phys},Q_{\rm phys},\widehat q_J)
\]

or prove that no such comparison exists under the stated support and grading. Concretely it must include:

1. a source comparison between the six-point J and the corrected Morse source;
2. a target comparison from T[1] to the actual supported Q object;
3. a 2-cell showing that a maps to \(\widehat q_J\);
4. endpoint-connector and Rees/Cartier compatibility.

Only after this square is typed can \(h\), \(e_\nu\), and \(-k_\nu h\) be transported into the physical mapping object and tested as the remaining faces/filler.

## Disposition

Iteration 1 identifies a genuine coefficient-level face equation and a concrete incompatible-target obstruction. It does not construct all six physical edges, four faces, or the tetrahedral filler. No Agda source was changed in this pass because encoding a four-vertex record now would turn absent comparison maps into parameters and add no mathematical progress. No Git operations were performed.
