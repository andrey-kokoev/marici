# The elementary spinor has a curved source link connection

## Result

The actual four-face spinor now has an exact weighted adapter to the existing matter/link action, including signed current, continuity, gauge covariance and a common zero-background exterior graph. The source connection is not flat: its face-loop phases are +/-i.

The existing electric-only specialization cannot preserve this source connection during unrestricted energy minimization. Cancelling the spinor holonomy lowers its energy and replaces its rank-two coherent ground with a rank-one fixed-field ground. This identifies a specific missing piece: the magnetic action on the actual source face loops.

## 1. Retain the four local spinor lines

Read P_i=(I-n_i.sigma)/2 from the existing spinor store. Each rank-one face projector gives a local negative-polarization line. Choose its nonzero first column v_i=P_i e_0 and retain its source norm m_i=v_i^dagger v_i. These norms are (1/2+sqrt(3)/6,1/2-sqrt(3)/6,1/2-sqrt(3)/6,1/2+sqrt(3)/6).

The embedding V(a_i)=(v_i a_i)_i has metric M=diag(m_i). Its metric decoder satisfies V^sharp V=I. The stage-defect control used in the interacting elementary reference is

    H_e=(I-L)+2(I-N_e).

Exact source reconstruction verifies

    H_e V=V K_e,
    K_e^2=2K_e.

The four local lines therefore contain two coherent zero modes and two modes at energy two. The other four raw spinor directions remain identified at energy three; they are not erased by the adapter.

## 2. Source hopping and holonomy

In normalized line coordinates, the off-diagonal hopping is the local spinor overlap. Tetrahedral projector identities give

    |<eta_i,eta_j>|^2=1/3, i!=j.

All six geometrically shared face edges thus have magnitude gamma=1/sqrt(3). Each vertex has three such edges, but K_e has diagonal one. The exact energy identity is

    <a,K_e a> = sum_edges gamma*|a_j-U_source,ij*a_i|^2
                +(1-sqrt(3))*sum_i |a_i|^2.

The negative onsite coefficient is fixed by the original operator. It is not a fitted rest-energy term. At the native phases the total operator remains positive and has the required doublet kernel. Dropping this coefficient changes the source Hamiltonian.

The loop phase follows directly from tr(P_i P_j P_k). In ascending vertex order, the normalized projector products on 012,013,023,123 are respectively +i,-i,+i,-i. The hopping transport convention takes their conjugates. Neither convention is flat. No local rephasing can turn these source loops into identity.

An ordinary connected scalar Laplacian with flat transport has only one coherent zero mode. It therefore cannot replace this curved connection while preserving the spinor doublet.

## 3. Reuse the signed weighted field equations

Attach the same canonical link variables A,E as in the existing feedback law, now multiplying the source hopping by exp(i*q*A). The electric charge sign q is a declared species assignment; it is not inferred from positive norm.

In the source-column metric, the hopping current is

    J_matter,ij=2 Im(conj(a_j)*h_source,ij*exp(i*q*A_ij)*a_i).

The actual electric current is q*J_matter. With the inherited canonical matter equation i*m_i*dot(a_i)=dH/dconj(a_i), the adapter checks

    dot(rho)+B J_matter=0,
    dot(E)=-q J_matter,
    d/dt(B E-q rho)=0.

Exact +/-1,+/-i phase fixtures verify gauge covariance, weighted density continuity and the energy/current derivative for both q=+1 and q=-1. The sourced onsite term is gauge invariant and contributes no link current.

## 4. One exterior graph for all three species

Extend the existing proton/belt graph by the spinor's four vertices, six source edges and four exterior leads. The common graph has 35 vertices and 97 links; inactive blocks remain present.

Declare charges proton +1, belt 0 and elementary spinor -1. With zero background the common Gauss source is

    (rho_p,0,-rho_e,q_ext),
    q_ext=-(Q_p-Q_e).

The checker constructs the actual incidence graph and verifies empty, proton, electron and simultaneous opposite-charge fixtures against that same Gauss law. The external flux energy is retained. These are still classical fixed-norm sectors; this step provides a signed field adapter, not a quantum charge-quantization mechanism.

At the four electron vertices, the internal graph is complete and each vertex has one lead. Its grounded electric Laplacian is 5I-ones, with inverse (I+ones)/5.

For a unit pure coherent logical spinor with Bloch vector s,

    rho_i=(1-n_i dot s)/4,
    sum rho_i^2=1/3.

The electric energy is therefore 2*beta/15 for every pure logical spin direction. Exterior energy eta/2 is the same for either unit charge sign. No particular logical spin is chosen to get this readout.

## 5. The electric-only global minimum changes the source sector

The preceding electric-only action has no magnetic cost for A. It can choose A to cancel every source hopping phase. Uniform density and aligned amplitudes then attain

    E_e,min = mu_e+1-sqrt(3)+beta/8+eta/2.

The lower bound is exact: pair-difference energies are nonnegative, density is normalized, and the four exterior leads carrying total unit charge have field energy at least beta/8. Uniform density attains the field bound; cancellation of source phases attains the matter bound.

At native source phases, the coherent spinor instead has

    E_e,coherent=mu_e+2*beta/15+eta/2.

The unrestricted minimum is lower by sqrt(3)-1+beta/120. Its fixed-field ground is rank one, not the native logical doublet. The scalar field extension is therefore not a source-sector-preserving elementary charging law.

With beta=3/5, eta=1/5 and the preceding occupation offset mu_e=1, the unrestricted elementary energy is approximately 0.442949192431. This is a consequence of changing the holonomy, not a successful correction to the earlier same-field electron gap.

The same signed electromagnetic specialization gives proton field correction beta/24+eta/2 and neutral belt correction zero. It does not generate a heavier neutral belt by electric loading alone. Earlier belt field excesses used INTERNAL norm charge, which must not be relabelled as neutron electric charge.

## Next specific construction

The source now supplies the actual four triangular face loops and their nontrivial spinor connection. Reuse the existing magnetic term from `record-gauge-feedback-loop.md` on these source loops, retaining the distinction between intrinsic spinor transport and the dynamical electric/gauge field. Construct its source-compatible flux sector and test the complete current/backreaction before comparing rest energies.

A free negative offset or a flat scalar link model would hide this obstruction. The needed object is the face-holonomy action and its physical coefficient, not another occupation counter or overall clock.

## Verification

    python research/voevodsky/checkers/check_spinor_matter_link_adapter.py

Results: `results/spinor_matter_link_adapter.json`. Exact Q(sqrt(3),i) checks cover the source embedding, weighted Hermiticity, reduced spectrum, all six hopping magnitudes, four loop phases, signed gauge/current identities, actual common incidence graph and pure-spin density/field invariants. Global electric-only minima follow the displayed nonnegative energy and flux bounds. Source spinor, weighted carrier and all-face contact receipts are separately hashed.
