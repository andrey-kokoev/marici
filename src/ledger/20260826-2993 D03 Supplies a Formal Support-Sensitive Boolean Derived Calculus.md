---
author: marici.Benincasa
date: 2026-08-26
sequence_claim: seqclaim-c1e23081a9bd189092166d30
---

# 2993 — D03 Supplies a Formal Support-Sensitive Boolean Derived Calculus

## Scope

This audit concerns only the fixed D03 occurrence-level Cox/Koszul--Cech and coefficient/Cousin models implemented by

- `research/voevodsky/check_d03_toric_cox_cousin_trace.rs`;
- `research/voevodsky/check_d03_x3_loaded_pc_endpoint_boundary.rs`.

It does not identify those models with the actual ringed PC extraordinary costalk, physical Cut sewing, or a G03 source map.

## Hard-to-vary claim

The D03 packet is a genuine positive model of

[
	ext{labelled Boolean incidence}
+
	ext{support-sensitive cubical maps}
+
	ext{source-defined coefficient transport}
]

at the fixed formal coefficient/Cousin level.

Unlike the five-site row audited in Entry 2992, its decisive maps are not inserted as a predeclared nonzero row.

## Construction audit

The first checker derives the oriented road square from principal monomial labels, verifies both weighted chain identities, and shows that the normalized complex resolves the Cartier ideal

[
(M),qquad M=x_0x_1x_3x_4.
]

On the (x_3) edge it constructs the one- and two-normal Koszul-to-Cech maps explicitly.  For endpoint normal (x_i), the degree-one comparison is

[
g_i^0(r)=(r/x_i,0),
qquad
g_i^1(t)=t/x_i,
]

and the checker verifies

[
d,g_i^0=g_i^1d.
]

The resulting top class is (1/(x_ix_3)), with both (v_{00}) and (v_{10}) residues fixed by the retained occurrence orientations.

The second checker preserves this construction after loading the frozen D03 coefficient packet.  It verifies:

- the endpoint quotient chain maps and their finite-free duals;
- the full two-normal Koszul--Cech comparison in every degree;
- the four-normal comparison across all (16) Boolean masks;
- localization of each negative exponent only in the target Cech summand that authorizes it;
- simultaneous retention of the Tor-zero quotient and primitive Tor-one repeated-normal excess;
- the independent physical orientation line.

Its negative control is decisive: deleting the lower component (g_i^0) destroys the chain equation.  The lower Cech term is therefore required by coherence rather than decorative bookkeeping.

## Boundary

The same checkers prove that ordinary coherent Cousin residue of a regular section is zero.  They also record that no occurrence-loaded purity comparison into the actual ringed PC costalk has been constructed.

Therefore the surviving architecture is

[
	ext{shared labelled Boolean incidence algebra}
+
	ext{a proved formal support-sensitive Boolean derived calculus}
+
	ext{sector-specific coefficient transport},
]

but only inside the fixed D03 formal coefficient model.

The stronger cross-sector claim remains open:

[
	ext{one shared ringed/physical support-sensitive Boolean derived calculus}.
]

## Consequence

Entry 2990 was too pessimistic if read as denying every positive derived realization.  D03 supplies one.  Entry 2992 remains valid: a support census and a preloaded A2 row do not automatically inherit D03's construction.

The next finite falsifier is the missing occurrence-loaded purity/costalk comparison

[
operatorname{pur}^{m PC}_{i3}:
C_{(x_i,x_3)}otimes C_Q
longrightarrow
i_{(v_{i3})}^{!}Q^{m PC}_{(03,partial,mathrm{lf})}.
]

It must be derived first at (v_{10}), then at (v_{00}), and commute with the quotient map, excess trace, graph-Cartier Bockstein, and every lower Cech component.  Failure closes promotion at the ringed-PC boundary without retracting the formal D03 theorem.

## Durable verification

Static source audit verified the exact map formulas, chain identities, all-mask normal comparison, localization discipline, and negative controls in the two frozen Rust checkers above.  No site build was run.
