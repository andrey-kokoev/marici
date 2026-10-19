# Common resource accounting: finite selected-K proof

Scope: the selected cycle-defect K with zero vacuum extension, all four native
chirality/doublet cases, one neutral two-level record, g=1/2. This is a finite
constructor theorem, not physical admission or kernel verification.

## Complete generators and the common reference

On the 101-state matter space let c=I100 direct_sum 0 and Pi=J Ps Jdagger
direct_sum 0. Both P=Pi and P=c-Pi are self-adjoint projections. With S=I101-P,

    R+ = [[S,P],[P,S]],   R- = [[-S,P],[P,-S]].

P S=S P=0 and P^2+S^2=I imply that both R signs are self-adjoint involutions.
Their nonnegative control projectors Qsign=(I-Rsign)/2 satisfy

    Q+ + Q- = [[I,-P],[-P,I]].

The complete bare Hamiltonian in record blocks is therefore

    Hbare(P) = [[K+gI,-gP],[-gP,K+(1+g)I]].

No diagonal or complementary record is omitted. On empty matter P=K=0,
the ready record has energy g, for BOTH rules. Subtract this single reference
g I202 to obtain

    H(P) = [[K,-gP],[-gP,K+I]] = K tensor I2 + I101 tensor N - g P tensor X.

Each displayed block is 101 by 101, so both rules retain all 202 joint
coordinates. K, P, the record gap, preparation and readout operators use the
same Hilbert space, native source, scalar input and constructor units. Only P
changes. K and P are self-adjoint, so H is a finite self-adjoint (hence bounded)
operator. The finite-dimensional spectral theorem gives unitary exp(-itH) with
inverse exp(itH): the premeasurement joint dynamics is reversible. This last
step is a written mathematical implication, not a kernel-checked analytic proof.

## Joint evolution, energy and retained readout

On the prepared normalized scalar pair, K has eigenvalue epsilon=2e. The primary
record Hamiltonian is h=N-gX=[[0,-1/2],[-1/2,1]]. The rival has h0=N because
(c-Pi) annihilates this scalar input. Its record stays |0>.

Write G=sqrt(2)(h-I/2); G=Gdagger and G^2=I. Ignoring the common phase,

    U(t) = C I - i S G, C=cos(t/sqrt(2)), S=sin(t/sqrt(2)).

Thus U is unitary when C^2+S^2=1. For rho0=|0><0|,

    rho(t)=C^2 rho0 + CS i(rho0 G-G rho0) + S^2 G rho0 G.

The checker verifies the coefficient matrices exactly. They imply trace rho=1,
record occupation p=S^2/2, interaction expectation -p, and tr(h rho)=0.
The total pre-readout energy is therefore epsilon, not epsilon+p. The rival's
occupation and interaction energy are zero and its total energy is also epsilon.
At t=1, p=(1-cos(sqrt(2)))/4 lies strictly between 0.21 and 0.22 by the previously
certified rational alternating-series bounds.

For ideal projective record readout M0=I101 tensor |0><0| and
M1=I101 tensor |1><1|, retain BOTH outcomes and the matter carrier. The primary
has probabilities 1-p,p and normalized conditional joint states scalar tensor
|0>, scalar tensor |1>. Their post-readout energies are epsilon and epsilon+1.
The nonselective post-readout density is diag(1-p,p) on the record and its mean
joint energy is epsilon+p. The increase p comes from destroying the negative
interaction coherence, not from the preceding closed unitary evolution. At
operator level D(h)-h=gX, where D is record-basis dephasing. The rival readout
is deterministic |0> and its energy remains epsilon.

This ideal measurement instrument is explicitly a readout convention. Its
apparatus energy is not included in the 202-state system: the increase p must
be supplied/accounted by an external measurement interaction. No claim is made
that dephasing is a reversible closed operation or that this constructs a
physical detector. Joint reversibility above refers only to exp(-itH).

## Scope of admission

These checks and the written finite-dimensional argument discharge common
resource accounting. They also provide reusable evidence for a later readout
proof. They do NOT automatically admit typed classification, the discriminator,
the umbrella theorem, the final comparison or physical admission. A separate
variable-phase contract and scoped downstream receipts remain necessary.
