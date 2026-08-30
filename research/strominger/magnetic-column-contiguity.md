# Actual magnetic columns obey an order-four contiguous law

Fix a reflected branch parameter `s` and set

\[
m=1-g+s-a.
\]

Let `B_{g,a,s}(x)` be the transported magnetic path polynomial.  Its exponential
grade-generating function has the closed form

\[
\boxed{
\mathcal B_{a,s}(t,x)
=(1+t)^{-a-1}(1-xt)^{a-5}N_{a,s}(t,x),
}
\]

where `N` is quadratic in `t`:

\[
\begin{aligned}
N={}&[-sx^2-sx-5x^2-x]t^2\\
&+[2ax^2+2ax-sx^2+s-5x^2+1]t\\
&-ax-a+sx+s+x+1.
\end{aligned}
\]

Under pole-depth shift,

\[
N_{a+2,s}-N_{a,s}=2(1+x)(2tx-1).
\]

Combining this with the square source character gives

\[
(1+t)^2N_{a,s}\,\mathcal B_{a+2,s}
=(1-xt)^2N_{a+2,s}\,\mathcal B_{a,s}.
\]

Both polynomial multipliers have degree four in `t`.  Coefficient extraction
therefore gives an exact recurrence involving only

\[
B_g,B_{g-1},B_{g-2},B_{g-3},B_{g-4}.
\]

This is the desired cutoff-independent elimination identity for the actual
magnetic columns.  The source family had order two; applying the magnetic
Euler operator adds the quadratic numerator and raises the transported order
to four.

The large sparse determinants are consequently presentations of a fixed
five-grade local system.  What remains is to take the exterior character of
this recurrence after imposing the two reflected branches `s=+q,-q`.  Its
branch determinant should be the observed even/odd scalar multiplier.

The checker verifies the generating function and recurrence formally through
grade 15 and on 1,386 exact reflected-branch cases.
