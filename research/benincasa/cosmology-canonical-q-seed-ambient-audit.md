# Canonical marked-q interior seeds are descriptor-identical across three cutoffs

An independent audit recomputed the descriptor-coefficient tuples from the
ambient-degree 12, 14, and 16 packets rather than trusting their summary
hashes. At every degree:

- the pole-0 seed has seven rows and digest `206b994e...92dcdb`;
- the pole-1 seed has eleven rows and digest `81abd0f7...3fc44`;
- every term is a `g1` marked-q row at levels `(1,1,2,1,1)`;
- the complete serialized term lists are identical under ambient inclusion.

This verifies finite-field ambient compatibility at prime 32003. It does not
establish source-natural uniqueness, second-prime survival, a boundary
operator, a tau map, or an unbounded induction. The next compatibility gate is
second-prime replay before using these seeds in the top-three-degree boundary
construction.
