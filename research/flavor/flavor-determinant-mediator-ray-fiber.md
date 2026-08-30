# Determinant-mediator ray fiber

## Question

WP979 asks whether the WP977 source grammar and its exact coercivity condition
select the coefficient ratio required by WP978.

Leading elimination gives

\[
q=\frac{\mu^2}{2m_A^2},\qquad
k=\frac{\gamma^2\mu^6}{2m_s^2(m_A^2)^6},
\]

and therefore

\[
\frac{k}{q}
=\frac{\gamma^2\mu^4}{m_s^2(m_A^2)^5}.
\]

The auxiliary stability condition
\(\lambda>|\gamma|/16\) constrains none of the positive mass ratio or the
\(\mu\) combination appearing in this ray.

## Exact hostile packets

Freeze \((\lambda,\gamma,\mu,m_A^2)=(1,8,1,1)\). Both packets then have the
same strict auxiliary stability margin \(1/2\).

\[
\begin{array}{c|c|c}
 m_s^2 & k/q & \text{WP978 side}\\
\hline
1 & 64 & \text{rank-two side}\\
1/512 & 32768 & \text{full-rank-control side}
\end{array}
\]

The crossing is \(24696\). Thus two source packets admitted by the same field
content, symmetry, vertex degree, positivity, and coercivity conditions make
opposite vacuum predictions on the exact hostile slice.

## Interpretation

WP977 is a source-derived operator constructor but not a coefficient-ray
selector. The light-scalar packet also shrinks the domain on which leading
elimination is quantitatively controlled; this is an additional threshold
gate, not a mechanism selecting the first packet.

The smallest falsifier is an independently derived relation among
\(\gamma,\mu,m_s^2,m_A^2\) that fixes the ray on one side of the global
crossing. No such relation is currently admitted.

## Reproduction

Run:

    python research/flavor/checkers/wp979_determinant_mediator_ray_fiber.py

The generated result is
research/flavor/results/wp979_determinant_mediator_ray_fiber.json.
