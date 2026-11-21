# Six cyclic templates give a generative normal form for Hall191 coalitions

ramsey_phase_compatibility_templates.py reconstructs the30-vertex/40-edge co-extendability graph WITHOUT reading the valid-model list. It rejects candidate singletons/pairs by unit propagation of the necessary low-order repair rules, then expresses the surviving graph in intrinsic C5 coordinates. The result independently matches the previously computed compatibility complex.

Six of the sixteen five-element switch orbits survive. Rename them:
A=old orbit5; B=6; C=14; D=12; E=13; F=11.
Let indices lie in F5, using the independently recovered generator and representative choices recorded in JSON. The complete compatibility edge rules are:
A_i--B_(i-1), A_i--C_(i+1), B_i--C_(i+2);
D_i--E_(i+1), D_i--E_(i+2), E_i--E_(i+1);
F_i--F_j for every i!=j.
No edges join these three sectors. This directly reconstructs the five isolated triangles, the five-triangle ring, and K5.

The ACTUALLY VALID nonempty coalitions, as distinct from extendable partial selections, have four recipes:
1. {B_i,C_(i+2)}: five pairs.
2. {A_i,B_(i-1),C_(i+1)}: five extensions of those pairs.
3. {D_i,E_(i+1),E_(i+2)}: five irreducible triples.
4. {F_0,F_1,F_2,F_3,F_4}: one irreducible quintuple.
Equivalently: a phase-locked pair with one optional extension; a three-way phase-closing repair; or full-orbit synchronization.

ramsey_phase_coalition_constructor.py generates these16 coalitions directly from the templates, checks disjointness and validates all16 output graphs (degree6, triangle-free, no independent seven). It does not look up completed coalitions. The K5 sector's exclusion of all proper nonempty subsets also has the earlier explicit domain-wall proof. Prior checks of isolated-triangle/ring subsets establish which extendable cliques are already valid.

Explanatory gain: the catalogue of successful operations has been replaced by cyclic recipes with fixed relative phases. Necessity of the six surviving templates is certified by repair-rule implications, rather than by extracting participants from finished successful outputs.

Limit: this is not yet a derivation purely from local incidence without independent-set information. The necessary repair clauses were originally compiled from global seven-sets. A first-principles proof that these clauses reduce to exactly the six templates remains open. The templates are specific to source191 and this candidate class; they do not automatically transfer to all regular witnesses or to original BRNN row semantics.
