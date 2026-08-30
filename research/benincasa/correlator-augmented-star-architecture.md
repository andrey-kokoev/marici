# Correlator augmented-star architecture

The source-derived three-edge correlator object has eight independently
defined coefficient sectors, indexed by the Boolean deletion subsets
(S\subseteq\{12,23,31\}). Each has a port

\[
T_S:\mathcal M_S\longrightarrow\mathcal R
\]

to the common correlator readout. The weighted-polytope formula supplies the
augmentation

\[
\epsilon
=
\sum_S(-2)^{|S|}T_S:
\bigoplus_S\mathcal M_S\longrightarrow\mathcal R.
\]

The grade multiplicities are (1,3,3,1), while the total weights by grade
are

\[
1, -6, 12, -8.
\]

No differential among the eight source modules is part of this data. Thus
the correct incidence diagram is a star with a common sink, not a chain
complex on the Boolean cube.

The kernel, fiber, or cofiber of (epsilon) is a legitimate future derived
object. Its possible classes would measure relations among physical ports.
They must be computed from the augmentation and sector coefficient systems;
they cannot be populated by assigning the Boolean incidences an assumed
differential.
