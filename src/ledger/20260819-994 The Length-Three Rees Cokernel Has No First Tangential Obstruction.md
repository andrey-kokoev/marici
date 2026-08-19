# The Length-Three Rees Cokernel Has No First Tangential Obstruction

## Question

Entry 947 constructs the intrinsic quadratic exact-valuation object

\[
E_2(C)=
\frac{\ker(\Lambda:C\to C)\cap\Lambda C}
     {\ker(\Lambda:C\to C)\cap\Lambda^2C},
\qquad \dim E_2(C)=7.
\]

Entry 952 shows that its rank is stable at three sampled generic points of
the triangle wall.  Pointwise rank stability does not prove compatibility
with tangential differentiation.  The first source-derived obstruction is
the mixed normal--tangential jet of the complete relation presentation.

## Bivariate jet

At the base point \((X_1,X_2,X_3)=(2,3,5)\), use

\[
(X_1,X_2,X_3)
=
(2+\tau,3,5+\tau+\Lambda).
\]

Thus \(\Lambda\) is normal to the triangle wall and \(\tau\) is tangent to
it.  The exporter evaluates the full source relation packet on an exact
seven-by-seven interpolation grid and retains the six bidegrees

\[
1,\quad\Lambda,\quad\Lambda^2,
\quad\tau,\quad\Lambda\tau,\quad\Lambda^2\tau
\]

over

\[
A=\mathbf F_{32003}[\Lambda,\tau]/(\Lambda^3,\tau^2).
\]

No relation family, marked divisor, or source label is removed.

## Intrinsic obstruction calculation

Let \(R_{<3}\) be the relation module over
\(\mathbf F[\Lambda]/(\Lambda^3)\).  Tangential differentiation induces the
canonical syzygy map

\[
\Theta_\tau:
\ker R_{<3}
\longrightarrow
\operatorname{coker}R_{<3}.
\]

The rank of this map is the excess of the mixed relation rank over twice the
unmixed rank.  Exact sparse reduction gives

\[
\operatorname{rank}R_{<3}=18932,
\]

\[
\operatorname{rank}R_{<3,\tau}=37864
=2\cdot18932,
\]

and therefore

\[
\boxed{
\operatorname{rank}\Theta_\tau=0.
}
\]

Equivalently, the complete length-three cokernel has no first-order
tangential flatness obstruction in the tested \(X_1\) direction.

The optimized syzygy-derivative algorithm was independently checked against
the direct doubled-matrix construction at ambient relation degree six.  Both
give zero excess at normal lengths one, two, and three.  Degree eight was
also audited and has quadratic rank four, so it was correctly rejected as a
surrogate for the stabilized rank-seven object at degree ten.

## Exact boundary of the result

This calculation proves neither of the following:

1. a canonical tangential connection matrix on \(E_2(C)\);
2. compatibility in the independent \(X_2\) tangential direction.

It proves that the full length-three presentation supplies no obstruction to
first-order base change along the tested direction.  Passing from this
cokernel statement to a connection on the exact-valuation subquotient still
requires proving that the kernel/intersection filtration commutes with the
tangential deformation and then deriving, rather than choosing, the induced
seven-dimensional transport.

## Consequence

The rank-seven sector survives a stronger test than sampled constancy:

\[
\boxed{
\text{its ambient length-three Rees cokernel is tangentially unobstructed
to first order in one wall direction.}
}
\]

The next admissible tests are:

1. compute the independent \(X_2\) mixed jet;
2. test base change for the exact-valuation kernel/intersection diagram;
3. only then extract the induced transport on \(E_2\);
4. compare that transport with occurrence symmetry and the generic
   rank-seven algebraic kernel.

## Durable artifacts

- `research/nima/export_triangle_wall_dual_rows.py`;
- `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- `research/nima/triangle-wall-dual-relation-rank.json`.

## Sequence

- allocator claim: `seqclaim-421c7aa62c0d7509fbaa1bbe`.
