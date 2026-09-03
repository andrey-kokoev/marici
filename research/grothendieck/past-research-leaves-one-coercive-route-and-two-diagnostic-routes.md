# Past research leaves one local coercive diagnostic and two scalar diagnostics

## Question

Which prior Marici constructions remain nonredundant after the source-normalized remainder cone was identified as RH-equivalent?

## Search scope

The search covered the prior Stieltjes, Loewner, Jacobi, local Sobolev Weil, broad-smoothing, canonical-system, and sampled-Hankel packets. It excluded branches already carrying explicit no-go results.

## Corrected conjecture

Fixed-support logarithmic ellipticity can reduce a local Weil problem to finite work, but it is not yet a route to the heat-polynomial cone. The archimedean Weil multiplier grows like `log|u|`, the prime sector is order zero on a fixed support window, and the endpoint is finite rank. A quantitative interval Gårding inequality could force positivity on the local high-mode complement. However, the inverse Fourier transforms of the Gaussian heat-polynomial amplitudes are Schwartz functions with unbounded support, so no fixed support window contains the target family. A complete route additionally needs uniform control as the support window grows and a form-norm tail approximation.

## Route 1: quantitative log-elliptic coercivity

Prior packets establish the structural decomposition:

- archimedean symbol `Re psi(1/4+iu/2)=log|u|+O(1)`;
- finitely many prime translations on support `[-L,L]`, with explicit bounded norm;
- finite-rank endpoint correction;
- compact self-adjoint realization relative to an `H_0^s` norm, so negative spectrum is discrete.

On a periodic fixture, Fourier diagonalization proves positivity above an explicit frequency threshold. The actual interval has boundary and commutator errors because zero extension and Dirichlet projection do not preserve frequency support. The missing theorem is therefore concrete:

\[
W_L(f,f)\ge c_L\|P_{>N_L}f\|_{H^{0,\log}}^2
-C_L\|P_{\le N_L}f\|^2,
\]

with source-computable `N_L,c_L,C_L`, followed by a certified finite matrix for the low modes. This is not yet a proof: obtaining a positive high-mode lower bound, rather than compactness or small norm, is the unresolved step.

## Route 2: rank-one arithmetic inequality as the cheapest discriminator

The first unknown consequence is

\[
H_R(t)-H_R(t+h)\ge0
\]

for every positive `t,h`. Differentiating the explicit endpoint–gamma–prime kernel turns this into `-H_R'(t)>=0`. Broad-smoothing research already proves uniform positivity of the completed shifted Gaussian for sufficiently small heat parameter, and prime terms there are exponentially suppressed. That machinery should be checked against the derivative remainder rather than against more sampled matrices.

This route can refute the programme cheaply or establish a bounded region, but rank one cannot imply the full cone. It is a diagnostic route only.

## Route 3: one source Loewner kernel

The order-two Stieltjes packets combine the derivative hierarchy into the divided-difference kernel

\[
\frac{H(x)-H(x-t)}t.
\]

A source factorization

\[
K_F(x,y)=R(x)^*R(y)
\]

from the completed prime–theta correspondence would prove every matrix restriction at once and generate a nonterminating Jacobi realization. Existing finite Jacobi reconstructions recover stable low rates and positive weights, but finite prediction does not supply the infinite factor or exclude later negative pivots. Defining `R` by polarizing the target kernel is circular; it must be built independently from source data.

## Useful theorem that is not a route

The one-time Stieltjes reconstruction theorem shows that all ordinary and shifted derivative Hankel matrices at one heat parameter, plus analytic growth, imply complete monotonicity globally. It reduces the parameter dimension but not the infinite-rank positivity burden.

## Rejected rivals

Do not retry the free differential operator, scalar theta Schrödinger ground state, fixed Wigner slices, repaired finite canonical systems that alter the source, finite Hurwitz transfer, fixed recurrences, rational transforms, terminating continued fractions, stabilized finite Jacobi matrices, sectorwise Gram factors, or Gaussian first-contact arguments. Existing packets give typed obstructions for each.

## Strongest falsification attempt and residual

Compactness proves only that a negative direction would be finitely approximable; it does not prove absence of negative eigenvalues. Broad smoothing controls one parameter end but does not control arbitrary polynomial superpositions. One-time reconstruction still assumes every Hankel rank. These failures leave quantitative log-elliptic coercivity as the sole route that could convert the infinite complement into a finite certificate without defining positivity from the target form.

## Disposition

Treat interval Gårding coercivity as a local diagnostic, not the sole RH route. It becomes relevant only together with constants uniform in the support size and a proved form-core approximation for the Gaussian heat-polynomial family. Use the differentiated rank-one remainder inequality only as a bounded falsifier. Keep the Loewner factorization dormant unless a source-defined map `R` appears.