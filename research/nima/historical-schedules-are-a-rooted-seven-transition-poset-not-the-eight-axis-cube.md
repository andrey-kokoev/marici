# Historical schedules are a rooted seven-transition poset, not the eight-axis cube

The attempted schedule dictionary fails at the level of types.

Historical schedules use

\[
0,A,J,P,C,T,E,F,
\]

where `0` is the initial source object and the remaining seven symbols are transitions:

- `A`: semilocal amplification;
- `J`: primal/contragredient presentation;
- `P`: convolution-square polarization;
- `C`: cutoff pair and Halmos colligation;
- `T`: trace observation;
- `E`: endpoint completion;
- `F`: positive apex filler.

The count `8!=40320` comes from allowing the initial object `0` to occupy every position in unrestricted permutations. Typed schedules require `0` first. After fixing it, the relevant operation-order space has seven transitions and at most `7!=5040` orders. Dependency relations reduce these to 28 admissible linear extensions.

The correct historical combinatorial object is therefore the order complex of the seven-transition dependency poset, rooted at `0`. It is not the Freudenthal triangulation of an eight-operation cube.

The proposed axes

\[
(H,V,D,q,L,C_{cmp},O,R)
\]

form a different architecture. There is no source-derived bijection:

- `H` and `V` have no separate historical schedule labels;
- historical `C` combines chart and cutoff roles;
- historical `E` combines observation and completion;
- historical `F` is a filler/comparison cell rather than an independent operation;
- `A`, `J`, and `P` each admit more than one plausible interpretation in the new axes.

The two structures can still be related by a many-to-one or refinement functor. Such a functor would map the fine operational axes to compound historical transitions, or split each historical transition into several operational directions. It cannot be a relabelling of eight symbols.

`check_eight_axis_vs_historical_schedule_dictionary.py` records the cardinality match, the root/transition mismatch, missing arity labels, and ambiguous compound correspondences.
