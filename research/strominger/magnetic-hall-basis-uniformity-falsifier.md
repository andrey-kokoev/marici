# Finite Hall-basis equivalence can fail uniformly at completion

Compare two depth-semantic maximal independent presentations of the same
consecutive-depth ordinary image:

1. increasing depth with minus branch before plus branch;
2. all plus columns by depth, followed by all minus columns by depth.

At every finite cutoff the selected bases span the same image, so their change
of coordinates is algebraically invertible. Its largest absolute coefficient,
however, grows strongly with cutoff:

| \((g,q)\) | \(N=12\) | \(N=15\) | \(N=18\) |
|---|---:|---:|---:|
| \((6,3)\) | 8.25 | 35.75 | 110.5 |
| \((6,8)\) | 6 | 126 | 792 |
| \((6,13)\) | 1.1189 | 1.1189 | 21 |

Therefore finite basis independence does not imply cutoff-uniform equivalence
in the raw coefficient norm. The universal column-relation quotient exists
algebraically, while its completion can still depend on the presentation.

The second ordering reverses the preferred reflected-branch orientation. It is
a hostile presentation, not yet a second source-authorized Hall basis. Hence
the calculation does not falsify the preferred lift. It proves that one cannot
claim invariance under arbitrary maximal independent presentations and that
the authorization class of Hall charts is essential data.

The decisive next test requires two genuinely authorized bases. Their
transition must satisfy both:

\[
\sup_N\|T_N\|<\infty,
\qquad
\sup_N\|T_N^{-1}\|<\infty
\]

in the source-derived graph norms. Raw coefficient boundedness is only a
hostile preliminary norm, not the final topology.

If only one orientation-compatible Hall basis exists, uniqueness replaces the
comparison theorem. If multiple authorized charts exist, their differences
must be generated relation syzygies with cutoff-uniform comparison constants.
