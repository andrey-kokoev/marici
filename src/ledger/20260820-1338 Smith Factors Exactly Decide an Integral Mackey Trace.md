# Smith Factors Exactly Decide an Integral Mackey Trace

Epistemic-graph event: 1356.

For an integral pushforward `S:Z^n->Z^m`, an integral trace satisfying

`S T=d I_m`

exists exactly when `S` has full row rank and every Smith invariant factor
`s_i` divides `d`.  Equivalently, `coker(S)` must be killed by the prescribed
norm degree.  The minimal possible scalar is `lcm_i(s_i)`.

The hostile rank-one case `S=2,d=3` has no integral trace, while `S=2,d=4`
admits `T=2`.  Existence does not give canonicity: all traces differ by maps
into `ker(S)`.

For a physical five-site branch of degree `2^k`, every Smith factor of the
relative pushforward must divide `2^k`.  Any odd factor or excessive two-adic
valuation falsifies the integral Mackey norm before boundary compatibility is
considered.

Research note:
`research/grothendieck/integral-mackey-trace-smith-criterion.md`.
