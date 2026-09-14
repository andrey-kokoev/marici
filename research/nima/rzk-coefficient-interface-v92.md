# v92: certified amplitude package

`rzk/120-certified-amplitude-package.rzk.md` defines the first Rzk type whose
inhabitants are complete amplitude certificates relative to supplied physical
operations.

A package consists of an amplitude map together with unit normalization,
homotopy invariance, symmetry covariance, and binary gluing factorization. The
constructor bundles these witnesses, and projections recover the amplitude,
its normalization theorem, and its factorization theorem.

This turns the previous sequence of amplitude properties into one dependent
acceptance boundary. A concrete Marici amplitude will be a term of this type
after the physical comparison filling, supported Gysin/residue evaluation,
gluing operation, path relation, and symmetry action are instantiated.

A fresh Rzk check passes all seven declarations. The symbol closure contains
one file and no `#assume` declarations. No concrete physical package inhabitant
is claimed yet.
