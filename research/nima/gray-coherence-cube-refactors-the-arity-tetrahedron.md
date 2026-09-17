# Gray coherence cube refactors the arity tetrahedron

## Three binary coordinates

Use

\[
(x,y,z)\in\{0,1\}^3.
\]

The coordinates mean:

- `x`: unary/many input;
- `y`: unary/many output;
- `z`: order or polarization of the two arity operations.

The two `z`-layers are copies of the arity square:

\[
z=0:\quad \text{rooted substitution followed by cut},
\]

\[
z=1:\quad \text{cut followed by rooted substitution}.
\]

A vertical cube edge is the mixed Beck--Chevalley comparison

\[
\beta:HV\Longrightarrow VH.
\]

Thus the third direction is not a third arity. It is a coherence operation between the two composite orders.

## Visual model

```text
                 z=1: VH

       (1,*) -------- (*,*)
         |               |
         |               |
       (1,1) -------- (*,1)
          |              |
          | beta         | beta
          |              |
       (1,*) -------- (*,*)
         |               |
         |               |
       (1,1) -------- (*,1)

                 z=0: HV
```

Every horizontal/vertical face records one arity operation with the other held fixed. The four side faces record naturality of `beta`. The whole cube records coherence of the interchange transformation.

A Hamiltonian Gray cycle is

\[
000\to001\to011\to010\to110\to111\to101\to100\to000.
\]

Each step changes exactly one of input arity, output arity, or coherence polarization.

## Relation to the tetrahedron

The tetrahedron already projects to the arity square by

\[
x=\lambda_3+\lambda_4,
\qquad
y=\lambda_2+\lambda_3.
\]

Write `t=lambda_3`. Its allowed interval is

\[
\max(0,x+y-1)\le t\le\min(x,y).
\]

Resolve that interval by a cube coordinate `z`:

\[
t=t_{min}+z(t_{max}-t_{min}).
\]

Then

\[
(\lambda_1,\lambda_2,\lambda_3,\lambda_4)
=(1-x-y+t,\ y-t,\ t,\ x-t).
\]

At the four arity vertices, `t_min=t_max`; the entire `z`-edge collapses to one tetrahedral vertex. At the square center, the two `z` endpoints are

\[
z=0:\quad \frac12(V_2+V_4),
\]

\[
z=1:\quad \frac12(V_1+V_3).
\]

These are exactly the two diagonal factorizations identified in the source.

So the tetrahedron is the compressed quotient of the coherence cube obtained by collapsing the polarization direction wherever the two operation orders coincide. The cube is the better operational visual model; the tetrahedron is its economical barycentric compression.

## Strict and derived regimes

On the transverse occurrence complex, mixed Beck--Chevalley is strict. The vertical maps `beta` are identities after canonical factor identification, so the cube collapses toward the tetrahedral model.

For loaded, nontransverse, cutoff, or graph-domain realizations, `beta` can be a nontrivial 2-cell. Then the cube must be retained. Its failure to close strictly is measured by a face curvature, and compatibility of those face curvatures is the tetrahedral Bianchi identity

\[
\Omega_{ikl}-\Omega_{ijl}
+D_{kl}\Omega_{ijk}
-\Omega_{jkl}D_{ij}=0.
\]

This identifies the hierarchy:

1. arity edge: one input/output operation;
2. arity square: two operation directions;
3. coherence cube: comparison of the two composite orders;
4. four-dimensional cube: coherence between coherence cubes, when `beta` itself varies.

`check_gray_coherence_cube_to_arity_tetrahedron.py` verifies the Gray cycle, the cube-to-tetrahedron map, collapse at all four arity vertices, and the two diagonal endpoints over the center.
