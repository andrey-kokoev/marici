# Clark source interface: domains, complete packets, and the strength of positivity

## Outcome

Following the actual tail and sewing construction gives three concrete advances:

1. An explicit weighted source domain supports all four tails, endpoint traces, mixed Green terms, and their completion on each bounded spectral region.
2. The full forcing reservoir on spectral packets requires the coefficient-sum channel. It is not just a sum of scalar reservoir values.
3. For the declared completed-xi normalization, positivity on **every finite Euler-chart packet** is already equivalent to RH, using the classical Nevanlinna–Pick theorem and the Hadamard product. It is not a routine consequence of completing the signed kernel identity.

The arithmetic-history Jordan obstruction imposes a separate descent constraint. It does not by itself decide the Clark kernel's positivity.

## 1. Source trail and typed comparison table

Inspected sources:

- `../nima/one-sided-mixed-green-block-is-closed-by-the-forcing-reservoir.md`
- `the-full-line-translation-resolvent-realizes-the-one-sided-theta-transform-as-an-exact-source-to-endpoint-cross-entry.md`
- `the-completed-clark-pair-is-a-fixed-codiagonal-sewing-of-four-oriented-resolvent-cross-entries.md`
- `../grothendieck/reciprocal-clark-sewing-leaves-one-explicit-forcing-correlation-row.md`
- `../grothendieck/clark-sewing-to-the-endpoint-gamma-prime-green-kernel.md`
- `../grothendieck/closure-generated-arithmetic-history-and-its-terminal-metric-obstruction.md`

| Layer | Actual carrier/map | Established comparison | Boundary still requiring attention |
|---|---|---|---|
| Source forcing | Real Phi, with f_0=Phi and f_1=x Phi | Common forcing generates all four tails | Exact theta normalization is inherited from the declared cosine-transform convention; not independently rederived here |
| Oriented bulk | D=-i derivative on L2(R), domain H1(R) | Source-to-endpoint resolvent cross-entry on its natural half-plane | Opposite orientations are not a single entire resolvent chart |
| Four tails | G_(sigma,j)(z) in H1(R_+), j=0,1 | Mixed integration-by-parts identity | Uniform source domain and trace bounds supplied below |
| Endpoint sewing | h in C4, M=D_phase h, output S M in C2 | Fixed matrix gives E,E_star; C=D_phase* S* diag(1,-1) S D_phase | The sewing is signed, not automatically passive |
| Full sewn numerator | N(w,z)=h(w)* C h(z) | N=B+R with all cross-orientation terms | B and R separately have not been identified with gamma and prime channels |
| Arithmetic kernel | K=N/[-i(z-conjugate(w))] | Endpoint-swap + gamma + prime-power expression on the Euler chart | Signed continuation is not a positivity proof |
| Spectral packets | Finite complex coefficients on spectral labels z | Entrywise identities polarize to complete packet forms | Division is pairwise in (w,z), not division of the aggregated numerator by one scalar |
| History memory | Truncated tensor algebra, presentations indexed by words | Actual arithmetic comparison and invariant Jordan subspace | No map identifying this memory form with the Clark spectral form has been constructed |
| Independent Green operator | Its specified completed domain, form, and operations | Scalar-kernel crosswalk available at the declared strength | Domain/intertwining equivalence and prime-resolved source realization remain distinct obligations |

## 2. A common weighted domain actually suffices for the tail calculation

Fix beta>Y>=0 and define the complex Hilbert source space

`H_beta = {Phi : exp(beta x)(1+x)Phi(x) in L2(0,infinity)}`,

with norm `M_beta = ||exp(beta x)(1+x)Phi||_2`. Use its real subspace for the real-forcing symmetry conventions. Compactly supported smooth functions on the open half-line are dense in this weighted L2 space.

For j=0,1, sigma=+1,-1, and |Im z|<=Y, set

`G_(sigma,j)(z;x) = integral_x^infinity exp(sigma i z(t-x)) t^j Phi(t) dt`.

Cauchy–Schwarz gives, with a=beta-Y>0,

`|G_(sigma,j)(z;x)| <= M_beta exp(-beta x) / sqrt(2a)`.

Indeed, bound the exponential by exp(Y(t-x)) and split exp(Yt)f_j(t) into exp(-a t) times exp(beta t)f_j(t). Consequently

`||G_(sigma,j)(z)||_2 <= M_beta / (2 sqrt(beta a))`,

`|G_(sigma,j)(z;0)| <= M_beta / sqrt(2a)`.

In the weak sense,

`G' = -sigma i z G - f_j`.

Thus G lies in H1, and on |z|<=Z,

`||G||_H1 <= (1+Z) M_beta/(2 sqrt(beta a)) + M_beta`.

These are actual bounded source-to-tail and source-to-trace maps. On compactly supported forcing, integration by parts has no infinity boundary term. The bounds extend the identity to H_beta by density: all tail pairings, forcing pairings, and endpoint values are continuous in that norm.

For real Phi, the correlation row also has an explicit dominating bound. With

`A(d)=integral_0^infinity Phi(x) f_1(x+d) dx`,

one has

`|A(d)| <= exp(-beta d) ||exp(beta x)Phi||_2 ||exp(beta x)f_1||_2`.

The same estimate holds with absolute values inside the integral. Since |sin(zd)|<=exp(Yd), it supplies the Fubini bound for the reduced forcing row whenever beta>Y. Polynomial factors in d, including the real-diagonal divided-difference limit, remain integrable.

Completed theta forcing has the required superexponential decay and hence belongs to every such weighted space, subject to the forcing convention of the source packet. This provides a compatible family of domains over spectral compacta, not a spectral-uniform bound for one unweighted source space over the whole plane.

**What this closes:** the tail/sewing identity has a concrete continuous extension from a common dense source domain. **What it does not close:** equivalence with an independently specified completed Green operator or its domain.

## 3. The endpoint delta requires a separate typing decision

The valid cross-entry is

`E_0 (D-z)^(-1) f_-`,

because f_- lies in L2, the resolvent maps L2 into H1, and evaluation E_0 is bounded on H1.

The formal two-port expression involving `E_0 (D-z)^(-1) delta_0` needs more care. For Im z>0,

`(D-z)^(-1) delta_0 = i exp(izq) 1_(q>0)`

distributionally. This function has a jump and is not in H1. Ordinary H1 endpoint evaluation therefore does not define that diagonal entry. Left, right, or symmetric traces, or a specified boundary-triple regularization, give additional conventions; they cannot be silently inferred from the valid source-to-endpoint cross-entry.

This is a domain qualification on the formal full Weyl matrix in the inspected note, not a refutation of the four smooth-source cross-entries or the sewn scalar-kernel identity. The present audit does not choose a new trace convention.

## 4. Complete finite spectral packets retain the reservoir's unit channel

For a finite packet c on spectral labels z_k, define

`lambda(c)=sum_k c_k`,

`U_a(c)=sum_k c_k G_a(z_k)`,

`V_a(c)=sum_k c_k z_k G_a(z_k)`,

`h_a(c)=sum_k c_k h_a(z_k)`.

The polarized numerator is `N(c,d)=h(c)* C h(d)`. Its bulk term is

`B(c,d)=i sum_ab C_ab [sigma_b <U_a(c),V_b(d)> - sigma_a <V_a(c),U_b(d)>]`.

Write

`r(c)=<Phi,U_(-,1)(c)-U_(+,1)(c)>`.

Then the exact packet reservoir is

`R(c,d)=conjugate(lambda(c)) r(d) + conjugate(r(c)) lambda(d)`.

The coefficient sums are forced by polarization of the source terms: the fixed forcing vector in one slot contributes the sum of coefficients in that slot. Omitting these factors is not an identity for signed or complex packets. The new checker verifies the formula symbolically with independent channel and packet entries.

For the divided kernel, retain the spectral indices and form

`sum_ij conjugate(c_i) d_j [B(z_i,z_j)+R(z_i,z_j)] / [-i(z_j-conjugate(z_i))]`.

In general there is no single denominator for the aggregated B(c,d)+R(c,d).

## 5. A signed feature realization, without assuming positivity

For Im z>0, let k_z(t)=exp(izt) in L2(R_+). Then

`<k_w,k_z> = 1/[-i(z-conjugate(w))]`.

Therefore the declared Clark kernel is exactly the signed Gram kernel of

`z -> (E(z)k_z, E_star(z)k_z)`

in `L2(R_+) direct-sum L2(R_+)` with signature diag(1,-1).

This yields a precise positivity criterion. On finite spectral packets let

`T_+ c=sum_k c_k E(z_k) k_(z_k)`,

`T_- c=sum_k c_k E_star(z_k) k_(z_k)`.

Every finite packet matrix is positive semidefinite exactly when

`||T_- c|| <= ||T_+ c||`

for every finite packet. Equivalently, `T_+ c -> T_- c` is well-defined and extends to a contraction between the closures of the indicated feature ranges. Well-definedness includes `ker T_+ subset ker T_-`.

This is a contraction **criterion**, not a construction of the contraction. The signed feature space is already explicit; replacing its minus sign by a plus sign would change the kernel.

## 6. The all-packet Euler-chart inequality is already RH-strength

This section is a mathematical implication using the classical Nevanlinna–Pick interpolation theorem, not an Agda or numerical certification and not a claim of a new RH proof.

Freeze

`X(z)=xi(1/2-iz)`, `m(z)=-X'(z)/X(z)`.

On the Euler half-plane Omega={Im z>1/2}, X has no zeros. The scalar crosswalk gives

`K(w,z)=2 conjugate(X(w)) X(z) P_m(w,z)`,

`P_m(w,z)=[m(z)-conjugate(m(w))]/[z-conjugate(w)]`.

The endpoint–gamma–prime sum is precisely P_m after the declared change of variables. On each finite Euler packet the X factors give an invertible diagonal congruence. Thus its odd-endpoint domination inequality is equivalent to positivity of every finite Pick matrix for m on Omega.

### All Euler packets positive implies RH

The finite Nevanlinna–Pick theorem gives an upper-half-plane Pick interpolant for every finite set of these prescribed values. Apply it to increasing finite subsets of a countable dense set in Omega. After a Cayley transform, normal-family compactness gives a Schur limit interpolating all those values, hence a Pick function on the entire upper half-plane agreeing with m on Omega.

An anchor with strictly positive imaginary part prevents degeneration to a boundary-valued constant. Such an anchor exists under the positivity assumption because m is analytic and nonconstant on Omega; an analytic function taking only real values there would be constant.

By meromorphic identity, this Pick extension equals -X'/X wherever defined in the upper half-plane. Every zero of X there would give a nonremovable logarithmic-derivative pole, impossible for the holomorphic Pick extension. Reality of X excludes lower-half-plane zeros as well. Hence all X zeros are real, which is RH in this spectral coordinate.

This step uses the interpolation/extension theorem. It is **not** a claim that positivity follows from analytic continuation of the signed formula.

### RH implies all packets positive

Under RH the standard even Hadamard product for X has real paired zeros ±t_n, with multiplicities, and sum_n 1/t_n^2 finite. Its logarithmic derivative gives

`m(z)=sum_n [1/(t_n-z)+1/(-t_n-z)]`.

Each real-pole summand has positive Pick kernel

`1/[(r-conjugate(w))(r-z)]`.

The paired series converges locally and its finite packet matrices are positive semidefinite. Multiplication by the X factors preserves positivity. This proves the converse.

**Consequence:** proving the full Euler-chart finite-packet inequality is already equivalent to RH under the frozen completed-xi convention. Testing only scalar diagonals, or a finite collection of small packets, is strictly less information. Completion estimates cannot replace the missing all-packet contraction theorem.

## 7. How the history obstruction constrains, but does not decide, this comparison

The history note constructs an actual same-terminal unipotent comparison with invariant subspace span(1,d,d^2). Its real symmetric invariant forms are

`[[a,-e/2,-e],[-e/2,e,0],[-e,0,0]]`,

with determinant -e^3. A positive semidefinite invariant form annihilates d and d^2; a nondegenerate invariant form there is indefinite.

Thus an injective, isometric identification of this whole subspace with one **positive-definite terminal-indexed invariant** Green space is impossible. But this does not prove that the Clark kernel fails positivity: no map identifying that Jordan representation with the Clark spectral feature representation has been provided, and the comparison invariance requirements have not been identified.

Any proposed bridge must specify:

- a history-indexed family of forms, rather than silently descending to terminal n;
- or an indefinite form and its preserved pairing;
- or an explicit quotient, acknowledging the comparison directions it kills.

The chosen source, its terminal integer, its word presentation, and a spectral label z are different types. No equation in the scalar Clark crosswalk identifies those indices.

## 8. Verification and next action

New checker:

`uv run --with sympy --with mpmath python research/voevodsky/checkers/check_clark_source_interface_audit.py --replay-existing`

Passed:

- exact polarized packet reservoir formula, including coefficient sums;
- failure of the formula with those sums omitted;
- exact Clark/Pick sign and factor;
- exact terminal Jordan invariant-matrix family and determinant;
- replay of Grothendieck's Gaussian polarized sewing checker;
- replay of Grothendieck's completed-xi arithmetic crosswalk checker, including its analytic prime-tail bounds.

Upstream checker code was executed unchanged, with only its `__file__`-relative artifact location redirected to a temporary directory. Original research-stream evidence files were not overwritten. Source hashes and replay outputs are retained in `results/clark-source-interface-audit.json`.

The checker does not prove the analytic domain estimates or the Pick/RH equivalence above. It also does not recheck the embedding of the Jordan block in the arithmetic tensor algebra, prove positivity, or certify every special-function value by intervals.

**Next construction:** specify the independently prescribed Green operator/domain and a candidate map from the retained source to it; test its full polarized local data, including the reservoir and the trace convention. The bounded tail domain above can supply the source side. If the requested conclusion includes positive all-packet contraction for the completed-xi kernel, record that as the RH-strength theorem itself, not as a routine consequence of the boundary-semantics machinery.
