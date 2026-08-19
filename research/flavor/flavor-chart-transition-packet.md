# Sparse-chart transition packet (WP3)

Agent: `marici.Figueiredo`. Date: 2026-08-19.
Source: arXiv:2607.27315v1 (Arkani-Hamed, Figueiredo, Hall, Manzari).
Conventions: `research/flavor/flavor-nine-link-conventions.md`.
Evidence: `research/flavor/checkers/nine_link_exact_checks.py`,
results in `research/flavor/results/nine_link_exact_checks.json`
(all arithmetic exact; no floating point).

## Question under test

Does the data of a nine-link texture — the unique cycle, its \(U(1)\)
holonomy \(\phi\), the perfect-matching determinant data, and the Yukawa
triangle — transport canonically between presentations of the same physical
flavor point?

## The two transitions tested

### T1 (positive direction): inside the sparse groupoid

Example I (Eq. S38) was mapped by a non-trivial element of the declared
sparse groupoid \(S_3^3\): left-handed rows cycled \(1\to2\to3\to1\),
up-type columns swapped \(1\leftrightarrow3\), down-type columns swapped
\(2\leftrightarrow3\). Exact results (`s3_cubed_permutation_transport`):

- the image is again a connected nine-node/nine-edge texture with
  \(b_1 = 1\) and a unique 4-cycle;
- the transported loop monomial is exactly
  \(i\,d_{12}d_{22}u_{12}u_{22}\,\epsilon^{16}\): the holonomy is preserved
  exactly (`holonomy_ratio_new_over_old = 1`, and it matches the placed
  phase \(\pi/2\) up to the orientation-conjugation ambiguity);
- the perfect-matching counts are preserved (one matching per sector);
- determinants change only by real signs
  (\(\det Y_u'/\det Y_u = -1\), \(\det Y_d'/\det Y_d = -1\)), so
  \(\arg\det(Y_uY_d)\) is preserved exactly.

Combined with the rephasing-torus audit (`rephasing_torus`: the loop
monomial's rephasing factor has identically vanishing Laurent exponent
vectors for all four source textures), transport under the full declared
groupoid — node rephasings plus row/column permutations — is canonical.

### T2 (negative direction): a general physical basis change

Example I was mapped by the exact rational \(U(3)_Q\) rotation with
\(\cos\theta = 3/5\), \(\sin\theta = 4/5\) in the \(q_1\)-\(q_2\) plane
(`u3q_rotation`):

- every weak-basis invariant checked is exactly unchanged:
  \(\mathrm{tr}\,H_u\), \(\mathrm{tr}\,H_u^2\), \(\det H_u\) (and down-type
  analogues) symbolically; \(\mathrm{tr}(H_uH_d)\),
  \(\mathrm{tr}(H_u^2H_d)\), \(\mathrm{tr}(H_uH_d^2)\),
  \(\mathrm{tr}(H_u^2H_d^2)\) and the commutator determinant at a concrete
  exact-rational point;
- the zero pattern is destroyed (up-sector nonzeros \(4\to5\), down-sector
  \(5\to7\)): the image lies outside the nine-link atlas;
- the chart's loop monomial, evaluated on the same edge set after rotation,
  acquires a nonvanishing real part: its argument is no longer \(\pi/2\).
  The loop phase is exactly what the rotation fails to preserve.

## The decisive source fact

The paper itself states the chart-level status of \(\phi\). With \(\phi\)
free, its textures are by design all equivalent under \(U(3)^3\) rotations;
but once \(\phi\) is fixed, "it is no longer guaranteed we can map any
textures into each other using \(U(3)^3\) rotations — since these might not
preserve \(\phi\)" (App. V, fixed-phase scan methodology). Corollary within
the source's own results: the free scan fits the same ten observables with
156 texture classes whose fitted phases cluster at distinct values
(\(\pi/2\), \(\pi/8\), \(3\pi/8\), \(\pi/4\)). Identical physical readout,
distinct \(\phi\). Therefore \(\phi\) cannot be a function of the physical
flavor point.

## Outcome per the brief's trichotomy

| Transport demand | Result |
|---|---|
| unique cycle in graph homology | canonical under the groupoid (T1); chart destroyed under general \(U(3)^3\) (T2) |
| \(U(1)\) holonomy \(\phi\) | canonical under the groupoid; not preserved by general basis change; not a function of the physical point |
| perfect-matching determinant data | canonical under the groupoid (real signs only); matching structure is a chart property |
| Yukawa triangle | chart data; only its CKM image at leading order is physical, with calculable NLO separation |
| leading CKM angle identification | invariant — it is a statement about weak-basis observables |

The verdict sits between the brief's second and third outcomes, and closer
to the third: transport works only inside the declared sparse groupoid —
i.e. only after the gauge choice that defines the chart. Between charts of
different classes representing the same physical point there is no
canonical sparse transition at all. Hence:

- Candidate A, \(\mathfrak F_9^{\mathrm{sparse}}\), is **not** an atlas
  with canonical transition functions for the physical quotient. It is a
  collection of useful parameterizations — charts with a well-defined
  intrinsic calculus.
- Candidate B,
  \(\mathfrak F_{\mathrm{phys}} = \{(Y_u,Y_d)\}/U(3)^3\),
  remains the only candidate physical carrier.
- The Yukawa triangle is recorded as an internal lens coordinate of the
  chart, not as the physical readout.

## Exceptional and boundary cases audited

- Disconnected synthetic graph with \(V=9\), \(E=9\): two components,
  \(b_1 = E - V + c = 2\). The slogan \(b_1 = E - V + 1 = 1\) presupposes
  connectedness; \(V\) and \(E\) alone never certify a single loop
  (`exceptional_diag_plus_extra`).
- Adding a tenth edge to a connected nine-node graph gives \(b_1 = 2\):
  the single-holonomy description breaks structurally, functorially in the
  rank count — independent of any fit. This is the graph-level content of
  the paper's observed sensitivity to switching on texture zeros.

## What this packet does not claim

- It does not claim the nine-link graph is fundamental (sparsity is a
  choice of presentation).
- It does not claim \(\phi\) is meaningless: it is a well-defined,
  groupoid-invariant chart coordinate, and its empirical clustering is
  evidence about viable textures as presented — not yet about a UV law.
- It does not decide H2S/H2LR. The chart-level verdict above is the input
  those hypotheses must accommodate.
