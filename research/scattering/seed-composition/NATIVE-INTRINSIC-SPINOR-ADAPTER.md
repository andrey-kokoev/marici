# Exact native/intrinsic face adapter and the distinction between inverse lift and conjugation

**Third batch, iteration 3 of 10.**

**Strength:** exact stored-coefficient comparison, stage intertwiners and residual-preserving conditional embeddings. Not physical charge conjugation or a derived source-library enlargement.

[Previous attachment bridge](FIVE-CELL-ATTACHMENT-BRIDGE.md) · [Checker](check_native_intrinsic_spinor_adapter.py) · [Receipt](results/native-intrinsic-spinor-adapter.v1.json)

## 1. Fresh native fixture and receipt boundary

The native tetrahedral spinor store supplies four Pauli projectors and the exact eight-coordinate L/G/N matrices. Their logical return has rank two and stage supports 16+64+64=144.

The prerequisite hash in its historical verification receipt still matches, but the producer-script hash no longer matches that receipt. This turn records the mismatch rather than rewriting the shared receipt or calling its producer (which writes shared stores). No claim is made that the full historical producer suite was freshly replayed.

The following adapter, isometry and stage identities are independently recomputed from the current stored matrices. Every input is hashed in the new local receipt.

## 2. No fitted Pauli rotation is needed locally

For both intrinsic chiralities, the attachment encoding matches the native one after reversing the four face blocks, retaining each block's two-component order. The eight-coordinate permutation is

    (6,7,4,5,2,3,0,1).

If S is that permutation matrix and J_n the native rank-two encoding, then

    J_intrinsic_local = S J_n,
    S* S=I,
    S L_native = L_intrinsic_local S,
    S N_native = N_intrinsic_local S.

Both G stages equal their N stages, so their intertwining follows as well. This is an explicit geometric-face/Pauli-frame comparison, not an arbitrary whitening or a particle-name identification.

## 3. Global embeddings retain the native rejected complement

Let J_g encode ten logical cell coordinates into forty intrinsic face coordinates, and let W_P be either of the two global doublet encodings. Define

    F_P=J_g W_P J_n*.

Exact sparse multiplication verifies the native/global L, G and N stage squares:

    F_P stage_native = stage_global F_P.

F_P has rank two and F_P*F_P=N_native. It is therefore an isometry on the native coherent doublet, not on all eight raw inputs.

Keep R=I-N_native as a separate native residual record. Then

    x -> (F_P x,Rx),
    F_P*F_P + R*R=I,
    decoder(y,r)=F_P* y+r.

This preserves all eight input coordinates and their counting norm; the residual has rank six. No rejected native information is silently squeezed into the rank-two global output.

Both choices of P remain possible. The adapter does not select a global doublet, replace native 144 transfers by global 3120, or establish equality of physical energy laws.

## 4. The transported five-cycle is additional symmetry data

For each chirality and global doublet, derive the logical action

    U_P=W_P* T_cell W_P.

The checker verifies unitary transport and the exact intertwiner T_cell W_P=W_P U_P. Under the displayed source lift convention,

    U_P^5=-I, U_P^10=I,

with neither U_P nor U_P^2 equal to I. Its order is exactly ten.

The native binary-tetrahedral symmetry group has order twenty-four. By the finite-group order theorem, no element in that group has order ten. Thus transporting the five-cycle into the native coherent frame gives a conditional enlargement, not a symmetry already contained in the native group.

A unitary extension to all eight raw native coordinates exists:

    U_native=J_n U_P J_n* + (I-N_native).

It acts as the induced logical transport on the doublet and identity on retained residuals. Its existence does not authorize it as a native physical operation.

## 5. Inverse action is not entrywise conjugation in this frame

For all four case/chirality/carrier combinations, exact matrices show

    U_P^-1=U_P* != entrywise_conjugate(U_P).

This distinguishes the actual inverse transported seed action from merely conjugating coefficients in the explicit adapter frame. The comparison is frame-dependent: it does not rule out a different antiunitary intertwiner with an additional unitary frame map.

Neither inverse action nor an antiunitary representation relation is automatically a physical charge-conjugation operator. The native source itself permits charge families Q_q=qN; the next test must ask what happens to those operators rather than importing opposite charge from reversed arrows.

## 6. Next executable gate

Construct a frame-explicit antiunitary intertwiner for the logical five-cycle and its reverse. Retain the native charge family Q_q=qN and test whether the intertwiner reverses the charge operator, or only a seed/representation action. Keep global doublet choices and central lift signs explicit.

The scientific root remains null. Shared atlas, source stores and formal contracts are unchanged. This turn repairs a mathematical comparison gap, not physical preparation, spin statistics, energy transport or annihilation.

## Reproduce

```sh
python research/scattering/seed-composition/check_native_intrinsic_spinor_adapter.py
python research/scattering/seed-composition/check_native_intrinsic_spinor_adapter.py --check
python research/scattering/seed-composition/check_five_cell_attachment_bridge.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Exact multiquadratic complex arithmetic reconstructs current stores. Owner producer entrypoints are not called; historical receipt freshness is reported separately from the new adapter checks. Only the local receipt is written and `--check` compares read-only.
