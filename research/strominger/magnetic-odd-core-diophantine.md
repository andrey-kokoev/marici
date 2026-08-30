# The odd collision core has one integral zero

The last global kernel-classification lemma is

\[
P(g,d)=0,
\qquad
g\ge2,
\qquad
d\ge3\text{ odd},
\]

for the polynomial derived in `magnetic-low-grade-core.md`.

At grade two,

\[
P(2,d)=-36(d-5),
\]

so `d=5` is the unique solution.

For `g>=3`, the leading coefficient in `d` is

\[
(g+3)(g-2)>0,
\]

and the discriminant is

\[
\Delta(g)=
g^6+4g^5-22g^4-24g^3+353g^2+148g-60.
\]

Set

\[
S(g)=g^3+2g^2-13g+14.
\]

The lower square gap is

\[
\Delta(g)-S(g)^2=128(g^2+4g-2)>0.
\]

For `g=67+x`, the upper gap is

\[
(S(g)+1)^2-\Delta(g)
=2x^3+278x^2+9780x+9129>0.
\]

Therefore, for every `g>=67`, the discriminant lies strictly between two
consecutive integer squares and cannot be square.

The finite interval `3<=g<=66` has exactly one square discriminant:

\[
g=6,
\qquad
\Delta(6)=240^2.
\]

But the corresponding roots are

\[
d=\frac{17}{3},
\qquad
d=\frac{37}{3},
\]

so neither is integral.  Hence

\[
P(g,d)=0,quad g\ge2,quad d\in\mathbb Z
\Longleftrightarrow
(g,d)=(2,5).
\]

Since `q=g+d`, the unique admissible odd-core zero is

\[
(g,q)=(2,7).
\]

This closes the final Diophantine gap in the arbitrary-grade initialization
classification.