# The ordered KN wall selects the Tate routing combinatorially

Date: 2026-08-23

Entry 210 orders every marked half-corridor basis as
`moving_then_persistent`. Entry 324 fixes the less intuitive axis dictionary:
the conductor-Tor axis \(\tau\) maps to the persistent corridor label, while
the two chart-normal axes map to the moving labels.

For a full-log row \((s_0,s_1,s_2;\{i,j\})\), let \(k\) be the omitted
axis. Its sign \(s_k\) selects the positive or negative half-corridor. Orient
\(\{i,j\}\) cyclically on the positive half and reverse it on the negative
half. Calling the resulting ordered axes \((m,p)\), define

\[
|H|-2=1_{s_m=-1},
\qquad
\operatorname{Tor}=1_{s_p=-1}.
\]

Exact enumeration proves that this is a bijection between the 24 maximal-cone
BC rows and the 24 literal missing-Boolean/Tor rows. Rotation acts literally.
The internally induced reflection fixes road zero, exchanges roads one and
two, reverses the half, and complements both square coordinates.

Thus the previous binary ambiguity is removed at the cyclic labelled
combinatorial KN level:

\[
\boxed{
\text{moving sign}\mapsto\Delta|H|,
\qquad
\text{persistent sign}\mapsto\Delta\operatorname{Tor}.
}
\]

It is **not** a strict \(D_3\) theorem.  Comparing with the independently
frozen literal short-facet incidence gives a mismatch: routed reflection
sends sector \(0\) to sector \(1\), whereas literal facet adjacency sends its
incident pair to sector \(4\).  Exact enumeration finds 256 rotation-only
adjacent-facet selections and zero reflection-compatible selections.

Entry 328 also explicitly leaves the algebraic
mixed-variance proper pushforward and Beck--Chevalley comparison
unconstructed. The next gate is therefore the strict reflection comparison
2-cell: it must reconcile the cyclic KN routing with literal short-facet
support. Without it, no oriented eight-cone sum is typed.

Evidence:

- `research/nima/checkers/check_tate_ordered_kn_routing.py`.
- `research/nima/checkers/check_tate_decorated_short_facet_selection.py`.
- Entries 210, 260, 262, and 328.
