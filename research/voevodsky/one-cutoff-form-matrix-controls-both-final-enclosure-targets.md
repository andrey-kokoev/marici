# One cutoff-form matrix controls both final enclosure targets

## Question

Must the candidate form and the first 160 projected-residual coefficients be interval-enclosed by separate analytic constructions?

## Claim boundary

No. Both are algebraic images of the same cutoff-form matrix on Legendre degrees 0 through 159. Once this single 160-by-160 matrix is interval-enclosed, exact decimal coefficient algebra produces both target objects.

## Exact finite data

Let \(C:\mathbb R^{25}\to H_{160}\) be the selected-space coefficient map, let \(G=C^*C\), and let

\[
P=CG^{-1}C^*.
\]

For exported tail map \(D\), define

\[
D_Q=(I-P)D,
\qquad
Z=C-D_Q.
\]

Let \(H\) be the cutoff form restricted to \(H_{160}\):

\[
H_{mn}=\langle p_m,Ap_n\rangle,
\qquad 0\leq m,n<160.
\]

## Candidate form

The trial candidate form is exactly

\[
J=Z^*HZ.
\]

Thus an interval enclosure of \(H\), combined with exact-decimal enclosures of \(C\) and \(D_Q\), produces the required 25-by-25 candidate matrix without a separate Schur integration.

## Low-degree projected residual

The first 160 Legendre coefficients of \(AZ\) are \(HZ\). Projecting away the selected span gives

\[
R_{<160}
=
(I-CG^{-1}C^*)HZ.
\]

Therefore the low-degree residual Gram matrix is

\[
R_{<160}^*R_{<160}.
\]

The factorial theorem controls the omitted degrees independently.

## Consequence

The remaining continuum calculation is one matrix enclosure problem: certify all entries of \(H\) tightly enough that interval propagation yields

\[
|\Delta J_{ij}|\leq10^{-4},
\qquad
|\Delta R_{nj}|\leq10^{-5}.
\]

The scout now exports the numerical 160-by-160 matrix so an Arb sensitivity checker can determine the admissible entry radius for \(H\). Analytically, each multiplier entry is the one-dimensional integral

\[
\frac1{2\pi}\int_{-250}^{250}
 s(u)\overline{\widehat p_m(u)}\widehat p_n(u)\,du,
\]

and the endpoint rank-two contribution has explicit modified-spherical-Bessel moments.

## Sensitivity result

Direct Arb propagation from independent radius boxes on all 25,600 entries of \(H\) gives:

- at radius \(10^{-8}\), maximum propagated candidate-form radius \(3.44\times10^{-5}\) and residual-coefficient radius \(9.22\times10^{-6}\);
- radius \(10^{-7}\) still proves the final lower form positive by correlated interval \(LDL^*\);
- radius \(10^{-6}\) fails.

Thus \(10^{-8}\) is a conservative entrywise target meeting the independently preregistered \(10^{-4}\) and \(10^{-5}\) downstream budgets. The wider \(10^{-7}\) radius is a directly tested fallback when correlations are preserved through the complete computation.

## Disposition

The candidate-form and residual-coefficient gates merge into one finite cutoff-form matrix gate with sufficient entry radius \(10^{-8}\). No continuum positivity or RH implication is asserted until the 160-by-160 entries are directed interval enclosures.
