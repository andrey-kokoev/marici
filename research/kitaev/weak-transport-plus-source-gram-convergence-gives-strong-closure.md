# Weak Transport Plus Source Gram Convergence Gives Strong Closure

Let (B_N:X\to Y) be bounded operators between Hilbert spaces and suppose

\[
B_Nx\rightharpoonup Bx
\]

for every (x\in X). If additionally

\[
\langle x,B_N^*B_Nx\rangle
\longrightarrow
\langle x,B^*Bx\rangle
\]

for every (x), then

\[
B_Nx\longrightarrow Bx
\]

strongly for every (x). Indeed,

\[
\|B_Nx-Bx\|^2
=\|B_Nx\|^2+\|Bx\|^2
-2\Re\langle B_Nx,Bx\rangle,
\]

and the three terms converge to zero residual by the two hypotheses.

Thus weak transport plus diagonal source-Gram convergence closes actuator
norms. By polarization, convergence of the full sesquilinear forms

\[
\langle B_Nx,B_Ny\rangle
\to
\langle Bx,By\rangle
\]

closes all mixed quadratic channels as well.

## Exact separation of the hostiles

For the orthogonal-tail actuators (B_N(1)=e_N), weak convergence gives
(B=0), but

\[
B_N^*B_N=1\not\to0=B^*B.
\]

The theorem correctly rejects strong closure.

For

\[
C_N=\operatorname{diag}(1,N^{-1}),
\qquad
C=\operatorname{diag}(1,0),
\]

one has weak convergence and

\[
C_N^*C_N=\operatorname{diag}(1,N^{-2})\to C^*C,
\]

so strong convergence follows.

## Source-first significance

The Gram limit must be constructed and controlled upstream from source atoms.
If one defines the limiting Gram only as (B^*B) after choosing the desired
weak limit, the argument is tautological. The required data are the same
two-variable operator kernels previously isolated:

\[
K_N(z,w)=J_N(z)^*J_N(w).
\]

Their mixed convergence supplies polarization-complete closure rather than a
scalar squared-divisor shadow.

For Green identities, this theorem licenses passage of actuator energies only
after both weak transport and source-Gram convergence are established in the
same topology. It still does not authorize the physical actuator.

## Falsifiers

- Weak convergence holds but Gram norms retain tail mass.
- Only diagonal scalar outputs converge while mixed forms do not.
- The limiting Gram is defined downstream from the desired limit.
- Convergence is pointwise but the claimed theorem requires a uniform state
  family without an additional compactness bound.
- Strong mathematical closure is reported as executable control.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. Weak transport, Gram convergence, strong closure, and mixed forms were
frozen.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The weak-energy obstruction gained an exact positive repair theorem.
The missing completion datum is upstream source-Gram convergence, precisely
linking the actuator lane back to the two-variable kernel programme.
