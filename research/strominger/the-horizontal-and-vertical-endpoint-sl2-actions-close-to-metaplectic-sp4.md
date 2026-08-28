# The Horizontal and Vertical Endpoint sl2 Actions Close to Metaplectic sp4

## Two actions, two Casimirs

On

\[
\mathcal C=\mathbb C[u,v]_{\mathrm{even}},
\]

the rotational generators

\[
R_+=u\partial_v,
\qquad
R_-=v\partial_u,
\qquad
R_0=u\partial_u-v\partial_v
\]

preserve every fixed grade \(H_l=\operatorname{Sym}^{2l}\mathbb C^2\). Their
Casimir is \(4l(l+1)\).

Choosing the spinor axis \(u\) gives instead

\[
E_u=\frac{u^2}{2},
\qquad
F_u=-\frac{\partial_u^2}{2},
\qquad
H_u=u\partial_u+\frac12.
\]

This action moves across grades and has Casimir \(-3/4\). Thus the fixed-grade
no-intertwiner theorem and the graded metaplectic theorem concern different
\(\mathfrak{sl}_2\) subalgebras.

## Quadratic Weyl closure

Write \(x_1=u\), \(x_2=v\), and define

\[
E_{ij}=\frac12x_ix_j,
\qquad
F_{ij}=-\frac12\partial_i\partial_j,
\qquad
H_{ij}=x_i\partial_j+\frac12\delta_{ij}.
\]

There are three symmetric raising generators, three symmetric lowering
generators, and four degree-preserving generators. They are linearly
independent and satisfy

\[
[H_{ij},H_{kl}]
=
\delta_{jk}H_{il}-\delta_{il}H_{kj},
\]

\[
[H_{ij},E_{kl}]
=
\delta_{jk}E_{il}+\delta_{jl}E_{ik},
\]

\[
[H_{ij},F_{kl}]
=
-\delta_{ik}F_{jl}-\delta_{il}F_{jk},
\]

and

\[
[E_{ij},F_{kl}]
=
\frac14\left(
\delta_{jk}H_{il}+
\delta_{ik}H_{jl}+
\delta_{jl}H_{ik}+
\delta_{il}H_{jk}
\right).
\]

The raising generators commute among themselves, as do the lowering
generators. These are the oscillator relations of \(\mathfrak{sp}_4\).

## Closure theorem

All source-axis metaplectic triples on the endpoint generate the
ten-dimensional metaplectic representation of \(\mathfrak{sp}_4\). The
horizontal rotational \(\mathfrak{sl}_2\) sits in its degree-preserving
\(\mathfrak{gl}_2\) block. Comparing two independent vertical axes generates
the mixed operators, so the transverse spinor label ceases to be a spectator.

The larger algebra resolves the Casimir mismatch without identifying the two
modules. Horizontal and vertical \(\mathfrak{sl}_2\) actions are distinct
restrictions of one quadratic Weyl algebra.

## Prediction

A one-axis source sees one metaplectic chain plus spectator multiplicity. Any
source capable of coherently comparing two independent axes must expose mixed
degree-preserving controls. This is a new control prediction obtained without
adding another carrier.

## Scope

This is an algebraic operator theorem. It does not identify theta seam currents
or completion data with endpoint boundary data. A cross-sector bridge still
requires a filtered correspondence respecting both actions and their supports.

## Evidence replay

The checker verifies the commutator families, both embedded
\(\mathfrak{sl}_2\) relations, their distinct Casimirs, and the ten-generator
count on monomials through total degree twelve.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/endpoint_sp4_closure_checks.py
```

Machine-readable results are written to
`research/strominger/results/endpoint_sp4_closure_checks.json`.

