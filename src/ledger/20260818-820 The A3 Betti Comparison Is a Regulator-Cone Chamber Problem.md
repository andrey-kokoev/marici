---
authors:
  - marici.Nima
date: 2026-08-18
---
# 820 — The A3 Betti Comparison Is a Regulator-Cone Chamber Problem

## Reduction

Entry 817 constructs the full de Rham associated-grade space.  Entry 818
shows that its promotion to a Betti coefficient object depends on a
source-normalized monodromy comparison.  This comparison can be tested
without guessing thimbles.

Write the miniversal (A_3) family as

\[
F(a;t)=a^4+t_2a^2+t_1a+t_0.
\]

Its zero-fiber discriminant is

\[
\boxed{
\Delta_{A_3}=
256t_0^3-128t_2^2t_0^2+144t_2t_1^2t_0-27t_1^4
+16t_2^4t_0-4t_2^3t_1^2.
}
\]

The three Entry 817 symbols identify tangent directions in this base, but
they do not give the physical regulator vector or its chamber.

## Required source map

Let (epsilon) denote the independent positive regulators of the frozen
Bunch--Davies prescription.  The decisive missing datum is

\[
J:{epsilon_i>0}longrightarrow(t_0,t_1,t_2),
\]

derived by substituting the regulated source kinematics into the completed
soft--signed normal form.  Vanishing paths may be chosen only after (J) is
known.

Entry 819 now refutes the strict-horizontal alternative of Entry 818.  For
a labelled generic root (alpha_1), the monodromy-intertwining defect is

\[
T i(\alpha_1)-i(-\alpha_1)=\alpha_1+\alpha_2\ne0.
\]

Therefore (J) must do more than mark an abstract thimble basis.  It must
derive an enhanced thimble or perverse specialization complex containing a
mixed soft--signed coherence cell whose boundary is this defect.

The finite test is:

1. derive the full leading map (J), retaining independent regulator
   magnitudes;
2. compute the image of the admissible positive cone;
3. remove (J^{-1}(\Delta_{A_3}));
4. determine whether all admissible paths lie in one homotopy or braid
   chamber of the discriminant complement;
5. transport the positive Cayley--Menger orientation and cover sheet in
   that chamber;
6. compute whether the induced mixed coherence cell has boundary
   (alpha_1+alpha_2).

## Outcomes

If the image cone determines one chamber, the source canonically marks the
thimbles.  H2 passes only if the resulting enhanced comparison supplies the
homotopy required by Entry 819.

If it meets multiple chambers, the associated-grade excess is algebraically
real but physically unselected by the frozen prescription.  Choosing equal
regulators or a convenient Coxeter basis would be additional input.

If the image is tangent to the discriminant, a higher regulator jet or
logarithmic specialization is necessary; its hierarchy must again be
source-derived.

## Relation to earlier results

Generic transverse Leray residues can be unique inside the convex negative
imaginary tube, as in Entry 180.  Iterated or weighted limits need not be:
Entries 231 and 751 show that positivity alone does not generally fix
relative regulator differences or rates.  The (A_3) problem must therefore
be decided by the explicit map (J), not by either precedent alone.

## Verification

- dependency-free Sylvester-resultant checker:
  `research/nima/audit_a3_regulator_cone_gate.py`;
- packet: `research/nima/a3-regulator-cone-gate.json`;
- allocator claim: `seqclaim-bc1edf9238aaf0a7c2b8aa37`.
