# Positive row witnesses compose strictly on square proof packets

For a row witness f from presentation A to B, record a bijection `p: B-row -> A-row` and positive scales s at B rows; each B row is s times the selected A row, and its Farkas multiplier is divided by s. Given g:B->C with row map q and scales t, the composite has row map `p∘q` and scales `s_(q(j))*t_j`. Fresh `check_composed_square_row_witnesses.py` checks this equality on P, Q and their SIGNED zero-bound difference, then composes a third witness and verifies associativity, identity and exact inverse. These are strict mathematical presentation/packet laws for the fixed square.

The isomorphism groupoid acts on the chosen proof data and its row supports, not on publisher history. A forged request to carry a source-event token along the row witness is refused: no such authority map appears in the row bijection/scales, and the B/C manifest digests differ from A. An owner could separately admit a rebind, but mathematical invertibility cannot supply that decision.

Next test a NON-invertible row-presentation change, such as adding a redundant source inequality. It may transport proofs forward while lacking a positivity-preserving inverse; determine the first failure of groupoid laws and the exact dependency cost. Do not infer an analytic S,A,R,C,G correspondence from the polyhedral groupoid.
