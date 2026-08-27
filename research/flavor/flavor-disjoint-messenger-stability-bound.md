# Disjoint-messenger stability bound: WP664

## Frozen branch

WP651 declares separate messenger chains for the independent frame
coefficients. Freeze that disjoint topology, assume canonical kinetic
normalization, and represent each relevant vectorlike messenger as a Dirac
spin-one triplet. For one chain coupled to
\(n\), its field-dependent mass is

\[
\mathcal M_n=M I+yJ_n.
\]

In the common one-loop supertrace normalization its exact contribution is

\[
-4\operatorname{Tr}\mathcal M_n^4
=-12M^4-48M^2y^2|n|^2-8y^4|n|^4.
\]

It therefore preserves the scalar operator support of WP662. A disjoint
\(m\)-chain behaves identically and no cross operator is generated.

## Exact tangent bound

Let

\[
F_n=\sum_i d_i y_{ni}^4,
\qquad
F_m=\sum_j d_j y_{mj}^4,
\]

where \(d_i,d_j\) include independently declared multiplicities and the
Yukawas are canonical. At the
WP661 benchmark, the completed tangent flow of the radial stability margin
\(D=4\lambda_n\lambda_m-\lambda_x^2\) is

\[
\frac{dD}{dt}=1136-32(F_n+F_m).
\]

The exact nonerosion condition is

\[
F_n+F_m\leq\frac{71}{2}.
\]

A WP651 unit example has two \(J_n\) and two \(J_m\) chains; its two identity
chains do not couple to the frame. Thus \(F_n=F_m=2\) and the derivative is
1008. A hostile strong-coupling packet with \(F_n=F_m=18\) has derivative \(-16\):
the positive margin initially erodes even though the tree word family is
unchanged.

## Disposition

The source-authorized disjoint branch preserves operator support, but its
frame stability is conditional on messenger multiplicities and Yukawa
couplings that WP651 leaves free. The inequality is a stability gate, not a
selector: it admits a region rather than fixing a numerical flavor point.

Finite-scale authority still requires deriving the multiplicities and
couplings from the messenger grammar and integrating the completed flow over a
declared interval.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp664_disjoint_messenger_stability_bound.py

Generated result: results/wp664_disjoint_messenger_stability_bound.json.
