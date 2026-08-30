# Transition balance cannot remove transition-specific memory

The order-two de Bruijn schedule balances all sixteen ordered treatment pairs. That completely removes additive memory depending only on the preceding treatment. It does not identify the associator when the disturbance depends jointly on the preceding and current treatments.

Write the mean observed after transition from `a` to `b` as

\[
y_{ab}=s_b+m_{ab}.
\]

Even exact knowledge of all sixteen values leaves a four-dimensional kernel. For any four numbers `k_b`, replace `s_b` by `s_b+k_b` and `m_ab` by `m_ab-k_b`. Every observation remains identical.

The executable hostile starts with zero signal and zero memory. A second model shifts only `L1` by `3/5` and subtracts `3/5` from every transition entering `L1`. Both models give the same complete transition table, but their associators are respectively zero and `3/10`. Replication, randomization, and balance cannot distinguish them.

This is a structural non-identifiability result. No schedule-only repair exists for unrestricted transition-specific memory. The optical apparatus needs an intervention: insert a certified memory-erasing reset before each measured crossed cell, or independently calibrate the complete transition response. A reset predecessor with verified zero carryover exposes each `s_b` directly.

This is the experimental counterpart of the admissible-frame condition. Algebraic character inversion is not enough when the carrier supplies an unconstrained connection term that shares the signal's current-cell character.

Executable witness: `checkers/check_transition_specific_memory_falsifier.py`.
