# Tiny copier-query nets have one normal form under individual eraser choices

Fresh `check_individual_eraser_alpha_states.py` explores every enabled COPY/Q1/Q2 choice AND every individually enabled ERASE agent, rather than fixing an eraser order. It alpha-quotients full port graphs rooted at OUT1/OUT2 and remaining garbage. Across all 86 input fixtures with support length 0..2 and both query indices 0..n+1, it visits 6,400 graph classes and 13,431 transitions. Every fixture has exactly one reachable terminal alpha-class containing the correct two Boolean outputs; the largest fixture has 119 states and 255 edges. Each rewrite retains the engine's one-symmetric-wire-per-port audit.

This removes the earlier within-family scheduling gap for these small inputs. It does not establish termination or unique normal form for arbitrary finite supports; the lexicographic rank argument and rule-boundary lemma still need a fully specified inductive reachability proof. Local add(i)/union and a surviving reusable support are separate extensions.

Next write a precise inductive component grammar for intended reachable nets and verify all 15 rules preserve it, including detached eraser tails and the temporary query-to-COPY-auxiliary wire. Prove no stuck graph except two BOOL--OUT normal form. This is the missing bridge from exhaustive finite search to a uniform theorem.
