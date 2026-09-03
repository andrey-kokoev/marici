# Standard monomials do not source-label the CM complement

The generic CM quotient decomposes by rank as seven equals the labelled
normal-tower rank four plus an unlabelled complement of rank three. The backend
computes standard monomials internally, but the generic normal-tower path
returns only their count. A separate tangential-wall mode serializes standard
monomials for a different quotient.

Even generic serialization would produce Gröbner presentation coordinates, not
source identities. No artifact maps three such coordinates to source classes
or transports their labels across points and primes. Therefore the
three-dimensional complement remains unlabelled and cannot support a canonical
matrix connection.

This closes the CM-coordinate route within its current interface. The next
independent route is the weighted relative homology–de Rham pairing; it does not
rely on choosing a complement by row reduction.
