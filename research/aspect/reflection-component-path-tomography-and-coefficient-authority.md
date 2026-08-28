# Reflection-component path tomography and coefficient authority

## Exact optical path

Let sheet exchange be

`X=[[0,1],[1,0]]`

and let the continuous relative-phase path be

`U(t)=diag(1,exp(i pi t))`.

It connects the identity to the selective gate `Z=diag(1,-1)`.  Track

`s(U)=trace(U^dagger X U X)/2`.

Along this path,

`s(U(t))=cos(pi t)`.

Hence `s` moves from `+1` to `-1` and crosses zero at `t=1/2`.  The endpoints
are projective eigenoperators of reflection:

`X I X=I`,

`X Z X=-Z`.

At the lossless midpoint `U=diag(1,i)`, neither projective sign works.  The
squared Frobenius defect from both fixed components is exactly four:

`||XUX-U||_F^2=||XUX+U||_F^2=4`.

The endpoint gate is valid, but this implementation path necessarily exits
the reflection-fixed projective locus.

## Source dyad

The infinitesimal sheet generator is `iZ`.  Under the electric/magnetic
Hadamard frame it becomes

`iX=i(|E><M|+|M><E|)`.

Full tomography must therefore recover the mixed electric-magnetic dyad.  A
fitted endpoint phase without this generator does not certify that the source
executed the duality rotation.

## Coefficient authority

The mixed generator is canonical over the complexified carrier.  It does not
preserve the original rational or integral real sheet lattice: applying `iZ`
to a rational basis vector produces an imaginary coefficient.

The apparatus can verify complex optical execution, path continuity,
unitarity, and the mixed dyad.  It cannot infer authority to reinterpret that
complex operation as a physical electric-magnetic duality on the original
real source lattice.  That requires an independently derived complex or dual
source structure.

## Fifth classifier label

Add constructibility to the dark-event classifier:

- endpoint-admissible: final operation has the required projective symmetry;
- path-admissible: every intermediate operation stays inside the declared
  symmetry locus;
- coefficient-admissible: the generator preserves the declared source
  coefficient ring or an authorized scalar extension is supplied.

For the standard path, the endpoint label passes, the path label fails, and
the coefficient label requires complexification.  These labels are
independent of packet zero, transmission zero, incidence alias, and
normalization erasure.

## Optical acquisition

Perform process tomography at multiple `t`, reconstruct `U(t)`, and report:

- unitarity residual;
- `s(U(t))`;
- defects from the `+1` and `-1` reflection components;
- the generator in both sheet and electric/magnetic frames;
- the coefficient ring used by the reconstruction.

A sample only at `t=0,1` cannot see the component crossing.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_reflection_component_path_tomography.py
```
