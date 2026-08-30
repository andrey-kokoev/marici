# Eta Squared Is Invisible to S3 but Detected by S4

## Result

The explicit braid

\[
W_{\eta^2}=[[c_{31},c_{13}],[c_{31},c_{22}]]\in P_4
\]

is independently nontrivial under Artin's action on the free group. A direct
symbolic expansion of its free-group automorphism grows too rapidly to be a
useful bounded certificate. Evaluation on finite groups gives a smaller exact
witness.

For a group \(G\), an Artin generator acts on \(G^4\) by the Hurwitz rule

\[
\sigma_i:(g_i,g_{i+1})longmapsto
(g_i g_{i+1}g_i^{-1},g_i),
\]

with the inverse rule used for \(\sigma_i^{-1}\). If a braid acts nontrivially
on one tuple in one group, its free-group automorphism is nonidentity and hence
the braid is nonidentity.

## Resolution threshold

The checker exhausts every one of the

\[
|S_3|^4=6^4=1296
\]

tuples in \(S_3^4\). Every tuple is fixed by \(W_{\eta^2}\). Thus this entire
finite probe is blind.

The corresponding \(S_4\) probe is not blind. One witness is

```text
input  = [(1,2,4,3), (1,2,4,3), (1,2,4,3), (2,3,1,4)]
output = [(1,2,4,3), (2,1,3,4), (2,1,3,4), (2,3,1,4)]
```

Here permutations are encoded by their value lists. The second and third
components change. Consequently \(W_{\eta^2}\ne1\) in \(P_4\).

## Meaning

This establishes three logically distinct facts:

1. strand deletion says the braid is Brunnian;
2. the \(S_4\) Hurwitz witness says the braid itself is nonidentity;
3. the Moore filling quotient says its residue is the order-two class
   \(\eta^2\).

The order two belongs only to the third statement. It must not be projected
back to claim that the raw braid has order two.

The blind \(S_3\) layer is also informative. Low-resolution nonabelian probes
can report complete coherence even when the next finite probe detects a
Brunnian obstruction. This is a concrete instance of contextual faithfulness
failing below a minimum observation capability.

Subsequent testing sharpens this statement: \(S_4\) is the first detecting
member of the symmetric-group sequence, but not the smallest detecting group.
The metabelian subgroup \(A_4\) already detects the braid. The exact dihedral
reflection criterion is recorded in the later response-modulus packet.

## Replay

```powershell
uv run python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py
```
