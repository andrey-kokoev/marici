# Retaining seed cycles: a reversible two-presentation trial

## Scope

Continuation of `lossless-arrow-record-pair-trial.md`. Use the actual six directed seed arrows AB, BC, CA, AD, DB, BA, with independent scalar additive values x. This retains additive cycle sums, not ordered traversal histories, permutation products or noncommutative holonomies. No particle identity is assumed.

## Lossless descent and reconstruction

Choose the spanning tree AB, BC, AD and set

    a=x_AB, b=x_BC, d=x_AD,
    c=x_AB+x_BC+x_CA,
    e=x_AD+x_DB+x_BA,
    h=x_AB+x_BA.

These three cycle records correspond to ABC, ADB and the two-cycle AB. The seed incidence matrix has rank three; its cycle space has dimension 6-4+1=3, and these cycles form a basis.

Let z=(a,b,d,c,e,h)=Dx. Reconstruction x=Rz is

    x_AB=a, x_BC=b, x_AD=d,
    x_CA=c-a-b,
    x_BA=h-a,
    x_DB=e-d-h+a.

Both DR=I and RD=I hold exactly. Every record deletion reduces rank from six to five. Any linear lossless encoding of arbitrary six-arrow values requires at least six scalar records. The three-record potential trial was lossless only because it fixed all cycle sums to zero. Nonzero fixed cycle sectors also allow three variable records, but the sector values then remain retained parameters, not free discarded information.

**Result:** retaining the independent cycles removes the apparent reduction in information dimension. It still changes the presentation into tree data plus explicit cycle data. Record dimension is not primitive arrow execution cost.

## Separate typed supports and declared reversible dynamics

Place x on six arrow ports and z on six record ports. Their agreement condition is z=Dx. These are separate typed supports, not a construction of spatially separated bodies.

Choose a trial update T that fixes (a,b,d) and cycles (c,e,h). This is an explicit extra rule, not a seed-derived symmetry: in particular it exchanges a two-cycle record with three-cycle records. It must not be presented as a derived physical law.

On arrow coordinates the corresponding update is A=RTD. Then DA=TD and A^3=I. Thus reconstruction and evolution commute, exactly.

A genuinely cross-support reversible update is

    U(x,z)=(RTz,Dx).

It satisfies U^6=I. One microstep generally takes a synchronized pair out of agreement; two steps satisfy

    U^2(Rz,z)=(RTz,Tz).

The two-support model therefore has an explicit two-step return with compatible dynamics on its synchronized sector. It does not settle: disagreement is not erased, and the dynamics is periodic.

With H=D^T D and W=diag(H,I), U^T W U=W. H is positive definite because D is invertible. Hence U is an isometry in the retained-record metric and becomes unitary after metric normalization (over complexified coordinates). A is not generally orthogonal in the ordinary arrow-coordinate Euclidean metric. This demonstrates reversibility with retained information without imposing the wrong coordinate metric.

## Pair and minimality controls

The joint agreement matrix [D,-I] has rank six and a six-dimensional kernel. Agreement supplies two representations of six variables, not a unique identity mode or two particle species. The full unconstrained joint space has twelve variables. Neither a spatial embedding, a binding interaction, nor an energy readout has been derived.

Minimality proved here concerns linear scalar records under exact arbitrary-data reconstruction. The checker does not prove pruning minimality of a primitive interaction graph. Counting nonzero entries of these chosen matrices would describe this particular implementation, not derive C(n,3).

## What this changes in the synthesis route

The lossless-cycle requirement can now be implemented explicitly. The remaining obstacle is not an inability to reverse descent: it is obtaining distinct physical realizations and their dynamics from the seed rather than assigning them. Next candidates must specify which information class the seed carries (scalar sums versus ordered transport), derive an allowed cycle update, and realize arrow and record ports on distinct supports. A proton/electron asymmetry and cost cannot be inferred just from the coordinate split.

## Verification

    python research/nima/checkers/check_seed_cycle_retained_pair.py

Standard-library exact rational checks verify incidence and cycle ranks, both inverse identities, all single-record deletions, a tree-only reconstruction counterexample, conjugate dynamics, metric conservation, and the full synchronized two-step matrix identity. All pass. During development the incidence control caught an incorrectly oriented ADB sum; the final formula uses AD+DB+BA.
