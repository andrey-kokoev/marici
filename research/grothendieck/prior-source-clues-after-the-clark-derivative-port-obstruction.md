# Prior-source clues after the Clark derivative-port obstruction

## Main finding

The prior source already supplies a local mixed Green identity and an attachment architecture that avoids composing singular moment-transpose columns with a first-order resolvent. The highest-value continuation is to use those existing source operations and compute their reciprocal arithmetic gluing. Rebuilding a local conservative realization would duplicate existing work.

This is a document audit. The cited packets' reported verification was not rerun.

## 1. The mixed forcing reservoir is already constructed

`research/nima/one-sided-mixed-green-block-is-closed-by-the-forcing-reservoir.md` starts with (partial_q+z)G_z=-Phi and proves

(z+conjugate(w))<G_w,G_z>
 = conjugate(G_w(0))G_z(0)-<Phi,G_z>-<G_w,Phi>.

With I_z=(Phi+G_z)/sqrt(2), O_z=(Phi-G_z)/sqrt(2), the mixed source terms become <I_w,I_z>-<O_w,O_z>. The local endpoint/forcing balance is therefore explicit on the actual stable tails.

This is more directly relevant than the recent scalar-state completion. It preserves the forcing as a channel. Its remaining obligation is global reciprocal sewing and transport through primitive, square, connected, and archimedean arithmetic currents.

## 2. Actual moment ports are smooth forcing columns

`research/voevodsky/the-full-line-translation-resolvent-realizes-the-one-sided-theta-transform-as-an-exact-source-to-endpoint-cross-entry.md` realizes the zeroth and first moments using

f_0(q)=1_(q<0)Phi(-q), f_1(q)=(-q)1_(q<0)Phi(-q),

with endpoint evaluation after the selfadjoint translation resolvent. These are forcing vectors in the admitted L2 model, and the resolvent sends them into H1 where the endpoint trace exists.

Thus the word 'moment' refers here to weighting the source by q. It does not authorize replacing f_1 with -delta_0', the transpose of a derivative evaluation. The derivative-port divergence diagnoses that attempted identification, rather than invalidating the smooth source-to-endpoint entries.

Caution: the same packet writes a full two-by-two rigged Weyl matrix involving the endpoint delta. Its singular self-entry requires its boundary-domain interpretation. Validity of the smooth cross-entry alone does not settle that self-entry.

## 3. Use boundary values and fluxes on their correct rungs

`research/voevodsky/the_doubled_half_line_derivative_realizes_the_full_rigged_green_real_boundary_ladder_20260911.md` gives explicit doubled H1 traces, Green matrix diag(-1,1), reciprocal action, and isotropic wall domains. It distinguishes:

- endpoint delta as a distributional transpose;
- exp(-r) as the graph-metric Riesz representative;
- the lack of a bounded ambient L2 trace.

This is the concrete boundary model for interpreting singular incidence. Substituting the graph Riesz representative changes the metric representation and must be accompanied by its Riesz map; it cannot silently repair the old resolvent product.

`research/nima/correction-the-four-port-observer-may-match-the-doubled-joint-trace-space.md` adds a relevant counting correction: four ports can represent Gamma_0 and Gamma_1 for two boundary channels. Treating all four as interchangeable forcing coordinates loses that distinction. Its proposed first test is the coefficient Green matrix and a source-derived value/flux splitting.

## 4. A coupled wall/profile extension already exists as a source construction

`research/nima/orthogonal-boundary-coupling-constructs-a-conservative-wall-theta-profile-extension.md` retains a native wall relation and a separate theta profile incidence B_theta. It couples them over the same boundary source c:

Gamma_0^wall f=c,
Gamma_1^wall f+M_theta(lambda)c=0,

M_theta=B_theta* (A-lambda)^-1 B_theta.

The opposite boundary orientations cancel in the Green identity. The source incidence supplies its own return; it is not identified with the native endpoint transpose. The packet retains both principal-value and spectral-jump contributions on the seam.

This provides the candidate common attachment relation to compare with the Clark completion. Its identification with the independently specified completed Green operator remains open in that packet.

## 5. Kernel realization is available, with its sign information retained

`research/voevodsky/the-generalized-nevanlinna-functional-model-supplies-the-conditional-abstract-boundary-relation.md` constructs an abstract boundary relation from the reflected kernel, conditional on finite negative index. Its Cayley transform preserves the negative-square count. It supplies an abstract comparison target, but a positive model or a unitary identification with the arithmetic differential carrier is a further theorem.

`research/voevodsky/correction-the-external-green-comparison-is-a-boundary-triple-problem-not-a-direct-intertwiner.md` locates the endpoint and Euler actions in different directions of a Heisenberg/Clifford system. It reports the signed pullback identity already established and isolates positive odd-endpoint control as the remaining stronger statement. This is a warning to avoid another direct differential-operator identification.

## Successor calculation selected by these clues

Use the existing local mixed identity on both stable tails. Apply the actual fixed Clark codiagonal to the source/endpoint records while retaining their input/output reservoir terms. Compute the resulting polarized form and compare it with the already recorded signed Green pullback on the common labelled core.

This calculation should expose the remaining global arithmetic term explicitly. It requires neither a fresh scalar-state completion nor the undefined derivative-transpose resolvent product. Positivity must be assessed on the resulting form after the reciprocal attachment has been calculated.
