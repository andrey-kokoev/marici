# The synthesis-to-certificate test produces an accepted control word

## Question and disposition

Try to falsify the proposed executable source-bound storage realization at its
actual missing boundary: a proposed control word must survive exact execution,
source-policy replay, numerical target certification, and end-to-end bounds.
A bounded numerical search failure alone would not refute the all-tolerance
existence/termination claim.

The attempt instead produces the first accepted word in this line of work:
312 conjugated bank phase gates, with certified bright-sector encoding error
at most 0.08543395404933576 (decimal display of an exact rational bound).
It meets an encoding tolerance of 1/10 and a free-storage decoded/contact bound
below 0.171. The identity word is rejected on an actual normalized contact input.

This is one finite constructive witness, not a terminating compiler for every
tolerance, an efficiency theorem, a formal WG term, or a physical device.

## Candidate generation, kept separate from evidence

`checkers/scout_encoder_control_word.py` uses NumPy/SciPy to optimize eight layers
of the 39 existing conjugated bank directions. A fixed random seed determines
the orders and initial phases. It uses a numerical polar factor as an optimization
target only. Three finite-difference gradient controls check reverse-mode signs.

The run stops after 1470 L-BFGS-B iterations. Its numerical Frobenius error is
about 0.08543297; this number does NOT authorize acceptance. Each optimized phase
is replaced by an exact dyadic stereographic parameter with denominator 2^36.
The resulting 312 proposed controls are saved independently of the verifier.
The finite search ran to its stopping criterion, not a promised universal bound.

## Permitted word and exact execution semantics

For every proposed gate, its direction index refers to an actual retained word
V_j of seam reflections, occurrence-memory writes and native rotation. The
verifier rebuilds those primitives from the source and independently replays every
conjugating word on the original frame-zero bank direction.

For a dyadic parameter t, use the existing exact field phase

    z(t)=(1-3t^2)/(1+3t^2) + i sqrt(3)*2t/(1+3t^2).

Its norm is exactly one. The conjugated gate is

    V_j [I+(z(t)-1)P_bank] V_j^-1.

Chronological implementation applies V_j^-1 first, then the bank gate, then V_j.
Every constituent is metric-unitary. No continuous phase actuator on a seam or
memory-write projector is introduced. Expanding the conjugations gives 2184
primitive operations when R^-1 is counted as one macro. Replacing each R^-1 by
two R operations would change that count and is not silently included.

The inverse recipe reverses gate order and negates every t. It recovers arbitrary
full input states exactly in this ideal software model. The source/frame and
composition assumptions are the same ones used in the conditional controllability
proof; this is not physical scheduling authority.

## Independent exact-metric acceptance

`checkers/check_encoder_control_word_acceptance.py` does not use the scout's
floating error for acceptance. It:

1. Validates source hashes and reconstructs every discrete conjugation and bank
   phase from exact rational data.
2. Checks the bright-domain source invariance, native-energy annihilation and
   the actual contact Gram 3I.
3. Replays the polar evaluator's degree-268 rational polynomial, exact kernel
   projectors and positive spectral bounds. It compares the reconstructed W_N
   entrywise with the evaluator output and recomputes its geometric tail.
4. Propagates the exact phase formulas in Q(i sqrt(3)), deliberately rounding
   certification arrays to dyadics after each gate. Each rounding error is
   bounded explicitly; unitarity prevents its amplification by later gates.
5. Computes the exact metric Hilbert-Schmidt discrepancy between those arrays
   and the rational polar approximation on the five bright columns. An upward
   dyadic square-root bound is checked by exact squaring.
6. Adds polar-evaluation and certification-rounding errors, and accepts only
   when their total is strictly below 1/10.

The implemented word is the exact unitary word. Rounded certification arrays
and the nonunitary polar polynomial are NOT substituted as execution gates.

For a 45-by-5 rounding matrix, each real and imaginary coefficient has error at
most 2^-96; complex squared entry error is at most 4*2^-192. With physical target
metric G and source bright metric g, weighted Hilbert-Schmidt norm is bounded by
sqrt(tr(G) tr(g^-1)) times ordinary Frobenius norm. The verifier uses a larger
rational constant and checks the requisite squared inequality. Summing that
bound over the 312 gates charges every rounding step.

## End-to-end consequence

Let delta be the certified bound above and A the accepted ready-memory map.
With the unchanged fixed free-storage Hamiltonian and actual ideal intertwiner,
`encoder-end-to-end-certificate-scope-v1.md` gives uniformly in the mathematical
storage parameter:

- encoded free-storage state error <= delta;
- decoded recovery error <= 2 delta;
- co-transported contact-amplitude error <= 2 delta.

The contacts must be produced by the SAME exact accepted word applied to the
ready raw contact columns and normalized by sqrt(3). The verifier retains this
recipe. Reusing the original contacts or rounded certification arrays would not
satisfy the contract. Ongoing coupled-lead dynamics, arbitrary initial stored
memory, noise, and control-work accounting are not covered by these bounds.

## Verification and artifacts

    OPENBLAS_NUM_THREADS=1 uv run --offline --with numpy --with scipy python research/strominger/checkers/scout_encoder_control_word.py --layers 8 --iterations 1500
    python research/strominger/checkers/check_encoder_control_word_acceptance.py

The final exact checker exits 0 with `word_accepted: true`; it was rerun after
adding independent polynomial replay and the identity-word rejection control.
The Python numerical dependencies were preflighted in the same offline uv
invocation family. No package installation into the system environment occurred.

- `results/encoder-control-word-scout.json`: proposed exact dyadic controls and
  numerical-search metadata, explicitly marked scout-only.
- `results/encoder-control-word-acceptance.json`: exact accepted bounds, inverse
  recipe, source hashes, operation count and scope.

The conjecture survives this implementation test. The new evidence closes the
absence of any accepted word, but not the universal compiler or formal WG
composition claim. No formal-kernel check, graph publication, commit or push.
