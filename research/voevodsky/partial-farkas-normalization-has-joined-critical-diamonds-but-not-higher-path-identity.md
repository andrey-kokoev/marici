# Partial Farkas normalization joins critical diamonds but not higher proof paths

On the fixed primitive interval `[0,1]`, allow a typed partial rewrite consuming a rational `0<=lambda<=c` of the proof surplus:

`(a,b;c) -> (a+lambda,b+lambda;c-lambda)`.

It is sound because the source-row normal relation is `(-1,1)·(1,1)=0` and the primitive upper bound contributes exactly lambda. For any lambda,mu with lambda+mu<=c, doing lambda then mu and doing mu then lambda reach the SAME final Farkas certificate, and both equal one lambda+mu step. Fresh `check_farkas_rewrite_critical_diamond.py` passes 32 finite diamonds, including six with different nontrivial intermediate proofs. It refuses surplus overdraw and a foreign source root; the source-bound-2 control shows the same formula cannot be moved to a different primitive bound unchanged.

The two *rewrite histories* are nevertheless distinct. Joining their final certificates is a local confluence statement, not a declared interchange 3-cell. There is also a termination trap: allowing arbitrary positive rational lambda permits repeatedly consuming half the remaining surplus forever. The earlier all-at-once `lambda=c` normalizer terminates in one step; a discretized grid with a fixed positive quantum could also terminate, but neither licenses arbitrary rational partial-rewrite termination. A proof-relevant higher construction needs explicit generators, support DAGs, a termination convention, and a coherence witness comparing the two paths—not just equality at their tips.

This is the precise scope of what the prior source-rooted interface clue provides: the primitive rows justify every local rewrite, and permitted controls determine whether endpoint equality suffices. It does not automatically equate histories or confer archive/analytic authority.
