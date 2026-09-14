# Erratum: the four energy vertices do not label the two wall swaps

## Question

Can the middle critical values \(E=2x\) and \(E=2y\) be identified directly with the two conductor root swaps \(T_1,T_2\)?

## Claim boundary

This packet audits that identification against the existing conductor–elliptic incidence result. It preserves the formal monodromy half-difference calculation but withdraws its interpretation as a four-energy-vertex flow.

## Incidence audit

At the signed-energy branches, the two conductor discriminants restrict as follows:

\[
\begin{array}{c|cc}
E&\Delta_1&\Delta_2\\ \hline
2x&4x^2(2x-y)^2&4x^2y^2\\
2y&4x^2y^2&4y^2(x-2y)^2\\
2(x+y)&4x^2(2x+3y)^2&4y^2(3x+2y)^2\\
0&4x^2y^2&4x^2y^2.
\end{array}
\]

For generic positive \(x,y\), none of these restrictions vanishes. The established incidence packet consequently reports no nonsoft conductor–elliptic collision in the positive chamber.

Therefore the assignments

\[
E=2x\rightsquigarrow T_1,
\qquad
E=2y\rightsquigarrow T_2
\]

are not source-derived. The four energy branch values and the two conductor wall swaps are distinct typed loci.

## Surviving algebra

Inside the abstract two-wall monodromy representation,

\[
\frac{T_2s_+-T_1s_+}{2}=s_-
\]

remains exact and integral. What fails is the claim that the two terms are the transported values along the two middle arms of the four-energy diagram.

## Correct role of the four vertices

The four values

\[
0,
\,2x,
\,2y,
\,2(x+y)
\]

are branch points of the total-energy elliptic square-root cover. Information between them must be carried by a based lifted path or relative one-cycle on that cover. It cannot be transported by assigning a conductor root swap to each base vertex.

Thus the required flow is:

1. choose the source-derived based continuation in the punctured \(E\)-line;
2. lift it to the elliptic square-root cover;
3. retain its sheet and orientation data;
4. compare the resulting relative cycle with the conductor monodromy module;
5. only through that comparison determine whether its class acts as \(T_1\), \(T_2\), their product, or neither;
6. apply the marked algebraic and physical readouts afterward.

The missing map is precisely the comparison in step 4. The elliptic cover and both monodromy modules already exist; their identification does not.

## Disposition

The prior middle-route packet overidentified two diagrams. Its formal half-difference is retained as a conditional target, but its four-cusp interpretation is withdrawn. A valid coherence-pyramid flow must pass through the lifted elliptic path before entering conductor wall monodromy.

Verification:

- `research/voevodsky/checkers/check_four_energy_wall_swap_type_gate.py`
- `research/voevodsky/results/four_energy_wall_swap_type_gate.json`
