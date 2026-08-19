---
author: marici.Figueiredo
---

# 1042 — The Nine-Link Loop Phase Is a Chart Invariant, Not a Physical Flavor Invariant

## Question

The flavor admission test (operator brief, this date) opens with one exact
question: is the loop phase \(\phi\) of a nine-link Yukawa texture an
invariant of a physical flavor point, or only of a selected sparse texture
chart?  The answer gates everything downstream: only if \(\phi\) descends
to the physical quotient
\(\mathfrak F_{\mathrm{phys}}=\{(Y_u,Y_d)\}/U(3)^3\)
may the almost-\(\pi/8\) clustering be read as evidence about a parent
object (H2S) rather than about a presentation.

## What the exact test establishes

All arithmetic exact (sympy symbolic / exact rationals, no floating
point); artifacts listed below.

*Chart-level invariance, positive.*  For all four worked textures of the
source (Eqs. S38, S43, S48, S53) the link graph is connected with
\(V=9\), \(E=9\), \(b_1=E-V+1=1\), and the auto-detected unique cycle's
monomial — entries conjugated when traversed toward a \(q\) node, per the
source convention — has argument equal to the placed phase up to the
orientation-conjugation ambiguity.  The loop monomial is exactly invariant
under the full diagonal rephasing torus \(U(1)^9\) (Laurent exponent
vectors of the rephasing factor vanish identically).  Under a non-trivial
\(S_3^3\) row/column permutation of Example I, the transported chart
retains \(b_1=1\), the holonomy is preserved exactly
(ratio \(=1\)), matching counts are preserved, and determinants change
only by real signs, so \(\arg\det(Y_uY_d)\) is preserved.  Inside the
declared sparse groupoid — rephasings plus permutations — transport is
canonical.

*Physical descent, negative.*  Under the exact rational \(U(3)_Q\)
rotation \(\cos\theta=3/5\), \(\sin\theta=4/5\) applied to Example I,
every weak-basis invariant checked is exactly unchanged
(\(\mathrm{tr}\,H_u\), \(\mathrm{tr}\,H_u^2\), \(\det H_u\), down-type
analogues symbolically; \(\mathrm{tr}(H_uH_d)\),
\(\mathrm{tr}(H_u^2H_d)\), \(\mathrm{tr}(H_uH_d^2)\),
\(\mathrm{tr}(H_u^2H_d^2)\), and the commutator determinant at a concrete
exact-rational point), while the zero pattern is destroyed
(\(4\to5\) up-type, \(5\to7\) down-type nonzeros) and the chart's loop
monomial acquires a nonzero real part: its argument leaves \(\pi/2\).
The physical point is unmoved; the chart and its phase are gone.

*Source-internal confirmation.*  The paper itself states that with
\(\phi\) fixed "it is no longer guaranteed we can map any textures into
each other using \(U(3)^3\) rotations — since these might not preserve
\(\phi\)" (App. V).  Its free scan fits the same ten observables with 156
texture classes whose fitted phases cluster at distinct values
(\(\pi/2,\pi/8,3\pi/8,\pi/4\)).  Identical physical readout, distinct
\(\phi\): \(\phi\) is not a function of the physical flavor point.

## Result

\[
\boxed{
\phi\ \text{is an invariant of the sparse texture chart under its declared
groupoid, and does not descend to the physical } U(3)^3 \text{ quotient.}
}
\]

Consequences for the admission test, stated no more strongly than the
evidence:

- the nine-link groupoid \(\mathfrak F_9^{\mathrm{sparse}}\) is a
  collection of charts with a well-defined intrinsic calculus, not an
  atlas with canonical transition functions over
  \(\mathfrak F_{\mathrm{phys}}\);
- the Yukawa triangle is chart data — an internal lens coordinate; only
  its leading-order CKM image (with calculable NLO separation) is
  physical;
- the almost-\(\pi/8\) clustering is, at this stage, evidence about
  viable textures as presented, not about a UV law or a parent object;
- exceptional audit: a disconnected \(V=9,E=9\) graph has
  \(b_1=E-V+c=2\); the single-holonomy slogan presupposes connectedness,
  and a tenth edge breaks it functorially (\(b_1=2\)).

This entry claims nothing about H2S/H2LR across sectors.

## Next finite test

Whether any *chart-independent* refinement of the phase data survives:
construct the smallest pair of distinct texture classes fitting the same
ten observables with different fixed \(\phi\), and test whether any
weak-basis-invariant functional (beyond the ten fitted observables)
separates them.  If none does, the \(\pi/8\) clustering is provably a
property of the presentation ensemble, and WP4's symbolic mechanism audit
(App. II) becomes the only route to a physical statement.

## Verification artifacts

- `research/flavor/checkers/nine_link_exact_checks.py`
- `research/flavor/results/nine_link_exact_checks.json`
- `research/flavor/flavor-nine-link-conventions.md`
- `research/flavor/flavor-nine-link-example.json`
- `research/flavor/flavor-chart-transition-packet.md`

Epistemic graph event: `ev-000000000662-d81a74bb-5882-4666-8a88-87d9da7ee9e4`.

## Sequence
- allocator claim: `seqclaim-c0941586e6bd846b2b44a89d`.
