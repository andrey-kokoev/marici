# Reflection gives the exact H1 seam transpose with value and flux traces

## Reflected seam correspondence

For a cut length `L>0`, define

\[
R_L:H^1(0,L)\longrightarrow H^1(-L,0),
\qquad
(R_Lu)(q)=u(-q).
\]

Change of variables gives

\[
\|R_Lu\|_{L^2(-L,0)}=\|u\|_{L^2(0,L)}.
\]

Since

\[
(R_Lu)'(q)=-u'(-q),
\]

the derivative norm is also preserved. Hence `R_L` is unitary for the full
`H1` graph norm.

## Endpoint values

Reflection exchanges the two endpoint values:

\[
(R_Lu)(0)=u(0),
\qquad
(R_Lu)(-L)=u(L).
\]

Both traces are continuous on their `H1` spaces.

## Oriented flux

Use outward-normal derivatives. On `(0,L)` they are

\[
\partial_nu(0)=-u'(0),
\qquad
\partial_nu(L)=u'(L).
\]

On `(-L,0)`, with `v=R_Lu`, they are

\[
\partial_nv(0)=v'(0)=-u'(0),
\]

and

\[
\partial_nv(-L)=-v'(-L)=u'(L).
\]

Thus the reflected seam preserves both value and outward-flux data after the
source-derived endpoint exchange. Coordinate derivative changes sign;
geometric normal flux does not.

## Transpose compatibility

For a seam distribution `lambda` on `(0,L)`, define conjugate-reflected
transport on the dual by

\[
(\mathfrak J_L\lambda)(g)
=
\overline{\lambda(\overline{R_L^{-1}g})}.
\]

If the completed theta forcing is real and even, its restrictions obey

\[
R_L(f|_{(0,L)})=f|_{(-L,0)}.
\]

Consequently

\[
B_f^\times(\mathfrak J_L\lambda)
=
\overline{B_f^\times(\lambda)}.
\]

This is the continuum seam analogue of the arithmetic grade identity. Unlike
the arithmetic packet, the full interval test space has no support gap inside
the seam.

## Concatenation

Reflected intervals concatenate in reverse order. This is the expected
contravariance:

```text
direct cut:       [0,L] followed by [L,L+M]
reflected return: [-L-M,-L] followed by [-L,0]
```

The common interface value and outward flux agree under reflection, so the
one-interval transpose is compatible with prime-window concatenation.

## Boundary status and provenance correction

We now have source-derived transpose compatibility on:

- primitive arithmetic distributions;
- square arithmetic distributions;
- connected-tail distributions;
- the complete continuum seam interval, including value and flux traces.

The archimedean endpoint/gamma component was already matched in
[Archimedean--Poisson reciprocity closes without RH force](archimedean-Poisson-reciprocity-closes-without-RH-force.md):
the gamma line inverts and the four Tate--Poisson channels swap pairwise.
Therefore, after adjoining that previously established result, the full
boundary transpose correspondence is matched across arithmetic, seam, and
archimedean grades.

The remaining problem is not another boundary grade. It is whether this
boundary transpose is realized as the lower bulk incidence of one completed
dynamical operator.

## Scope

This proves the reflected `H1` seam correspondence and its trace behavior. It
does not prove that the assembled global rigged block is selfadjoint, that its
characteristic section is the completed theta transform, or that its
zero-state boundary flux vanishes.
