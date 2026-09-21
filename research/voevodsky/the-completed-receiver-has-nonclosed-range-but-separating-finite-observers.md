# The completed receiver has nonclosed range but separating finite observers

## Result

The weighted-l1 completion from `endpointwise-separation-and-bounded-differentials-close-the-fixed-depth-l1-receiver.md` is injective but already at depth one has nonclosed image in the unweighted cut-l1 target. This can be proved in the vacuum sector, without Clark conditioning estimates.

Nevertheless finite-endpoint ambient paired observations separate every element of the completed source, and their induced functionals are weak-star dense in its continuous dual. Thus the completion supports faithful weak paired observation, not stable reconstruction in the target norm.

## 1. A fixed image with an increasing source cost

Let a be the forgotten diamond relation on the first two events. Follow it by the unique selected all-forgotten route w_n through n-2 further distinct events, and put v_n=[a w_n] in the n-event endpoint conormal corner I/I^2.

The path derivative obeys

    D(a w_n)=D(a) rho(w_n)+rho(a) D(w_n)=D(a),

where the right side retains the full outer endpoint via its vacuum suffix buffer. The four first-diamond edges have coefficients +1,+1,-1,-1, so its cut-l1 norm is exactly four. The output endpoints vary with n; the displayed equality concerns its local edge coefficients, not an identification of different outer endpoint summands.

All paths in this endpoint corner have length n. The source presentation norm weights every path coefficient by

    W_n=(1+n) a_bound^n,

with the fixed a_bound>=1 from the uniform letter estimate.

Let ell be the coefficient of the first root-to-first-event edge with vacuum prefix, Omega seam letter, and vacuum suffix in D. Its value on any marked path basis vector has absolute value at most one: the monotone path can cross that edge at most once, and this vacuum coordinate requires every event to be forgotten. The product rule shows D(I^2)=0, so ell descends to I/I^2. Also ell(v_n)=1. Consequently

    W_n <= ||v_n||_source <= 2 W_n,
    ||j(v_n)||_target=4.

Normalizing v_n to source norm one gives target norm at most 4/W_n, which tends to zero. A bounded injective map between Banach spaces with closed image would have a bounded inverse on that image. This family rules that out.

## 2. A literal missing range point

Choose a subsequence n_k with 4/W_(n_k)<=2^(-k), and let x_k be the corresponding source unit vectors in distinct endpoint corners. The series

    y=sum_k j(x_k)

converges absolutely in the target. Every partial sum is in the receiver image. But y has no source preimage: endpointwise injectivity would force a preimage to have coordinate x_k at every selected endpoint, whose source l1 norm is infinite.

This is a target limit outside the image, not a nonzero source vector mapped to zero. It does not contradict completed injectivity.

## 3. Positive paired observability survives

Write the completed source as X=l1 direct_sum_c G_c with finite-dimensional endpoint corners, as in the preceding theorem. For each corner retain the finite source-generated target envelope inside its prescribed signature-closed ambient carrier.

The finite injection j_c and nondegenerate ambient form imply that every functional in the conjugate dual G_c^h is obtained by pairing j_c with some ambient observer. No inverse of the restricted source Gram is used. A finite collection of such observers lies in the target's finite-support carrier and gives a continuous source functional.

If x is nonzero, one endpoint component x_c is nonzero. A finite-corner observer detects it. Thus finite-support ambient observations separate X.

More strongly, every finite-support functional on X is realized this way. The continuous dual of this l1 sum is the bounded product of the corner duals. Its finite-support truncations converge weak-star: for x in X, the omitted pairing is bounded by the functional's sup norm times the summable endpoint tail of x. Therefore the induced finite-support observations are weak-star dense in X^h.

The ambient norms of observer lifts need not remain bounded. This result is neither a bounded right inverse to the observation map nor surjectivity onto the full source dual. It supplies exact weak separation, not uniform measurement stability.

## 4. Disposition for the lane

Keep the completed source as a stronger Banach domain continuously and injectively mapped into the balanced analytical carrier. Its endpointwise paired observations are faithful, its seam differential is bounded at fixed depth, and its relative current identities are continuous.

Do not promote it to a closed embedded source in the ambient cut-l1 norm. Such a strengthening requires a different, explicitly justified topology or additional source controls. The vacuum counterexample shows that theta-tail improvements alone cannot provide it.

These conclusions concern the specified monotone coefficient completion, not all inverse-limit families or a universal terminal-invariant metric.

## Verification

`uv run python research/voevodsky/checkers/check_completed_receiver_closed_range_obstruction.py`

Checks the exact forgotten-suffix derivative family through length 64. The quotient norm bound, infinite subsequence argument, and weak-star observation result are the proofs above, not extrapolations from finite rank tests.
