# Destructive membership cannot supply two continuations from one linear head

The previous fixed-signature B0/B1 membership net computes ONE query by consuming support nodes. Fresh `check_linear_membership_reuse_obstruction.py` tests 126 nonempty supports and confirms its normal form contains only BOOL and OUT, leaving no support for another query. Wiring two query principal ports to one support head also fails the one-wire-per-port invariant. Two separate support copies satisfy incidence, but their construction must be explicit; the current net has no duplicator or persistent read discipline.

This is an obstruction for THIS destructive encoding, not a theorem that interaction nets cannot implement reusable support. It matters to the programme: a sufficient continuation state must survive the future observations it promises. An in-place add(i) alone would not establish that property if the first probe consumes the result. Nima remains untouched.

Next implement an explicit fixed-signature duplicator for B0/B1/NIL lists, with local erasure and per-rewrite linearity, then feed separate copies to two distinct queries and compare with original support membership. Alternatively define a linear API that consumes and RETURNS a fresh support together with the answer; specify which observational contexts are allowed before choosing.
