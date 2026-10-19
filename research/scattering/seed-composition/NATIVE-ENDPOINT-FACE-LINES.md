# Exact native spinor/endpoint face-line adapter with retained polarization complement

**Third batch, iteration 6 of 10.**

**Strength:** exact coordinate, metric and operator bridge; conjugate-source and loop-phase tests. Not physical field admission or signed-charge preparation.

[Previous signed-sector comparison](SOURCE-CHARGE-SECTOR-BRIDGE.md) · [Checker](check_native_endpoint_face_lines.py) · [Receipt](results/native-endpoint-face-lines.v1.json)

## 1. Fresh source adapter

The owning `check_spinor_matter_link_adapter.py` already selects one nonzero column from each native Pauli projector P_i, retaining its norm as a line-coordinate metric. This turn reconstructs that adapter and compares it exactly with the normalized conference-matrix convention used by the endpoint parent.

The native carrier has eight raw complex coordinates. Its local projector L=diag(P_i) selects four negative-polarization face lines. Inside those lines, the coherent return N has rank two. These are distinct restrictions.

No owner producer is called. Current matrices are reconstructed read-only, with the historical native producer-hash caveat still retained in prerequisite evidence.

## 2. Rooted gauge and exact conference matrix

Let endpoint K=I-Q, where Q is its exact Hermitian conference matrix with Q^2=I. Choose

    w0=P0 e0,
    wi=Pi w0/Q(i,0) for i=1,2,3.

The endpoint anchor phases specify a coordinate convention, not a new interaction. Exact checks of all non-anchor overlaps confirm compatibility with the source projectors, rather than only forcing the first row to match.

All four w_i have the same norm

    n0=(3+sqrt(3))/6.

Define V by placing w_i in native face block i, and D=V*/n0. Then

    V*V=n0 I4, DV=I4, VD=L.

The four line coordinates use metric n0 I4. A formal V/sqrt(n0) gives an ordinary isometry, but the executable uses weighted coordinates so it does not need additional radical extensions.

The original owning column frame differs by an explicit diagonal rescaling/phase matrix. That relation and every norm are checked exactly. It is an adapter of known source coefficients, not a fitted replacement kinetic law.

## 3. Retain the four excluded directions

Let R=I-L. The map

    x -> (Dx,Rx),
    decoder(a,r)=Va+r

recovers all eight raw coordinates. Its weighted norm satisfies

    n0 ||Dx||^2 + ||Rx||^2 = ||x||^2.

R has rank four. No discarded polarization directions are hidden in the reduced face-line description.

The other rank-two noncoherent directions remain inside the four line coordinates; the adapter does not silently project them onto the logical doublet either.

## 4. Exact stage and kinetic transport

For the native defect operator

    H=(I-L)+2(I-N),

exact multiplication gives

    HV=VK,
    DLV=I4,
    DNV=(I4+Q)/2,
    NV=V(I4+Q)/2.

The native G stage equals N, so it has the same transported projector. Endpoint K has eigenvalues zero and two, each with multiplicity two. On the excluded polarization complement, HR=3R.

These identities supply the missing native-to-endpoint kinetic comparison. They do not identify all physical field interactions or energy scales. Nor is native 144-transfer support replaced by the support count in the reduced basis; support counts are coordinate/protocol-dependent.

## 5. Coefficient conjugation changes the selected raw source

Bare conjugation changes L and V. The checker finds

    L != conjugate(L),
    rank((I-L) conjugate(V))=4.

Thus coefficient conjugation does not stay in the same four native face lines. Its consistent partner is the conjugate source:

    conjugate(H) conjugate(V) = conjugate(V) conjugate(K).

Each labelled triangular loop phase +/-i changes sign. A diagonal face-phase gauge cannot map conjugate(K) back to K at fixed face labels, since loop products are gauge invariant.

This does not exclude an additional face permutation or antiunitary Pauli-frame transformation. Those are extra maps to specify and test; the bare sign of external charge does not supply them.

## 6. Next interaction test

The free native/endpoint bridge is now exact. Pull the actual endpoint charging diagonals back through V and test whether the native rank-two coherent return remains invariant. Keep both the rank-two line-mismatch record and rank-four polarization record.

That will distinguish a kinetic adapter preserving the free doublet from a charged interaction that mixes it with noncoherent directions. Signed charge, lead flux, coupling coefficients and physical admission remain explicit inputs.

The root stays null; shared sources, atlas and formal contracts remain unchanged. No opposite-charge preparation or annihilation is derived.

## Reproduce

```sh
python research/scattering/seed-composition/check_native_endpoint_face_lines.py
python research/scattering/seed-composition/check_native_endpoint_face_lines.py --check
python research/scattering/seed-composition/check_source_charge_sector_bridge.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Exact multiquadratic arithmetic verifies all frames, norms, operators and ranks. Prerequisites are recomputed; only the local receipt is written and `--check` is read-only.
