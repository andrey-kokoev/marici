# The Higher Finite-Sextic Critical Loci Stay on Frozen Support

## Universal critical model

Entry 806 leaves one possible failure locus for the generic Kato--Gysin
normal form:

\[
S_{ij}=\alpha_{ij}=\beta_{ij}=0.
\]

Write the source-normalized Cayley--Menger determinant in squared edge
variables

\[
A=a^2,
\qquad
B=b^2.
\]

It is quadratic in \((A,B)\).  Its Hessian has determinant

\[
\boxed{
\det\operatorname{Hess}_{A,B}K_{\rm CM}
=-\Lambda(P_1,P_2,P_3),
}
\]

where

\[
\Lambda=(P_1-P_2-P_3)(P_1-P_2+P_3)
(P_1+P_2-P_3)(P_1+P_2+P_3).
\]

Away from \(P_1P_2\Lambda=0\), the unique critical point is

\[
\boxed{
A_{\rm crit}=E^2+P_2^2,
\qquad
B_{\rm crit}=E^2+P_1^2.
}
\]

Its exact critical value is

\[
\boxed{
K_{\rm CM}(A_{\rm crit},B_{\rm crit})=E^2\Lambda.
}
\]

Therefore the nontransverse interior part of every Entry 802 sextic is
supported on the already frozen divisors

\[
E=0
\qquad\text{or}\qquad
\Lambda=0,
\]

together with the two source-labelled equations placing its marked point at
the universal critical point.

## Coordinate-boundary branches

The original derivatives are

\[
\partial_aK=2a\,\partial_AK,
\qquad
\partial_bK=2b\,\partial_BK.
\]

Hence \(a=0\) and \(b=0\) must be audited separately.  At \(A=0\), after
solving \(\partial_BK=0\), the critical value factors as

\[
-\frac{(E-P_2)^2(E+P_2)^2\Lambda}{4P_2^2}.
\]

At \(B=0\), the corresponding value is

\[
-\frac{(E-P_1)^2(E+P_1)^2\Lambda}{4P_1^2}.
\]

Thus these branches add only signed-energy support and the same momentum
triangle divisor.  At \(A=B=0\),

\[
K_{\rm CM}
=P_3^2
\left[
E^4-E^2(P_1^2+P_2^2-P_3^2)+P_1^2P_2^2
\right],
\]

which is soft support times the frozen Cayley--Menger restriction at the
double coordinate boundary.

## Eight representatives

Substituting each of Entry 802's eight source-labelled points changes only
the explicit marked-coordinate equations \(a_0=0\), \(b_0=0\),
\(a_0^2=E^2+P_2^2\), and \(b_0^2=E^2+P_1^2\).  The universal support
factors above do not change.  Cyclic transport therefore supplies the other
sixteen occurrences without introducing a new component.

## Result

Set-theoretically,

\[
\boxed{
S_{ij}=\alpha_{ij}=\beta_{ij}=0
\text{ lies on frozen marked, total-energy, signed-energy, soft,}
\atop
\text{momentum-triangle, and Cayley--Menger restriction strata.}
}
\]

No new unlabelled higher carrier stratum appears.  The generic Kato--Gysin
line can acquire more complicated vanishing-cycle structure on these loci,
but that complexity is a degeneration of the existing carrier calculus.

## Scope

This is a set-theoretic support classification obtained by the exhaustive
interior, single-coordinate-boundary, and double-coordinate-boundary cases.
It is not a primary decomposition and makes no claim about embedded
components or scheme multiplicities at intersections of the listed strata.

## Verification

- checker: `research/nima/audit_finite_sextic_higher_critical_locus.py`;
- packet: `research/nima/finite-sextic-higher-critical-locus.json`;
- allocator claim: `seqclaim-6f43d9839010f22ee2cc7d23`.

## Next falsifier

Compute the local Milnor/Kato ranks on the two universal degeneration types
\(E=0\) and \(\Lambda=0\).  H2 requires those higher coefficient objects to
be induced by the existing nearby-cycle and momentum-triangle Gysin maps;
an excess rank not accounted for by those maps would be the next genuine
failure.
