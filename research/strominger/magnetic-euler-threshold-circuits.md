# Euler thresholds carry explicit Hall circuits

The first cap transition admits an exact three-column identity. Let
\(M_a\) and \(P_a\) denote the minus and plus columns in consecutive-depth
order. At

\[
q=g+\beta-2,
\]

the first missing plus depth is \(a=\beta+1\), and

\[
\beta P_{\beta+1}
+(g+\beta-1)P_\beta
+(-1)^g(g-1)M_0=0.
\]

This was checked as an exact integer column identity for all \(133\) pairs

\[
2\le\beta\le8,\qquad 2\le g\le20.
\]

The displayed coefficients have common divisor

\[
d=\gcd(\beta,g-1).
\]

Division by \(d\) gives the primitive circuit. Thus the first Euler zero is
not merely a vanished coordinate: it is the visible endpoint of a universal
three-column Hall relation.

## Source-level proof reduction

Let \(c_j(a)\) be the source coefficients. With
\(R=\beta^{\overline g}\), the three relevant depths collapse to endpoint
atoms:

\[
c_j(0)=R\,\delta_{j,g},
\qquad
c_j(\beta)=(-1)^gR\,\delta_{j,0},
\]

and

\[
c_0(\beta+1)=(-1)^g\frac{\beta+g}{\beta}R,
\qquad
c_1(\beta+1)=(-1)^g\frac{g}{\beta}R,
\]

with all \(c_j(\beta+1)=0\) for \(j\ge2\).

At \(q=g+\beta-2\), the three branch exponents are
\(m(P_{\beta+1})=0\), \(m(P_\beta)=1\), and
\(m(M_0)=1-2g-\beta\). Substitution into the path-coefficient rule reduces
the column identity to cancellation of these endpoint atoms. Hence the
relation follows coefficientwise from rising-factorial identities; no Hall
determinant expansion is needed.

## Second threshold

At

\[
q=2g+\beta-3,
\]

two adjacent depths are missing:

\[
\beta+g-1,qquad \beta+g.
\]

Exact primitive witnesses show a different mechanism from the first
three-column circuit. The second relation uses the full grade-length source
packet

\[
M_0,quad P_\beta,P_{\beta+1},\ldots,P_{\beta+g-2},
quad P_{\beta+g},
\]

while the already missing \(P_{\beta+g-1}\) is omitted. The first relation
at this threshold uses the same lower plus interval with target
\(P_{\beta+g-1}\).

Normalize the coefficient of \(P_{\beta+g}\) to one. The coefficient of
the opposite endpoint atom is

\[
[M_0]=(-1)^g g\,
\frac{(\beta+g)^{\overline{g-2}}}
     {\beta^{\overline{g-1}}}.
\]

The circuit and endpoint formula pass all \(63\) exact cases with
\(2\le\beta\le8\) and \(2\le g\le10\). The lower-frontier law independently
passes all \(133\) cases through \(g=20\). The remaining coefficients
are the connection coefficients of the truncated rising-factorial packets.
Their closed form is the remaining convolution problem.

Because the triangular packet is a basis, the terminal relation is unique
inside this boundary presentation. In the \(63\)-case census its primitive
support size is at least \(g\), and generically \(g+1\). Exceptional internal
coefficient zeros reduce the support by at most one in the tested range.
Therefore the circuit memory is unbounded in grade even after adjoining
\(M_0\).

A bounded-width augmentation could exist only by adjoining a new port whose
constructor already evaluates this grade-dependent convolution. Such a port
would compress the relation at readout, but would not remove its source memory
unless its own recurrence were independently source-derived.

## Parity checksum compression

Let \(\lambda_r\) be the normalized coefficients of
\(P_{\beta+r}\), with \(\lambda_{g-1}=0\) and \(\lambda_g=1\), and
define

\[
\Lambda_{\beta,g}(u)=\sum_{r=0}^{g}\lambda_r u^r.
\]

If \(\mu\) is the coefficient of \(M_0\), exact computation gives

\[
\Lambda_{\beta,g}(-1)+\mu=0.
\]

This passes all \(63\) tested circuits. Thus a single parity-evaluation port
compresses the endpoint compatibility condition. It does not reconstruct the
individual \(\lambda_r\), whose primitive support remains at least \(g\).

The distinction is typed:

- invariant closure has width one: evaluate the circuit polynomial at
  \(u=-1\);
- executable construction still has grade-growing memory: generate every
  coefficient \(\lambda_r\).

## Constant-recurrence obstruction

For each exact coefficient sequence, solve for the least homogeneous
constant-coefficient recurrence order. Across all \(133\) cases through
\(g=20\), the result is

\[
L_{\min}(g)=\left\lfloor\frac g2\right\rfloor+1,
\]

independently of \(\beta\) in the tested range. The maximum observed order is
\(11\) at \(g=20\). Hence no fixed-order constant-coefficient transport can
generate the terminal circuit family.

A second hostile class tests first-order rational transport

\[
Q(r)\lambda_{r+1}=P(r)\lambda_r.
\]

The minimum polynomial degree also grows essentially as
\(\lfloor g/2\rfloor\), reaching \(10\) at \(g=20\). Thus no
fixed-degree first-order hypergeometric recurrence explains the family.

More generally, test Ore recurrences

\[
\sum_{j=0}^{k}P_j(r)\lambda_{r+j}=0,
\qquad \deg P_j\le d.
\]

For \((k,d)=(2,1),(2,2),(2,3),(3,1),(3,2)\), every system becomes full
column rank at the first grade where its equation count reaches its unknown
count, and remains without a survivor through \(g=20\) for all tested
\(\beta\). The lower-grade fits are therefore underdetermined interpolation,
not transport laws.

This still does not exclude a recurrence outside these fixed bidegrees whose coefficients depend on
the depth index, grade, and source parameter. That hypergeometric possibility
is a separate constructor and remains the next falsifier.

## Grade-changing lift obstruction

Monicity and \(\lambda_{g-1}=0\) force the unique monic degree-one grade
comparison to be multiplication by \(u\). Define

\[
R_{\beta,g}(u)=
\Lambda_{\beta,g+1}(u)-u\Lambda_{\beta,g}(u).
\]

For every tested \(\beta\) and every \(3\le g\le19\), the residual has
exactly \(g\) nonzero coefficients. Thus the canonical grade-changing lift
does not have bounded correction width; it recreates a full grade-sized
packet.

Consequently there are two kinds of memory:

- the first Euler transition has constant circuit width three;
- the separated-boundary transition has support width growing with grade.

This explains why the scalar Euler factor locates both thresholds but does not
by itself furnish both primitive relations. The second threshold requires the
entire finite source jet.

## Proof target

The first identity should follow directly by substituting the factorial source
coefficients into the three columns and applying adjacent rising-factorial
relations. For the second threshold, the target is a closed convolution
formula for the coefficients on
\(P_\beta,\ldots,P_{\beta+g-2}\). Proving that convolution has exactly two
independent terminal relations would upgrade the bounded four-stratum census
to a symbolic Hall theorem.