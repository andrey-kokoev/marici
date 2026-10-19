# Positive forward operations do not prepare odd parity; signed detail is a different readout

**New batch, iteration 1 of 10.**

**Strength:** cone-preservation obstruction for a declared class, with exact tests of the existing retained-path API. Not a no-go for signed source operations or physical coherent preparation.

[Full boundary split](FULL-BOUNDARY-SPLIT.md) · [Checker](check_parity_preparation_gate.py) · [Receipt](results/parity-preparation-gate.v1.json)

## Fresh question

The twelve-occurrence selected spectral sector has rank four. Its old rank-two construction additionally selects odd reflection parity. Generic prefix-copy input reaches both parities. Does an existing retained operation actually supply that selection?

This turn reads the current state and the owning `RetainedSuccessorLedger` implementation. It distinguishes positive forward transport from the ledger's signed observer operations rather than treating all registered rational coefficients as derived preparation.

## 1. A scoped positive-cone obstruction

Start with nonnegative coefficient payloads. Successor copying, incidence sums, fiber means, reindexing, nonnegative masks and bilinear retained concatenation preserve coefficient nonnegativity. This follows directly from the nonnegative matrices and from multiplication of parent coefficients at each retained composition slot. Finite compositions of these operations preserve the same cone.

If J is a permutation reflection, a nonnegative vector v satisfying Jv=-v must vanish: every coordinate of Jv is nonnegative, whereas every coordinate of -v is nonpositive. Thus this forward class cannot prepare any nonzero odd state from such inputs.

The checker exercises all 100 primitive basis-pair products and the actual copy/decoder/summary matrices at word lengths 2, 3 and 4. These tests accompany the structural cone argument; they are not an exhaustive enumeration of every circuit.

**Scope matters:** arbitrary signed input payloads, signed masks, subtraction, algebraic spectral selection and physical phase control are outside this positive class. Coefficient nonnegativity is not assumed to characterize physical amplitudes or probabilities. This obstruction cannot close the overall physical gate.

## 2. The source already has signed subtraction—but as detail

The owning source implements `split_payload` by

    parent = D x,
    inherited = L D x,
    detail = x-L D x.

Its detail map is an idempotent signed readout, not positive forward transport. Nonnegative basis input can indeed produce negative detail coefficients. This prevents the erroneous stronger statement that the source API has no signed operation.

Reflection intertwines both L and D, so detail commutes with reflection. Nonetheless it is not an odd selector. Exact ranks are:

| Child word length | Parent / child coordinates | Detail rank | Even detail | Odd detail |
|---|---:|---:|---:|---:|
| 2 | 10 / 16 | 6 | 3 | 3 |
| 3 | 16 / 26 | 10 | 5 | 5 |
| 4 | 26 / 42 | 16 | 8 | 8 |

In addition, the detail map kills nonzero inherited odd directions. Therefore neither its image nor its action equals the odd-parity projector. Each basis test checks the actual source API and exact reconstruction by inherited-plus-detail records.

The relevant fibers differ: source detail compares sibling extensions of one parent; parity detail compares words related by the global graph reflection. The existing stage method must not be relabelled as a symmetry-orbit preparation.

## 3. An orthogonal parity observer is available mathematically

On the twelve-occurrence boundary, define

    E_even=(I+J)/2, E_odd=(I-J)/2.

Both have rank six and are symmetric orthogonal projectors in the ordinary coordinate-counting metric. The split x -> (E_even x,E_odd x) is reversible by summation and is a counting-norm isometry when both records are kept.

This differs from the generally oblique spectral split checked previously. Orthogonality of parity alone does not make its further rank-two spectral restriction orthogonal.

For a single coordinate input, its odd record contains +1/2 at that coordinate and -1/2 at the reflected coordinate. Such cross-word subtraction is exactly what the positive-forward class cannot supply. The even record is retained, not treated as an independently prepared physical output.

The actual ledger accepts a signed primitive odd payload through `retain_payload`, but the resulting record has operation **`supplied`**. Registration validates coefficients and provenance; it does not derive the odd input or its physical preparation.

## 4. Result and continuation

Two shortcuts are now ruled out within their stated scope:

1. Positive forward path transport cannot generate a nonzero odd payload from nonnegative inputs.
2. Existing successor mean/detail subtraction is not the required reflection-parity selection.

The next executable construction is a retained **symmetry-orbit mean/detail adapter**, using the actual graph involution and retaining both records. Test its equivariance under path concatenation, including mixed-parity products. This will expose which cross-word subtraction must be supplied and whether parity is even compatible with the proposed composition rule; it will not by itself implement preparation.

The scientific root remains null. No native phase control, physical measurement, photon output or normalization gain is admitted. Existing pinned work-net and downstream contracts remain unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_parity_preparation_gate.py
python research/scattering/seed-composition/check_parity_preparation_gate.py --check
python research/scattering/seed-composition/check_full_boundary_split.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

All tests use exact rational arithmetic. The checker recomputes its prerequisites, writes only its own receipt, and compares read-only under `--check`.
