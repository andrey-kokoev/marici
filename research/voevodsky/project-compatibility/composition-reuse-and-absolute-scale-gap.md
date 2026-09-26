# Composition synthesis: prior closure and an absolute-scale gap

## Prior results recovered

1. `research/benincasa/cosmology-boundary-correction-composition-audit.md` and its checker/receipt already compare the actual direct A12->A16 lower-edge correction with the translated A12->A14 correction followed by A14->A16. At prime32003 the two K-pole cases have respectively40 and66 source coefficients and zero coefficient difference. This is stronger than equality modulo a source syzygy. It is a prior finite source result, not a fresh all-degree or characteristic-zero theorem. We inspected the receipt and checker; we did not rerun that potentially expensive source computation or edit owner outputs.
2. `research/nima/canonical-coherence-composites-need-depth-independent-condition-bounds.md` already formulates the general composition/completion issue. It correctly separates finite coherence from uniform control and gives an anisotropic exponential-growth counterexample. A further correction is needed to its proposed sufficient condition.

Neither generic compositional coherence nor its possible depth instability is a new research topic here.

## Precise gap: condition number does not control absolute scale

The prior note proposes uniform kappa(T)=||T|| ||T^-1|| for canonical transports and connects this to bounded-energy preservation. Uniform kappa does bound the condition numbers of comparisons. It does NOT imply uniform forward and inverse bounds or E(Tx) comparable to E(x) with fixed constants.

Freeze the usual norm on a one-dimensional real fiber. For T_n=2^n id,

    ||T_n||=2^n, ||T_n^-1||=2^-n, kappa(T_n)=1.

For the quadratic energy E(x)=|x|^2, E(T_n x)/E(x)=4^n. Reversing transport produces collapse with exactly the same condition number. Changing the fiber norm with n would change the frozen problem, not solve it.

This is compatible with perfect coherence. Assign each presentation a potential a(tau), and define U(tau,tau')=2^(a(tau')-a(tau)) id. Every composition telescopes and every loop is identity. On the rotation graph of bracketings choose a(tau) to be graph distance from the canonical bracketing. Adjacent differences have absolute value at most1, so each elementary map and inverse has norm at most2. Distances are unbounded across word lengths, hence some composites grow without bound. Every condition number is still1. This is a logical falsifier of the proposed sufficient bound, not evidence that a particular physical source implements these rescalings.

## Corrected sufficient hypotheses

For carrier-energy preservation require independent uniform bounds

    sup ||T_tau|| < infinity and sup ||T_tau^-1|| < infinity

in the actual source norms, or uniform two-sided energy/seminorm estimates. A condition-number bound becomes sufficient only with an additional absolute-scale anchor controlling, for example, the norm ratio on a nonzero reference vector in each fiber. Such an anchor must be independently source-authorized.

For a readout-only objective this can be stronger than necessary. If F_j:X_(j-1)->X_j and O_j:X_j->R are admitted maps with a fixed reading type R and

    O_j F_j = O_(j-1),

then induction gives O_n(F_n ... F_1)=O_0. In a normed-linear model, a uniform bound ||O_n||<=C yields

    ||O_0 x|| <= C ||F_n ... F_1 x||.

This is the relevant readout-sized recovery estimate, not a uniform inverse on every carrier coordinate. Extension to completions additionally needs the stated continuous maps and complete reading target. It does not itself prove that an arbitrary infinite assembled state belongs to a source's bounded-energy domain.

Thus retain two different obligations:

- preservation of the admitted completed carrier or bounded-energy class;
- stable preservation of the independently intended observation.

Do not replace either by a dimensionless condition-number test.

## Disposition for the recovered sector composition

The actual cosmology result supplies finite algebraic composition of two specified correction words. Its mod32003 coefficient comparison supplies neither an Archimedean norm nor characteristic-zero lifts with uniform size control. The completion hypotheses cannot be checked from that receipt alone; nor does the scalar counterexample refute the finite source identity.

The productive synthesis result is a bounded correction to the proposed composition-to-completion criterion, not another universal coherence framework. Any next analytic promotion must name source-authorized absolute normalization and topology, or explicitly restrict its claim to readout recovery.

## Verification and ownership boundary

`check_composition_absolute_scale.py` checks the stored finite-source receipt's stated scope and exact scalar composition/conditioning/energy controls. The all-depth counterexample is the formula above, not an inference from finitely many samples. Owner documents and results are read-only; this note records a proposed correction, not owner acknowledgment or adoption.
