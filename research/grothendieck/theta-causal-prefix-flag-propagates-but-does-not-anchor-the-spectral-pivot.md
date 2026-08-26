# Theta causal-prefix flag propagates but does not anchor the spectral pivot

## Bounded question

Can a moving covector assembled from the causal source prefix cancel the theta
forcing residual and prove nonvanishing?

## Tail and prefix

Fix the spectral parameter \(z\). Let

\[
G_q=-zG-f(q)c,
\qquad
c_q=0,
\]

with tail boundary condition giving

\[
G(q,z)
=
e^{-zq}
\int_q^\infty e^{zr}f(r)\,dr.
\]

Define the causal prefix coordinate

\[
d(q,z)
=
e^{-zq}
\int_0^q e^{zr}f(r)\,dr.
\]

It is source-derived before zero inspection and satisfies

\[
d_q+zd=f,
\qquad
d(0,z)=0.
\]

## Exact moving flag

For

\[
X=
\begin{pmatrix}
G\\
c
\end{pmatrix},
\qquad
K_z=
\begin{pmatrix}
-z&-f\\
0&0
\end{pmatrix},
\]

take the moving covector

\[
\ell(q,z)
=
\begin{pmatrix}
1&d(q,z)
\end{pmatrix}.
\]

Then

\[
\ell_q+\ell K_z=-z\ell.
\]

Thus the source prefix cancels the off-parabolic forcing residual exactly. The
flag is local in the causal scale direction and does not require division by
the theta transform.

## What the invariant pivot is

The associated readout is

\[
Y(q,z)=G(q,z)+d(q,z)c.
\]

For \(c=1\), prefix and tail reconstruct the complete source integral:

\[
Y(q,z)
=
e^{-zq}
\int_0^\infty e^{zr}f(r)\,dr
=
e^{-zq}F(z).
\]

The moving flag therefore propagates the theta scalar multiplicatively:

\[
Y_q=-zY.
\]

## Missing anchor

If \(F(z)\ne0\), the pivot remains nonzero for every \(q\). But if

\[
F(z)=0,
\]

then

\[
Y(q,z)=0
\]

for every \(q\), while the separate prefix and tail states may both be
nonzero. The full scale trajectory lies inside the moving hyperplane from the
start.

Therefore exact parabolic transport does not provide a known nonzero anchor.
It preserves the zero or nonzero status already carried by \(F(z)\).

## Parameter-category correction

The invariant-flag evolution acts in the logarithmic scale variable \(q\).
The RH incidence question concerns variation in the spectral parameter \(z\).
Confinement in one parameter does not imply confinement in the other.

The identity

\[
Y(q,z)=e^{-zq}F(z)
\]

makes the distinction exact:

- \(q\)-transport is multiplicative and zero-preserving;
- the unknown divisor is entirely in the initial spectral section \(F(z)\);
- no \(q\)-flow argument can remove a zero already present at fixed \(z\).

## What would add force

A successful flag argument must supply one of:

1. a source-derived nonzero boundary value of \(Y\) at every off-seam \(z\);
2. an invariant or monotone connection in the \(z\)-direction;
3. a two-parameter flatness law coupling \(q\)-transport to spectral
   deformation;
4. a reciprocal boundary condition incompatible with \(Y\equiv0\) off the
   seam.

The first is the target conclusion unless obtained from independent boundary
data. The second and third require a new source-derived spectral connection.

## Relation to the seam flag

The antisymmetric reciprocal flag of packet 252 is still informative: it
explains why a common relative coordinate exists on the critical seam. The
causal-prefix flag exists separately at fixed \(z\) in a one-sided sector.
Neither supplies the missing spectral anchor.

Together they separate two achievements:

- scale coherence has been derived;
- spectral zero confinement has not.

## Result

The causal prefix gives an exact source-derived moving invariant flag and
absorbs the forcing residual. But its pivot is simply
\(e^{-zq}F(z)\). It propagates the theta divisor rather than excluding it.

This closes the naive moving-flag proof and identifies the next genuine
object: a source-derived connection or conservation law in spectral
parameter space, coupled nontrivially to the scale flow.

## Sharp falsifier

Set \(F(z_0)=0\) while retaining nonzero prefix and tail pieces. Then

\[
G(q,z_0)=-d(q,z_0),
\qquad
Y(q,z_0)=0
\]

for all \(q\). Any proposed scale-flow proof that accepts this exact solution
cannot exclude the spectral zero.
