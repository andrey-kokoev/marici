# 1807 — The Complementary Pole-Log Is Occurrence-Even

## Question

Does Entry 1806's doubled-occurrence logarithm contain a relative-sign
component that survives the physical occurrence trace?

## Frozen object

Retain the two complementary labels

\[
e_1=g_{15},
\qquad
e_2=g_{234}
\]

before imposing their common physical section at \(y_{45}=0\). Because the
source integrand contains their product, the scalar occurrence space is

\[
\operatorname{Sym}^2\langle e_1,e_2\rangle
=
\langle e_1^2,e_1e_2,e_2^2\rangle.
\]

The class derived in Entry 1806 is the mixed class

\[
v_{\rm phys}=e_1e_2.
\]

## Complement involution

The label-complement involution exchanges \(e_1\leftrightarrow e_2\). In the
ordered symmetric basis its matrix is

\[
S=
\begin{pmatrix}
0&0&1\\
0&1&0\\
1&0&0
\end{pmatrix}.
\]

Therefore

\[
\boxed{S v_{\rm phys}=v_{\rm phys}.}
\]

The physical diagonal trace sends all three symmetric monomials to the same
section and maps \(v_{\rm phys}\) nontrivially. The antisymmetric wedge
\(e_1\wedge e_2\) is not a scalar coefficient class of the frozen product.
Consequently

\[
\boxed{
\dim(\text{relative-sign scalar excess})=0.
}
\]

This statement concerns the scalar occurrence coefficient. It does not erase
orientation signs belonging to an independently typed iterated residue map.

## Cyclic assembly

The complementary pair has a free orbit under \(C_5\). Hence its five
pole-twisted logarithms assemble as one regular representation,

\[
\mathbb Q[C_5],
\qquad
\chi=(5,0,0,0,0).
\]

Each occurrence carries the rank-one nilpotent from Entry 1806. Thus the
assembled nilpotent satisfies

\[
\operatorname{rank}N=5,
\qquad
N^2=0.
\]

## Narrow result

The only activated complementary soft family is occurrence-even and survives
physical diagonal identification. Its complexity is a regular \(C_5\)-orbit
of pole-twisted rank-one logarithmic extensions. No anti-diagonal scalar
coefficient and no new carrier structure are generated.

## Next falsifier

Analyze intersections among the 34 transverse supported region-wall pairs.
Determine whether their normal-crossing coefficient objects are exhausted by
tensor products of the already derived rank-one Kummer lines, or whether an
independently source-derived extension couples two transverse wall factors.

## Evidence

- research/benincasa/checkers/five_site_g5_complement_soft_occurrence_trace.py
- research/benincasa/results/five-site-g5-complement-soft-occurrence-trace.json
- allocator claim: seqclaim-6427456ae8d03e2b70846277
