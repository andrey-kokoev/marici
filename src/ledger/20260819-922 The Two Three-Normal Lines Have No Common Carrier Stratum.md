# 922 — The Two Three-Normal Lines Have No Common Carrier Stratum

## Question left by Entry 921

Entry 921 compares the diagonal and off-diagonal coefficient lines in ambient kinematics and finds two independent directions. It leaves open whether the frozen marked-incidence carrier supplies a differential between them.

That question must be answered before constructing any mixed cone.

## Frozen flags

The diagonal flag is

\[
F_x=(s_{14},s_{23},s_{235}),
\]

and the off-diagonal flag is

\[
F_y=(s_{14},s_{35},s_{235}).
\]

Write their cut subsets as

\[
a=\{1,4\},
\qquad
x=\{2,3\},
\qquad
y=\{3,5\},
\qquad
q=\{2,3,5\}.
\]

Each flag is separately compatible:

\[
x\subset q,
\qquad
y\subset q,
\qquad
a\cap q=\varnothing.
\]

## Incompatibility of the union

The differing cuts obey

\[
x\cap y=\{3\},
\]

but

\[
x\not\subset y,
\qquad
y\not\subset x.
\]

They are neither nested nor disjoint. Hence

\[
\boxed{F_x\cup F_y\text{ is not a compatible nested set}.}
\]

The ambient kinematic locus obtained by setting all corresponding Mandelstam variables to zero is therefore not a stratum of the frozen marked-incidence carrier.

## Incidence-degree audit

Both (F_x) and (F_y) are length-three maximal flags. A cellular or nested-set boundary changes flag length by one. It cannot directly connect two distinct maximal generators of equal degree:

\[
|F_y|-|F_x|=0.
\]

Thus the frozen incidence differential supplies no arrow

\[
\mathcal L_x^{(1)}longrightarrow\mathcal L_y^{\rm Rees}
\]

or its reverse.

## Narrow conclusion

The comparison proposed after Entry 920 was overtyped. The two coefficient lines may be evaluated on an ambient algebraic intersection, as in Entry 921, but that intersection is not a common carrier face:

\[
\boxed{
\text{ambient common zero locus}
\neq
\text{marked-incidence stratum}.
}
\]

Consequently the surviving typed object at this level is the pair of occurrence-labelled coefficient lines on separate compatible flags. There is no frozen carrier differential between them, and no mixed cone is authorized.

This is not evidence for a missing carrier cell. Adding the incompatible union as a new cell would violate the predeclared nested-set compatibility rule.

## Next falsifier

Move from a nonexistent direct incidence map to the first legitimate comparison: determine whether both lines restrict to a common lower-dimensional deletion or contraction object through two separately typed maps. A nontrivial comparison may exist only as a span

\[
\mathcal L_x\longrightarrow\mathcal L_0\longleftarrow\mathcal L_y
\]

or the variance-correct dual span, with (mathcal L_0) derived independently from the frozen deletion–restriction calculus.
