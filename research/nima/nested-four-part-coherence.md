# Third whole-composite witness and coherent changes of attachment order

## Question

Extend the declared active comparison model by one stage. Does a witness of the whole three-part composite preserve earlier agreements, and do comparisons between different construction orders themselves compose? The added witness is an abstract comparison slot, not an asserted third physical electron. Active obligation: whole-composite attachment compatibility and coherence of record transport.

## Construction

In four real comparison coordinates, the canonical agreement normals are

\[
r_1=(1,-1,0,0),\quad r_2=(1,1,-2,0),\quad r_3=(1,1,1,-3).
\]

They impose x0=x1, x2=(x0+x1)/2 and x3=(x0+x1+x2)/3. They are mutually orthogonal, with squared norms 2,6,12. The existing reversible projection lift therefore enforces each new agreement without reopening the prior ones. Each step retains its scalar mismatch coefficient, and the inverse updates recover the complete input exactly.

The terminal active state is the four-coordinate barycenter. Three independent retained mismatch coordinates accompany it. Together the mean and these coefficients reconstruct all four inputs. This is a rank-three record space; it has not been identified with spatial volume.

## Order comparisons

With the root coordinate fixed, the three witness slots admit six attachment orders. For source frame rows r_i and target rows s_j, the exact record map is

\[
T_{ji}=\frac{s_j\cdot r_i}{s_j\cdot s_j}.
\]

All 36 maps are invertible. They preserve the record metric D=diag(2,6,12), and all 216 ordered triples of frames satisfy T_bc*T_ab=T_ac. These are finite indexed composition checks, not 216 independent cells or an identification with the earlier 1836 counting factors.

Adjacent order swaps act by

\[
A=\begin{pmatrix}1/2&3/2&0\\1/2&-1/2&0\\0&0&1\end{pmatrix},
\qquad
B=\begin{pmatrix}1&0&0\\0&1/3&4/3\\0&2/3&-1/3\end{pmatrix}.
\]

Exact arithmetic verifies

\[
A^2=B^2=I,\qquad ABA=BAB,\qquad AB\ne BA.
\]

Thus two different three-swap paths representing the same final order agree on the retained records, even though adjacent swaps do not commute. The nonzero AB-BA matrix is the deliberate failed-commutation control. The six records are not erased or declared literally identical.

For input (1,2,4,8), every order reaches (15/4,15/4,15/4,15/4), and the transferred squared budget is 115/4. Its distribution among stages depends on the order. Exact linear-basis checks establish the readout identities for arbitrary real input vectors, not only this example.

## Disposition and verification

The chosen next comparison adds a third mismatch direction and a testable coherence relation between order-change paths. This develops the barycenter-plus-linked-record architecture without guessing another particle. The result follows from the supplied affine averaging law and Euclidean pairing; it does not select that law from native physical principles or predict mass, binding or emission rates.

`python research/nima/checkers/check_nested_four_part_coherence.py` passed via `structured_command_execution:e_32876_1791228208496091600_51`. Results: `results/nested-four-part-coherence.json`. The checker verifies orthogonality, full recovery, metric preservation, all frame compositions, the braid relation and noncommutation control exactly. No commit or publication is claimed.
