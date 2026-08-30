# 1799 — Singleton-Wall Bases Meet the Five-Site Threshold Transversely

## Corrected claim

This entry records only a base/carrier statement. It does not classify the
integrated three-wall coefficient singularity.

Let the threshold occurrence be labelled by \(g_i\), and impose a further
singleton equation \(g_j=0\), \(j\neq i\). There are twenty ordered labels in
four free \(C_5\)-orbits, indexed by \(j-i=1,2,3,4\pmod5\).

At fixed loop variables, the source-energy block

\[
(E_T,X_i,X_j)\longmapsto(q_e,g_i,g_j)
\]

has identity Jacobian and determinant one. Hence the corresponding equations
are transverse in the external-energy base.

\[
\boxed{
\text{The singleton-wall base incidence is transverse and already belongs
to the marked carrier.}
}
\]

## Essential qualification

The loop-distance part of \(g_j\) is not constant on the integration fiber.
Near the threshold Morse point it has the form

\[
g_j=h+\lambda_1u+\lambda_2v+\cdots.
\]

Therefore the local integral is not established to factor as a pole line
times the threshold extension. The extra gradient can participate in a
three-wall Landau singularity.

The earlier stronger wording that the coefficient object was a transverse
tensor product is withdrawn.

## Next falsifier

For each of the four relative-label orbits, compute the source-labelled
gradient of \(g_j\) at the physical threshold point. Reduce

\[
\int\frac{du\,dv}
{(\tau+H_1u^2+H_2v^2)(h+\lambda_1u+\lambda_2v)}
\]

with the complete source coefficient and classify its two-parameter
nearby-cycle object.

## Evidence

- research/benincasa/checkers/five_site_g5_spectator_singleton_intersections.py
- research/benincasa/results/five-site-g5-spectator-singleton-intersections.json
- allocator claim: seqclaim-30c52699ab04fe3d7ee05856
