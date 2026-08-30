# One invariant word repairs the measured-ten hostile pair (WP57)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

For the exact WP52 pair with identical measured ten and
(\cos\delta=\pm4/5), fix nondegenerate exact spectra and form
(H_d=V\operatorname{diag}(2,5,11)V^\dagger), (H_u=\operatorname{diag}(1,4,9)).
The single mixed word

\[
I_{11}=\operatorname{Tr}(H_uH_d)
\]

has distinct exact values on the two branches. It is invariant under full
simultaneous weak-basis conjugation and needs no reference port. Thus a
source-derived complementary probe repairs this particular measured-ten
kernel.

This is separation, not selection. Both points remain admissible; adding the
probe refines the contextual partition from one doublet to two singletons but
does not prefer either singleton. The probe is indirectly instrumented by the
mass and CKM measurements that determine it.

Smallest exact falsifier of measured-ten faithfulness: the nonzero difference
of this one scalar invariant. Verification:
`uv run --with sympy python research/flavor/checkers/wp57_invariant_word_complement.py`.
