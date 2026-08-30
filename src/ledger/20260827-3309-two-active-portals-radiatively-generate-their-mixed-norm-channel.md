# Two Active Portals Radiatively Generate Their Mixed Norm Channel

Author: `marici.Figueiredo`

## Claim

Any source symmetry admitting both representation-labelled Higgs portals also
admits the neutral scalar operator (R_AR_B). In the radial scalar sector with
component counts

\[
(N_h,N_A,N_B)=(4,18,18),
\]

the exact Hessian-square divergence generates the mixed-norm coefficient

\[
C_{AB}\big|_{w=0}=8\delta_A\delta_B.
\]

Thus the uncoupled surface (w=0) is not radiatively closed when both portals
are nonzero. At nonzero (w), the two portal equations contain the mutual
feedback terms (36\delta_Bw) and (36\delta_Aw).

## Boundary

The theorem covers the radial norm sector. The complete complex matrix-scalar
grammar contains further single-trace and mixed tensor quartics that may alter
the fixed point and stability matrix. They must be included before granting RG
selector authority.

## Verification

- Packet:
  `research/flavor/flavor-direct-sum-mixed-norm-radiative-closure.md`
- Checker:
  `research/flavor/checkers/wp731_direct_sum_mixed_norm_radiative_closure.py`
- Result:
  `research/flavor/results/wp731_direct_sum_mixed_norm_radiative_closure.json`
- Exact checker outcome: 10/10 PASS.
- Epistemic-graph admission:
  `ev-000000007055-aafb72ea-affa-4eab-90a3-558d3b02ab65`.

## Remaining gate

Enumerate every independent mixed matrix-scalar quartic under the admitted
flavor symmetry, derive the closed beta system, and evaluate the complete
fixed-point stability eigenvectors against WP730's contrast projection gate.
