# The Two-Sector Boundary Incidence Is the de Branges Krein Norm

## Boundary two-plane

Let the two half-line transforms be

\[
F_+(z)=\int_0^\infty A(u)e^{izu}\,du,
\qquad
F_-(z)=F_+(-z),
\]

and form the boundary vector

\[
\mathbf F(z)=\left(F_+(z),F_-(z)\right).
\]

The symmetric scalar readout is (X(z)=F_+(z)+F_-(z)). A zero means that (\mathbf F(z)) lies on the antisymmetric line.

The natural indefinite form on this two-plane is

\[
J(\mathbf F)=|F_-|^2-|F_+|^2.
\]

Both diagonal and antisymmetric lines are null for (J). Therefore a sufficient zero-confinement theorem is that the source boundary vector remains strictly in one timelike cone in each open half-plane and becomes null only on the reciprocal seam.

## Exact identification

This proposed cone theorem is not a new route. It is exactly the Hermite–Biehler/de Branges modulus condition:

\[
|F_-(z)|>|F_+(z)|
\]

in one open sector, with the inequality reversed in the other. If it holds, the boundary vector cannot meet the antisymmetric null line off the seam.

Thus the new seam geometry has supplied the correct geometric type—a Krein two-plane of signature ((1,1))—but it has not yet supplied the orientation theorem. The missing sign is the same sign isolated earlier by the de Branges kernel.

## Source expansion of the Krein norm

For (z=x+iy) and real source (A), direct expansion gives

\[
J(z)
=
2\int_0^\infty\int_0^\infty
A(u)A(v)
\sinh\!\left(y(u+v)\right)
\cos\!\left(x(u-v)\right)
\,du\,dv.
\]

The factor involving the hyperbolic sine has the sign of (y), but the cosine factor oscillates. Positivity of (A) alone therefore does not orient (J). This is the same obstruction previously seen in the source-separation measure and adjacent-band transport programme.

## Geometric-algebra interpretation

The six-channel split evaluation form restricts on the completed boundary pair to this ((1,1)) form. The two open half-planes should correspond to its two timelike cones; the critical seam is the null interface. A scalar zero is incidence with one distinguished null generator, not annihilation of the full vector.

This vindicates the hyperbolic-rotation intuition but also states its proof burden exactly: the source evolution must remain in the appropriate spin semigroup. Declaring the comparison hyperbolic is equivalent to assuming the missing modulus dominance.

## Research compression

The recent chain has not produced an independent RH proof condition. It has explained why several formulations coincide:

- symmetric seam (H^1) admission detects scalar cancellation;
- antisymmetric boundary incidence records the surviving relationship;
- Krein timelikeness is Hermite–Biehler dominance;
- its source expansion is the oscillatory double-integral orientation problem.

These are now one invariant viewed through quotient, geometric-algebra, operator, and source coordinates. Agreement among them is not multiple evidence.

## Remaining hard theorem

Prove—or finitely falsify—a modularly source-derived orientation of the oscillatory double integral. The allowed mechanism must use information absent from an arbitrary positive source, such as labelled prime-scale sewing, a canonical adjacent-band transport, or a conserved current on the full boundary-bearing adelic object.

## Verification

The checker `research/grothendieck/checkers/boundary_krein_debranges_identity.py` verifies on a positive three-atom source that the Krein norm equals the oscillatory double sum, that the antisymmetric line is null, and that positive source weights do not remove negative cosine factors.
