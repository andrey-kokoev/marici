# Held-out neutron mass comparison: the direct single-clock identifications fail

## Result

We tested the single-clock seam model against the retained rounded neutron–proton mass difference, without changing any model coefficient. Neither of its two immediate electron-gap identifications works.

| Reference identification | Predicted neutron–proton increment | Retained reference |
|---|---:|---:|
| Isolated involution gap E* = electron rest energy | 6.632109 MeV | 1.293333 MeV |
| Inactive dressed-record gap sqrt(5) E* = electron rest energy | 2.965969 MeV | 1.293333 MeV |

This rejects these **direct reference identifications for the seam-only increment with equal bare carrier baselines**. It does not refute the geometric belt formation construction, nor every possible interface interaction.

## 1. What is held fixed

The preceding single-clock construction fixes

    epsilon=J=kappa=1, g=1/2,
    delta/E*=(sqrt(5)-1)/2,
    Delta E/E*=21(sqrt(5)-1)/2.

Its source is the actual 21-seam network. Each seam was assigned a neutral record with occupation, consistency and mixing involutions. Those operations and their common clock were declared once, not selected from the measured mass.

The comparison assumes the extra seam energy is the neutron–proton splitting; other bare carrier contributions are equal. We do not insert an unknown negative bare-energy shift or binding correction to cancel the discrepancy.

## 2. Reference provenance

The input is the existing Nima receipt:

    research/nima/results/proton-hydrogen-helium-structure.json

It records rounded reference values, not an independently audited precision-constants dataset:

    m_p/m_e = 1836.152673,
    m_n/m_e = 1838.683662,
    m_e c^2 = 510998.95 eV.

Thus the frozen reference difference is 2.530989 electron masses, or approximately 1.293333 MeV. Attempting to refresh the NIST constants table during this audit returned HTTP 403. No fresh CODATA retrieval or uncertainty analysis is claimed. The discrepancies here are much larger than the displayed rounding scale.

The checker uses exact rational inputs and rigorous rational enclosures of sqrt(5). Decimal values in the table are presentation, not numerical tolerances used to decide agreement.

## 3. The two predicted dimensionless ratios

If E* is identified with m_e c^2, the predicted increment is

    21(sqrt(5)-1)/2 = 12.978714 electron masses.

If the actual inactive-record excitation sqrt(5) E* is identified with m_e c^2, the predicted increment is

    (21/2)(1-1/sqrt(5)) = 5.804257 electron masses.

Both exceed the reference 2.530989. Changing from electron masses to atomic-mass units cannot change this failed dimensionless comparison. Atomic binding energies are not corrections to the mass difference between a free neutron and a free proton.

Anchoring the proton to its observed value makes these failures especially transparent, but is not a prediction of the proton itself. A prediction of the neutron's relative atomic mass still requires the complete common-reference mass construction.

## 4. Redundant seam removal does not repair the prediction

Each paired sector's interface graph consists of two three-cycles connected by one bridge. Its six vertices represent six physical small triangles, and its seven edges represent their seams.

The checker enumerates all 128 subsets of the seven edges. Exactly sixteen are connected:

- nine spanning trees with five edges;
- six connected six-edge graphs;
- the full seven-edge graph.

Repeating a chosen graph under threefold sector rotation gives 15, 18 or 21 seam records. All preserve the connected amplitude-matching condition. Removing seams is a change to the physical record network, not a coordinate transformation; it is tested only as a diagnostic alternative.

Even the smallest such network gives

    15(sqrt(5)-1)/2 = 9.270510 electron masses

under the first identification, or

    (15/2)(1-1/sqrt(5)) = 4.145898 electron masses

under the second. Both remain too large. Thus identifying the fifteen independent matching equations instead of the twenty-one geometric seams does not resolve the discrepancy.

This enumeration concerns connected within-sector subgraphs repeated under C3, not every imaginable collective-register model or new interaction.

## 5. What would fitting the scale do?

Forcing the full 21-seam expression to equal the reference would require

    E*/(m_e c^2) approximately 0.195010773.

That is neither of the tested direct identifications. It is a descriptive fitted scale, not a derived constant, and it is not fed back into the Hamiltonian.

Likewise, adding a bare-core offset equal to the discrepancy would reproduce the target without explaining it. Any proposed extra contribution must instead be obtained from the same physical source and checked independently.

## 6. What remains useful, and the next gate

The exact formation result remains: native phase constraints, geometric seams and alignment select the existing coherent belt. The persistent-register model remains an explicit demonstration that a satisfied interface can support extra stored energy while leaving that return intact.

What fails is promoting the independent-record single-clock candidate to a neutron mass prediction using either immediately available electron reference.

The next source-level question is therefore not another numerical coefficient. It is whether the retained physical carrier really supplies **one independent elementary resource per seam**, and whether its elementary excitation is the electron reference at all. The seam projectors are constraints on overlapping carrier modes; their number alone does not establish that many independent physical excitation factors. The construction explicitly added those factors.

A further model must derive its excitation Hilbert space, interface interactions and common elementary reference together. It should retain this failed candidate as a control rather than silently replacing its parameters. No unique replacement is asserted by this comparison.

## Reproduction

    python research/voevodsky/checkers/check_single_clock_seam_record.py
    python research/voevodsky/checkers/check_seam_mass_comparison.py

Results: `research/voevodsky/results/seam_mass_comparison.json`.

The report includes frozen-reference provenance, source hashes, exact prediction formulas, rational enclosures, all connected subgraph counts and the explicitly nonpredictive fitted-scale diagnostic.
