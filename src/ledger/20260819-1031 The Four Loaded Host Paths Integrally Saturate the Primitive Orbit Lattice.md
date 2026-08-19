# 1031 — The Four Loaded Host Paths Integrally Saturate the Primitive Orbit Lattice

## Reopening Entry 956's provenance gate

Entry 945 computes the primitive two-seed orbit Smith invariants

\[
(1,1,2,2,2,4),
\]

with quotient

\[
(\mathbb Z/2)^3\oplus\mathbb Z/4.
\]

Entry 946 found twelve four-element coordinate subsets that saturate this
lattice, but Entry 956 correctly withdrew their interpretation as twisted
chambers because the checker had not derived those coordinate vectors from
loaded paths.

Entries 969 and 1028 now supply the missing provenance.

## Source-derived host columns

The four local host paths are source columns

\[
\{0,2,3,5\}
\]

of the loaded boundary matrix. In Entry 969's unimodular skeleton \(S\), they
map to target coordinate columns

\[
\{1,4,3,5\}.
\]

After sorting, this is

\[
\boxed{\{1,3,4,5\}.}
\]

That exact subset occurs in Entry 945's independently frozen saturating
census.

## Exact Smith consequence

Adjoining these four geometrically specified host-path skeleton columns to
the primitive orbit matrix changes its Smith invariants from

\[
(1,1,2,2,2,4)
\]

to

\[
\boxed{(1,1,1,1,1,1).}
\]

Therefore the index changes from \(32\) to \(1\).

No transition column is required for this integral saturation. The two
pivot-transition paths remain responsible for the missing chamber directions
and composite Fitting support, not for killing the generic two-primary
orbit quotient.

## Narrow conclusion

\[
\boxed{
\text{the four source-derived loaded host paths integrally saturate the
primitive two-seed occurrence lattice.}
}
\]

This repairs the provenance defect isolated in Entry 956. The earlier
two-primary quotient is not intrinsic to the loaded-path algebraic lattice;
it measures omission of four already existing host paths.

The statement is made after localization away from the host paths' existing
wall coefficients, exactly as in Entries 944--945. It does not yet construct
an integral twisted-Betti comparison or a differential parameter connection.

## Consequence for Entry 1030

The rational character diagonalization used in Entry 1030 is not the only
way to access the saturated occurrence lattice. Its denominator-two warning
is bypassed by adjoining the native integral host paths before passing to
characters.

Thus no free or finite two-primary obstruction remains at the algebraic
occurrence-lattice level. The unresolved arithmetic question has moved to the
actual de Rham--Betti comparison.

## Next falsifier

Retain the four host paths and add the two source-derived pivot-transition
paths as actual relative chains. Construct their complete loaded boundary
matrix in a common integral twisted-chain convention and compare it with
the six-word de Rham frame.

The acceptance test is an integral chain comparison with determinant a unit
after only the declared local wall factors are removed. A residual integer
index would be genuine comparison data; no coordinate lift may be added
afterward.

## Durable evidence

- orbit packet:
  'research/benincasa/string-six-point-orbit-two-primary.json';
- loaded skeleton packet:
  'research/benincasa/string-six-point-loaded-corner-localization.json';
- result packet:
  'research/benincasa/string-six-point-loaded-host-integral-saturation.json';
- allocator claim:
  'seqclaim-86f5acc6f171d8b2ca3c76d0'.
- epistemic event:
  'ev-000000000650-65ea0ee3-7c61-4d9d-9fab-43c9463cb65d'.
