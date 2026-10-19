# Neutron canonical binding, iteration 3: exact occupied-state closure

## Completed construction and its scope

The declared retained-bank interface now has an exact minimal closure for the actual coherent neutron preparation under all bound pulses and its native rotation. The closure has **11 complex dimensions**, with an explicit **22-dimensional real canonical chart**. It is not the neutron's one-dimensional return space.

Together with the preceding two receipts this supplies:

1. an isometric full-source binding to six actual neutron rim modes and the retained 16-coordinate dynamical source bank;
2. covariance using a retained three-valued native rotation frame;
3. the exact minimal occupied-state closure, canonical Hamiltonians, full pulse/rotation generators and reverse recovery.

This completes the mathematical binding for that declared interface. The address policy, moving interaction frame and empty-bank preparation remain explicit inputs. Nothing here selects a unique intrinsic neutron rest-energy law.

## Fresh inputs

Read and validate current hashes for:

- `neutron-canonical-record-binding.json`;
- `neutron-canonical-rotation-frame.json`;
- the native `belt_three_by_twelve_store.json`.

No shared neutron/source backend was changed.

## An exact 13-coordinate starting envelope

Use coordinates (r,a,s):

- r: six normalized actual neutron rim-mode amplitudes;
- a: six coefficients of the original source bank features f_i;
- s: the prepared coherent neutron's component orthogonal to all six rim modes.

The bank feature Gram is D_ij=f_i* H f_j. The metric is

    M13=diag(I6,D,beta),
    beta=S/nu-6,
    nu=4198/675, S=1196/15.

The unnormalized coherent neutron is x0=(1,1,1,1,1,1,0,0,0,0,0,0,1), with budget B=S/nu. Dividing by sqrt(B) gives the unit preparation used in the previous energy calculation.

The remaining bank directions start at zero and no pulse generates them. The native spectator here is one *prepared vector*, not a claim that arbitrary neutron spectator states are one-dimensional. Its invariance follows from the actual native rotation fixing both the full coherent mode and the sum of the six rim modes.

At frame t, each pulse direction is

    d_i,t=(e_(pi^t i),-e_i,0),
    P_i,t=d_i,t d_i,t^T M13/2,
    E_i,t=I-2P_i,t.

Thus no new generator is fitted to obtain closure.

## Minimal closure, not a guessed truncation

Starting with x0, repeatedly apply the six frame-zero pulses and the native rotation. Exact rational rank tests add independent images until the generated space stabilizes at dimension 11. The receipt retains a generator-word witness for every added basis vector.

Let B11 be its 13-by-11 basis matrix and g=B11^T M13 B11. The metric left inverse is

    L=g^-1 B11^T M13.

For the rotation and all 18 port/frame exchanges, the compressed operator A11=L A13 B11 obeys

    A13 B11=B11 A11,
    A11^T g A11=g.

Every continuous pulse projector obeys the same intertwiner. Therefore no information generated from this preparation is discarded.

## Ten active modes and one fixed prepared component

The eighteen port/frame directions span ten complex dimensions. The prepared state also has one nonzero component fixed by every pulse and rotation. This produces the 11-dimensional closure.

For the unit coherent preparation, the metric weights are

    active: 2031832/9333285,
    fixed:  7301453/9333285.

They sum to one. These are component norms, not additive energy assignments. The fixed component is retained rather than deleted as a zero-energy nuisance.

## Explicit canonical pulse calculation on the closure

For a complex closure coordinate z, set

    z=q+i g^-1 p/2.

The inherited symplectic form becomes sum dq_i wedge dp_i. For each stored exchange E, let P=(I-E)/2. Its canonical Hamiltonian is

    h(q,p)=q^T g P q + p^T P g^-1 p/4.

The real Hamiltonian generator intertwines exactly with zdot=-iPz. All 18 such comparisons are checked. The inherited action primitive is

    p dq-d(q^T p)/2.

This is a coordinate transport of the original source energy, not a newly declared summed Hamiltonian. The preserved quadratic budget is q^T g q+p^T g^-1 p/4.

## What happens to the occupied neutron

After the first AB pi pulse, starting from the unit coherent neutron and empty bank:

| Component | Exact norm weight |
|---|---:|
| Original coherent neutron mode | 615585721/724148100 |
| Other native neutron directions | 52078289/724148100 |
| Dynamical source bank | 2099/26910 |

These sum to one. With a=nu/S=2099/26910, the three weights are (1-a)^2, a(1-a), and a.

Applying the native rank-one return projection at this point would discard both the noncoherent neutron component and the bank. It is therefore not a valid replacement for this occupied-state evolution.

The initial addressed pulse energy remains **2099/53820**, exactly as before. Pulse energy, native occupation probability and conserved budget are three different quantities.

## Verification

```sh
python research/strominger/checkers/check_neutron_canonical_occupied_closure.py
```

Ten checks passed, including minimal generation, all pulse/rotation intertwiners, the real canonical chart and exact recovery of a six-occurrence mixed pulse/rotation history.

Full basis, metric, left inverse, all compressed generators, history states and provenance:

`research/strominger/results/neutron-canonical-occupied-closure.json`.

## What is and is not completed

The requested operation binding is now executable with actual native coefficients, retained dynamical records, actual rotation and a lossless occupied-state closure. It is a conditional interaction construction, not an identification of the pulses with the old L/G projection stages or with free C3 evolution.

A neutron rest-energy calculation would additionally need a sourced occupied-sector evolution/charging law and its normalization. No such law was inserted to turn these pulse values into a mass.
