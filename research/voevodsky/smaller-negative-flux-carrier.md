# Electron trial: a smaller negative-flux carrier

## Result

A four-whole-face carrier gives **−1 mode-oriented radial flux**, with **228 coefficient transfers**, compared with the original proton's 1836.

This is not simply the conjugated twelve-triangle proton: it has four modes rather than twelve, and a different transformation character under the proper tetrahedral group.

However, extracting its negative-circulation channel from the original proton while preserving amplitude gives **−1/3**, not −1. The standalone unit-reference normalization and the inherited source amplitude must not be conflated.

## Construction

The earlier retained-phase electron trial conjugated all twelve proton triangle modes. That preserves the complete 1836-arrow structure. Here we instead use one cyclic mode on each whole face:

```text
ABC, BAD, CDA, DCB.
```

These orders are outward oriented and obtained from ABC by the four proper diagonal tetrahedral rotations. For a face (a,b,c), define

```text
V = a + ω b + ω² c.
```

Use conjugate(V) for negative circulation. The mode bivector is the negative of the face area. Each face subtends π at the center and therefore contributes −1/4 to the same radial-flux observable used for the proton. The complete boundary contributes −1.

Scaling all coordinates by 1, 1/2, 1/10 or 1/100 leaves this flux unchanged. Thus the flux fixes no preferred geometric size.

## Same coefficient protocol

Keep the ambient three spatial coordinates and use the existing constructor without modifying its transfer-count convention:

| Stage | Nonzero transfers |
|---|---:|
| Local mode selection L | 36 |
| Four-placement alignment G | 48 |
| Collective return N | 144 |
| **Total** | **228** |

The exact checks give GL=LG=N, rank(N)=1 and a positive fixed-weight deletion certificate covering every arrow. There are 144 positive closed three-step cycles, with total trace 1.

This is a smaller *specified protocol*, not a proof of a global minimum over all representations. No extra conversion interface is included in the 228 core count.

If transfer count alone were used as a mass readout, the proton-to-candidate ratio would be 1836/228=153/19, approximately 8.05—not 1836. The smaller construction therefore does not reproduce the electron mass under that readout.

## Distinct symmetry character

The original twelve-site proton mode is invariant under the combined proper rotation and site-permutation action. Conjugating it leaves that property unchanged.

The four-face negative mode instead transforms by a one-dimensional character taking values 1, ω and ω², each on four of the twelve proper rotations. Its selected line is preserved, but its amplitude acquires a cyclic phase. This distinguishes it from the original conjugated proton construction.

## What can actually be extracted from the proton?

On one face, let F be its centroid and let

```text
v0 = F + ω a + ω² b,
v1 = F + ω b + ω² c,
v2 = F + ω c + ω² a.
```

The three Fourier channels, before dividing by sqrt(3), are exactly

```text
v0 + v1 + v2             = 0,
v0 + ω v1 + ω² v2        = 2ω V,
v0 + ω² v1 + ω v2        = −ω² conjugate(V).
```

With the unitary normalization 1/sqrt(3), their squared norms per face are 0, 16 and 4. The original three small-triangle modes have total squared norm 20. Thus the positive and negative channels retain 4/5 and 1/5 of the original squared norm.

Because each small triangle has one third of its face's area and solid angle, the same quadratic flux is preserved by this facewise Fourier transform. Summed over the four faces, it splits as

```text
+4/3 − 1/3 = +1.
```

The inherited negative channel is therefore not a unit negative-flux excitation. It has the same selected line as the standalone four-face candidate, but one third of its reference squared amplitude. Making its flux −1 requires multiplying that inherited amplitude by sqrt(3).

The transform uses the retained cyclic face orders. It supplies an explicit algebraic channel decomposition, not a particle-emission rule or a reason to reset that channel's amplitude.

## Outcome

We have a genuinely smaller negative-circulation construction and an exact relation to the original proton modes. We do not yet have a source-selected electron amplitude, mass or size. The strongest new source-bound result is the exact **+4/3 and −1/3 flux decomposition**, with its amplitudes retained.

## Reproduce

```text
python research/voevodsky/checkers/check_smaller_negative_flux_carrier.py
```

Twelve checks pass. Algebraic identities, group characters, source matching and operator checks use exact arithmetic. Numerical solid angles independently check the closed-boundary flux and scale controls.

Artifacts:

- `results/smaller_negative_flux_carrier.json`
- `results/smaller_negative_flux_carrier_store.json`

The original source and visualization are unchanged.
