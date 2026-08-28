# The spectral planes have a 2-primary integral gluing

## Question

Does the rational parabolic--hyperbolic factorization split the faithful
response lattice integrally, and does its gluing explain the observed
three-adic decoration jet?

## Rational factorization

Let

\[
p(x)=(x-1)^2,
\qquad
q(x)=x^2-147458x+1.
\]

The rational response space is the direct sum

\[
\ker p(C)\oplus\ker q(C).
\]

Both summands have dimension two.

## Saturation correction

Raw row-reduction produced integer bases with Plücker content 8 in both
planes. Those bases were not saturated. Using them directly gives the false
index

\[
65536.
\]

After saturation, exact bases are:

\[
L_p=
\left\langle
(1,-23,8,0),
(1,1,1,1)
\right\rangle,
\]

and

\[
L_q=
\left\langle
(31,55,24,0),
(10,18,9,1)
\right\rangle.
\]

Each has Plücker content one and is therefore primitive in its rational plane.

## Actual integral gluing

Their direct sum has index

\[
[\mathbb Z^4:L_p\oplus L_q]=1024=2^{10}.
\]

Thus the rational spectral splitting fails integrally, but its actual gluing
is purely 2-primary.

## Resultant versus realized gluing

The polynomial resultant is

\[
\operatorname{Res}(p,q)
=q(1)^2
=147456^2
=2^{28}3^4.
\]

The resultant bounds the possible torsion primes. It does not assert that
every permitted prime occurs in the actual lattice quotient.

Here the 3-primary allowance is unrealized:

\[
v_3([\mathbb Z^4:L_p\oplus L_q])=0.
\]

Therefore the previously observed three-adic source jet does not arise from
the integral gluing of the parabolic and hyperbolic spectral planes.

## Explanatory consequence

We have separated two local arithmetic mechanisms:

- 2-primary spectral gluing between rational response planes;
- 3-adic periodicity in the content of the nested magnetic readout.

Their common appearance in the unsaturated resultant was misleading. The
three-adic effect must enter downstream through the nonlinear commutator
readout or Smith saturation, not through the linear spectral decomposition of
the neutral constructor.

## Oddball retained

The failed first gate is essential evidence. A nonsaturated rational-nullspace
basis inflated the index by

\[
8\cdot8=64.
\]

This is precisely the sort of presentation defect that can manufacture false
prime support. Saturation is required before any integral gluing claim.

## Theorem status

The kernel equations, Plücker contents, saturated bases, determinant index,
resultant, and prime valuations are exact. Eight of eight corrected gates pass.

## Claim boundary

This theorem excludes spectral-plane gluing as the source of the three-adic
periodicity. It does not yet identify the downstream nonlinear operation that
creates that periodicity.
