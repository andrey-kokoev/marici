# v167: inhabited synthetic principal-road model

The global relation/Bockstein construction and support-zero extension now form
an inhabited full principal-road model on the coefficient side.

Take road cells to be integral A-relations. Their soft-D1 boundary is Bx; every
other principal-road component is the fixed zero. Define the coefficient Cech
value by the same pair `(Bx,0)`. The full boundary comparison is then
reflexivity, with no Smith-basis or finite-cutoff choices.

`rzk/195-l2-synthetic-principal-road-model.rzk.md` implements this model. It
shows that all coefficient-level principal-road data are globally coherent and
that no D2/D3/incidence construction remains.

The sole road comparison gate is now geometric and soft-D1-specific: map each
synthetic integral relation cell to an actual physical nearby-cycle cell while
preserving its Bx boundary. This does not inhabit module 132 until that map is
constructed at the candidate physical point.

The module passes all eight declarations without assumptions.
