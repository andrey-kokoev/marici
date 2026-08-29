# Prime-power cut atoms form a horizontal section of the moving-seam bundle

## Why one fixed fiber is wrong

For a scale \(a\ge0\), the exact cut atom consists of

\[
g_a(t)=\Phi(a+t),\qquad t\ge0,
\]

and

\[
h_a(t)=\Phi(a-t),\qquad 0\le t\le a.
\]

The seam component naturally lives on an interval whose length depends on \(a\). Therefore prime-power atoms at different values of \(a=k\log p\) do not begin in one identical cut geometry.

Embedding every seam interval into \(L^2(0,\infty)\) is useful for synthesis, but it hides the moving boundary needed for naturality.

## Cut fibers and reassembly

Define the fiber

\[
E_a
=
L^2(a,\infty)
\oplus
L^2(0,a).
\]

Equivalently, use shifted tail and reversed seam coordinates. Define the reassembly map

\[
R_a:E_a\longrightarrow L^2(0,\infty)
\]

by placing the seam component on \([0,a]\) and the tail component on \([a,\infty)\).

In shifted coordinates,

\[
(R_a(g,h))(x)
=
\begin{cases}
h(a-x),&0\le x\le a,\\
g(x-a),&x\ge a.
\end{cases}
\]

This is unitary. For the source cut atom

\[
u_a=(g_a,h_a),
\]

one has

\[
R_au_a=\Phi.
\]

Every cut is therefore a different presentation of the same reassembled source vector.

## Moving-seam transport

For \(a,b\ge0\), define

\[
T_{b\leftarrow a}
=
R_b^{-1}R_a:E_a\longrightarrow E_b.
\]

These maps are unitary and obey

\[
T_{c\leftarrow b}T_{b\leftarrow a}
=
T_{c\leftarrow a},
\qquad
T_{a\leftarrow a}=1.
\]

Moreover,

\[
T_{b\leftarrow a}u_a=u_b.
\]

Thus the cut atoms form a horizontal section of a Hilbert bundle over the scale half-line.

This is the exact coherence law between tail and seam presentations. It is stronger than equality of their total norms and weaker than reconstructing the seam as a function of the tail.

## Arithmetic restriction

Prime-power incidence restricts the bundle to the discrete source scales

\[
a_{p,k}=k\log p.
\]

Adams transport sends

\[
a_{p,k}\longmapsto a_{p,rk}=r\,a_{p,k}.
\]

Its analytic lift is the moving-seam transport

\[
T_{r a\leftarrow a}.
\]

The first grade-wise naturality condition is

\[
T_{r a\leftarrow a}\,\mathcal I(p,k)
=
\mathcal I\!\left(\psi^r(p,k)\right),
\]

before applying the changed Euler coefficient. On unweighted source atoms this condition holds exactly.

The Euler weights do not remain unchanged:

\[
\frac1k p^{-k/2}
\longmapsto
\frac1{rk}p^{-rk/2}.
\]

Hence full weighted naturality requires a coefficient transport in addition to geometric moving-seam transport. Geometry alone commutes; the weighted Fock incidence needs the declared Adams coefficient law.

## Fourier–Poisson transport

Let \(F\) be the source-authorized Fourier–Poisson operator on the reassembled source space. Its action in the cut fiber is

\[
F_a=R_a^{-1}FR_a.
\]

For different cuts,

\[
F_bT_{b\leftarrow a}
=
T_{b\leftarrow a}F_a.
\]

This naturality is forced by reassembly and the source Fourier operator. If \(\Phi\) is an eigenvector of \(F\), every cut atom is the corresponding eigenvector of \(F_a\).

The important qualification is that \(F_a\) varies with the cut. There is no source basis for replacing the family by one fixed operator on one fixed tail–seam presentation.

## What is proved

- the analytic cut fibers;
- unitary seam motion;
- exact cocycle coherence;
- horizontality of source atoms;
- geometric Adams naturality;
- fiberwise Fourier–Poisson naturality.

## What remains

- the coefficient part of Adams naturality;
- type-fiber transport for primitive, square, and connected grades;
- endpoint evaluation under seam motion;
- archimedean attachment;
- continuity of the weighted sum of fiberwise operators;
- the doubled Green identity on the bundle.

## Falsifiers

1. A fixed-fiber Fourier operator that ignores \(a\)-dependence.
2. An Adams square that transports the cut but not the Euler coefficient.
3. A claimed seam reconstruction inferred from horizontal transport.
4. A scalar naturality test performed only after summing grades.
5. Failure of the cocycle law for any three cuts.

## Verdict

The arithmetic incidence is geometrically natural after it is typed as a section of the moving-seam Hilbert bundle. The remaining obstruction is no longer the analytic Fourier–Poisson square; it is the weighted and type-fiber lift of Adams transport, followed by endpoint and archimedean attachment.
