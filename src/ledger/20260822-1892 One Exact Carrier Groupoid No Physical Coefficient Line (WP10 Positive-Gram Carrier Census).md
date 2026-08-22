---
author: marici.Figueiredo
---

# 1892 — One Exact Carrier Groupoid, No Physical Coefficient Line (WP10 Positive-Gram Carrier Census)

## Question

After WP6–WP9 established that the nine-link loop phase is chart data
that does not descend to the physical flavor quotient, the carrier
question itself remained: what is the exact support-level structure of
the viable sparse presentations — their feasibility boundary, their
multiplicity over one physical point, and the incidence geometry
connecting them — and does any coefficient-line object on that
geometry descend to physical flavor space?

## Method

Exact symbolic elimination and certified numerics over the full
oriented census: 36 sector-labelled \(S_3^3\) orbits (the
\(Y_u \leftrightarrow Y_d\) exchange is *not* a physical symmetry; no
orbit is exchange-fixed), 61 fitted presentations at the WP7 best-fit
physical point, 549 codimension-one face occurrences, and the
17-observable Tab.-S2 readout.  Positive-Gram realizability replaces
optimizer absence as the feasibility criterion; weak-basis equivalence
is tested by explicit \(U(3)^3\) intertwiners, never inferred from
support matching.  32 checkers under `research/flavor/checkers/wp10_*`;
consolidated packet:
`research/flavor/flavor-positive-gram-carrier-packet.md`.

## Findings

### 1. Oriented feasibility census with exact certificates

Fourteen viable and four excluded representatives per orientation
(orbits 1, 3, 8, 12 excluded in each), but the proofs are
sector-typed: the 18-orientation discriminator
\(\text{excluded} \iff \min_j \deg_{Y_d}(j) \ge 2 \ \text{or}\ z(H_d) \ge 2\)
is a summary of tested orientations, not an orientation-free law.
Swapped orbit 2, missed by the numerical pilot, is realizable by exact
Gram elimination (factor residual \(2.6\times10^{-79}\)):
positive-Gram construction is strictly stronger evidence than absence
of minima.  For the zero-diagonal support the exact interior wall is

\[
\Delta_{\rm Gram} = L^2 - 4pqr = 0,\qquad
L = ABC - Ar - Bq - Cp \ge 0,
\]

certified twice: it is the discriminant of the eliminated fiber
quadratic, and its pullback is exactly \((tyz - vwx)^2 = \det(dF)^2\).
The wall is intrinsic to the positive Gram map, not fitted from
labels.

### 2. The phase clusters live in the regular readout, not on a singular wall

All 28 viable oriented classes are certified regular near the observed
\(\pi/8, \pi/4, 3\pi/8, \pi/2\) clusters (24 by coordinate-monomial
Gram Jacobians; 4 phase-sensitive classes by exact full-rank
\(10\times10\) phase-aware Jacobians).  None of the nominal clusters
is a critical-value wall.  The phase–modulus-imbalance correlation
(\(r = 0.695\), orbit-preserving \(p < 10^{-4}\)) is regular
chart/readout coupling.  Profile-Jacobian audit: observable rank ten
everywhere; the phase column retains a median \(0.906\) information
fraction off the magnitude span, decreasing with folded phase
(\(r = -0.904\)):

\[
\boxed{\text{sparse lens + physical readout selects phase,}
\quad \text{but phase does not descend globally.}}
\]

### 3. Gribov copies: locally immersive, globally noninjective

Four same-chart doublets have observable separation
\(< 5.1\times10^{-7}\sigma\) with phase separation up to \(0.469\)
rad; both endpoints have rank-ten Jacobians whose tangent spaces agree
to \(3.0\times10^{-8}\) rad.  The induced first-order transition maps
intertwine the endpoint Jacobians to \(1.95\times10^{-9}\) and compose
to the identity to \(1.55\times10^{-14}\): genuine local differential
groupoid arrows.  The ordinary deck-cover and isolated-crossing
hypotheses are both falsified (\(N_{\rm finite\ interior\ branch} = 0\);
orbit 2's candidate branch is a collapsed *continuous* positive fiber,
not an \(A_3\) germ).  Each doublet lies on a ten-dimensional local
correspondence component of the equal-readout fiber product.  Bounded
phase scans (\(0.75\) rad both directions) keep the branches off the
diagonal; continuation to a source-defined coordinate face
compactifies the correspondence with unit normal slope.

The four limiting boundary arrows fail the complete
\(S_3^3\)-plus-rephasing candidate test (zero of four) but pass the
full \(U(3)^3\) weak-basis equivalence test (worst relative Yukawa
residual \(7.6\times10^{-12}\)).  Stabilizer audit: weak-basis orbit
dimension 25; the gauge-fixed sparse slice is transverse
(intersection dimension zero) but globally nonunique — a Gribov-copy
geometry for the sparse lens.  The four arrows lie in four distinct
double-coset transition classes (minimized chordal distances
\(3.07\)–\(3.99\), seed agreement \(5.4\times10^{-13}\)).  A
three-representative audit verifies honest weak-basis groupoid
composition modulo the common-phase stabilizer (residual
\(1.46\times10^{-15}\)).

### 4. One exact carrier groupoid

Sparse incidence under the declared groupoid (\(S_3^3\) closure plus
the four certified doublet arrows) leaves 34 connected components.
The codimension-one face atlas is abundant but nonselective (67
canonical face types; 442 eligible component pairs; connected).
Requiring normalized boundary readout and unit normal valuation
discriminates: a bounded nonlinear census reduces to \(60 + 1\), and
the apparent orbit-9 singleton is closed by an *exact* row-Gram
transition

\[
Y_s=\begin{pmatrix}a&0&0\\0&0&b\\e&c&d\end{pmatrix}
\longrightarrow
Y_t=\begin{pmatrix}ac/r&0&ae/r\\0&b&0\\0&d&r\end{pmatrix},
\qquad
Y_sY_s^\dagger = Y_tY_t^\dagger ,
\]

with exact unit boundary valuation.  Independently, an exact global
certificate needs no optimizer at all: 28 of the 67 canonical
eight-link faces are trees (connected, nine vertices, no holonomy),
and their support-permutation incidence contains a 33-edge spanning
tree connecting all 34 components:

\[
\boxed{\text{all 61 presentations lie in one codimension-one carrier
groupoid (exact).}}
\]

### 5. The coefficient line does not descend

Identity gluing of smoothing normals is exactly falsified: 28 of 391
carrier pairs pass the tree-automorphism gate, leaving 14 components
(not evidence for 14 physical sectors — a falsification of the naive
lens).  The fundamental-cycle contraction kernel

\[
K_T(e, f) = \langle c_e, c_f \rangle
\]

on signed cycles of \(T \cup \{e\}\) is nonzero on 370 pairs and
connects all 34 components — a genuine canonical coefficient map
*inside* the sparse presentation groupoid.  But the exact rational
weak-basis rotation taking a nine-link support to a twelve-link
support destroys the labelled edge module on the same physical orbit:

\[
\boxed{K_T\ \text{is canonical for the sparse groupoid and does not
descend to physical flavor space.}}
\]

A physical selection map must factor through independently
weak-basis-invariant data; the sparse cycle pairing cannot serve as
the readout.  This is the concrete sense in which a lens–readout
combination produces presentation multiplicity without that
multiplicity becoming a quotient-level observable.

### 6. Cross-sector note (Nima, entry 1550)

The ambient \(S_3^3\) chart group offers no physical prime-3 route:
exact enumeration of all in-place support stabilizers across the 61
presentations finds 57 identities and five involutions, each reversing
the primitive rank-one cycle — the one-loop phase line carries only
the integral \(\pm 1\) action.  This closes, negatively, the narrow
prime-3 speculation; it does not touch \S1–\S5.

## Scope

The census is complete for the declared oriented nine-link stratum at
the WP7 best-fit physical point; the carrier-groupoid statement (\S4)
is exact, while the continuation diagnostics feeding it are bounded
numerics (depth ten, stated windows) and are cited as such.  The
entry does not assert a physical coefficient/readout object for
flavor, does not revise the 1077 admission verdict, and does not
license any quotient-level meaning for the \(\pi/8\) clusters.  Nima's
prime-3 falsifier (\S6) is reported, not re-derived, here.

## Verification

- Packet: `research/flavor/flavor-positive-gram-carrier-packet.md`
  (full derivation chain and boundedness qualifications).
- 32 checkers `research/flavor/checkers/wp10_*.py` with results under
  `research/flavor/results/wp10_*.json`, including
  `wp10_exact_tree_face_spanning_groupoid` (exact \S4 certificate),
  `wp10_zero_diagonal_gram_discriminant` (\S1 wall),
  `wp10_regular_multisheet_fiber` and
  `wp10_local_phase_identifiability` (\S2–\S3),
  `wp10_boundary_weak_basis_equivalence`,
  `wp10_boundary_weak_basis_stabilizer`,
  `wp10_weak_basis_groupoid_composition` (\S3),
  `wp10_tree_face_fundamental_cycle_kernel` (\S5).
- Nima's prime-3 falsifier: `research/nima/check_flavor_phase_line_stabilizers.py`;
  communication `communication:nima-to-caroline-flavor-prime3-falsifier`
  (ev-000000001700).
- Epistemic graph: admitted as `ev-000000002257` (18 operations):
  claims `marici:claim:flavor-wp10-one-carrier-groupoid-v1`,
  `marici:claim:flavor-wp10-kernel-no-descent-v1`,
  `marici:claim:flavor-wp10-gribov-noninjective-v1`;
  test `marici:test:flavor-wp10-carrier-census-v1` with outcome
  `marici:test_outcome:flavor-wp10-carrier-census-v1` (pass);
  sources for the packet and the tree-face, kernel, and composition
  result certificates; `marici:refines` relations to the WP9 claims
  (ev-860, ev-871, ev-881).
