# Erratum: the D4 discriminant group is not yet the source parity plane

The compound-\(D_4\) geometry and its discriminant group

\[
D_4^\vee/D_4\cong(\mathbb Z/2)^2
\]

are genuine. So is the source-supported monodromy plane

\[
\langle e_6,v_{\rm alg}\rangle/2
\langle e_6,v_{\rm alg}\rangle
\cong(\mathbb Z/2)^2.
\]

But equality of cardinality does not identify these groups.

There is an immediate equivariance test. On the geometric \(D_4\) quotient, site exchange swaps two perfect matchings and fixes the third. Its matrix is

\[
T=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad \operatorname{rank}_{\mathbb F_2}(T-I)=1.
\]

On the currently displayed source support frame, loop-coordinate exchange fixes \(e_6\), fixes \(e_7\), and swaps only \(e_8,e_9\). Since the displayed reduction of \(v_{\rm alg}\) has no \(e_8,e_9\) part modulo two, its recorded action is

\[
I_2,
\qquad \operatorname{rank}_{\mathbb F_2}(I_2-I_2)=0.
\]

These two representations are not conjugate over \(\mathbb F_2\). Therefore the naive equivariant identification

\[
D_4^\vee/D_4
\stackrel?= 
\langle e_6,v_{\rm alg}\rangle/2
\]

is false with the currently asserted actions—or, equivalently, at least one purported action has not been transported through the missing integral comparison.

The correct conclusion is narrower:

- the \(D_4\) resolution supplies a natural upstream geometric invariant;
- the total-energy arm gives a distinguished nonzero class in that geometric group;
- no integral specialization homomorphism from the \(D_4\) resolution lattice to the rank-seven Gysin kernel has yet been constructed;
- therefore the diagonal matching cannot yet be called the ambient cusp parity.

The earlier files claiming that the \(D_4\) class already *is* the two-bit source parity, or that it selects the ambient class, are superseded by this erratum.

The required object is now precise:

\[
\Phi_{\rm sp}:D_4^\vee/D_4
\longrightarrow
\langle e_6,v_{\rm alg}\rangle/2.
\]

It must be derived from integral specialization/intersection geometry, not inferred from matching group orders. Its two components are exactly the two direct mod-two intersection calculations originally requested.

Certificate:

- `research/voevodsky/checkers/audit_D4_to_source_parity_comparison.py`;
- `research/voevodsky/results/D4_to_source_parity_comparison_audit.json`.
