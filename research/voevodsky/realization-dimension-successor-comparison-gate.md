# Comparison gate from stabilized to arithmetic realization dimension

## Constructed successor

The anchored graph category has the canonical stabilization

\[
S_k:M_k\longrightarrow M_{k+1}^{stab}=M_k\oplus\mathbb C,
\qquad x\mapsto(x,0).
\]

It is isometric, natural for all four chart comparisons, compatible with the moving-current pullback, and commutes with translation-center covariance.

## Required arithmetic identification

To turn stabilization into a successor landing in an independently prescribed arithmetic realization `M_(k+1)^arith`, one needs a comparison equivalence

\[
C_k:M_k\oplus\mathbb C\xrightarrow{\sim}M_{k+1}^{arith}.
\]

The genuine arithmetic successor would then be

\[
A_k=C_kS_k.
\]

For this formula to be admitted, `C_k` must satisfy all of the following.

1. **Source anchor:** it carries `(x,0)` to the declared image of the old source inside the new source.
2. **Four charts:** for every `i`,
   \[
   C_{i,k}q_{i,k}^{stab}=q_{i,k+1}^{arith}C_k.
   \]
3. **Forms:** it is unitary/isometric for the weighted relative graph form.
4. **Endpoint and index ports:** it carries the old fixed endpoint and moving-current coordinates to their declared successors.
5. **Translation covariance:** `C_k U_a^{stab}=U_a^{arith}C_k`.
6. **Differentials/domains:** it maps the completed graph domain onto the new graph domain and intertwines closed generators.
7. **Orientation:** it preserves the determinant line and tetrahedral boundary orientation.

Under these hypotheses, `A_k` is automatically a functorial one-unit successor on every edge, face, and tetrahedron, because each naturality square is obtained by composing the stabilization square with the corresponding `C_k` square.

## Search disposition

The repository does not define a concrete independent object `M_(k+1)^arith`, its source inclusion, or its coordinate maps in a form from which `C_k` can be constructed. Existing nearby operations have different types:

- `U_1` changes translation center, not realization dimension;
- the four-chart rotation changes presentation index;
- stable suspension changes homological degree;
- cutoff successors change regulator rung;
- the fixed-block observer inverse returns to the source at the same `k`.

Consequently no honest identification can presently be made. Declaring any of these maps to be `C_k` would conflate independent gradings explicitly separated by prior audits.

## Minimal missing input

A concrete arithmetic dimension package must provide at least:

\[
(D_{0,k+1},q_{1,k+1},q_{2,k+1},q_{3,k+1},q_{4,k+1})
\]

and a source map

\[
a_k:D_{0,k}\to D_{0,k+1}.
\]

Once these are supplied, `C_k` is tested by the seven conditions above; if it exists, `A_k=C_kS_k` completes the requested identification.
