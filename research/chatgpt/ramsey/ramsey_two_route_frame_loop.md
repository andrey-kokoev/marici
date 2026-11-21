# Two genuinely different cooperative routes: intermediate change, zero return drift

ramsey_two_route_frame_loop.py constructs all ten four-edge completions from source191 that preserve its center0 and create a second Hall center. For each h in {2,3,4,5,6} there are exactly two distinct completions B_h,C_h, each with centers0,h. They have the same neighborhoods of0 and h, but their h-centered duad signatures differ at FIVE vertices. B_h and C_h differ by five removed/five added red edges.

For every one of the120 old label permutations fixing h, test the route:
G at0 -> B_h at0 -> B_h at h -> C_h at h -> C_h at0 -> G at0.
The graph changes preserve validity; when switching incidence charts, comparison actions are canonically re-lifted. The middle change B_h->C_h is NOT assumed to preserve the h-chart; it explicitly requires a new canonical lift on the same six h-label vertices.

Results for EACH of the five loops:
-120 comparisons tested;
-115 comparisons genuinely change their22-vertex realization in the middle;
-ZERO comparison permutations change after returning to the original chart.
Thus this is not just transfer followed by its literal inverse, nor are the intermediate transports all identical. Nevertheless all600 round trips are trivial.

Structural reason: the entire route stays inside the same original root0 incidence backbone. For any alternative Hall center h among its six labels, old finite label a has h-centered signature {0,vertex_of_old_duad_{h,a}}. That correspondence is determined by unchanged label-duad incidences, independently of which completion B_h or C_h is used. Re-lifting at h preserves the action on those h-label vertices and hence on the old finite-label star. Returning to0 therefore restores the original label action; its canonical extension to the fifteen duads is unique.

This proves a restriction on future searches: changing only the perfect-matching completion inside one fixed root-incidence backbone cannot generate drift by these two-center excursions, even if the intermediate chart itself changes. Nontrivial return requires a route that changes the incidence backbone itself (or a different rule that carries additional marking data). No conclusion about every conceivable multi-center loop follows.

Evidence: JSON preserves the ten completion graphs, signature-change lists, and per-loop counts. The helper's comparison permutations need not be symmetries of the graph: they are canonical six-label relabelings, so intermediate changes in their22-vertex representation are meaningful even when the endpoints are isomorphic.
