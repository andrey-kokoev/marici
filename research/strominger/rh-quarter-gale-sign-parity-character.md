# Every fixed-eight terminal sign is a checkerboard parity character

## Question

Is the failed single-crossing pattern irregular, or does it arise from a deterministic grading?

## Claim boundary

It is deterministic at fixed \(k=8\). For every nonzero source term in all 3,584 terminal cases,

\[
\operatorname{sgn} w_K=c_{R,S}(-1)^{\sum K},
\qquad c_{R,S}\in\{+1,-1\}.
\]

The exact census tested 108,573 nonzero terms. Exactly 1,792 terminal cases have \(c_{R,S}=+1\), and 1,792 have \(c_{R,S}=-1\). No residual sign defect occurs.

Together with zero-extended log-supermodularity of \(|w_K|\), this identifies the fixed-eight signed source as a checkerboard twist of an MTP2-type nonnegative weight. It remains a finite certificate and does not by itself prove the alternating total or weighted Hall inequalities.

## Disposition

The sign obstruction is now typed rather than irregular. Test the narrowest chainwise consequence: whether every Gale cover joining opposite parity has magnitude dominance toward the case-positive parity. Universal cover dominance would give a local pairing proof; an exact failure would show why the successful transport requires nonlocal Hall flow despite parity and MTP2 structure.
