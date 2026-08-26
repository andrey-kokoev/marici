# A complex Tate detector line has no nontrivial gauge-invariant positive cone

Owner: `marici.Kitaev`

## Bounded question

Can a convex order cone on the complex relative-detector line be invariant
under its full \(U(1)\) presentation gauge and thereby orient the finite part?

## Cone no-go

Let \(L\simeq\mathbb C\) be a complex line and let \(C\subseteq L\) be a
convex cone: it is closed under addition and multiplication by nonnegative real
scalars. Assume

\[
uC=C
\qquad\text{for every }u\in U(1).
\]

In particular, the phase \(u=-1\) gives

\[
C=-C.
\]

If \(C\) contains a nonzero vector \(v\), then it contains both \(v\) and
\(-v\). Hence

\[
C\cap(-C)=C\ne\{0\}.
\]

Therefore \(C\) is not pointed. The only pointed cone invariant under the full
phase gauge is the zero cone.

Consequently no nontrivial gauge-invariant order on a complex detector line
can prove off-seam divisor avoidance.

## Finite subgroup witness

The obstruction already appears for the two-element subgroup
\(\{1,-1\}\). For the four phases \(1,i,-1,-i\), the positive hull of one
nonzero orbit contains both coordinate axes in both orientations and equals
the entire underlying real plane. Continuous \(U(1)\) adds no escape.

## Required source reduction

An anti-linear real structure

\[
\kappa:L\to L,
\qquad \kappa^2=1,
\]

defines a fixed real line

\[
L^\kappa\simeq\mathbb R.
\]

That real line has two pointed rays. A further positive orientation—such as a
source vacuum, tensor unit, or normalized real section—must choose one. Thus

\[
\text{complex line}
\longrightarrow
\text{compatible real structure}
\longrightarrow
\text{chosen positive ray}.
\]

Duality or conjugation alone does not select the ray. Reflection coherence
can preserve both \(h\) and \(-h\); positivity must come from the Hilbert/source
typing or another independently fixed unit.

## Transport coherence

Across cutoff bonding maps \(U_{X,Y}:L_X\to L_Y\), real structures must obey

\[
\kappa_YU_{X,Y}=U_{X,Y}\kappa_X.
\]

A chosen positive reference \(e_X\in L_X^{\kappa_X}\) must then satisfy

\[
U_{X,Y}e_X=e_Y.
\]

Without these cells, choosing a sector in one scalar trivialization is a gauge
fix, not a source-invariant order.

## Application to the theta detector

The relative heat detector canonically constructs a complex finite-part line
and its scalar section. Regulator normalization fixes the section but does not
reduce the full phase presentation gauge to a real ordered ray.

The current source packets discuss reciprocal dual/conjugate lines and a
positive Hilbert metric on the critical seam. A Hermitian metric fixes norms,
not phases or a real fixed line. The global compatible real-structure cell and
positive detector ray have not been supplied for the off-seam relative finite
part.

Therefore the ordered-quotient/positive-cone route is closed at present except
on a separately source-derived real slice.

## Sectorial estimates

A complex sector estimate

\[
\operatorname{Re}(e^{-i\theta(s)}z)\ge c(s)>0
\]

does imply \(z\ne0\), but the phase \(\theta(s)\) is precisely an orientation
frame. It must transform with the detector-line gauge or be fixed by a source
real structure. Choosing it from the completed value is circular.

## Hostile fixtures

- full \(U(1)\)-invariant cone: nonzero implies nonpointed;
- (\{1,-1\}\)-invariance already suffices for failure;
- Hermitian norm: positive but does not choose a phase ray;
- conjugation: supplies a real line only after a compatible involution is
  frozen;
- target-fitted sector angle: proves the desired value by importing its phase.

## Disposition

Complex finite-part positivity cannot be gauge invariant. Any explanatory
orientation theorem must construct and transport a real structure and a
positive ray from the source, or use a determinant/kernel mechanism that does
not require ordering the scalar line.

## Claim strength

Exact convex-cone no-go and typing theorem. No claim is made that the theta
source cannot eventually supply the required real structure.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_theta_complex_cone_no_go.py`.
The result is written to
`research/kitaev/results/theta-complex-cone-no-go.json`.
