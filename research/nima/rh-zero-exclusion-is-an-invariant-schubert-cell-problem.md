# RH zero exclusion is an invariant Schubert-cell problem

## Relative geometry of the fixed observer

Let a regular operator connection transport a nonzero state `v(z)` in a
two-component splitting

\[
H=V\oplus W.
\]

Let the fixed Evans observer select the `V` coordinate. Write

\[
v(z)=
\begin{pmatrix}
x(z)\\y(z)
\end{pmatrix},
\qquad
v'(z)=
\begin{pmatrix}
\alpha&\beta\\
\gamma&\delta
\end{pmatrix}
v(z).
\]

The Evans readout is `x(z)`. Its nonvanishing defines the Schubert big cell in
the projective state space.

Inside that cell, the graph coordinate

\[
r(z)=\frac{y(z)}{x(z)}
\]

satisfies the Riccati equation

\[
r'=\gamma+(\delta-\alpha)r-\beta r^2,
\]

while

\[
x'=(\alpha+\beta r)x.
\]

An Evans zero is therefore a projective chart exit: `r` reaches infinity even
though the full transported state and full operator frame remain regular.

## Exact unsafe flow

For

\[
A=
\begin{pmatrix}
-1&-1\\
1&1
\end{pmatrix},
\qquad
v(0)=e_1,
\]

the solution is

\[
v(z)=(1-z,z)^T.
\]

Hence

\[
r(z)=\frac{z}{1-z},
\qquad
r'=(1+r)^2.
\]

The projective coordinate blows up at `z=1`, exactly where the fixed overlap
vanishes. The connection itself remains entire and its transport determinant
remains one.

## Exact safe triangular flow

Remove the block that feeds the hidden coordinate back into the observed
coordinate:

\[
A_0=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}.
\]

Then

\[
U_0(z)=I+zA_0,
\qquad
U_0(z)e_1=(1,z)^T.
\]

The fixed overlap is identically one and `r(z)=z` has no finite pole.

The block condition `beta=0` is equivalent to contragredient invariance of the
fixed observer line:

\[
qA=\alpha q.
\]

It is a sufficient source law for big-cell invariance, but it is probably too
strong for the theta/Tate system. It would prevent all hidden-to-observed
feedback rather than controlling it.

## More flexible target

The general target is a source-derived invariant domain for the Riccati flow.
Such a domain could be:

- a disk, half-plane, or sector preserved by the projective generator;
- a contractive graph-transform region;
- a monotone Lagrangian chart;
- a total-positive Grassmann cell;
- a dissipative or passive system domain;
- a nonlinear constructor orbit known to avoid the Schubert divisor.

Any one of these would turn zero exclusion into forward invariance rather than
scalar positivity.

## Fifth-tower interpretation

The first towers construct the two sectors, their transports, and their
observer comparisons. The next tower must control their relative position in
the Grassmannian. Its operative datum is not the determinant of the full frame
but the source-selected Schubert cell defined by the fixed observer.

A source-authorized two-cell family would have RH force if its infinitesimal
generator made that cell forward invariant throughout each open half-plane.
The seam may remain the boundary where the two opposite invariant charts meet.

## DPC

For the actual theta/Tate operator connection:

1. derive the fixed-observer splitting before examining zeros;
2. compute all four generator blocks `alpha`, `beta`, `gamma`, and `delta`;
3. derive the projective Riccati or graph-transform flow;
4. identify a source-defined invariant domain containing the normalized state;
5. prove the domain excludes the Schubert divisor;
6. prove invariance survives the primitive, square, seam, archimedean, and
   restricted-product completion channels;
7. test the polynomial unsafe flow and signed prime perturbations.

Reject:

- full-frame invertibility without projective control;
- determinant nonvanishing without Pluecker-coordinate control;
- a chart chosen using the known zero set;
- a Riccati coefficient obtained by dividing by the Evans readout;
- finite-cutoff invariant regions whose distance to the divisor tends to zero.

## Verdict

The correct geometric target is now exact: source-derived invariance of the
Evans Schubert big cell. This is strictly stronger than operator
horizontality, strictly different from scalar positivity, and directly
falsifiable through the projective generator blocks.

