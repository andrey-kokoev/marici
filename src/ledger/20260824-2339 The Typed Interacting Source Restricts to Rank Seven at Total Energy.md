# 2339 — The Typed Interacting Source Restricts to Rank Seven at Total Energy

## Frozen question

Restrict the correctly typed rank-twenty-six interacting three-site quotient
directly to the already declared total-energy divisor

\[
E_T=X_1+X_2+X_3=0.
\]

Use the literal source numerator \(q_{g_{23}}+q_{g_{31}}\), its source-derived
first derivatives, all three labelled connection axes, and the complete
rank-twenty-six moving-wall extension.  Do not project through the obsolete
rank-twenty-one presentation.

This calculation is the tangent Gauss--Manin closure inside the specialized
quotient, using

\[
\partial_{X_1}-\partial_{X_3},
\qquad
\partial_{X_2}-\partial_{X_3}.
\]

It is not identified with a complete derived pullback or logarithmic nearby
cycles.  An independent all-ambient-axis census gives the same rank, so the
normal derivative does not enlarge this closure.

## Exact finite-field result

At the three nonsoft fibers

\[
(2,3,-5),\qquad(3,5,-8),\qquad(5,8,-13)
\]

over \(\mathbf F_{32003}\), the specialized tangent source closure has

\[
\operatorname{rank}=7.
\]

All three fibers have the same relation rank \(11501\).  The literal source
continues to have support three, and its first covariant jet has rank three.
The generic rank is twenty-six, so specialized tangent closure loses nineteen
directions.

At the transverse control fiber \((2,3,-4)\), where \(E_T=1\), the same
presentation and source recover rank twenty-six.  The tested collapse is
therefore localized on the declared total-energy support rather than being a
generic failure of the chosen source.

## Interpretation

This is a supported collapse on an existing Carrier divisor, not new support:

\[
26\longrightarrow7
\qquad\text{on}\qquad E_T=0.
\]

It must not be conflated with the already derived rank-twelve logarithmic
nearby-cycle system, whose nilpotent has rank four and square zero.  Tangent
closure in the specialized quotient, derived pullback, and nearby cycles have
different variance and can retain different grades.

The next finite construction is therefore the rank-twenty-six total-energy
Rees/nearby object itself:

\[
\psi_{E_T}(\mathcal M_{26}).
\]

The direct rank-seven source closure is one associated restriction grade.  The
missing nineteen directions are not yet classified as vanishing cycles, exact
tails, or physical readout loss.

The known rank-twelve marked nearby system is a smaller localization sector,
not automatically the target of a rank-twenty-six specialization map.  A
comparison with it is admissible only after deriving the required
deletion/localization morphism from the five-mark relative union.  No map is
inferred from the ranks seven and twelve.

## Narrow conclusion

The generic contextual-faithfulness theorem does not specialize by naive
restriction across total energy.  This does not falsify contextual
faithfulness of the nearby-cycle object, and it introduces no new Carrier
stratum.

## Artifacts

- `research/benincasa/check_rank26_total_energy_direct_specialization.py`
- `research/benincasa/rank26-total-energy-direct-specialization.json`
- `research/benincasa/check_rank26_tangent_support_closure.py`
- `research/benincasa/rank26-tangent-support-closure.json`

Sequence claim: `seqclaim-f573f574ec8b08541a51b2dc`.
