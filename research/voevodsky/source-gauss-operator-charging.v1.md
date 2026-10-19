# Source-derived Gauss charging: a constructed replacement, and its exclusion

## Problem and conjecture

The unit-gap-per-arrow mass law was already excluded. Test a materially different
law: retain the native source kinetic operator but replace independent occupied
register gaps by the operator square of the source graph's Gauss response. Can
one common charging law explain both the proton/elementary ratio and the
belt-minus-proton splitting?

SCC classification: **forward realization** from incidence to a Gauss energy,
with **attachment transport** of the weighted source modes before scalar energy
readout. The stratum is the selected 12-, 18-, and 4-mode one-occupation sectors,
not the full native carrier or an independently quantized dynamical link field.

## Frozen source and rivals

Before computing candidate energies, the contract was frozen in
`contracts/source-gauss-operator-charging.v1.json`. Coefficients beta=3/5 and
eta=1/5 reuse the old feedback fixture. Neither is fitted to a mass. The positive
coefficient family keeps these same source graphs, K operators and boundary rule.

The proton/belt matter coefficients and metric come from
`results/weighted_matter_link_adapter.json`. Their exterior ports are the actual
cross-face endpoints in `results/all_face_contact.json`. The elementary sector
uses its four source modes, all six internal links and four exterior leads, with
K_e=I-Q from the source spinor conference matrix (Q=Qdagger, Q^2=I, trace Q=0).
The boundary rule, electrostatic reduction and single-occupation quantization
are declared constructor inputs; source data do not uniquely select them.

Named rivals:

1. The excluded independent unit-gap-per-arrow law.
2. Classical Gauss charging of an expected density.
3. The operator-square Gauss law tested here.

No extra neutral mediator, fitted species offset or arrow-count multiplier is
included. The common electrical-looking charge is an **internal occupation
charge**, not an identification of physical proton/electron/neutron charges.
In particular the occupied belt is not being declared electrically positive.

## Construct the operator before reading masses

For a sector let B be the internal incidence and let D count exterior ports.
The grounded electric Laplacian and response are

    L_boundary=B B^T+D,   C=L_boundary^(-1),
    F=B_full^T(C,0).

For every basis occupation e_i, F e_i obeys the full Gauss constraint, including
exterior charge -1. The checker verifies the full Gram identity F^T F=C, not
only diagonal field energies. Circulation fields are orthogonal to gradient
fields and add nonnegative electric energy; this is a static minimized response.

On the single-occupation quantum space N_i N_j=delta_ij N_i, put

    E_e=sum_i F_ei N_i,
    H_s=K_s+(beta/2)sum_e E_e^2+(eta/2)Q_s^2
       =K_s+(beta/2)diag(C_ii)+(eta/2)I.

The vacuum sector has N=E=Q=0 and energy zero in the same direct-sum system.
All three carrier graphs share one retained exterior coordinate. Inactive
sectors are not replaced by differently normalized reservoirs.

The proton/belt kinetic operator K=M^-1 L_matter retains the source metric;
M^1/2 K M^-1/2 is a positive symmetric graph operator. The elementary K_e has a
two-dimensional zero-energy subspace. This replaces the old unit register
occupation baselines by graph-response energy rather than renaming them.

### Charge variance is not optional

For a normalized density rho, the quantum electric expectation is
(beta/2) sum rho_i C_ii, not (beta/2) rho^T C rho. Their difference is

    (beta/2) sum_i rho_i (e_i-rho)^T C(e_i-rho) >= 0.

For the uniform elementary state the coefficients are 1/5 versus 1/8, giving
an energy difference 9/200 at the frozen beta. This follows from the operator
product; it is not a mass-fitting correction or adjustable vacuum offset.

The E_e here are constrained response operators, not independent canonical
momenta with a constructed conjugate link-field Hilbert space. This is a
reduced electrostatic candidate. No dynamical quantum-field parent, physical
preparation or full-native ground-state claim is inferred.

## Risky consequences and exact results

The checker first constructs all energies, then opens the separately pinned
held-out reference. No empirical quantity enters C, K, beta or eta.

The proton response diagonal is constant 29/105; the elementary diagonal is
constant 2/5. Hence the source kinetic ground states survive unchanged and

    E_p=29 beta/210+eta/2,
    E_e=beta/5+eta/2.

The belt diagonal has THREE values, repeated six times, rather than two.
The attempted reuse of the classical two-density reduction failed this exact
test. The final calculation retains the complete 18-mode weighted operator.
Rational LDL positive-definiteness of M(H-xI), bracketed by the minimum charging
diagonal and the coherent-source Rayleigh trial, certifies the lowest eigenvalue
by 80 bisections. The reported energy interval has width below 10^-23.

| Readout | Frozen candidate | Held-out reference |
|---|---:|---:|
| Proton/elementary | 64/77 = 0.831168831... | 1836.152673 |
| (Belt-proton)/elementary | 0.10606296078761786... | 2.530989 |

Absolute model-unit energies are E_p=32/175 and E_e=11/50; the full rational belt
interval is retained in the result. Both energies use the same empty reference.
No physical unit is assigned from these mismatches.

## Strongest falsifier: all common positive coefficients

For EVERY beta>0 and eta>=0 in the frozen graph family,

    E_p/E_e = [(29/105) beta+eta]/[(2/5) beta+eta],
    29/42 <= E_p/E_e < 1.

The ratio is a weighted mean of 29/42 and 1. The inequality is an algebraic
family-wide result, not extrapolation from a parameter sweep. It rules out the
required proton ratio and therefore the simultaneous mass comparison regardless
of beta, eta or an overall conversion of model units. A coarser check follows
from L_p=I+L_internal >=I: C_p<=I would already bound the ratio by 5/2.

## Disposition and surviving scope

**Refuted as a joint mass explanation within this declared reduced branch.**
The source-backed Gauss constructor, positive operator energies and retained
variance calculation survive. No physical mass law is admitted, and the earlier
unit-gap no-go is neither weakened nor overwritten.

The new exclusion localizes another failure: one-occupation charging on these
fixed response graphs yields comparable sector energies, not a hierarchy near
1836. Tuning a common field coefficient cannot repair it. A new branch must
supply independently sourced collective occupations, an inequivalent charging
form/boundary mechanism, or additional interactions with their energy-bearing
degrees of freedom specified. This result does not establish which such branch
is correct. Do not introduce capacitances or offsets fitted to the missing mass.

The first missing source object remains a physically selected charging action
on sharp sectors with its quantum parent and common empty reference. This branch
stops here; no authority-only successor is presented as an executable theorem.

## Verification and provenance

    python research/voevodsky/checkers/check_source_gauss_operator_charging.py
    python research/voevodsky/checkers/test_source_gauss_operator_charging.py

Seven regression controls pass. The new result binds the prospective contract,
source packets, reference and checker dependencies. Upstream packets were read
and hash-checked, not all freshly rerun. No existing mass or reaggregation ledger
was reset, charged or promoted.

The first two SCC freezes preserve implementation failures: a wording assertion
and the unjustified two-type diagonal assumption. Neither produced a scientific
receipt. The final freeze retains the same prospective model and coefficients,
with corrected full-matrix computation. The checker succeeds when it correctly
certifies the candidate's failure; checker success is not conjecture survival.
