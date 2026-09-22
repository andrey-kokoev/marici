# Frame discrepancy observers form a compatible consistency tower

## Result

For a declared finite family of CORRECTED observer frames, their discrepancies form a second compatible tower over the source-observer tower. At each depth its kernel is precisely the synchronized frame states. It is a source-bimodule construction, not merely comparison of scalar witness values.

With F frames, F-1 comparisons along a spanning tree suffice WHEN the frame transitions have already been proved coherent. Frame count does not determine filtration depth. For F=100 this means 99 independent frame comparisons at every chosen rung, not 50 rungs.

This construction certifies consistency relative to the supplied transitions. It cannot distinguish a correct common observation from a shared erroneous one, cannot certify an unweighted infinite-depth source realization, and cannot turn arbitrary noisy records into source chains.

Input: `lower-filtration-corrections-make-saturated-observer-frames-coherent.md`. The construction applies only after the required lower-filtration corrections have been retained. It does not identify the uncorrected original and private cubic towers.

## 1. Frame data at each rung

Let m>=1 be source-filtration depth. For frames f=0,...,F-1 let O_m^f be copies/presentations of the corrected finite observer module. Let

`p_m^f:O_(m+1)^f -> O_m^f`

be their tower restrictions. The established frame changes are source-bimodule isomorphisms

`T_m^(g<-f):O_m^f -> O_m^g`

satisfying identity, composition and compatibility with restriction:

`T_m^(h<-g) T_m^(g<-f)=T_m^(h<-f)`,

`p_m^g T_(m+1)^(g<-f)=T_m^(g<-f) p_m^f`.

Their corrected source evaluations satisfy T_m^(g<-f) Obs_m^f=Obs_m^g. At a fixed finite stage these maps are bounded. No depth-uniform bound on their norms is assumed.

The construction does not assert that 100 concrete physical protocols have already been admitted. F may be any finite number of specified frames meeting these hypotheses; arbitrary new measurement protocols still require their own transition proof.

## 2. The reference-frame discrepancy observer

Define

`C_m^0=direct_sum_(f=0)^(F-1) O_m^f`,

`C_m^1=(O_m^0)^(F-1)`.

The consistency observer is the linear map

`Delta_m((y_f)_f)
  =(T_m^(0<-f)y_f-y_0)_(f=1,...,F-1)`.

Its values are vector discrepancies in the corrected observer modules. A scalar functional can subsequently test a discrepancy, but scalar agreement alone need not imply vector agreement.

Its kernel is exactly

`{(T_m^(f<-0)z)_f : z in O_m^0}`.

This follows directly by solving each component equation. Delta_m is onto: for prescribed discrepancies d_f, set y_0=0 and y_f=T_m^(f<-0)d_f. Thus there is a split exact sequence of source modules

`0 -> O_m^0 -> C_m^0 --Delta_m--> C_m^1 -> 0`.

The splitting chooses a reference frame; it is not an assertion that the underlying observer filtration extensions split. The two constructions have different kernels and meanings.

## 3. Discrepancies themselves form a tower

Restrict each frame state componentwise, and restrict each reference discrepancy by p_m^0. The transition identity gives

`(p_m^0)^(F-1) Delta_(m+1)
   =Delta_m (direct_sum_f p_m^f)`.

The synchronized-state inclusion and the explicit splitting also commute with these restrictions. Hence the split exact sequences assemble into a compatible consistency tower. Their inverse limits remain split exact by those explicit compatible maps; no general exactness theorem for arbitrary inverse limits is invoked.

For every genuine source x, the frame-state tuple (Obs_m^f(x))_f has zero discrepancy at every rung. Conversely, zero discrepancy identifies one state in the corrected observer tower, not necessarily a single summable source realizing all rungs. The previously proved source-budget gates remain necessary for any such realization claim.

An independently prescribed tuple at different depths must also satisfy its tower restriction equations. Zero cross-frame discrepancy at each rung does not supply depth compatibility if the input was not already a tower.

## 4. Spanning trees and transition checks are different tasks

Any spanning tree on the F frames can replace the reference star. Along an oriented edge f->g use

`d_(g,f)=y_g-T_m^(g<-f)y_f`.

Tree-edge discrepancies vanish if and only if the states synchronize, provided the transitions are already coherent. This needs F-1 edges. For nonzero errors, propagation along a tree path pays the norms of its intervening transitions; a long path is not automatically as well conditioned as a reference star.

If all pairwise state differences are desired, set z_f=T_m^(0<-f)y_f. Then reference-coordinate edge differences are z_g-z_f. Their sum around every triangle is automatically zero, and all of them are determined by the F-1 differences z_f-z_0. This is an explicit incidence/coboundary construction, not a new simplicial source or an additional source-filtration rung.

There is a separate task when the TRANSITIONS have not yet been verified. Assuming identity and inverse conventions, the fundamental-loop defects of a connected graph with E edges number E-F+1 after choosing a spanning tree. Vanishing of those operator defects makes every edge agree with the tree-induced transports and supplies path independence.

For a complete 100-frame graph there are 4950 pairwise edges. Its 99 tree edges leave 4851 fundamental loops. Once their operator consistency is established, 99 state comparisons suffice. These counts are not counts of detector depth, and a scalar loop probe does not by itself verify an operator identity.

If inverse/identity conventions have not been established, they too must be checked. If a graph is disconnected, its components can synchronize independently without establishing a common state across components.

## 5. Stagewise noise budgets

Suppose exact synchronized states are y_f^*=T_m^(f<-0)z and measured states satisfy ||y_f-y_f^*||_f<=epsilon_f. Then

`||Delta_m(y)_f||_0
 <= ||T_m^(0<-f)|| epsilon_f+epsilon_0`.

In the maximum discrepancy norm this gives

`||Delta_m(y)||_max
 <=max_(f!=0)(||T_m^(0<-f)||epsilon_f+epsilon_0)`.

For the l1 state norm, ||Delta_m|| is bounded by max(F-1,max_(f!=0)||T_m^(0<-f)||) when the discrepancy norm is also l1. For maximum norms an upper bound is 1+max_f||T_m^(0<-f)||. These are finite-stage bounds, not uniform estimates across depth or arithmetic location.

Conversely, if all reference discrepancies have norm at most eta, the tuple is within eta of a synchronized tuple in the reference-aligned maximum norm: choose z=y_0. This proves proximity to CONSISTENCY, not proximity to the unknown true state.

A shared bias z->z+b in every aligned frame has zero discrepancy. No internal frame checker can detect it without an additional reference or observation. Transition uncertainty and calibration defects must be included in the discrepancy budget rather than assumed absent. For example an approximate transition error bounded by delta_f contributes delta_f||y_f||, in addition to the frame-state errors.

The observed large cubic transition constants remain relevant. Merely changing frame cannot remove their amplification.

## 6. Typed scope

The discrepancy observer is a linear, source-equivariant map between existing corrected observer-state modules. It does not supply a new physical observer in the original scalar-test space without a separate realization map. Evaluating or reconstructing these observer states from measured response fields retains the previously declared forward/noise bounds.

Nor does adding this consistency layer automatically preserve nonzero extension classes under a pushout: the supplied split-first/nonsplit-later theorem concerns its specified source-observer tower, not this split discrepancy sequence or every corrected target.

At product-topology level the consistency tower is defined and continuous. Bounded or summable all-depth discrepancy norms require uniform control of transition constants and frame-state/error sequences, which is not inferred from the finite-stage theorem.

## Verification

`uv run python research/nima/checkers/check_frame_discrepancy_tower.py`

Exact rational fixtures check 100-frame synchronization, detectable disagreement, invisible shared bias, split surjectivity, restriction compatibility, and the separate graph counts. These fixtures verify the construction; the admission and analytical conditioning of concrete physical frames remain inputs.
