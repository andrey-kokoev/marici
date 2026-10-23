# Strict-diagram/native comparison with coefficient witnesses retained

## Constructed comparison

The [checker](checkers/check_strict_native_comparison.py) now compares the actual native44-channel fixture with the structure required by the strict analytical diagram. It uses the saved exact multiradical generator, embedding and readout matrices, not synthetic observer operators.

Fourteen checks pass:

-196 pairwise native full-field/readout and five-coefficient binding squares;
-2744 native comparison triangles, retaining both field and coefficient cocycles;
-all18 original interface coefficient laws;
-3136 symbolic analytical/native squares, **conditional on an observer encoder that is not yet supplied**.

The14-packet fixture is still the native domain of this result, not all esd7 packets.

## Actual native normalization

Write U_a for the source-derived full-field frame, P_a for the retained coefficient permutation, B_a for the five-coefficient embedding and R_a for its readout.

The checker directly recomputes the exact matrices

    R_a U_a = P_a R_root,
    U_a^-1 B_a = B_root P_a^-1.

The first is an equality of5x44 matrices, not only an equality on prepared five-dimensional states.

Consequently, with

    C_(a,b) = U_b U_a^-1,
    Pi_(a,b) = P_b P_a^-1,

all196 pairs satisfy

    R_b C_(a,b) = Pi_(a,b) R_a,
    C_(a,b) B_a = B_b Pi_(a,b).

All2744 triangles preserve both comparison laws. A normal form for the field map does not replace the coefficient witness or either execution history.

## Concrete information lost by a field-only comparison

For retained packets6 and24 in the assembled fixture:

- the full-field comparison is the identity;
- the coefficient comparison is `[1,4,0,2,3]`, of order5;
- their actual readout matrices differ;
- their actual coefficient embeddings differ.

Thus replacing their complete comparison by the identity breaks a full44-coordinate readout square, even though the physical field frames agree. This is actual native witness data, not a hypothetical objection to strictification.

## The precise analytical/native bridge family

Use different notation for the analytical charts: S_i,R_i^an, with source transition S_j R_i^an. A comparison to native packet a would have the form

    K_(i,a) = U_a L R_i^an,

where

    L : D -> C^44

is a source-defined observer encoder on an admitted common domain or finite packet.

Then the analytical route followed by K_(j,b) and K_(i,a) followed by the native comparison both reduce to

    U_b L R_i^an.

The checker type-checks all3136 such squares. Omitting L produces a domain error; the analytical observer domain is not silently identified with the native44-coordinate root.

The transported coefficient readout must additionally be

    R_native,a K_(i,a) = P_a R_native,root L R_i^an.

This identifies the remaining interface more precisely than an unspecified whole-diagram equivalence.

## Still missing

**No L has been supplied.** Formal field naturality holds for any typed L, including an uninformative map; it therefore cannot select the intended observer encoding. A valid source binding must specify:

1. the admitted observer domain or finite packet and the actual encoder;
2. which analytical endpoint/residual readouts factor through it, with exact intertwining equations;
3. which retained analytical face/tetrahedral witnesses correspond to the native coefficient comparisons and histories;
4. the direction and metric conventions, without silently identifying analytic chart roles with P/N/E species.

A finite44-coordinate encoding is not claimed to faithfully recover an arbitrary infinite-dimensional observer domain. Any finite packet restriction, quotient or nonfaithful observation must be explicit.

The intended analytical witness identification, native transport on the full esd7 complex,114-record producer and physical evolution remain open. The new result supplies the exact native side and the conditional comparison family; it does not manufacture the missing source map.

## Reproduction

```sh
python research/strominger/checkers/check_strict_native_comparison.py
```

- [Pairwise comparisons and order-five witness](results/strict-native-comparison.json).
- [Verification receipt](results/strict-native-comparison-verification.json).
