# Simple zero-state fibers do not force Real--reciprocal isotropy

## Tempting shortcut

Suppose a source-derived operator family `D_z` has a one-dimensional kernel at
every simple scalar zero. Reciprocal and Real symmetries give maps of the form

\[
U_F:\ker D_z\longrightarrow\ker D_{-z},
\qquad
U_C:\ker D_z\longrightarrow\ker D_{\overline z}.
\]

One might hope that uniqueness of the kernel state identifies these images and
forces `z=-conjugate(z)`.

## Typing obstruction

The two images live in different fibers. One-dimensionality says that each
target kernel is a line; it does not identify the line over `-z` with the line
over `conjugate(z)`. Even canonical generators in every fiber do not equate
their base parameters.

A comparison requires an additional cross-fiber transport or a common ambient
observer. Without it, the statement that both images are unique is merely
fiberwise uniqueness.

## Exact hostile family

Take positive `a,b` and the real even polynomial

\[
H_{a,b}(z)
=
\left((z-a)^2+b^2\right)
\left((z+a)^2+b^2\right).
\]

Its four roots are

\[
a+ib,
\quad
a-ib,
\quad
-a+ib,
\quad
-a-ib.
\]

They are simple when `a` and `b` are nonzero. Define the one-dimensional
operator family

\[
D_z:\mathbb C\longrightarrow\mathbb C,
\qquad
D_zv=H_{a,b}(z)v.
\]

At every root, `ker D_z` is exactly one-dimensional. Reality and reciprocal
evenness transport those kernel lines around the free four-point orbit, but no
root lies on the centered seam when `a` is nonzero.

The positive even two-cell transform supplies the stronger source-level
version of the same witness: its off-seam zeros are simple and still form free
quartets.

## Required comparison wall

To turn a simple kernel into seam confinement, one needs all three properties:

1. a source-derived transport from the reciprocal and Real target fibers into
   one common comparison fiber;
2. equality of the two transported zero-states, derived from the zero-domain
   boundary conditions;
3. faithfulness of the transported source features in the spectral parameter,
   so equality implies `-z=conjugate(z)`.

The first property types the comparison. The second contains the RH-bearing
force. The third prevents two different parameters from producing the same
state shadow.

## Categorical reading

Simplicity gives a line bundle over the divisor. Equivariance gives isomorphisms
between its fibers. Isotropy enhancement instead requires a descent datum that
identifies two different symmetry paths over each zero. A line bundle with
equivariant transport does not supply that 2-cell automatically.

## Disposition

The simple-kernel shortcut is closed. The next viable attack is to derive a
common comparison fiber from the full interval or boundary observer and test
whether the reciprocal and adjoint zero-state images coincide there. The
hostile quartet must remain separated by that observer.

