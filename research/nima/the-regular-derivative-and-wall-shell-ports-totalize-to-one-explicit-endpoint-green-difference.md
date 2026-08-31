# The regular derivative and wall shell ports totalize to one explicit endpoint Green difference

## Question

Can the regular derivative and wall terms in the prime-shell residual be
computed as one source expression rather than treated as two unknown bulk
pairings?

## Claim boundary

Yes on the declared first-order completion graph. The closed Green identity
shows that the regular derivative and retained wall jump totalize exactly to an
endpoint difference, with no interior remainder. This computes their combined
shell contribution but does not determine cancellation with the ordinary,
reciprocal, or linking ports.

## First-order pair

Use the source factors

\[
 A_+=\partial_q+\frac12,
 \qquad
 A_-=\partial_q-\frac12.
\]

On the common closed graph domain,

\[
 \langle A_+f,g\rangle
 +\langle f,A_-g\rangle
 =\left[f\overline g\right]_{a}^{b}
\]

for a shell interval \([a,b]\). Continuous graph traces justify passage from
the rapid core to the closed domain.

The half-density terms cancel in the interior. The discontinuity of a cut
function is retained in the wall coordinate, so no delta distribution is
misidentified as an \(L^2\) derivative.

## Consecutive-prime shell

For consecutive primes \(p<q\), set

\[
 a=\log p,
 \qquad
 b=\log q.
\]

Let \(f_{p,q}\) be the theta profile on this shell with its source cut/wall
extension. Pair it with the Evans history \(u_z\). The sum of the regular
first-order and wall contributions is

\[
 I_{p,q}^{(1)}(z)+I_{p,q}^{({\rm wall})}(z)
 =f_{p,q}(b)\overline{u_z(b)}
 -f_{p,q}(a)\overline{u_z(a)},
\]

with the endpoint values read in the frozen outward-minus-inward orientation.
For the ordinary theta shell convention, this becomes

\[
 I_{p,q}^{(1)}(z)+I_{p,q}^{({\rm wall})}(z)
 =\Phi(\log q)\overline{u_z(\log q)}
 -\Phi(\log p)\overline{u_z(\log p)}.
\]

If the final centered column uses an additional source coefficient, that
coefficient multiplies both terms and must be retained before taking the
arithmetic adjoint.

## Evans substitution

On the positive end,

\[
 u_z(x)=-e^{zx}\int_x^\infty e^{-zr}\Phi(r)\,dr.
\]

For the Hermitian Green pairing displayed above, the endpoint expression is

\[
 -\Phi(b)e^{\overline z b}
 \int_b^\infty e^{-\overline z r}\Phi(r)\,dr
 +\Phi(a)e^{\overline z a}
 \int_a^\infty e^{-\overline z r}\Phi(r)\,dr,
\]

for real theta forcing. It is compact-locally bounded but is anti-holomorphic
in \(z\) under this slot convention.

## Analytic transpose versus Hermitian adjoint

Multiplicity jets belong to the holomorphic operator-pencil lane. They must be
formed with the analytic dual/transpose pairing, not by differentiating a
Hermitian expression containing \(\overline{u_z}\).

For the analytic transpose convention, the endpoint totalization is

\[
 I_{p,q,{\rm an}}^{({\rm end})}(z)
 =\Phi(b)u_z(b)-\Phi(a)u_z(a),
\]

which equals

\[
 -\Phi(b)e^{zb}\int_b^\infty e^{-zr}\Phi(r)\,dr
 +\Phi(a)e^{za}\int_a^\infty e^{-zr}\Phi(r)\,dr.
\]

This section is holomorphic. Parameter differentiation commutes with endpoint
trace on the Evans graph, so every jet is obtained by differentiating these
explicit integrals. No new wall distribution appears.

The Hermitian shell controls Green signs and flux. The analytic-transpose shell
controls Xi divisibility and local module length. Identifying the two requires
a declared real structure on the sewing locus; it is not automatic off that
locus.

## Revised shell decomposition

The complete shell residual may now be grouped as

\[
 \mathcal S_{p,q}(z)
 =I_{p,q}^{(0)}(z)
 +I_{p,q}^{({\rm end})}(z)
 +I_{p,q}^{({\rm recip})}(z)
 +I_{p,q}^{({\rm link})}(z),
\]

where

\[
 I_{p,q}^{({\rm end})}
 =I_{p,q}^{(1)}+I_{p,q}^{({\rm wall})}
\]

is the explicit endpoint difference above.

Thus derivative and wall are still distinct typed ports in the carrier, but
their Green totalization is one computable shell scalar.

## Hostile qualification

The formula fails if:

- the half-density connection signs are changed;
- the wall delta is omitted;
- endpoint orientation is reversed;
- a plain Volterra history replaces the twisted graph;
- source coefficients differ between the regular and wall pieces.

Any such change must be treated as a different constructor.

## Disposition

Two previously unevaluated shell terms reduce to one exact endpoint expression.
Candidate one now requires cancellation of the ordinary term plus this endpoint
term, reciprocal response, and ordered linking contribution, with every
multiplicity jet retained. No RH conclusion is authorized.
