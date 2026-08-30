# Mixed-portal CKM no-go: WP1013

## Question

Does the WP1012 linear mixed portal land on the fitted mixing block once its
parameter is chosen to reproduce the observed Jarlskog scale?

## Ordering-independent probe

For rank-one spectral projectors \(P_i(s)\) of \(X+sY\) and \(Q_j\) of \(Y\),
define

\[
w_{ij}(s)=\operatorname{Tr}(P_i(s)Q_j)=|V_{ij}(s)|^2
\]

and the row-and-column-permutation invariant

\[
S_2(s)=\sum_{i,j}w_{ij}(s)^2.
\]

This probe is defined on the weak-basis quotient and is unchanged by eigenvalue
ordering, row phases, column phases, or simultaneous presentation changes. It
is a mathematical function of the already instrumented CKM moduli; no new
reference port is introduced.

## Exact portal constraint

The eigenvalues of \(Y\) are \(0,\pm\sqrt{86}/5\), while those of \(X+sY\)
are \(0,\pm\sqrt{86s^2+25}/5\). Exact polynomial spectral projectors give, with
\(x=s^2\),

\[
S_2(x)=
\frac{164102448x^2+51772000x+4698125}
{7396(86x+25)^2}.
\]

Its derivative is

\[
\frac{25(872728x+113075)}{43(86x+25)^3}>0
\]

for \(x\geq0\). Meanwhile

\[
J^2(x)=\frac{87890625}{636056(86x+25)^3}.
\]

At \(x=4\), \(J^2>10^{-6}\). Therefore every portal point with
\(|J|<10^{-3}\) has \(x>4\), hence

\[
S_2>S_2(4)=\frac{315269477}{111894084}>\frac{281}{100}.
\]

All 1,210 stored viable sheets obey the stated J bound.

## Fitted mixing obstruction

Freeze the stored WP16a physical10 values of
\(|V_{us}|,|V_{ub}|,|V_{cb}|\). The remaining unitary CKM ambiguity is the
phase branch. Writing \(c=\cos\delta\), its \(S_2\) is an exact quadratic in
\(c\). Bounding it for the complete interval \(-1\leq c\leq1\) gives

\[
S_2<\frac{281}{100}.
\]

Thus the portal and fitted CKM blocks are disjoint across both phase branches
and every row/column permutation. Matching \(J\) cannot repair this independent
quotient invariant.

## Smallest exact falsifier

A portal point with \(|J|<10^{-3}\) and \(S_2\leq281/100\) would falsify the
portal lower bound. A fitted unitary CKM completion with the frozen three
moduli and \(S_2\geq281/100\) would falsify the target upper bound. The checker
retains both strict exact margins.

## Claim boundary

This result excludes only the one-parameter linear mixed portal
\(H_u=aI+X+sY,\ H_d=bI+Y\). It does not exclude higher mixed covariants,
multi-parameter source maps, or a different independently derived source
domain. The fitted block is a readout constraint, not authority to tune a
portal. The result neither supplies a source selector nor a physical
instrument beyond the already admitted CKM-modulus readout.

## Disposition

Close the minimal linear mixed portal negatively at the measured mixing block.
Any successor must derive additional independent mixed coefficients upstream
and must be tested against complete physical16, not fitted by reversing the
readout map.
