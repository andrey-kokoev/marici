# Integral complex constructor scaffold

This scaffold performs the operations demanded by the lift gate on an integral matrix packet:

- exact rational rank;
- gcds of maximal minors as saturation/Smith determinantal certificates;
- primitive integral annihilator basis derived by exact fraction elimination;
- reduction of the complete matrices and derived covectors at every declared good prime;
- quotient-dual incidence checks.

The bundled fixture uses one primitive relation in a free rank-three carrier. It constructs the rank-two primitive annihilator rather than choosing covectors first.

The emitted packet is marked synthetic_fixture. Replacing its matrices with a source-derived interaction-net complex is the only allowed promotion route. Matching finite-field rows alone does not authorize that replacement.

