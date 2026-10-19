# Neutron canonical pulses: an exact retained-record binding

## Result of this iteration

An explicit isometric binding now exists between the full original source pulse space and the neutron's actual rim modes **with the original source carrier retained as a dynamical record bank**. All six operations, their continuous projectors, energies and occurrence histories are preserved. The neutron is not reduced to its rim modes: its other 30 complex directions remain present and unchanged under these pulses.

This is a conditional interaction adapter. It is not yet a source-selected address assignment or a binding of the neutron's free rotation to those pulses. That distinction is visible in the construction rather than hidden in an energy parameter.

## Actual native inputs and address policy

The fresh source is `research/strominger/results/neutron-arrow-native-bridge.json`, together with its bound native stores. The 36 intrinsic coordinates and their denominator metric are unchanged. The actual six rim triangles are selected by their lower/lower or upper/upper edge labels, in the already retained `triangle_order`.

The declared address policy pairs that sequence with the live source registry:

| Source label | Native triangle | Stored triangle index |
|---|---|---:|
| AB | (F_L1_L2_U0, L1, L2) | 1 |
| BC | (F_L1_U0_U1, U0, U1) | 13 |
| CA | (F_L0_L1_U1, L0, L1) | 4 |
| BA | (F_L0_U1_U2, U1, U2) | 10 |
| AD | (F_L0_L2_U2, L2, L0) | 7 |
| DB | (F_L2_U0_U2, U2, U0) | 16 |

These are port addresses, not an asserted vertex map from ABCD to the six rim vertices. Typed source endpoints and ordered occurrences remain separate retained fields. The assignment is reproducible but not selected by a physical symmetry argument.

Let w_i be the native selected mode supported on the two intrinsic coordinates of rim triangle i. Exact inherited norms give

    <w_i,w_j>_neutron = nu delta_ij,
    nu=4198/675.

Set v_i=w_i/sqrt(nu). No neutron metric is changed by this normalization.

## Binding with no discarded source coordinates

The original source space consists of carrier y in C^16, metric H=(10I+ones) tensor (10I+ones), and six independent records r_i. Its feature vectors are f_ab=e_(a,b)/11.

Bind it into neutron-plus-bank by

    J(y,r)=(n=sum_i v_i r_i, y).

Thus the independent source record amplitudes occupy actual neutron modes. The original source carrier is kept as a 16-dimensional dynamical record bank; it is not replaced by a passive occurrence log.

The source has 22 complex coordinates. The target has all 36 neutron coordinates plus the 16 bank coordinates. The 30-dimensional neutron complement is retained, so any target state can be decomposed and recovered exactly. On the source image,

    <J(y,r),J(y',r')> = y* H y' + r* r'.

## Actual bound pulse and energy

For addressed port i define

    delta_i=<v_i,n>_neutron - <f_i,y>_source.

The pi pulse is

    n' = n-v_i delta_i,
    y' = y+f_i delta_i.

This is exactly the existing source exchange under J. Put d_i=(v_i,-f_i), with total metric M=metric_neutron direct-sum H. Then

    P_i=d_i d_i* M/2,
    U_i(theta)=I+(exp(-i theta)-1)P_i,
    h_i(n,y)=<state,P_i state> = |delta_i|²/2.

The full direction Gram is

    <d_i,d_j> = delta_ij+f_i* H f_j = K_ij.

Consequently all the source's noncommuting cross-port response is retained. This is not an attempt to fit its infinite-order loop into the neutron's finite geometric action. The missing dynamics lives in the explicit bank.

Metric and complex-linear intertwining preserve the inherited symplectic form and action primitive on the source image. Hence the previously derived canonical h_i=(Kq)_i²/2+p_i²/8 is transported, not replaced with another Hamiltonian.

## Energy for an actual neutron preparation

Take the stored coherent neutron mode u, normalized to unit native norm, and the explicit empty-bank preparation y=0. Its unnormalized squared norm is

    S=1196/15.

Each rim projection has amplitude sqrt(nu/S). Therefore **each addressed pulse** has energy

    h_i = nu/(2S) = 2099/53820.

The total quadratic budget is one. The addressed neutron weight is 2099/4485; the retained spectator weight is 2386/4485. These spectators are not silently discarded to inflate the pulse energy.

This number is a pulse-Hamiltonian value at a specified neutron-plus-record preparation, in the existing pulse-angle normalization. It is not a neutron rest energy, nor an autonomous sum of the six pulse energies.

As a separate regression, a unit AB rim excitation with empty bank reproduces all four source pulse energies for AB,BA,AB,BA from `canonical-source-energy.json` exactly.

## Why the record bank is essential

A full AB pulse moves a unit AB rim excitation entirely into the retained source bank. The full norm stays one. Deleting the bank at this point loses the entire excitation. Thus this adapter must not be advertised as closed dynamics of the 36-coordinate neutron alone.

## Fresh verification

```sh
python research/strominger/checkers/check_neutron_canonical_record_binding.py
```

Eleven checks passed. They include:

- native/source hash and content-root validation;
- actual rim norms and orthogonality;
- all six source intertwiners on all 22 complex source basis vectors;
- all source metric pairings;
- recovery and pulse tests on all 52 ambient target basis vectors;
- exact non-endpoint phase exp(-2pi i/3) and inverse tests;
- source projector energies and full cross-port Gram;
- retained occurrence states and reverse recovery;
- a record-deletion negative control;
- the unit coherent neutron energy evaluation.

Port coefficient numerators, denominators, full occurrence states and provenance:

`research/strominger/results/neutron-canonical-record-binding.json`.

No shared source or neutron backend was modified.

## Nonredundant continuation

Audit how the native C3 rotation permutes these six rim addresses and whether the inherited source feature Gram admits the same port permutation. If not, decide explicitly between a rotating addressed interaction frame, a larger source-port family, or a different source-selected assignment. This iteration makes no free-rotation/port covariance claim.
