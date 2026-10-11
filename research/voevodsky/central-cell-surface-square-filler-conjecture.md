# Central-cell surface-square filler conjecture

## Operator proposal

Locate the prior coherence pyramid with eight nodes / seven segments per edge, related to the 3+3+1 two-sided indexing and involution. Test whether the innermost cell's surface, squared, gives the full filler. The meaning of the square operation is not yet specified; do not silently replace it by Euclidean area squared, a Cartesian product, or composition.

## Located prior constructions

- `the-eight-node-pyramid-is-the-seventh-edgewise-subdivision-and-should-be-proved-coherent-by-one-simplicial-extension-not-343-independent-checks.md`: the geometric complex is esd_7(Delta^3), with barycentric integer coordinates summing to 7. Polarity is a dagger together with orientation reversal; it does not assert that every typed transfer is a self-map squaring to identity.
- `../nima/nested-closure-system-full-categorical-construction-sketch.md`, section 7: twisted-arrow indexing [3]^op star [3] gives 3+3+1=7 and eight vertices. The note explicitly does not identify that indexing operation with uniform seventh edgewise subdivision.
- `eight-node-lattice-analytical-form-coverage-ledger.md`, iterations 8–9: explicit lattice incidence and analytical-form labels.
- `checkers/check_esd7_explicit_analytical_census.py`: rerun during this investigation; all its finite enumeration checks passed. Analytical-form fields are labels; this rerun is not a fresh proof of their analytical interpretations.

## Fresh central-cell check

The census has f-vector (120,560,784,343), with boundary f-vector (100,294,196).

The unique tetrahedron with barycentric vertices

- (1,2,2,2)
- (2,1,2,2)
- (2,2,1,2)
- (2,2,2,1)

is T184. Its barycenter is (7/4,7/4,7/4,7/4), equal to the parent barycenter. Its boundary faces are F403, F404, F406, F538. This identifies a specific innermost cell rather than choosing a visually central cell in the unrelated Three.js assembly.

Let v_i=7e_i be the parent corners, w_i the corresponding central corners, and c their common center. Then

w_i = c - (v_i-c)/7.

Equivalently,

v_i = c - 7(w_i-c).

Thus the central cell is a reflected homothetic copy of the parent with scale 1/7. Its surface and volume ratios are 1/49 and 1/343. The homothety is not itself an involution; applying the scale -7 map twice has scale 49.

## Conjecture status and next test

The literal numerical equation 'surface area squared = volume' is not scale-invariant: its sides scale with fourth and third powers of length. It cannot be a universal geometric identity without additional normalization or an operation converting types/dimensions.

The proposed structural square remains open. The next necessary definition is a typed operation on the complete marked boundary of T184, including its involution and gluing, with a specified output filler type. Once defined, compare its incidence, boundary restriction, and filler against esd_7(Delta^3). Equality of counts alone is insufficient.

The current 26-tetrahedron Three.js assembly has not been identified with this 343-cell lattice. No scene geometry was changed in this investigation.
