---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Individual Occurrence Periods Are Not Source-Canonical

## Record

Status: the strong conjecture that both occurrence-resolved weight-zero
classes possess individually regulator-independent physical periods is
falsified. The primary contour construction explicitly leaves a hierarchy
choice at spurious subdivision poles, and the two lower occurrences meet at
exactly such a reduced pole after the ordered
\(q_{\mathcal G_{12}}\) residue. Their algebraic de Rham classes and endpoint
jets remain canonical, but the source fixes a physical relative period only
for their unsplit sum.

No regulator hierarchy, boundary counterterm, carrier cell, support summand,
or normalization is added.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{the occurrence-resolved endpoint classes are individually relative,
their physical periods are regulator-independent, and they sew to the
unsplit period.}
}
\]

The finite falsifier is a pair of source-admissible regulator hierarchies
which induce different currents on the same frozen marked intersection.

## Primary-source regulator theorem

Albayrak--Benincasa--Duaso Pueyo, arXiv:2305.19686v2,
equations (4.15)--(4.20), proves the required distinction.

- True facet poles carry a sign-definite negative imaginary part assembled
  from positive contour regulators.
- Spurious subdivision poles carry
  \(\alpha\epsilon_{\hat b}-\beta\epsilon_{\hat a}\), with
  \(\alpha,\beta>0\), so their side depends on an arbitrary regulator
  hierarchy.
- The ambiguity disappears from the complete canonical form because the
  residue on the spurious boundary vanishes.
- The induced negative imaginary parts of site and edge energies are linear
  combinations of the contour regulators; their magnitudes are not equated.

This closes the upstream question left open in entry 231. The graph-level
construction does not collapse the reduced-pole cone to one chamber. It
classifies the ambiguous poles themselves as hierarchy-dependent spurious
poles.

## Frozen exceptional current

After the ordered Cut residue,

\[
q_{\mathfrak g_{31}}=A+i\alpha,
\qquad
q_{\mathfrak g_{23}}=B+i\beta,
\]

where

\[
\alpha=\xi_2-\eta_{23},
\qquad
\beta=\xi_1-\eta_{31}.
\]

On the exceptional divisor \(B=-A\). Therefore

\[
\frac1{A+i0s_\alpha}+
\frac1{-A+i0s_\beta}
=-i\pi(s_\alpha+s_\beta)\delta(A).
\]

The chambers

\[
(--),(-+),(+-),(++)
\]

give, in units of \(i\pi\delta(A)\),

\[
2,0,0,-2.
\]

Thus the boundary-value operation and the weighted nearby limit do not
commute occurrence by occurrence. The ambiguity is supported on the already
frozen marked intersection.

## Endpoint-relative obstruction at weight zero

Entry 243 gives exact reductions

\[
\eta_i=c_i\frac{dn}{w}+d\Phi_i,
\qquad
\Phi_i=\frac{H_i(n)}{8(xy)^{3/2}w^9},
\]

where every \(H_i\) is odd and has nonzero polar jets at \(w=0\). Hence
\(d\Phi_i\) is absolute-meromorphically exact but not relatively trivial
without a chosen endpoint trivialization. Different finite-part
subtractions change an individual regulated period by boundary values of
\(\Phi_i\).

The source provides no occurrence-by-occurrence endpoint subtraction.
Assigning one would be a post hoc chain-level choice prohibited by the
frozen-source rule.

By contrast, the exact identities

\[
\eta_{31}+\eta_{23}=\eta_{\rm unsplit},
\qquad
\Phi_{31}+\Phi_{23}=\Phi_{\rm unsplit}
\]

show that both de Rham classes and endpoint jets sew before a physical
boundary value is taken. The complete source canonical form then fixes the
unsplit physical germ.

## Verdict

The strong conjecture is falsified narrowly:

\[
\boxed{
\text{individual occurrence periods are not source-canonical.}
}
\]

The smaller hypothesis survives:

\[
\boxed{
\text{occurrence resolution is canonical at de Rham/endpoint-jet level,
but the physical period is canonical only after source sewing.}
}
\]

This updates H2 without weakening the shared-carrier claim. The failure is
in sector-specific relative-chain/coefficient assembly, not incidence.

## Compatibility statements

- infinity-Gysin quotient: each wall class still has zero direct Legendre
  image;
- algebraic kernel \(\mathcal T_7\): the occurrence data can only enter its
  relative/algebraic extension sector;
- Gauss--Manin horizontality: not defined for either physical occurrence
  period separately because the source does not define those periods;
- sewn horizontality: remains the next legitimate test;
- soft and discriminant limits: not needed for the generic falsifier and
  may only add supported terms;
- new carrier datum: none.

## Evidence

- primary source arXiv:2305.19686v2, equations (4.15)--(4.20), especially
  the hierarchy statement between (4.15) and (4.16);
- entry 231's exhaustive four-chamber current census;
- entries 242--243's exact individual de Rham reductions and endpoint-jet
  sewing;
- `research/benincasa/occurrence-resolved-physical-period-no-go.md`.

## Next finite falsifier

Construct the minimal source-defined relative extension

\[
0\longrightarrow \mathcal B_{\partial}
\longrightarrow \mathcal R_{\rm occ}
\longrightarrow
\mathcal K_{31}\oplus\mathcal K_{23}
\longrightarrow0
\]

whose boundary object \(\mathcal B_{\partial}\) records the two endpoint-jet
vectors, and test whether the source sewing map descends to a horizontal
quotient

\[
\mathcal R_{\rm occ}\longrightarrow\mathcal R_{\rm unsplit}.
\]

Freeze the exact primitives, endpoint divisor, cyclic occurrence orbits,
Kummer sign monodromy, and source unsplit chain. If no horizontal sewn
quotient exists without a fitted boundary splitting, canonical global
occurrence assembly is falsified. A failure remains coefficient/extension
data unless it demands a source-derived new incidence.

## Outcome contract

~~~json
{
  "claim": "Occurrence-resolved endpoint classes have individually regulator-independent physical periods which sew to the unsplit period.",
  "status": "falsified",
  "primary_source_result": "spurious reduced poles require arbitrary regulator hierarchy",
  "individual_de_rham_classes": "canonical",
  "individual_endpoint_jets": "canonical_algebraic_relative_data",
  "individual_physical_periods": "not_source_canonical",
  "source_canonical_object": "unsplit_sewn_period",
  "generic_chamber_currents": [2, 0, 0, -2],
  "direct_legendre_gysin_image": 0,
  "new_carrier_incidence": false,
  "surviving_hypothesis": "canonical occurrence data before physical pairing; canonical physical period only after source sewing",
  "next_experiment": "Construct and test the horizontal sewn relative extension with endpoint-jet boundary object."
}
~~~
