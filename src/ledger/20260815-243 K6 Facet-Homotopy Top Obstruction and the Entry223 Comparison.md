# K6 Facet-Homotopy Top Obstruction and the Entry223 Comparison

## Record

Date: 2026-08-15

Status: proved that the nine literal facet homotopies forced by reflection
assemble into one primitive global obstruction, namely minus the boundary
of the unique \(K_6\) top cell. The remaining comparison with entry223 is
therefore a single top-cell problem rather than nine independent choices.
The spatial comparison itself is not constructed. No graph admission is
claimed.

## Exact top computation

Let \(F_a\), for the nine diagonals \(a\), denote the oriented literal
facets of \(K_6\). Entry242 derives a reflection homotopy coefficient
\(\epsilon_a=\pm1\) from
\[
r(c_a)-c_{ra}=\epsilon_a\,dF_{ra}.
\]
The executable accumulates the nine coefficients into
\[
H_{\mathrm{refl}}=\sum_a\epsilon_aF_a.
\]
It then applies the full literal facet-to-edge incidence matrix. The result
is
\[
dH_{\mathrm{refl}}=0.
\]
Comparison with the independently generated boundary column of the unique
empty-face/top generator \(T_{K_6}\) gives
\[
\boxed{H_{\mathrm{refl}}=-\,dT_{K_6}}.
\]
The coefficient is primitive, its Smith form is \([1]\), and there is no
torsion or division by two. Thus the nine local reflection defects have one
canonical higher filler in the literal cellular complex.

## Relation to entry223

Entry223 supplies a different primitive top
\(W_{012}\) in the projectivized-conductor SNC category, with three
long-road facets and
\[
dW_{012}=q_\Sigma-s_{14}-s_{03}-s_{25}.
\]
The present calculation does not identify \(T_{K_6}\) with \(W_{012}\).
The literal top has nine facet rows: six short-sheet facets and three
long-road facets. A valid comparison must derive:

1. a canonical contraction of the six short-facet rows into the
   normalization-sheet/AW acyclic complement;
2. the three long-facet images as the entry223 special residues;
3. the generic top image as the based nonzero \(q_\Sigma\) comparison; and
4. compatibility of those contractions with the endpoint odd counits,
   reflection, and \(D_3\).

This is now the earliest missing correspondence. Stipulating the six
contractions would merely choose the unresolved rank-nine AW lift.

## Downstream status

The primitive top computation removes an independent top-scalar or
top-torsion ambiguity. It does not instantiate the endpoint/\(Q\) mapping
fiber. Consequently \(p_{\partial,Q}\), its polarity Bockstein, and the
\(D_8\)/Jordan coherence tests remain undefined.

## Executable evidence

Checker:
research/voevodsky/check_dp6_oriented_facet_corridors.rs

SHA-256:
1324c0eedf6f5380344a40d83681df0171176693b589e99d75821043f65f1fc8

The user-site structured-command MCP ran rustfmt, rustfmt --check,
warnings-denied optimized compilation, executable assertions, and JSON
output. All passed.

## Outcome contract

~~~json
{
  "claim": "The nine literal reflection facet homotopies form a closed chain equal to minus the primitive boundary of the unique K6 top cell.",
  "status": "proved_scoped_literal_K6_facet_homotopy_top_obstruction",
  "scope": "literal K6 cellular incidence; comparison to the external entry223 projectivized-conductor top excluded",
  "matrix": {
    "facet_rows": 9,
    "homotopy_chain_closed": true,
    "equals_top_boundary": true,
    "top_boundary_coefficient": -1,
    "smith": [1],
    "torsion": false
  },
  "consequence": "the nine local reflection defects require one canonical literal K6 top filler rather than nine independent higher choices",
  "minimal_additional_datum": "a support-typed comparison from the literal K6 top to entry223 that canonically contracts six short facets and maps three long facets and the generic top to the special residues and based qSigma row",
  "unconstructed": [
    "six short-facet contraction rows",
    "three long-facet residue comparison rows",
    "based nonzero qSigma top comparison",
    "rank-nine AW contraction",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_oriented_facet_corridors.rs",
  "checker_sha256": "1324c0eedf6f5380344a40d83681df0171176693b589e99d75821043f65f1fc8"
}
~~~
