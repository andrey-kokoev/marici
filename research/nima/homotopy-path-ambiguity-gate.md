# Existence of a homotopy does not make its witnesses interchangeable

## Second coherence obstruction

Suppose (S,T:F\Rightarrow G) are two chain homotopies:

\[
F-G=\partial S=\partial T,
\qquad
\partial X=\bar D X+X D.
\]

Their difference (Z=S-T) is a degree (-1) cycle.  The two comparison
paths are themselves coherently interchangeable only if there is a
degree (-2) cell (U) with

\[
\boxed{S-T=\partial U.}
\]

The obstruction is therefore

\[
[S-T]\in H^{-1}\operatorname{Hom}(C,\bar C).
\]

This is independent of the degree-zero obstruction deciding whether any
homotopy (F\Rightarrow G) exists.

## Minimal finite witness

Over (mathbf F_2), take zero-differential complexes with

\[
C^1=\langle x\rangle,qquad
\bar C^0=\langle y\rangle,
\]

and no other nonzero groups.  Let (F=G=0).  Both

\[
S(x)=y,qquad T(x)=0
\]

are valid homotopies because (partial S=partial T=0=F-G).
However, the degree (-2) Hom group is zero, so no (U) can satisfy
(partial U=S-T).  Hence

\[
[S-T]\ne0.
\]

Two valid equivalence witnesses for the same maps are not equivalent.

## Compiler consequence

A compiler may:

1. retain the exact homotopy witness and its constructor provenance; or
2. quotient witnesses only when an authorized higher cell is supplied.

It may not flatten both paths into a Boolean `equivalent=true`.
Otherwise later composition can depend on which invisible comparison
path was used.

```json
{
  "code": "homotopy_witness_ambiguity",
  "endpoint_maps_equal": true,
  "both_homotopies_valid": true,
  "difference_class_degree": -1,
  "difference_rank": 1,
  "higher_cell_available": false
}
```

## Cross-sector consequence

- Constructor trees require comparison-cell identity, not only endpoint
  equality and existence of some comparison.
- A direct-image reducer must preserve chosen descent homotopies or carry
  higher comparison cells.
- Two schedules with the same logical action can remain distinct
  authority paths.
- Scalar completion cannot erase the provenance of an operator-level
  comparison.

## Boundary

This does not require an infinite coherence tower in every finite
problem.  It says precisely that truncation is valid only when the
relevant negative Hom cohomology vanishes or a source-authorized
truncation law is supplied.

