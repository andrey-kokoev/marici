# RH operation/composition squares: six cell audit

Dictionary: `research/conjecture_net/contracts/rh-stage-dictionary.v1.json`.
Checker: `research/voevodsky/checkers/check_rh_operation_composition_audit.py`.
Receipt: `research/voevodsky/results/rh-operation-composition-audit-v1.json`.

Run `uv run research/voevodsky/checkers/check_rh_operation_composition_audit.py --replay` for fresh exact upstream suites. Normal execution validates the retained replay, source hashes, cell coverage and scoped controls without repeating those suites.

## Scope and result

All six required operation/composition cells are accounted for. Four have positive witnesses at their declared scope; two retain rejected operation identifications rather than replacing native operations. The radial/spectral positive witness is an analytic argument on a declared regularized core, not an infinite-domain result inferred from finite checks.

This closes the operation/composition audit for the frozen inventory, conditional on its declared analytic conventions and core. It does not close identity/continuation, completed test/dual domain transport, a common source for the independent channel and carrier branches, or the stagewise-interface assembly.

| Cell | Witness/disposition | Verification |
|---|---|---|
| `finite-squares` | Six repaired full-permutation reductions, generator/form/energy gates and composite exactly equal to original P | Fresh carrier and six-step suites |
| `history-generator` | Full endpoint continuous-generator square and coherent actual-history sections | Fresh active/full endpoint suites at dimensions 10,16,26,42 |
| `native-tick-no-go` | Fixed same-tick intertwiner is zero; added Fourier stays a different operation | Fresh rank-16 full endpoint system and rank-8 active system |
| `generator-quarter-turn-no-go` | Skew quarter-flow differs from full Fourier by twice the alternating projector | Fresh carrier suite, discrepancy rank one |
| `lattice-weyl-bonding` | Additive Fourier lift, finite convolution, Weyl phase and dyadic bonding | Fresh rational formal-phase suite; analytic formulas below |
| `radial-spectral-square` | Oriented half-density conjugation and gamma matrix followed by spectral reflection | Existing kernel argument, explicit regularization derivation below, fresh symbolic parity/reflection checks |

## Finite route and composition witness

The parity-resolved frame preserves the selected four-coordinate embedding E and the independently constructed source action. Each reduction satisfies

    P_step C_n = C_m P_step,
    C_n E_step = E_step C_m,
    N_step C_n = C_n N_step.

The product of the six P_step maps equals the original metric-adjoint P, not a newly fitted endpoint map. With the actual cyclic assignment J,

    J P_total C12 = F_cyc J P_total.

The analytic attachment B_a therefore composes with either reduction route to the same chosen generic comb realization. The original generator-only frame is retained as a hostile: full-tick leakage ranks 1,2,1,0,0,0. The repaired result does not relabel it as successful.

### Angular normalization in the history branch

The implementation factors out sqrt(3) from its rational large-history matrices. Its small rational generator is

    A0 = [[0,2/3],[-2,0]],
    A = sqrt(3) A0.

For Q=[R,V], A_endpoint=Q diag(A,0,0) Q^-1 and the declared J satisfy

    (F-F^-1) J = J A_endpoint,
    O_n L_n = A_endpoint O_n.

Equivalently, the exact suite checks D J=sqrt(3) J A_endpoint0 with A_endpoint0=Q diag(A0,0,0) Q^-1, and transports rational L0 before restoring sqrt(3). Dropping that factor would change the clock convention and break the square. Initial complementary sections and subsequent transported sections are not chosen independently at every stage.

Native endpoint M has polynomial (x^2+x+1)(x^2-x-1). Its spectrum is disjoint from Fourier roots. The full equation F X=X M has rank16, hence X=0. The additional chart operation J^-1 F J is not M and does not commute with it. Likewise, exp(pi D4/4)-C4=2 M_minus retains the alternating character. These rejected identities are exclusions in the positive bounded interface, not unsolved required positive squares.

## Lattice operations: universal finite-packet identity, not sampling inference

For finite c, the two routes both give

    F_R(j_h c)(y) = sum_n c_n exp(-2pi i h n y)
                  = (L_h F_lattice c)(y).

This holds for every y, not just the rational test grid. Convolution expands a finite double sum, so its Fourier image is the product of the two character sums. Translating by b=hk introduces exp(-2pi i b y); modulation by exp(2pi i alpha x) substitutes y-alpha. Direct substitution gives

    T_b M_alpha = exp(-2pi i alpha b) M_alpha T_b,
    F_R T_b = M_-b F_R,
    F_R M_alpha = T_alpha F_R.

Under dyadic bonding n -> 2n, (h/2)(2n)=hn exactly, so both atom and lifted-character routes agree. The suite checks these identities before evaluating formal rational phases, preserving the failed exponential-position embedding as a separate counterexample. These claims concern finite convolution; continuity and limits for infinite packets remain with the analytic child.

## Radial and Mellin operation witness

Use the supplied additive Fourier convention and signed half-density chart

    (U f)_epsilon(u) = exp(u/2) f(epsilon exp(u)).

On its induced image, W_or=U F_R U^-1 by the already derived kernel

    K_(epsilon',epsilon)(v,u)
      = exp((u+v)/2) exp(-2pi i epsilon epsilon' exp(u+v)).

A nonzero atom x0 has radial weight |x0|^-1/2 at log|x0|. Multiplication by the kernel amplitude cancels that weight, leaving exp(v/2) times the Fourier character. This checks that U j_h uses log|hn| and the same Fourier convention, not the previously failed exponential-position chart. The zero atom stays separately retained; this argument does not extend every endpoint distribution to arbitrary growing radial tests.

For a concrete common core take two-component compactly supported smooth functions of log radius, corresponding under U^-1 to smooth additive functions supported away from zero. Regularize the sum-kernel by replacing its last exponential with

    exp[-(delta + 2pi i sigma) exp(u+v)], delta>0,
    sigma=epsilon epsilon'.

For this core the log Fourier integral is absolutely integrable after regularization. Substitution w=u+v gives

    exp(-itv)=exp(-itw)exp(itu).

Thus the input transform is evaluated at -t, not t. With x=exp(w), the multiplier is

    m_(sigma,delta)(t)
      = integral_0^infinity x^(-1/2-it)
          exp[-(delta+2pi i sigma)x] dx
      = Gamma(1/2-it)(delta+2pi i sigma)^(-1/2+it).

The last equality is the standard gamma integral for Re(1/2-it)=1/2 and a complex rate with positive real part, using its continuous principal branch. Taking the Abel boundary delta -> 0+ yields

    m_sigma(t)=(2pi)^(-1/2+it) Gamma(1/2-it)
               exp[-i sigma pi(1/2-it)/2].

Hence, on that regularized/Abel-interpreted core,

    M_log W_or = G(t) R_t M_log,
    G(t)=[[m_+,m_-],[m_-,m_+]], R_t g(t)=g(-t).

This is an operation identity with a specified interpretation, not a claim that an unsmoothed comb has an ordinary globally convergent Mellin integral. Extending it to the dictionary's entire completed test/dual carrier, identifying all endpoint terms and justifying limits there are obligations of `rh-analytic-domain-completion-transport`.

### Independent reflection/parity consistency check

Let q(t)=(2pi)^(-1/2+it) Gamma(1/2-it) and theta=pi/4-i pi t/2. The parity multipliers are 2q cos(theta) and -2i q sin(theta). Euler reflection gives

    q(t)q(-t)=1/[2 cosh(pi t)].

Both cos(theta)cos(theta_ref) and sin(theta)sin(theta_ref) equal cosh(pi t)/2. Therefore the reflected products of the parity multipliers are +1 and -1 respectively. Returning to oriented coordinates gives

    G(t)G(-t)=[[0,1],[1,0]].

Two Fourier operations swap orientations; four return. The symbolic checker verifies these elementary products and the atom-weight cancellation, using the stated gamma reflection identity as analytic input. It does not claim to prove gamma continuation through SymPy.

## Boundaries and verification

`channel-source-binding` remains outside the required positive cells: the independent channel lattice and twelve-arrow carrier are not identified by this audit. All half-phase/ideal-attachment applicability flags remain unbound to RH. No metric equality, new physical clock, all-test positivity or RH result is admitted.

Fresh replay checks the five existing carrier, active, full endpoint, repaired descent and lattice suites. Their receipts must remain byte-identical to the frozen dictionary pins; a changed receipt stops admission and requires review. Four structural hostiles reject missing coverage, promotion of either no-go, and inserting the unbound source identification as a successful cell. Source hashes and the retained replay are validated in subsequent ordinary runs.
