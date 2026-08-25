# Naturality under source enlargement

Fix a grade `g` and the full target.  Let the object poset consist of pairs

\[
X=(A,I),
\]

where `A` is a finite admitted depth set and `I` a finite Laurent interval.
There is a morphism

\[
j_{X,X'}:X\hookrightarrow X'
\]

exactly when `A subset A'` and `I subset I'`; it is the labelled monomial
inclusion.

## Readout naturality

Every old sparse column is unchanged under enlargement, so

\[
E_{g,X'}j_{X,X'}=E_{g,X},
\qquad
M_{g,X'}j_{X,X'}=M_{g,X}.
\]

Consequently

\[
j_{X,X'}(\ker M_{g,X})
=\ker M_{g,X'}\cap j_{X,X'}(S_X),
\]

and similarly for `E`.  Enlargement can reveal a newly complete named support,
but it cannot alter an old relation or create a relation supported entirely on
old columns.

Fold transport, the mixed-derivative packet, and the fixed character transform
obey the same square.  Thus the half-Hadamard reconstruction is a natural
isomorphism, not a basis choice made separately at each cutoff.

## Exactness and cohomology naturality

Rational exactness is intrinsic to the realized rational one-form.  Hence

\[
j_{X,X'}(K_{g,X}^{rat})
=K_{g,X'}^{rat}\cap j_{X,X'}(K_{g,X}^M).
\]

There is an induced map

\[
H_{g,X}^{rat}\longrightarrow H_{g,X'}^{rat}.
\]

Before a positive tower is visible, the source quotient is zero.  Once one is
visible, every later nonzero quotient identifies canonically with
`Q*[eta]`, and all enlargement maps between nonzero quotients are the identity
on `[eta]`.

For integral residue images, if `T subset T'`, then

\[
d_{g,T'}\mid d_{g,T},
\]

and the natural inclusion is

\[
d_{g,T}\mathbb Z\eta
\hookrightarrow d_{g,T'}\mathbb Z\eta.
\]

In normalized free generators this map is multiplication by
`d_{g,T}/d_{g,T'}`.  The rational map becomes the identity after tensoring
with `Q`.

## Why deletion is not a kernel morphism

The coordinate projection

\[
p:S_{X'}\to S_X
\]

left inverse to `j` generally does not send `ker M_{X'}` into `ker M_X`.
Deleting one vertex of a circuit destroys the relation.  At grade two,

\[
1-\bar z^{-2}\in\ker M_2,
\]

but projection onto either single supported monomial is nonzero under `M_2`.

Therefore cutoff contraction is represented by choosing a smaller source and
restricting the operator, not by projecting already-classified kernel vectors.
This directionality prevents partial circuits from being mistaken for
boundary classes.

## Natural port completion

Let `P,Q` be fixed sheet covectors with `det(P,Q)!=0`.  For every source object,

\[
O_{P,Q}=(P,Q)J_g
\]

is a split monomorphism, and its inverse commutes with source inclusions.  For
the source-authorized characters `P=E`, `Q=M`, the inverse is the fixed
half-Hadamard matrix.

Changing the port covectors with the cutoff would define a different observer
family.  Rank alone would not supply a natural reconstruction certificate.
