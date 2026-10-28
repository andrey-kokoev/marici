# A reversible path source with two local causal readouts

## Frozen candidate and scope

Active SCC obligation: forward realization of a declared reversible source and two typed local causal readouts. The earlier `dual-causal-realization` card had no candidate maps and is not an executable physical test. This note freezes a bounded mathematical replacement. It does not resolve the physical WG-I3 conjecture.

Source objects are WG-I5 nonempty consecutive paths p_ij on a supplied line, 1<=i<=j<=m, retaining their complete NNMHV decoder h_n(j+4,i+4), n=m+5. Morphisms are retained executions, not endpoint-equivalence classes.

Use the already constructed L=pending preceding edge (i,j)->(i-1,j) and R=append succeeding edge (i,j)->(i,j+1). Add their canonical partial inverse actions l=(i,j)->(i+1,j) and r=(i,j)->(i,j-1), defined only for i<j. They remove the unique initial or final edge; their inverses reconstruct the edge from the remaining endpoint. Retain original state, action and output in the execution witness. This is an explicitly declared reversible envelope of WG-I5, not evidence that the original forward-only source already included every inverse operation.

Candidate question: does this one reversible source support the two stated causal readouts, preserve full records under its operations, and retain a nonempty shared future-operation sector? Reject the candidate if an admitted future edge or two-edge interior violates its assigned cone, inverse/payload recovery fails, or shared operations require incompatible source actions.

## Explicit maps and observation domains

Both readouts send p_ij to the ordered real endpoint point (u,v)=(i,j) in U={u<v}. The object maps are literally the same on this subset, but target metrics and future cones differ:

    R_plus(p_ij)=(i,j) in (U, g_plus),  g_plus=4 du dv/(v-u)^2;
    R_minus(p_ij)=(i,j) in (U, g_minus), g_minus=-4 du dv/(v-u)^2.

The scalar curvature convention is the one already audited: +2 and -2. These are supplied local dS2/AdS2 metrics, not derived metrics. The source lattice is a subset of their charts, not a continuum limit. Metric scale 4 is fixed for the experiment and not selected by the source.

Diagonal source objects i=j remain admitted algebraic records with upper boundary replacements, but neither metric readout is defined on them. A metric-visible execution must have ALL intermediate states in U. This explicitly prevents a source step through a singular point from masquerading as a spacetime trajectory.

Define time coordinates solely for the candidate charts:

    t_plus=v-u,       t_minus=u+v.

For negative-norm timelike convention the future cones are

    plus: du<=0, dv>=0;
    minus: du>=0, dv>=0,

with at least one nonzero component. Their interiors are timelike; their edge rays are null. These are distinct causal structures, not a direct isometry between the metrics.

The plus future source actions are {L,R}. The minus future actions are {l,R}, restricted to visible states and edges. Thus R is a shared future null operation with the exact same source record transition and label. L is a plus-future edge but a minus-past edge; l has the opposite status. No requirement identifies these incompatible future roles.

## Proof on every finite source

The path operation bounds give inverse pairs lL=id and Ll=id on their respective domains, and likewise rR=id and Rr=id. These equations concern path objects and decoded full records. Two-step executions retain both edges and are not erased as empty histories.

For plus future words every prefix has nonincreasing u and nondecreasing v; for minus future words both endpoints are nondecreasing. The declared time coordinate increases by exactly one at each single-edge step. Consequently every visible future execution is an order-preserving chain in its respective cone. There is no claim that every order-related pair in a continuous chart is reachable in the finite source.

For a tangent displacement (a,b), g_plus(V,V)=4ab/(v-u)^2 and g_minus(V,V)=-4ab/(v-u)^2. Hence mixed plus-future motion (-a,b), a,b>0, is timelike only for g_plus; mixed minus-future motion (a,b) is timelike only for g_minus. Single endpoint moves are null. Interpolating each admitted edge linearly stays in U because its endpoint gaps are positive. A two-coordinate straight displacement between ordered points remains in U for the same convexity reason. This supplies a local piecewise-null or timelike interpretation, not Einstein dynamics.

When both orders are visible, LR and RL have the same complete endpoint; so do lR and Rl. The intermediate objects and execution words remain distinct. The shared R-only subcategory is mapped identically by both realizations. Record observers recover the same complete NNMHV state along this shared subcategory; causal labels and metric values are target-specific.

## Why this does not solve the physical conjecture

The forward-only graph cannot realize the minus future-left ray l without reversal/enlargement. The reversible envelope makes that extra assumption visible. No experiment or source principle selects either future subcategory, the continuous chart or normalization. All arrows of the common envelope cannot be future-directed for either observer because it includes inverse pairs. An autonomous clock and physical observer algebra are not supplied.

Thus this completes only a candidate construction: a common reversible source with two conditional local geometric/causal interpretations, a shared nontrivial operation sector and explicit incompatibility outside that sector. WG-I3 remains open at its physical realization scope; WG-I2 scale selection is unchanged. The next physical bridge must explain admissibility of the inverse envelope and selection of the two observer/future structures from source data, rather than count this supplied choice as a derivation.

## Verification

`checkers/check_dual_causal_path_candidate.py` uses the original compose implementation for extensions, unique path trims for inverses, and the actual history compiler for full-record decoding. Exact rational tests cover fixed finite cutoffs, inverse recovery, both cone signs, shared operations, visible squares and the diagonal/past-operation hostiles. The all-cutoff proof is above; no continuum or physical inference is drawn from finite tests.
