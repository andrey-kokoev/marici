# The tidal readout needs second-jet control, not merely a reversible encoding

## Live issue and recovered owner input

Fresh objective-oriented resume selected
`issue-tree:marici-project-objective:completion-stable-observability:v2`.
Its declared task is an actual source/readout/completion tuple, not a universal
common topology. The current project map and dependency correction were reread.

The inbox contains Nima's request
`naradaepistemiccommunication:32a11500c255a4bdb6dd` (event sequence 15584), asking
for an exact physical interface for the new annotated fibration constructor
bridge. Fresh inspection of `research/nima/fibration-constructor-equivalence.md`
confirms that its generic readout theorem is decode/encode transport, not a
comparison with an independently constructed physical evaluator or a continuity
theorem. No owner artifact is modified here.

This turn supplies a NONREDUNDANT regularity test of the already constructed
plane-wave observer readout. It does not assign this topology to all sectors or
claim the owner has admitted it as a completion of the annotated Code system.

## Source/readout tuple

- Source V: the smooth Rosen vacuum metrics constructed in the preceding two-
  polarization note, restricted to a compact u interval before a caustic,
  with declared affine/null normalization, central observer and initial frame.
- Representation Enc_k: the transverse metric gamma as a C^k matrix function,
  with retained corner frame. This is NOT the Agda Code encoder; its connection
  to that encoder remains an owner-local instantiation obligation.
- Physical law: supplied vacuum Einstein equation; frame transport follows the
  Levi-Civita connection. The two-polarization focusing construction realizes
  the compatible image rather than treating arbitrary matrix triples as sources.
- Reading O: observer electric tidal field E(u) in the transported frame, or its
  corner value E(0). Reading type is a symmetric 3 by 3 real matrix field (or
  matrix), with a zero longitudinal block in this sector.
- Physical selection: complete characteristic shape history, area/expansion,
  observer and frame data; no preferred boundary history is inferred.
- Topology: compare candidate C1 and C2 completions in this fixed gauge. C2 is
  the ordinary classical metric regularity sufficient for this pointwise
  curvature readout; it is not asserted to be the unique possible weak theory.

This is nonlinear readout factorization. It is not legitimate to invoke a
linear operator norm theorem without controlling inverses and observer transport.

## An exact vacuum C1-loss family

For n>=1 on 0<=u<=1, take the polarized subfamily

    beta_n(u)=(1-cos(nu))/n^2,
    r_n''=-beta_n'^2 r_n,  r_n(0)=1, r_n'(0)=0,
    p_n=r_n exp(beta_n), q_n=r_n exp(-beta_n),
    gamma_n=diag(p_n^2,q_n^2).

The focusing equation makes each metric an EXACT vacuum solution, not an
arbitrary perturbation with unverified stress. Elementary bounds are

    |beta_n|<=2/n^2, |beta_n'|<=1/n,
    1-1/(2n^2)<=r_n<=1, |r_n'|<=1/n^2.

To justify the radial bounds, assume positivity up to a first zero. Concavity
then gives r<=1 and the Volterra formula gives r>=1-u^2/(2n^2)>=1/2, contradicting
that first zero. Integrating the ODE yields the derivative bound. The metrics
have a uniform positive lower bound, for example exp(-4)/4, so no caustic or
inverse-metric singularity is hiding in the limit.

It follows that

    gamma_n -> I in C1([0,1]),

because r_n-1 and beta_n are O(n^-2), while their first derivatives are
O(n^-2) and O(n^-1). Every member has the same corner first jet as flat space:

    gamma_n(0)=I, gamma_n'(0)=0.

However beta_n''(0)=1 and r_n''(0)=0, so

    gamma_n''(0)=diag(2,-2),
    E_n(0)=diag(-1/2,+1/2,0).

The flat limit has E_flat(0)=0. Thus the pointwise tidal observation is not
continuous even on the smooth vacuum source equipped with the C1 topology.
No continuous extension through its C1 completion can preserve all these
values and the flat value. The spectral/operator-norm gap is exactly 1/2.

This does not refute weak/distributional curvature limits or smeared detectors:
point evaluation and such readouts have different continuity requirements.
It also does not refute the owner's full value equivalence. A reversible code
can retain the second jet; first-jet forgetting or an inadequate topology is
where this example loses the observation.

## Positive result on the C2 closure, with explicit controls

Let gamma and eta be two source metrics on [0,T], with the SAME normalized
corner gamma(0)=eta(0)=I and initial transverse frame I. Use operator norms and
assume the fixed bounds

    gamma,eta >= lambda I, lambda>0,
    ||gamma'||,||eta'|| <= B1,
    ||gamma''||,||eta''|| <= B2.

Set delta=||gamma-eta||_C2, where the C2 norm is the maximum of the three
uniform derivative norms. Put

    K=B1/(2 lambda),
    L_Gamma=(1/lambda+B1/lambda^2)/2,
    B_R=B2/2+B1^2/(4 lambda),
    L_R=1/2+B1/(2 lambda)+B1^2/(4 lambda^2).

For Gamma_gamma=(1/2)gamma^-1 gamma', the inverse identity gives

    ||Gamma_gamma-Gamma_eta|| <= L_Gamma delta,
    ||Gamma_gamma||,||Gamma_eta|| <= K.

The transport F'=-Gamma F with F(0)=I satisfies

    ||F|| <= exp(KT),
    ||F_gamma-F_eta|| <= T exp(KT) L_Gamma delta.

The second bound follows by variation of constants: the forward propagator
from s to t has norm <=exp(K(t-s)), while ||F_eta(s)||<=exp(Ks).

For the coordinate curvature block

    R_gamma=-gamma''/2+gamma' gamma^-1 gamma'/4,

product differences give ||R_gamma||<=B_R and

    ||R_gamma-R_eta|| <= L_R delta.

Finally E_gamma=(1/2)F_gamma^T R_gamma F_gamma, so

    ||E_gamma-E_eta||_C0
      <= exp(2KT) [L_R/2 + T B_R L_Gamma] ||gamma-eta||_C2.

This is a readout-sized stability bound. It does not claim recovery of every
metric from its tidal tensor. A fixed positive gap in E cannot disappear along
a C2-convergent sequence satisfying these uniform hypotheses.

Define the completion specifically as the C2 closure of this bounded smooth
source class, with the corner data and positive lower bound retained. Density
in that closure holds by definition; surjectivity onto all weak Einstein
solutions is NOT asserted. The displayed formulas extend continuously to that
closure. Ricci depends continuously on the same controlled two-jets, so vacuum
is preserved. The extension of the intended readout is unique by density.
This is the scoped positive extension result, not an owner-authorized topology
on arbitrary constructor packages.

## Finite-resolution observation is a distinct successor

For the polarized hostile family, in its parallel frame,

    E_11=-beta_n''/2-(r_n'/r_n) beta_n'.

For a fixed C1 detector kernel w with w(0)=w(1)=0, integration by parts gives

    |integral w E_11|
      <= ||w'||_L1/(2n) + 2||w||_L1/n^3 -> 0.

Thus a finite-resolution smeared readout can converge while an ideal pointwise
one fails. Choosing w, its proper-time calibration and which quantity the
actual detector measures is physical input. A next branch should recover that
interface, not declare the stronger C2 topology mandatory for every observation.

## Exact owner-local instantiation request

The already checked finite interface to use is
`research/nima/agda/NewtonianTidalRoutes.agda`:

- `potentialTotal8 a b` versus `geometric8`;
- `routeAgreement`, `adPackage`, `directPackage` and `comparisonRule`;
- all tensor entries with their common denominator, and the retained source
  and route history.

Requested next owner step: instantiate the fibration bridge on those actual
packages, define a direct tensor projection from the translated fields, and
compare it to the old route outputs without defining the new observer solely
as old-readout after decode. Add a hostile first-jet-only projection that cannot
recover the Hessian. State whether the full retained jet/tensor representation
admits a declared completion at all. A generic decode/encode equation alone
cannot answer that last question.

This is an evidence-bearing request, not permission to modify Nima's modules,
a claimed owner acknowledgment, or a new requirement on all physical sectors.

## Verification and disposition

Run:

    python research/voevodsky/check_tidal_completion_regularity_gate.py

Nine exact Fraction controls passed, covering corner jets, nonzero tidal gap,
uniform radial margin, decreasing analytic envelopes and the extension-bound
prefactors. The all-n convergence proof and Gronwall/closure theorem above are
written mathematics, not inferred from finite tests or newly formalized in Agda.
Receipt: `research/voevodsky/tidal-completion-regularity-gate.json`.

This resolves the bounded plane-wave regularity question: C1 fails for the
pointwise readout, controlled C2 succeeds. The project-wide completion leaf is
split rather than marked universally solved. Successors retain finite-resolution
source selection, the owner-local independent fibration observer, and the
remaining sector-specific completion obligations.
