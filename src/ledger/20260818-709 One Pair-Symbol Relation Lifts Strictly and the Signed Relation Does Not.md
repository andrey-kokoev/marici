---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 709 — One Pair-Symbol Relation Lifts Strictly and the Signed Relation Does Not

## Question

Entry 707 finds two relations in the branch-discriminant symbol. This entry
tests them against the frozen double-residue geometry before invoking any
derived comparison.

## The repeated plus occurrence

For the two pair supports

\[
(q_{\mathfrak g_2},q_{\mathfrak g_{23}}),\qquad
(q_{\mathfrak g_3},q_{\mathfrak g_{23}}),
\]

direct substitution into the Cayley--Menger polynomial gives literally the
same quadratic \(K_+(c)\). Moreover, in the common orientation and coordinates
\((a,b)\),

\[
\det\frac{\partial(q_{\mathfrak g_2},q_{\mathfrak g_{23}})}
{\partial(a,b)}=1,
\qquad
\det\frac{\partial(q_{\mathfrak g_3},q_{\mathfrak g_{23}})}
{\partial(a,b)}=1.
\]

Hence both double residues are represented by the same form

\[
\frac{dc}{\sqrt{K_+(c)}}.
\]

Therefore the first symbol relation lifts strictly:

\[
\boxed{[2,23]-[3,23]=0}
\]

in the frozen pair-residue model. No homotopy or fitted identification is
required.

## The signed pair relation

The minus pair \((q_{\mathfrak g_2},q_{\mathfrak g_3})\) and the plus pair
above have discriminant ratio

\[
\boxed{
\frac{\Delta_{23}^-}{\Delta_{23}^+}
=
\frac{(P_1-X_2+X_3)(P_1+X_2-X_3)}
{(P_1-X_2-X_3)(P_1+X_2+X_3)}.}
\]

This is not a square in the generic rational function field. Since the square
class of a quadratic branch divisor is invariant under rational changes of
fiber coordinate and coefficient rescaling, the two quadratic residue local
systems are not rationally isomorphic over the frozen base.

Thus Entry 707's weighted signed relation does not lift by a direct rational
identification of the two pair-residue complexes.

## Narrow conclusion

The two-dimensional symbol kernel splits by mechanism:

\[
\boxed{
\text{one strict occurrence identity}
\;\oplus\;
\text{one relation requiring additional derived data}.}
\]

The nonsquare test does not rule out a correspondence, extension, or
specialization-cone homotopy involving a larger complex. It rules out only the
tempting direct identification of the signed quadratic residues.

## Evidence

- `research/benincasa/check_pair_residue_relation_lifts.py`;
- `research/benincasa/generic_lower_collision_result.json`;
- Entries 185, 707;
- allocator claim `seqclaim-990e04dec806903b10bbf353`.

## Next falsifier

Form the specialization cone for the signed pair
\((q_{\mathfrak g_2},q_{\mathfrak g_3})\) and one plus occurrence while
retaining their distinct quadratic Kummer characters. Test whether the
weighted symbol relation is the boundary of a source-derived triple-support
cell. The only nearby candidate in the deletion cube is the disappearing
triple \(q_{\mathfrak g_2}q_{\mathfrak g_3}q_{\mathfrak g_{23}}\); its
boundary must be computed, not inferred from the matching one-dimensional
grade.
