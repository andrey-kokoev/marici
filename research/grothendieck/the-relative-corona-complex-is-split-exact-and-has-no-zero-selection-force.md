# The Relative Corona Complex Is Split Exact and Has No Zero-Selection Force

## Two independently typed charts

Let \(V_+\) be the direct residue-tree boundary space, let \(V_-\) be the
reciprocal character-tree boundary space, and let

\[
U:V_+\longrightarrow V_-
\]

be the source-derived local Fourier identification. At each finite conductor
\(U\) is unitary.

Use the common boundary frame \(B=V_+\). The two restriction maps are

\[
r_+=I:V_+\longrightarrow B,
\qquad
r_-=U^{-1}:V_-\longrightarrow B.
\]

The alternating relative incidence is therefore

\[
\delta(v,w)=r_+v-r_-w=v-U^{-1}w.
\]

Its sign is supplied by the ordered two-chart cover, not by Fourier phase.

## Exact relative sequence

Define

\[
i(v)=(v,Uv).
\]

Then

\[
0\longrightarrow V_+
\xrightarrow{i}
V_+\oplus V_-
\xrightarrow{\delta}
B
\longrightarrow0
\]

is exact:

\[
\delta i=0,
\qquad
\ker\delta=\operatorname{im}i,
\]

and \(\delta\) is surjective because \(\delta(b,0)=b\).

The sequence is split. For example,

\[
j(b)=(b,0)
\]

is a right inverse of \(\delta\). Thus the relative corona complex is
contractible at every finite conductor and remains algebraically exact
whenever the Fourier identification extends continuously.

## Energy and boundary flux

Give both charts their source Hilbert metrics. For a compatible pair
\((v,Uv)\),

\[
\|(v,Uv)\|^2
=
\|v\|^2+\|Uv\|^2
=
2\|v\|^2.
\]

Thus bulk energy adds and is faithful.

The oriented boundary quadratic form is

\[
\mathcal J(v,w)
=
\|r_+v\|^2-\|r_-w\|^2.
\]

On the compatible diagonal,

\[
\mathcal J(v,Uv)=0.
\]

In particular, the equal-sign corona pair \((-f_0,-f_0)\) cancels under
relative incidence while retaining twice its bulk norm.

## Why this is not yet RH force

The cancellation is universal. It uses only that \(U\) is an isomorphism.
Every \(v\), for every admissible source, gives a compatible pair
\((v,Uv)\) with positive additive energy and zero relative boundary flux.

Therefore the split-exact relative complex:

- supplies the missing boundary orientation;
- removes the local common corona without deleting either state;
- does not select a spectral parameter;
- does not connect a scalar transform zero to a special compatible pair;
- cannot distinguish theta from a hostile self-dual source.

If one inserted this boundary cancellation directly into two Green identities
for arbitrary chart solutions, it would falsely force a seam condition for
every state. The missing premise is dynamic: the two chart solutions and
their forcing terms must themselves form a source-derived relative cycle.

## Remaining dynamic gate

Let \(\mathcal G_z^\pm\) denote the independently derived Green systems and
let \(\mathcal F_z^\pm\) denote their forcing states. The next theorem must
show, without using scalar zeros, that an admissible zero-state satisfies

\[
r_+\mathcal F_z^+
=
r_-\mathcal F_z^-,
\]

while the spectral bulk terms enter with the same positive orientation and
the boundary terms enter through \(\delta\).

This is not implied by

\[
r_+c_\infty^+=r_-c_\infty^-.
\]

Corona agreement is only the degree-zero boundary face. Dynamic forcing
agreement is the unconstructed top cell.

## Falsifier

Apply the relative construction to an arbitrary self-dual local source. If
the proposed zero-confinement argument uses no datum beyond the split exact
sequence, it applies equally to that hostile source and is invalid.

At finite conductor, compute

\[
R_z=r_+\mathcal F_z^+-r_-\mathcal F_z^-.
\]

Any nonzero \(R_z\) is the typed dynamic obstruction. Declaring it zero
because the terminal corona states agree confuses two distinct coherence
grades.
