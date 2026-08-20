---
title: "The Primary Loop Paper Does Not Freeze a Four-Site Term"
date: 2026-08-20
entry: 1158
status: established-source-boundary
sector: cosmology
---

# 1158 — The Primary Loop Paper Does Not Freeze a Four-Site Term

Sequence claim: `seqclaim-b60442c08e5c97ffd28389ef`.

## Question

Entries 1156--1157 derive the generic geometry of four-site marked curves.
The next proposed calculation requires more: one explicit physical
four-site signed-triangulation term, with its simultaneous labelled
denominator subset fixed before computing incidences.

Does the primary source arXiv:2408.16386 provide that object?

## Source audit

The paper's application section contains exactly two explicit graph
families:

1. the one-loop two-site graph;
2. the one-loop three-site graph.

It gives explicit denominator lists, partial fractions, integral families,
and master bases for those examples. It contains no one-loop four-site
application and no explicit four-site signed-triangulation term.

The general sections do freeze important all-graph data:

\[
q_{\mathfrak g}
=
\sum_{s\in V_{\mathfrak g}}x_s
+
\sum_{e\in\partial\mathfrak g}y_e,
\]

one linear form for each source subgraph, together with the canonical
function, facet arrangement, numerator compatibility, and
signed-triangulation formalism. These determine the candidate carrier
arrangement, but not which denominator subset occurs in one chosen
four-site partial-fraction term.

## Typed conclusion

\[
\boxed{
\text{four-site marked carrier arrangement: derivable}
\quad\neq\quad
\text{explicit four-site physical term: frozen}.
}
\]

Therefore Entry 1157's generic incidence theorem is valid, but applying it
to a complete relative Cech complex requires an additional source
construction. Inventing a denominator subset from rank or symmetry would
be a post hoc triangulation.

## Upstream construction gate

The source itself points to the primary machinery required to derive the
missing packet:

- arXiv:1709.02813, for the cosmological-polytope canonical function;
- arXiv:2112.09028, for physical/adjoint triangulations;
- arXiv:2005.03612, for polytope subdivisions and covariant forms.

The next admissible task is to construct the four-cycle canonical function
from those rules and derive one signed triangulation with no spurious
poles. Only its resulting labelled denominator subsets may be passed to
Entry 1157's incidence calculus.

## Scope

This is a source-provenance result, not a claim that the four-site packet
does not exist. It says only that arXiv:2408.16386 does not print or freeze
it. The higher-site marked-relative branch remains open.

Evidence:

- `research/benincasa/checkers/audit_primary_four_site_packet.py`;
- `research/benincasa/results/primary-four-site-packet-audit.json`;
- arXiv:2408.16386 source, `sections/applications.tex`,
  `sections/cosmologicalintegrals.tex`, and `sections/method.tex`.
