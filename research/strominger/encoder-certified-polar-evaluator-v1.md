# A source-exact polar evaluator survives the compiler's precision falsifier

## Question and disposition

The synthesis framework requires at least one route to a certified implementation;
another failed shortcut would not falsify that claim. Test the fair-search route's
remaining numerical prerequisite: can the exact source-defined polar encoder be
approximated with a rigorous arbitrarily refinable operator-norm error, without
the saved binary64 archive's floor?

Yes, under the inherited finite-dimensional metric. This packet constructs an
exact rational polynomial evaluator and executes it at tolerance 1e-6. It does
not construct a control word, optimized compiler, WG composition or hardware.
The existential synthesis framework is not falsified by this test.

## Exact support and spectral interval

From the stored rational residual B and metrics M,Gamma, reconstruct

    Bsharp=M^-1 B^T Gamma,
    S=Bsharp B.

The checker verifies entrywise that S consists of three identical six-coordinate
blocks plus a zero six-coordinate bank block. Each six-block has rank five and
kernel the constant-amplitude line. Its metric-orthogonal support Q6 is exact;
there is no numerical rank cutoff. The assembled native support Q has rank 15.
An independent rational column basis of B constructs the exact occurrence-memory
support Qmem, also rank 15, retaining its six-dimensional kernel.

On the positive five-dimensional block the exact inherited energy form satisfies

    (1/6) g < g S_positive < (25/9) g.

Both inequalities are certified by strictly positive rational elimination pivots
on their symmetric differences. Deliberately false lower bound 1/5 and upper
bound 2 are rejected. The same interval encloses every positive eigenvalue of
the full source operator, because the block decomposition was checked exactly.

## Rational functional calculus and general error proof

Set b=25/9 and rho=47/50. On the positive support,

    X=I-S/b,
    0 <= X <= rho I.

Let c_0=1 and c_k=c_(k-1)(2k-1)/(2k). The binomial series gives

    S^(-1/2) Q=(3/5) sum_(k>=0) c_k X^k Q.

Every coefficient and finite matrix power is rational. The kernel is annihilated
by Q throughout; no inverse square root is evaluated at zero. Since 0<c_k<=1,
truncation f_N after degree N obeys

    ||f_N-S^(-1/2)Q|| <= (3/5) rho^(N+1)/(1-rho).

All norms are induced by the inherited positive metrics. Because ||B||<5/3,

    W_N=B f_N,
    ||W_N-W|| <= rho^(N+1)/(1-rho),

where W is the exact polar partial isometry. Form

    U_N=[[I-Q,W_N^sharp],[W_N,I-Qmem]].

Its difference from the ideal full encoder has only off-diagonal blocks
W_N-W and its metric adjoint. Its norm equals ||W_N-W||, so the same bound
certifies the entire 45-dimensional encoder, hence its ready-memory restriction.
This is a written spectral-theorem/binomial-tail proof; the checker establishes
its exact finite matrix hypotheses and computes the rational bound.

U_N is an approximation, NOT an exactly unitary control word. A compiler must
still produce exact isometries and separately account for its distance to U_N.
Conflating the evaluator with an executable unitary would repeat the archived
matrix mistake.

## Termination and actual run

For every rational epsilon>0, increase N until

    rho^(N+1)/(1-rho) < epsilon.

Since 0<rho<1, this terminates. Each chosen polynomial is a finite exact rational
calculation. This is mathematical termination; no practical time or memory bound
for arbitrarily small epsilon is claimed.

Fresh final execution:

    python research/strominger/checkers/check_encoder_certified_polar_evaluator.py --epsilon 1/1000000

It chooses degree 268 and certifies a full-encoder norm error at most

    9.845581418188595e-7.

That decimal is a display of the exact rational bound retained in the receipt,
not a measured floating residual. The default tolerance 1/10 was also executed
at degree 82 before adding the two false-bound controls; the final source and
receipt correspond to the repeated 1e-6 run with those controls.

The receipt retains W_N, Q, Qmem, the assembly formula, spectral pivots and
source/checker hashes. All source inputs remain unchanged during execution.
Earlier source suites were not rerun.

## Remaining synthesis obligation

The exact dense word vocabulary and this precision-refining evaluator now give
the two ingredients for a fair baseline search. To turn them into a compiler,
implement an exact-metric acceptance bound for each candidate word, dovetail
precision and enumeration, and retain the accepted word with its certificate.
Strict margin is essential: a failed or threshold-equal candidate must not stall
the whole search. No such accepted encoder word is produced in this packet.

Artifacts:
- `checkers/check_encoder_certified_polar_evaluator.py`
- `results/encoder-certified-polar-evaluator.json`

No optimization comparison, formal-kernel proof, SCC registration, graph
publication, commit or push is claimed.
