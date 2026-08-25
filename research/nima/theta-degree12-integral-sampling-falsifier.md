# Degree-twelve integral-sampling falsifier

Put (t=\pi x^2).  The Fourier-fixed, vacuum-null Gaussian-polynomial space
through degree twelve has basis

\[
F=4t^2-6t,
\]

\[
Q=t^4-7t^3+\frac{105}{8}t,
\]

\[
R=t^6-\frac{33}{2}t^5+\frac{3465}{8}t^3-
\frac{31185}{32}t.
\]

Consider

\[
P=F+\frac{13}{20}Q+\frac1{160}R.
\]

It is exactly Fourier-fixed and (P(0)=0).  Moreover,

\[
P(t)=\frac{t}{5120}S(t),
\]

where

\[
S(t)=32t^5-528t^4+3328t^3-9436t^2+20480t-18225.
\]

An exact Sturm calculation gives no real root for (S').  Its leading
coefficient is positive and (S(3)=13155), hence

\[
P(\pi n^2)>0
\qquad(n\in\mathbb Z\setminus\{0\}).
\]

The Mellin window still contains the forced factor (r(2r-1)), but its
remaining factor, with (y=(r-1/4)^2), is

\[
H(y)=\frac{256y^2+5920y+87325}{81920}.
\]

Its discriminant is

\[
5920^2-4\cdot256\cdot87325=-54{,}374{,}400<0.
\]

Thus its (y)-roots are nonreal.  Their square roots have nonzero real part,
so the corresponding Mellin-window zeros do not lie on
\(\operatorname{Re}s=1/2\).

Therefore

\[
\text{Fourier self-duality}
+\text{vacuum nullity}
+\text{positive integral samples}
\not\Rightarrow
\text{critical-line Mellin orientation}.
\]

Grothendieck's sampling and Poisson-positivity theorem remains valid.  What
fails is its promotion to an orientation mechanism.  Any surviving theorem
must use additional source information, such as the minimal differential
order, the moving-endpoint cocycle, or the complete labelled Poisson
correspondence.
