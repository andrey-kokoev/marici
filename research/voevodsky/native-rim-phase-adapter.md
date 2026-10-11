# Interaction continuation — iteration 2: native rim adapter and moving port

## System-level follow-up

Iteration 3, `native-adapter-collective-closure.md`, embeds this operation with
all intrinsic belt coordinates. The three proposed collective inputs require
an exact nine-dimensional invariant space; arbitrary local inputs require 27.
No scalar-intermediate approximation is silently substituted for those closures.

## Result and scope

A constructive local successor to the rim-port obstruction now passes **24 exact
checks**. It provides:

- a metric-unitary, reversible adapter on both independent local port inputs;
- exact transfer of the selected carrier triangle character to the stored native
  belt mode, with the norm difference retained on the carrier side;
- an explicit moving electron face/cell policy using its actual supplied
  five-cycle;
- frame covariance and reversible identification over a 15-step joint labelled
  schedule.

The adapter is a declared local operation, not a uniquely forced interaction.
The electron side transports the **geometric triangle character within its moving
attachment cell**, not its full spinor operator. Full native L/G/N coupling,
collective closure, dynamics and asymptotic scattering remain to be checked.

Fresh starting sources: `neutron-rim-port-transport.md`, its checker, and the native
belt mode constructor. The stored belt coefficient packet is verified against
its content root and geometry hash before comparison.

## 1. Derive the local metric from the actual geometry

For an ordered local triangle (F,a,b), define

    e = (a-b)/2,
    r = F-(a+b)/2,
    u = r + i sqrt(3) e.

At each of the six neutron rim occurrences, e and r are orthogonal. Keep the
previously declared neutron metric scale 8/3. The carrier ABC triangle and belt
panel then have

    <e,e> = 2 on both sides,
    alpha = <r_carrier,r_carrier> = 2/3,
    beta  = <r_belt,r_belt> = 148/675.

Consequently,

    ||u_carrier||^2 = 6+alpha = 20/3,
    ||u_belt||^2    = 6+beta  = 4198/675,
    alpha-beta = 302/675.

These are reconstructed from source coordinates. Every transported belt mode
is also checked against the actual stored collective coefficient vector, using
the existing native coefficient frame rather than a fitted replacement.

## 2. The declared contraction and its retained completion

Choose the local transfer contract:

> Preserve the ordered edge coefficient and send the carrier transverse
> coefficient to the belt transverse coefficient in their respective geometric
> bases.

In unnormalized coordinates this transfer is the identity matrix between
*different* metric spaces, diag(2,alpha) and diag(2,beta). It is a contraction,
not an isometry. Its metric defect is diag(0,alpha-beta), of rank one.

In orthonormal coordinates its transverse transmission amplitude is

    kappa = sqrt(beta/alpha) = sqrt(74)/15.

Choose the positive retained amplitude

    delta = sqrt(1-beta/alpha) = sqrt(151)/15.

Other phase conventions or adapter contracts are possible. Geometry determines
these magnitudes only after the above transfer contract is selected; it does
not derive a scattering coupling a, b or c.

Retain both independent inputs. In the ordered coordinates

    (carrier edge, carrier transverse, belt edge, belt transverse)

use the physical Gram metric

    G = diag(2, alpha, 2, beta)

and the exact operation

    U = [[0, 0,     1, 0],
         [0, delta, 0, beta/alpha],
         [1, 0,     0, 0],
         [0, 1,     0, -delta]].

The checker proves

    U* G U = G,
    U^2 = I.

U is not Euclidean-unitary in these unnormalized coordinates; assuming that
would be an error. In orthonormal coordinates its edge block is a swap and its
transverse block is [[delta,kappa],[kappa,-delta]].

## 3. Exact native-mode transfer without losing the residual

For a carrier native mode and initially empty belt port,

    (i sqrt(3), 1, 0, 0)
      -> (0, delta, i sqrt(3), 1).

The last two coordinates reconstruct precisely the native belt mode. The first
two retain the missing transverse information. The norm budget is

    20/3 = 4198/675 + 302/675.

Applying U again with the retained output restores the entire input. Clearing
the carrier residual first fails the inverse test. In particular, a belt mode
plus vacuum cannot be silently converted into the larger-norm carrier mode.

The operation preserves arbitrary complex inputs on both ports, not just this
one-sided native vector: the full matrix identity establishes that result, and
basis/complex-probe controls also pass. The selected one-sided transmission has
rank-one defect; general two-port inputs still occupy four complex coordinates.

For six independent rim occurrences, this local direct sum has 24 complex
coordinates. It is not permission to discard the remaining belt triangles,
carrier modes, incident-cell marks or spinor records. Embedding it in the full
native operator system is the next obligation.

The pure-transverse probability weights are 74/225 and 151/225. For the specified
whole native input the retained norm fraction is only 151/2250, since its edge
part transfers completely. None of these is a photon branching probability or
a fit to 372.

## 4. Explicit electron moving-port policy

Use the supplied electron action

    E -> A -> B -> C -> D -> E.

Transport both the ordered ABC face and the ordered ABCD attachment cell. The
face visits

    ABC -> BCD -> CDE -> DEA -> EAB -> ABC.

Do not sort away the inherited corner order. The incident tetrahedral cell is
retained separately; the full electron has not been replaced by this triangle.

Let R_N be the supplied neutron rotation and R_E the supplied electron action.
From the initial identification f_0(U_i)=ABC_i, declare at macrostep n

    f_n(R_N^n U_i) = R_E^n ABC_i,
    equivalently f_n = R_E^n f_0 R_N^(-n).

Thus the receiver face moves and its relative registration is recorded. This is
not a fixed-port intertwiner, and does not overturn the earlier obstruction.
It is an explicit change of interface policy.

For the lower rim, use the previously found face-preserving proton action,
chronological generator word [0,0,1,0], once per macrostep. It intertwines the
lower rim rotation, so the lower vertex map remains constant.

The timing policy is supplied. A macrostep contains one neutron rotation, one
electron action and the selected proton word; it is not derived physical time.
No global non-overlap, force law, energetic accessibility or continuously
maintained spatial attachment is inferred from this labelled transport.

## 5. What returns after five versus fifteen steps

After five macrosteps the electron's face and cell return, but the neutron has
advanced by two rotations modulo three. The relative vertex identification has
not returned. The first return of the entire upper labelled registration is
**15 macrosteps**.

This is a label/schedule period, not a particle period or a claim that applying
the adapter at every step has period 15. The adapter is an involution; the
schedule specifies transport of the interface, not an implicit repeated pulse.

Every one of the fifteen inverse identification steps is checked. Recording
only the electron face/cell would confuse steps zero and five; the neutron
registration is necessary to distinguish them.

## 6. Covariance and replay checks

At 16 snapshots including both endpoints:

- all six local chart Gram matrices have the same derived values;
- all 96 belt character comparisons agree with stored native coefficients;
- all 90 consecutive local-frame transitions agree with the source isometries;
- the adapter matrix is unchanged in these transported charts;
- inverse label transport restores every prior interface identification;
- JSON replay of the full output followed by U restores the input.

These checks establish a local covariant adapter and a reversible moving-port
record. They do not establish covariance of every native L/G/N or electron
spinor operator under this new interaction.

## 7. Updated five-step frontier and next executable work

1. Finite-operator audit: completed for the specified finite models in iteration 1.
2. Native rim adapter/moving port: a local constructive witness now exists at the
   geometric triangle-character level; full electron spinor integration is open.
3. Retention: both local input spaces and the residual are explicit. They must
   now be embedded together with all untouched native modes, not compressed to
   a scalar C merely by naming them an intermediate.
4. Collective closure: test actual native operators and the embedded adapter on
   the proposed visible/hidden subspaces. A local gate alone is insufficient.
5. Asymptotic channels/scattering: still pending this system-level construction.

Next read the intrinsic belt store and L/G/N constructor. Embed the six local
adapters with identity on all untouched belt coordinates, retaining carrier and
registration records. Test leakage from candidate collective subspaces under
both the adapter and native operators; retain any generated complement. An
obstruction or a larger required space is a substantive result, not a reason
to silently drop modes.

## Reproduction

```sh
python research/voevodsky/checkers/check_neutron_rim_port_transport.py
python research/voevodsky/checkers/check_native_rim_phase_adapter.py
```

Receipt: `results/native_rim_phase_adapter.json`, with the full metric/matrix,
source hashes, stored-packet root, norm budget and all 16 labelled snapshots.
