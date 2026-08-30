# 1818 — The Active Transverse Pairs Assemble into a Rank-110 Physical Coefficient Object

## Construction

Combine:

- Entry 1809's exact nonzero source coefficients;
- Entry 1810's 110 labelled cyclic occurrences;
- Entry 1811's rank-one rational quadratic quotients
  \(\mathcal L_{A,B}\);
- Entry 1813's normal orientation lines;
- Entry 1817's physical intersection pairings;
- Entry 1216's external-Gram Kummer density.

On the nonsingular external-Gram chart, the supported physical object is

\[
\boxed{
\mathcal P_{\rm tr}
=
\mathcal K_{\det(H)^{-1/2}}
\otimes
\bigoplus_{(A,B)\in\mathcal O_{110}}
i_{A,B*}
\left(
\mathcal L_{A,B}\otimes\det N^*_{A,B}
\right).
}
\]

Here \(\mathcal O_{110}\) is the complete labelled active occurrence set.

## Normalization

For each ordered occurrence, the physical real-chain intersection index
cancels the sign of the determinant-line frame. The remaining scalar is
exactly the source double-residue coefficient certified in Entry 1809.
Every such scalar is nonzero.

Therefore

\[
\operatorname{rank}\mathcal P_{\rm tr}=110,
\qquad
\chi_{C_5}=(110,0,0,0,0).
\]

## Monodromy and support

The two coefficient factors remain distinct:

\[
T_{\rm quadratic}=+1,
\qquad
T_{\det H}=-1.
\]

On their generic normal-crossing locus these monodromies commute. At the
central threshold node, Entry 1812 shows that the quadratic factor splits
over the constant field \(\mathbb Q(i)\); it introduces no new kinematic
character.

## Result

The five-site transverse-pair lane yields a source-normalized, physically
activated, rank-110 supported coefficient object. Its support and twists are
compiled entirely from:

- existing threshold and marked-wall incidence;
- the existing external-Gram Kummer density;
- normal-orientation/Gysin data;
- source-specific rational quadratic quotients.

No new carrier generator is required.

## Scope

This is a local supported physical object on the nonsingular external-Gram
chart. Global continuation through \(\det(H)=0\) and simultaneous deeper soft
corners is not asserted.

## Next falsifier

Push \(\mathcal P_{\rm tr}\) to the external-Gram divisor. Compute whether the
Kummer twist and oriented quadratic quotient extend by the existing Gram
nearby-cycle/Gysin calculus or leave a supported excess.

## Evidence

- research/benincasa/checkers/five_site_g5_transverse_supported_physical_object.py
- research/benincasa/results/five-site-g5-transverse-supported-physical-object.json
- Entries 1216 and 1809--1817
- allocator claim: seqclaim-61b6cd114a1f001e721a634f
