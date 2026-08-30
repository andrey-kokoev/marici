# The Quarter-Density Makes the Dilation Generator Skew but Restores the Infinite Raising Wall

## Transported logarithmic generator

Use the dilation coordinate and quarter-density from the positive Jordan
packet:

\[
y=e^{2u}-1,
\qquad
h(u)=(1+y)^{1/4}\psi(y).
\]

Direct differentiation gives

\[
(\partial_u+z)h
=(1+y)^{1/4}
\left(2(1+y)\partial_y+\frac12+z\right)\psi.
\]

Thus the source-native transported generator is

\[
A=2(1+y)\partial_y+\frac12.
\]

It is not ordinary differentiation in the Jordan coordinate.

## Natural measure and exact Green boundary

The original half-line norm transports as

\[
\int_0^\infty|h(u)|^2\,du
=
\frac12\int_0^\infty
|\psi(y)|^2(1+y)^{-1/2}\,dy.
\]

Let

\[
d\nu(y)=\frac12(1+y)^{-1/2}dy.
\]

Because

\[
2(1+y)\frac{d\nu}{dy}=(1+y)^{1/2},
\]

integration by parts yields

\[
2\Re\langle A\psi,\psi\rangle_{\nu}
=
\left[(1+y)^{1/2}|\psi(y)|^2\right]_{0}^{\infty}.
\]

For a decaying state this is `-|psi(0)|^2`. Hence the quarter-density is
exactly the connection that makes dilation transport skew modulo the physical
seam boundary. This part of the construction is canonical and successful.

## The three-state closure fails for the physical generator

For

\[
e_j(y)=y^je^{-\lambda y},
\]

the transported generator acts by

\[
A e_j
=
2j e_{j-1}
+\left(2j-2\lambda+\frac12\right)e_j
-2\lambda e_{j+1}.
\]

The last term is an outward raising arrow. On a polynomial packet of top
degree `N` with top coefficient `c_N`, its uncancelled boundary grade is

\[
-2\lambda c_N e_{N+1}.
\]

Since every theta label has `lambda=pi n^2>0` and a nonzero quadratic top
coefficient, the positive length-three packet immediately produces a fourth
grade. Adding that grade produces a fifth, and so on. No nonzero finite
polynomial-exponential module is invariant under the actual logarithmic
transport.

The earlier length-three closure under ordinary `partial_y` was correct but
was not closed under the physical generator. The coordinate rotation moved
the infinite raising wall; it did not remove it.

## Interpretation in the multi-tower language

The three positive coefficient states form a preparation tower. The
transported Green generator supplies a distinct control tower whose outward
incidence is

\[
e_N\longrightarrow e_{N+1}.
\]

The missing fourth wall is therefore real, but it is not terminal. It is the
first cell of an infinite control completion. Any finite closure that discards
the top arrow manufactures an artificial invariant packet.

The durable object is the completed polynomial-exponential Fock module for
each arithmetic label, equipped with:

- the positive initial three-state preparation;
- the tridiagonal dilation generator;
- the seam evaluation boundary;
- the full outward-grade completion.

## Next gate

The infinite raising wall does not by itself kill the route. The generator is
skew modulo one exact seam boundary, so the full completed module may still
have a closed Green identity. The next question is whether the natural
weighted Fock completion makes the tridiagonal operator closed and whether
the initial theta packet is an analytic vector for it.

The hostile falsifier is escape of the top-grade current under finite
truncation. If its boundary norm fails to vanish as `N` tends to infinity,
the finite packet Green identities do not converge to the completed one.

## Result

The quarter-density exactly repairs the Green adjointness, but the physical
dilation generator destroys every finite Jordan closure through a canonical
raising arrow. The theta orientation problem therefore requires an infinite
completed control tower even though its initial source packet has only three
positive grades.

