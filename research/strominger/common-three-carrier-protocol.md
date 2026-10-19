# One coefficient assembler for proton, neutron and electron

## Implemented contract

`checkers/assemble_metric_coefficient_protocol.py` accepts labelled complex coordinates, a positive diagonal metric, a local-selection projector L and an alignment projector G. Its code has no particle branches.

It verifies metric orthogonality, idempotence and commutation, then constructs

    N = G L,
    H = (pi/4) [(L-I)^sharp(L-I) + (G-I)^sharp(G-I)]
      = (pi/4) (2I-L-G).

Sharp is the adjoint in the supplied metric. The return N is derived, not supplied to the assembler. Its exact matrix is subsequently compared with each independently stored native return. N is the feedback stage; it is not counted again as an energy defect.

This is a common **projector-stage constraint energy**. The proton/neutron construction, exchanged excitation multiplicities, equal-weight degeneracy and representation controls were already established in `research/voevodsky/constraint-energy-and-retained-record-accounting.md`. This implementation consolidates that rule and adds the native electron to its common executable interface; it does not newly discover the proton/neutron energy law. It is distinct from the older triangle-character Hamiltonians, which use different elementary operations. All three new energy results below use precisely the same two-defect rule and normalization.

The arithmetic is exact Q(sqrt(2),sqrt(3),sqrt(5),i). Three explicit native import adapters translate existing coefficient conventions into this one schema. In particular, neutron numerator matrices are divided by d_j and retain metric diag(1/d_i); they are not treated as Euclidean matrices.

## Common measures

Energy entries below are in units pi/4.

| Carrier | Coordinates | rank L | rank G | rank N | Stage supports L/G/N | Transfers | tr(H)/(pi/4) |
|---|---:|---:|---:|---:|---|---:|---:|
| Proton | 36 | 12 | 3 | 1 | 108 / 432 / 1296 | 1836 | 57 |
| Neutron | 36 | 3 | 12 | 1 | 432 / 108 / 1296 | 1836 | 57 |
| Electron | 8 | 4 | 2 | 2 | 16 / 64 / 64 | 144 | 10 |

The common energy spectrum is obtained from the four joint projectors LG, L-LG, G-LG and I-L-G+LG:

| Carrier | multiplicity at 0 | multiplicity at 1 | multiplicity at 2 |
|---|---:|---:|---:|
| Proton | 1 | 13 | 22 |
| Neutron | 1 | 13 | 22 |
| Electron | 2 | 2 | 4 |

All return states have zero constraint energy. Traces are sums over excitation energies, not the energies of the return states.

**Finding:** proton and neutron interchange local/alignment ranks and supports, but this symmetric two-defect energy gives the same spectrum. It cannot supply their rest-energy difference. Electron here means the native tetrahedral attachment protocol, not the conditional full-five-cell protocol.

## What “weight” can mean in this interface

The retained protocol has a directly measured computational weight: its nonzero transfer count. There is also a basis-independent carrier dimension, rank N, and a metric-covariant operator spectrum. These are separate measures.

A checked control rotates the same rank-one projector from diag(1,0) to the projector on (3/5,4/5). With L=G it changes the three-stage count from 3 to 12 while leaving the spectrum unchanged. Consequently bare transfer count cannot itself be an intrinsic mass observable.

Physical weight requires an energy attached to the retained state relative to a common vacuum and a common unit. The current shared constraint operator gives zero there for all three. The neutron's prior 21-register occupation law supplies a separate nonzero term; it has not been inserted into the common rule by special-casing the neutron. The next unification target is the retained occupation/interactions layer for all three.

## Exact verification

```sh
python research/strominger/checkers/check_common_three_carrier_protocol.py
```

Twenty checks passed:

- Native return matrices reconstructed exactly, with expected supports and ranks for all three.
- Metric-adjusted rational chart rescalings preserve all reported measures and conjugate both return and energy operators correctly.
- Singular metrics, nonprojectors, nonorthogonal projectors and noncommuting projectors rejected.
- The non-invariance of transfer count under an orthonormal frame change demonstrated explicitly.

Inputs bind the proton native manifest, the source-bound neutron bridge and native electron spinor store. Shared source/store files are not written. Packets and source hashes are in `results/common-three-carrier-protocol/`.

## Unified and remaining layers

- Geometry and scheduled cycle evolution: existing common backend.
- Coefficient return and projector-stage energy: common backend implemented here.
- Primitive geometry-to-local-coefficient adapters: still explicit native data.
- Vacuum-relative occupation energy and its calibration: next work.
