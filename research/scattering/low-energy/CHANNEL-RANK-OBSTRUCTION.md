# C7 — fixed-energy single-excitation channel-rank obstruction

C2 identifies the absolutely continuous scattering space of the fixed model with the three free Dirichlet leads. Their sine transforms have spectral parameter E=2-2cos(k), 0<k<pi, with multiplicity three for almost every E in (0,4). Metric whitening does not change that multiplicity. Thus the single-excitation outgoing channel fiber is C3 at almost every open-band energy.

The target specified in C3 is C2 tensor C2 with positive metric

    H_target=G_gamma tensor G_gamma=diag(9,3,3,1).

Its determinant is 81 and its rank is four. These are facts about the target definition, not assertions that the failed C3 or C8 carrier exists.

Suppose a fiber map F(E):C4->C3 obeyed F(E)*F(E)=H_target. Its left side has rank at most three, whereas the right side has rank four. Equivalently, rank-nullity gives a nonzero v in ker F(E), forcing

    0=||F(E)v||²=v*H_target v>0,

a contradiction. Hence no such isometry exists for any three-dimensional fiber, and in particular for almost every E in the fixed model's open band.

The same statement holds before whitening: replacing F*F by F*H_port F cannot increase rank, since H_port is positive invertible. It is not a dimension claim about the whole infinite-dimensional three-lead Hilbert space. Allowing energy mixing, multiple excitations/Fock sectors, extra channels, a degenerate target metric, or only a proper subspace of the target changes the proposition. In particular, abstract separable Hilbert-space embeddings do not answer this energy-fiber question.

`check_channel_rank.py` freshly checks C2's source/certificate inputs and computes the target tensor metric, determinant and strict positive lower bound with rational arithmetic. The fiber/rank argument above is the analytic proof; no finite search for candidate F is needed. Physical photon-channel identification remains outside the result.
