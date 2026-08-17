# The One-Road Target Cell Exists Coefficientwise and Leaves One Purity Comparison

## Result

The three-face target demanded by Entry 379 already exists in the established
finite coefficient/Cousin model.  The Entry-129 \(x_3\) occurrence
Koszul--Cech Gysin, externally tensored with the fixed Entry-97/100 \(D03\)
packet, simultaneously supplies:

1. a nonzero degree-zero lower Cech component;
2. the degree-one \(x_3\)-edge component;
3. both endpoint faces \(v_{00}\) and \(v_{10}\);
4. both repeated-normal \(\operatorname{Tor}_0\) and
   \(\operatorname{Tor}_1\) grades; and
5. the positive physical line \([dX_{03}]\).

Deleting the lower component breaks its chain equation, exactly as predicted
by Entry 379.  Thus there is no remaining target-shape or coefficient-level
endpoint obstruction for the one-road cell.

The remaining gap is one categorical comparison, not three new maps.  For
each endpoint \(v_i\), one needs an occurrence-loaded purity/costalk map

\[
\boxed{
\operatorname{pur}^{\rm PC}_{i3}:
\mathcal C^{\rm fin}_{(x_i,x_3)}\widehat\otimes D_3
\longrightarrow
i^!_{(v_i,x_3)}
\mathcal Q^{\rm PC}_{03,\partial,\rm lf},
}
\]

and the two maps must be restrictions of the same \(x_3\)-edge comparison.
Here \(\mathcal C^{\rm fin}_{(x_i,x_3)}\) is the already constructed loaded
finite Koszul--Cech corner, not a newly postulated target.

## Exact coefficient cell

For \(i=0,1\), the two-normal occurrence corner has the full comparison

\[
K(x_i,x_3)\longrightarrow C_{(x_i,x_3)}
\]

in all degrees.  Entry 129's extraordinary edge map is

\[
g_0(r)=(r/x_i,0),
\qquad
g_1(t)=t/x_i.
\]

Its chain equation is

\[
d g_0=g_1d,
\]

and the endpoint top is

\[
\frac1{x_ix_3}.
\]

Tensoring with the four-normal Cech residue, the repeated-normal packet, and
the positive physical orientation gives

\[
v_{00}:
+\frac{[dX_{03}]}{x_0x_3u_0u_1u_3u_5},
\qquad
v_{10}:
+\frac{[dX_{03}]}{x_1x_3u_0u_1u_3u_5}.
\]

Every inverse occurs only in the target Cech summand that localizes that
parameter.  No occurrence or support normal is inverted in the base.

## Combination with the Rees bridge

Entry 378 fixes the generic coefficient as \(x_3\) and its first Cartier
symbol as \(+1\).  Entry 379 proves that the lower Cech and endpoint faces
must survive in the same cell.  The finite endpoint construction satisfies
precisely that coefficient-level requirement at both ends.

What is not yet justified is identifying its coefficient codomain with the
ringed PC extraordinary costalk.  The source and target still have distinct
reciprocal-regular and locally-finite/Borel--Moore variance.  The required
comparison must be geometric and extraordinary; neither finite duality nor
ordinary coherent restriction supplies it.

## Consequence

The next experiment should construct only
\(\operatorname{pur}^{\rm PC}_{i3}\), first at \(v_{10}\), where the old
typing failure was explicit, and then transport it along the same oriented
\(x_3\) edge to \(v_{00}\).  Its acceptance tests are already fixed:

- commute with the quotient \(\pi\) and excess trace
  \(\operatorname{tr}_{\rm ex}\);
- preserve the graph-Cartier Bockstein;
- preserve every lower Cech term;
- yield the two displayed positive endpoint residues; and
- agree with Entry 377 on the closed finite Cartier packet.

If such a comparison exists, the coefficientwise three-face cell becomes a
typed one-road Beck--Chevalley cell.  If it does not, the obstruction lies in
the passage from finite Cousin coefficients to the actual extraordinary PC
costalk, not in incidence, signs, endpoints, or Rees coefficients.

## Evidence boundary

`research/voevodsky/check_d03_x3_loaded_pc_endpoint_boundary.rs` was rerun
after repairing three edition-sensitive array iterations.  It verifies both
endpoint quotient complexes, the full lower occurrence-Cech map, all sixteen
normal Cech degrees, both Tor grades, the graph-Cartier square, and the two
positive residues.  It continues to report the actual ringed PC
extraordinary map as untyped.  No such map or full primal trace is claimed
here.
