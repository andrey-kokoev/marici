# Vacuum-tail aggregation fails the endpoint test for source-module restriction

## Result

The actual scalar restriction square in Nima's vacuum-tail certificate does NOT lift, with its displayed aggregate coordinates and the fixed labelled source evaluation, to a square of source-bimodule quotients.

The obstruction occurs already for vertex idempotents. It therefore precedes any question about ideal-depth filtrations or derived attachment classes. No choice of action on the displayed scalar targets can repair it while retaining the stated evaluation maps.

This does not invalidate the numerical task, budget transport, source realizability, or order-independent scalar restriction certificates. It establishes that these coarse scalar models are not themselves the saturated source observers of the structural lane.

## 1. Use actual labelled sources

For each background A, let k_A be the product of the forgotten diamonds on the successive pairs (2,3), (5,7), (11,13). It is an eight-term source in I^3 with actual outer vertices

    (A,30030 A).

Its selected unit-vacuum row chi_A has seams

    A->2A, 6A->30A, 210A->2310A,

and chi_A(k_B)=1 if A=B and zero otherwise. This identity is checked directly from the actual eight paths and ordered cut positions, including their outer labels.

Let e_A be the vertex idempotent acting on the initial source endpoint. On these sources,

    e_A k_B = delta_(A,B) k_B.

The finite span of any collection of k_A is stable under these endpoint projections. It need not be stable under every positive-length action; this is irrelevant because failure for one admitted idempotent already rules out full source equivariance.

## 2. A two-source obstruction

On the span of k_3 and k_4, the proposed aggregate is

    T_3(b_3 k_3+b_4 k_4)=b_3+b_4.

Set h=k_3-k_4. Then

    T_3(h)=0,
    T_3(e_3 h)=T_3(k_3)=1.

Thus ker T_3 is not stable under the source action. The kernel of any equivariant linear map MUST be stable. Hence T_3 cannot be a source-equivariant quotient map under ANY proposed action on its scalar target.

Equivalently, k_3 and k_4 have the same proposed image. Acting by e_3 would require that image to map both to itself and to zero.

This argument concerns actual source evaluation. Assigning arbitrary common trivial actions to the numerical coordinates might make their scalar matrices intertwine, but would destroy compatibility with the labelled source. It would not solve the lifting problem.

## 3. The entire saved square fails the same test

Restrict the actual source to the four backgrounds 3,4,5,6. The node evaluations are

    00: (b_3+b_4+b_5+b_6),
    10: (b_3,b_4+b_5+b_6),
    01: (b_3+b_4,b_5+b_6),
    11: (b_3,b_4,b_5+b_6).

The checker reads the partition edges from the saved numerical square and verifies their exact compositions on these source coordinates. Both scalar routes agree, as claimed by the owning certificate.

Nevertheless each node has a nonstable kernel:

| Node | Source in evaluation kernel | Endpoint projection making it visible |
|---|---|---|
| 00 | k_3-k_4 | e_3 |
| 10 | k_4-k_5 | e_4 |
| 01 | k_3-k_4 | e_3 |
| 11 | k_5-k_6 | e_5 |

In particular, exposing b_3 and b_4 does not turn the remaining scalar T_5 into a source-module coordinate. The obstruction is not confined to the first coarse node.

All witnesses have finite support. No infinite-tail topology, limiting operation, or source completion can remove these finite endpoint identities.

## 4. The distinction persists inside the actual worked constraints

The obstruction is linear-algebraic, so it does not require feasible witnesses. Nevertheless it also occurs among actual sources satisfying the same final intervals and the true moment prior.

Consider

    x=(3/2000) k_3+(1/20000) k_4,
    y=(77/50000) k_3+(1/100000) k_4.

Both satisfy the final b_3 and b_4 intervals, have zero remaining tail, and have true cost

    sum_A 8(A/2)^12 |b_A| <40.

They have the same coarse aggregate 31/20000, but different endpoint-projected readings.

Also put

    z=x+10^(-9)(k_5-k_6).

The sources x and z have exactly the same final three numerical coordinates, including T_5=0, but their e_5-projected tail readings differ. Both still satisfy the true finite-source budget and the final positive task. The checker verifies these statements with exact rationals against the saved final problem, not a substituted example interval.

Feasibility regions are not modules, and no closure of those regions under idempotents is assumed. The pairs illustrate the lost source information; the nonstable-kernel argument is the structural proof.

## 5. What structural repair would require

### Retain endpoint information

A genuine source-stable observer containing an aggregate functional must also contain its source translates. On a finite background set, translating the sum by e_A extracts each individual coordinate:

    (T_r composed with e_A)(x)=chi_A(x), A>=r.

Consequently endpoint saturation of the aggregate on backgrounds 3,4,5,6 already has dimension four, not one. The checker verifies this lower bound for every displayed partition node. Full source-action saturation may require still more coordinates.

For the unrestricted tail, the same argument on arbitrarily large finite subsets forces infinitely many independent endpoint coordinates. This is a dimension obstruction, not a construction of a completed infinite observer.

Retaining those labelled coordinates formally does not mean they have been acquired. It enlarges the structural state space; a measured or prior-bounded aggregate still supplies only a constraint on that space.

### Keep aggregation at the scalar-constraint layer

A compatible architecture can retain the endpoint-resolved source or saturated observer as the structural object and place the numerical aggregate bounds on its feasible states. Tail splitting then refines constraints and exposes coordinates without claiming that summation is a module quotient.

Alternatively one could explicitly forget the endpoint algebra and work only with vector spaces or the scalar subalgebra. Summation is then legitimate, but that is a change of category and does not transport the original source-bimodule filtered attachment automatically.

No choice of basis or whole-row gain repairs the present failure while preserving the fixed source evaluation and all endpoint actions.

## 6. Consequence for the mixed-history certificate

`../nima/mixed-refinement-histories-have-an-independent-finite-route-verifier.md` explicitly declares `structural_transport: not-certified`. The present audit explains why that boundary is substantive, not merely an omitted test: histories containing these aggregates cannot use their numerical node spaces as source-module quotients of the original labelled source.

Their all-route scalar coherence remains valid. A structural enhancement would need endpoint-resolved ambient states and explicit maps, with the aggregate task/data functionals separately recorded. The existing invertible structural gain fixture cannot simply be attached to these aggregation edges.

This result does not say that a filtered class vanishes under tail refinement. Rather, the displayed scalar maps do not yet define the source-module comparison along which such a transport question could be asked.

## Verification

    python research/voevodsky/checkers/check_vacuum_tail_endpoint_obstruction.py

The checker uses only the standard library. It hashes and reads the actual saved tail square, reconstructs the forgotten sources at four actual endpoint pairs, checks their vacuum readings and scalar routes, exhibits a kernel-instability witness at every node, and checks finite feasible sources under the saved final intervals and true moment costs.

Artifact: `results/vacuum-tail-endpoint-obstruction.json`.

It does not rerun the numerical square's independent task verifier or construct a completed source observer. Those responsibilities remain separate.
