# Quarter-source capacity-proportional branching

## Question

Does one uniform local branching rule realize exact Hall transport by distributing each negative source mass proportionally to positive capacities in its interlacing neighborhood?

## Claim boundary

Exact rational evaluation across all 769 bounded cases finds the rule feasible in only 86. Its first failure occurs for base `(2)`, endpoints `0,1`: the positive index `(0,2)` is overloaded by an exact factor greater than one. This rejects capacity-proportional local branching, not other local kernels, global flow solutions, or source recurrences.

## Disposition

Reject the capacity-proportional branching rival. Preserve unrestricted max-flow feasibility. The surviving mechanism must coordinate allocations across negative vertices rather than normalize each neighborhood independently; the next nonredundant test is whether exact max-flow solutions admit a uniform augmenting-path or recurrence rule.
