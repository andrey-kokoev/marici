# Categorical completion of the cyclic residue-feedback fork

## Question

What objects, arrows, limits, and coherence cells must be added so the residue-feedback construction is categorically closed, independently of whether it proves positivity or RH?

## Claim boundary

This packet completes the spectral-shift deformation family under its halving transport and identifies the still-missing three-vertex coherence data. It audits categorical representation only. Positivity and RH implication are outside scope.

## Deformation category

Let \(F_a\) denote the infinitely supported density object

\[
d\rho_a(x)=(1+\varepsilon\cos(ax))e^{-x^2}dx,
\qquad a\in[0,\infty).
\]

The previous fixture class used \(a>0\), so transport \(h_a:F_a\to F_{a/2}\) generated an omega-chain whose limit was absent. Complete the object family by adjoining \(F_0\). Then

\[
h_0=\operatorname{id}_{F_0},
\qquad
h_{a/2^n}\circ\cdots\circ h_a=h_a^{(n)}:F_a\to F_{a/2^{n+1}}.
\]

The chain \((F_{a/2^n})_{n\geq0}\) has declared limit \(F_0\), with analytic convergence certified by the sign-set obstruction bound and the nonvanishing mass floor. Class exit is therefore repaired as missing categorical completion, not treated as scientific failure.

## Simultaneous cyclic signature

`cyclic-residue-feedback-signature.json` now declares all three vertex interfaces, generators, coherencers, residue transports, admitted transitions, edge comparison 2-cells, the cycle cell, and completion-preservation obligation in one symmetric signature transaction. Its checker verifies counterclockwise typing and distinguishes declaration from realization.

## Three dual-role vertices

For each counterclockwise vertex \(i\in\mathbb Z/3\mathbb Z\), categorical completeness requires four typed components:

1. an identity-generator functor \(G_i:P_i\to O_i\);
2. a final coherencer \(C_i:O_i\to R_i\);
3. a residue transport \(T_i:R_i\to P_{i+1}\);
4. a comparison 2-cell between \(G_{i+1}T_iC_i\) and the admitted transition from \(O_i\) to \(O_{i+1}\).

The present fork materializes only the following instances:

- \(G_A\): analytic kernel/deformation generator;
- \(C_B\): arithmetic completion residue;
- \(T_B:R_B\to P_C\): prime-tail parameters for positivity probes;
- \(C_C\): signed-measure obstruction extraction;
- \(T_C:R_C\to P_A\): gauge or spectral-shift deformation;
- the omega-limit object \(F_0\) for iterates of \(T_C\).

It does not yet materialize \(C_A\), \(T_A:R_A\to P_B\), or the three comparison 2-cells as sourced constructors. Consequently, the cyclic signature is now object-complete for the tested deformation family but not coherence-complete.

## Coherence obligations

A complete cyclic representation must verify:

\[
T_{i+1}C_{i+1}G_{i+1}T_iC_i
\simeq
T_{i+1}C_{i+1}\Phi_i
\]

for each edge comparison \(\Phi_i:O_i\to O_{i+1}\), compatibility of these cells around the three-cycle, and preservation of the omega-limit cones by every defined composite. No equality of the three residual types is assumed; cyclic transport uses typed maps rather than coercion.

## Disposition

The spectral-shift result is reclassified: it supplies a missing completion object and limit cone. It neither succeeds nor fails as an RH proof mechanism because that is not the active question. The categorical audit now has a precise boundary:

- deformation-family object closure: supplied;
- identity and composition for halving transports: supplied;
- omega-limit object and cone: supplied analytically;
- all three vertices simultaneously serving as generator and coherencer: incomplete;
- cyclic comparison 2-cells and three-cycle coherence: incomplete;
- preservation of completion under cyclic composites: incomplete.

The next construction is \(C_A\) and \(T_A:R_A\to P_B\), followed by its comparison 2-cell. No work in `research/grothendieck/` is mutated.

## Verification

- `research/voevodsky/checkers/check_cyclic_residue_categorical_completion.py`
- `research/voevodsky/results/cyclic_residue_categorical_completion.json`
- `research/voevodsky/results/spectral_shift_transport.json`
