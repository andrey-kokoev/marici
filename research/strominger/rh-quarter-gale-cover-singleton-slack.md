# Every fixed-eight negative singleton has strict Gale-cover Hall slack

## Question

Is Hasse-local feasibility already nontrivial at the smallest Hall cuts?

## Claim boundary

Yes. Across all 3,584 terminal cases, the exact census tested 54,261 negative singleton demands. Every singleton has strictly positive supply slack in its opposite-parity Gale-cover neighborhood; zero-slack count is zero.

The minimum occurs for base \(\{1,3,4,5,6\}\), exchanged labels \((i,j)=(7,0)\), and negative label \(\{0,2,3,5,6,7\}\). Its cover neighborhood has exactly two positive labels,

\[
\{0,2,3,4,6,7\},\qquad \{0,2,4,5,6,7\},
\]

and positive exact slack. Negative cover degrees range from one to seven; 1,471 negative labels have only one positive cover neighbor, yet all retain strict slack.

This establishes strict singleton Hall inequalities only. Multi-demand subsets can share neighbors, so the all-order and multi-cut problem is not reduced to singleton checks.

## Disposition

The common-architecture handoff remains active. Continue locally by extracting the minimum degree-two singleton identity into its three complementary-minor terms. Its two-supply/one-demand inequality is the smallest Hasse-local source pattern that an all-order proof must reproduce.
