# The mixed acquisition history lives as constraints on one endpoint-resolved source

## Result

The saved seven-node mixed refinement history now has an explicit realization on ONE fixed labelled source domain. Its scalar coordinates are evaluation maps and constraints, not source-module quotients.

All eight edge diagrams commute after source evaluation. The observation diagrams commute symbolically for the same actual retained calibration E. Both routes impose the same terminal constraints. Every saved numerical witness has a finite actual-source lift, and these lifts satisfy the appropriate ancestor constraints.

This supplies the missing same-source interpretation without contradicting the endpoint obstruction to equivariant aggregation. No filtered-class transport is inferred from the scalar maps.

## 1. Fix the source, not an aggregate-module presentation

Use sources of the form

    x=a_0 v_(2,0)+sum_(A>=2) b_A k_A,
    C(x)=32|a_0|+sum_(A>=2)8(A/2)^12|b_A| <=40.

Here v_(2,0) is the actual mixed/mixed/forgotten cubic product at background 2, and k_A is the actual all-forgotten cubic product at background A. Their outer vertices remain (A,30030 A). The feature and vacuum products at A=2 are different marked sources, despite sharing those endpoints.

The retained source has 32 distinct marked path terms and each vacuum source has eight. Their supports are disjoint in the declared source coefficient norm. The displayed moment cost is the owning p-prior on this family, not an inferred response norm.

The weighted summability implies absolute summability of the vacuum coefficients. Since these paths all have length six and the vacuum letter weights are one, their sum lies in the declared common-path and actual-letter domains. Only the stated order-12 moment bound is claimed, not every higher background moment.

This selected family is not asserted to be closed under all positive-length source actions. It lives inside the fixed full labelled source domain. Endpoint actions remain available there; no endpoint is identified by a numerical aggregate.

All other source coefficients are set to zero for this realization. This realizes the declared retained-plus-vacuum task model, not an assertion that every possible source or unlisted measurement has been reconstructed.

## 2. Explicit evaluation charts for the seven nodes

Write T_r=sum_(A>=r)b_A. In canonical units the three chart types are

    C_R(x)=(a_0,b_2,T_3),
    C_A(x)=(a_0,b_2,b_3,T_4),
    C_F(x)=(a_0,b_2,b_3,b_4,T_5).

The complete saved history uses

    C_B=2 C_R, C_C=2 C_A, C_D=2 C_F, C_E=C_F.

These are bounded scalar evaluation maps. They are NOT claimed equivariant for the labelled source algebra.

The checker represents the source directions v_(2,0),k_2,k_3,k_4,k_5,k_6 separately. Every distinct A>=5 has the same evaluation column as k_5 but retains its own actual endpoint and weight. The finite column check extends to the full tail because each chart coefficient is constant on that tail and the source series converges absolutely.

For each numerical edge old->new with source restriction R_s, it verifies

    C_old(x)=R_s C_new(x)

for the SAME source x. Thus an edge is not implemented by relocating an aggregate to a different background.

## 3. Keep one actual retained calibration

Let E be the fixed positive private response of v_(2,0). Vacuum calibration is one. Before coordinate gains, the raw evaluation is

    (E a_0,b_2,T_3),

or the corresponding refined list. The gained nodes multiply the source and observation coordinates by the same factor two, so the physical E is unchanged.

Write the raw observation chart as Z_v(E)=Z_(v,0)+E Z_(v,1). The checker verifies BOTH coefficient matrices in

    Z_old(E)=R_o Z_new(E).

Hence the identity is exact for the one actual E; no numerical midpoint is substituted. Narrower calibration intervals add knowledge or model constraints about that same quantity. The formal identity for E does not assert that every interval point is a realized detector setting.

The retained response's actual theta calibration and the interpretation of acquired intervals remain external inputs from the owning physical certificate.

## 4. Source budgets and feasible-set pullback

For every node v, weighted triangle inequalities give

    sum_j w_(v,j)|C_v(x)_j| <= C(x).

For a tail beginning at r this is precisely

    8(r/2)^12 |T_r| <= sum_(A>=r)8(A/2)^12 |b_A|.

The gained-coordinate weights are divided by the same gain, so this inequality is unchanged. A prior tail interval is therefore a consequence of C(x)<=40, not an acquired reading.

Define F_v to consist of pairs (E,x) satisfying the SAME actual-source prior, the node's enclosure of E, and its raw data constraints through Z_v(E). The independently verified edge conditions and the chart identities imply

    F_new subseteq F_old.

This is identity pullback on the labelled source and fixed calibration parameter. It is not a module morphism between the aggregate-coordinate spaces. The feasible sets are constraint sets, not submodules.

The saved square/history verifies every edge's necessary numerical implication, including the rule allowing a prior-derived interval to be justified by the source budget rather than by a new measurement. The new checker invokes that independent verifier before adding the source interpretation.

## 5. Every numerical feasible vector has a finite source realization

Each chart has only one aggregate tail. Given its numerical coefficient vector, undo the coordinate gain, retain the explicit coefficients at their actual backgrounds, and place the aggregate tail coefficient at its first allowed background r.

This finite source has exactly the prescribed chart and

    C(x)=sum_j w_(v,j)|coordinate_j|.

Thus every feasible numerical vector in the declared model has a finite source lift within the same prior. The acquired data constraints are preserved because the evaluation charts commute, including the retained response E.

These finite sections are witness constructions. They are NOT a coherent relocation rule between nodes: lifting a coarse vector at its first tail background can yield a different source from lifting a finer vector. The coherence statement concerns evaluation of a fixed x, not equality of separately chosen representatives.

The checker lifts all eleven saved node witnesses and checks their own data at both calibration endpoints. It also performs 22 ancestor-feasibility checks using the destination calibration interval. It does not incorrectly demand that a destination witness fit every excluded calibration in an ancestor's larger box.

In particular a lifted terminal witness gives one actual finite source compatible with every ancestor constraint. This does not make the independently saved ancestor witnesses identical to it.

## 6. Terminal equality and reading provenance

F and E have literally identical canonical problems and charts. D is exactly the same terminal problem in doubled source/observation units. The checker verifies the intervals, calibrations, weights and target coefficients under that normalization, not merely equality of target signs.

Both routes therefore impose the same terminal subset of the common source/parameter space. Since every edge is a constraint refinement, the terminal constraints imply the intermediate constraints on either route.

The saved report separately labels every row:

- the acquired retained reading;
- each explicitly exposed acquired vacuum reading;
- the remaining PRIOR-BOUNDED, UNACQUIRED tail.

Exposing b_3 or b_4 changes this constraint inventory. It does not manufacture their values from an old aggregate or make an unknown tail into an observed channel.

## 7. What this bridge establishes

The acquisition history and the endpoint-resolved source interpretation now commute at the evaluation/constraint layer. This is stronger than agreement of scalar task values and does not require the false claim that aggregation preserves the source action.

It does NOT yet identify numerical nodes with source-bimodule observer quotients, define structural tail-restriction morphisms, or transport an adjacent filtered extension along them. Those claims remain excluded by `vacuum-tail-aggregation-fails-the-endpoint-test-for-source-module-restriction.md` unless a different structural object is supplied.

The source remains fixed, while its feasible subset becomes smaller. This is the appropriate common-source realization of the currently declared acquisition history.

## Verification

    python research/voevodsky/checkers/check_endpoint_resolved_mixed_history.py

The standard-library checker imports the independent numerical history verifier, not its solver or producer. It freshly verifies the seven nodes, eight edges and three alternative-route comparisons; reconstructs the actual 32-term and eight-term source columns; checks symbolic fixed-E diagrams, budgets, witness lifts, terminal constraints and row provenance; and detects a deliberately omitted endpoint column.

Artifact: `results/endpoint-resolved-mixed-history.json`.

Physical calibration and acquisition assumptions are not re-proved by this exact algebraic audit.
