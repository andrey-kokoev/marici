# The completed-theta diagonal shell expansion selects reciprocal-balanced total grades divisible by four

## Question

Beyond the first grade-four correction, which reciprocal-balanced prime-delay
grades are compatible with the completed-theta late-shell expansion?

## Claim boundary

The completed-theta endpoint-relative expansion is in integer powers of
\(p^{-2}\). A balanced delay monomial of total grade \(2k\) has order
\(p^{-k}\). Therefore only even \(k\), equivalently total grades divisible by
four, can occur without cancellation. This is an asymptotic selection rule, not
a construction of the coefficients.

## Completed-theta scale

At \(a=\log p\),

\[
 \Lambda(a)=2\pi p^2-\frac92+O(p^{-2}).
\]

Consequently

\[
 \Lambda(a)^{-1}
 =\frac{1}{2\pi}p^{-2}
 \left[1+O(p^{-2})\right].
\]

Endpoint-relative Watson expansions are series in integer powers of
\(\Lambda^{-1}\), with superexponentially small higher-label corrections.
Thus their algebraic prime orders are

\[
 p^{-2},p^{-4},p^{-6},\ldots.
\]

No \(p^{-1},p^{-3},p^{-5},\ldots\) term occurs in this asymptotic scale.

## Balanced delay grades

A reciprocal-balanced monomial has equal direct and reciprocal exponents:

\[
 S_{p,+}^kS_{p,-}^k=p^{-k}.
\]

Its total delay grade is \(2k\). Compatibility with the completed-theta prime
orders requires

\[
 k=2r.
\]

Therefore the allowed total grades are

\[
 2k=4r.
\]

The first are total grades four, eight, twelve, and so on.

## Forced cancellations

Balanced total grades congruent to two modulo four produce forbidden algebraic
orders:

\[
 S_{p,+}S_{p,-}=p^{-1},
\]

\[
 S_{p,+}^3S_{p,-}^3=p^{-3},
\]

and similarly at higher odd \(k\). If such terms appear in an intermediate
Cayley, determinant, or constitutive expansion, their codiagonal coefficient
must vanish by a source identity before comparison with the diagonal shell
response.

Unbalanced terms must also vanish or remain in a separately typed
parameter-dependent channel.

## First two admissible slots

The first diagonal correction is

\[
 c_4S_{p,+}^2S_{p,-}^2,
 \qquad
 c_4=-\frac1{4\pi}
\]

under the current unit normalization, subject to source derivation.

The next possible balanced slot is

\[
 c_8S_{p,+}^4S_{p,-}^4=c_8p^{-4}.
\]

Determining \(c_8\) requires the second relative Watson coefficient, including
higher theta curvature and the ordinary-overlap correction.

## Relation to determinant filtration

The order-three regularized determinant removes the first two trace cumulants
and retains connected grades at least three. That filtration alone does not
enforce the modulo-four balanced selection rule. A separate reciprocal
codiagonal or completion-parity theorem is required.

The four-grade Gaussian constructor packet shows that grade four is present in
the source grammar, but does not prove the all-order divisible-by-four rule or
its response coefficient.

## Hostile

A diagonal response compiler fails the late-shell asymptotic test if, after
normalization and reciprocal codiagonalization, it retains any nonzero balanced
term of total grade congruent to two modulo four.

Checking total grades two and six is the cheapest finite falsifier.

## Disposition

The diagonal reciprocal response must obey a divisible-by-four balanced-grade
selection rule. Grade four is the first admissible correction; grade six must
cancel. The source mechanism enforcing this rule remains unidentified. No RH
conclusion is authorized.
