# Local failure to a joint decay-product channel

## Scope and result

The objective is now product-directed: identify a local computation failure whose next realization can enter a joint proton/electron/partner carrier, rather than merely lose a neutron coherence condition.

This calculation connects an actual native neutron contrast subspace to a **new, explicitly chosen** joint-product channel. It does not derive that channel from the native realization grammar, identify the partner as an antineutrino, or determine a decay rate. The target proton return and the pair map are chosen candidate outputs, not discovered decay products.

The native local-coherence fault is tested immediately after L, before G. All 432 individual coefficient omissions excite the candidate joint channel. All 144 patterns obtained by omitting the same local coefficient in all three sectors have zero joint-channel output. The relevant signal is unequal weighted loss between sectors, not the count of omissions.

## Source material actually inspected

Repository `andrey-kokoev/marici`, retrieved through its GitHub connector:

- `research/strominger/neutron-contrast-electron-transport-v1.md`
- `research/strominger/checkers/check_neutron_contrast_electron_transport.py`
- `research/strominger/neutrino-rim-attachment-and-contact.md`
- `research/strominger/global-PN-and-two-channel-E-v1.md`

The neutron geometry and 36-coordinate L/G/N matrices are reconstructed by the prior conversation's uploaded `neutron_seam_reconstruction.py`, SHA-256 `d7501e12fb41461012183f5f2f0af3796110664c4865e7792e2256d6f220afed`. That script is included. Its source formulas and missing-generated-file qualification remain in force. This is not a fresh rerun of all repository producers or an audit of their complete dependency chain. No repository file was modified.

The native source already supplies an exact rank-two contrast projector C=L-N and a conditional C3-compatible partial isometry into the electron return doublet. It also supplies an electron/partner singlet contact and metric-isometric raw encoders. These are separate candidate interfaces, not an established common decay vertex.

## 1. The point in the update where the signal exists

In metric-whitened coordinates write

    a = (1,1,1)/sqrt(3)
    u = a tensor v,       v* v = 1
    L = I_3 tensor vv*
    G = aa* tensor I_12
    N = aa* tensor vv*
    C = L-N.

Let Q have columns (1,-1,0)/sqrt(2) and (1,1,-2)/sqrt(6), and let K=Q tensor v. Then K*K=I_2 and KK*=C. Importantly, GK=0.

An intact alignment therefore removes exactly the sector contrast that the candidate electron interface can read. Testing only the completed G L_F update misses that route.

This contrast is distinct from the earlier nine-triangle-versus-nine-triangle mode obtained by opening three seam checks. Here the varying amplitudes belong to the three rotating sectors.

## 2. Exact fault signature

Write r_i=|v_i|^2, with sum r_i=1. Removing the local matrix entry (s,i,j) gives

    delta = -e_s tensor e_i * v_i r_j/sqrt(3).

Its contrast coordinates are

    c = K* delta = -(r_i r_j)/sqrt(3) Q* e_s,
    ||c||^2 = 2(r_i r_j)^2/9.

Every native r_i is positive, so every one of the 432 single local omissions has a nonzero contrast. Location still matters: it selects one of three contrast directions and a source-derived magnitude.

For an arbitrary omission set F let

    D_s = sum_{(s,i,j) in F} r_i r_j.

Then

    ||C L_F u||^2
      = ((D_0-D_1)^2+(D_1-D_2)^2+(D_2-D_0)^2)/9.

Equal D_s produces no contrast, even when many computations fail. A full threefold orbit of the same failed coefficient has equal D_s. All 144 such controls were tested.

## 3. Why a separate electron map is insufficient

The repository's neutron-to-electron map concerns a direct-sum field exchange. It does not by itself produce a joint proton/electron/partner state.

Furthermore, the already constructed scalar singlet contact is invariant under the selected C3 action, whereas the contrast plane has eigenvalues omega and omega^2. A fixed linear intertwiner from that plane to the invariant singlet is zero: det(R_C3-I)=3. This obstruction is restricted to a fixed map without an additional transforming defect, orbital, or context record. It is not a prohibition on singlet production under other couplings.

## 4. An explicit joint-channel candidate

Reuse the actual order-three electron action V from the repository checker and its unitary frame W, with VW=W R_C3. In the contrast plane let q_+ and q_- have eigenvalues omega and omega^2, and set e_+=W q_+, e_-=W q_-.

Define the NEW pair map

    B q_+ = e_- tensor e_-
    B q_- = e_+ tensor e_+.

The products have the correct C3 eigenvalues. Exact symbolic checks establish

    B*B=I_2
    (V tensor V) B = B R_C3
    swap B = B
    singlet* B = 0.

Thus this is a symmetric two-spinor channel, not the existing singlet contact. Two central full-turn signs multiply to +1, matching the vector-type source contrast. These checks cover C3 and central-turn parity, not a complete physical rotation or weak-interaction theory.

Let E be the normalized native raw electron encoder, V_o the retained omission-zero partner encoder, and p_0 the normalized native proton return candidate. The raw product-valued map is

    J = p_0 tensor [(E tensor V_o) B] K*.

Its source is the 36-coordinate neutron field. Its target is the tensor product of the 36-coordinate proton field, 8-coordinate electron field, and 6-coordinate partner field: 1728 coordinates. This is a joint-product target, not three independent output labels.

The reconstructed raw encoders are isometries and numerical checks give

    J*J=C,       Ju=0,       JG=0.

It follows that J L_F u has exactly the contrast norm in section 2. Assigning p_0 and choosing this normalized B and coupling order are additional hypotheses. Neither a proton species assignment nor antineutrino flavor/charge/chirality has been derived here.

A reversible exchange can be built on neutron-direct-sum-product sectors using

    T = [[I-C, J*], [J, I-JJ*]].

The identities give T*T=T^2=I. This avoids cloning and conserves the norm of the input to this exchange. It does not repair the earlier coefficient-deletion loss, establish energy conservation, or make the outgoing channel irreversible.

## 5. Computed controls

- 432 single L-coefficient omissions: all have positive conditional joint-channel squared norm.
- 144 matched three-sector omission patterns: all have zero channel output, to numerical residual below 1.1e-16.
- 140 random multiple-omission masks: all agree with the exact weighted-loss formula.
- No omission: zero channel output.
- Intact G applied before J: zero channel output.
- Maximum numerical squared-norm identity error for the single-fault census: below 5.1e-18.
- Exact SymPy checks of the 2-by-2 and 4-by-2 intertwining, isometry, swap, and singlet identities.

Single-fault channel amplitude norms range from 3.20828024028e-5 to 0.0240247519363. These refer to the unnormalized post-omission vector and the explicitly chosen unit-gain channel. They are not decay probabilities or physical couplings.

## 6. What has changed in the research target

A recoverability or minimum-cut calculation alone cannot select decay products. This probe supplies a concrete local signal and a mathematically allowed product-valued map to test against the realization grammar.

The immediate selection test is whether the native next-step rule actually admits and selects this product branch, rather than realignment, a deformed neutron, another product, or no valid successor. A nonzero fixed map is not enough: the zero map and arbitrary strengths also satisfy the same symmetry requirements. The new B and proton output must therefore be tested, not promoted to native operations.

The current precursor is not rare: every single local omission excites it. No 13-error trigger or other lifetime-fitting threshold was introduced. The rate question should follow identification of a source-authorized conversion and escape event, including damage persistence where relevant.

Still unestablished are the full particle/charge/energy/momentum readers, partner identity, source-selected coupling and timing, irreversibility, and a per-tick hazard. The computation is a product-directed candidate construction, not a neutron-decay derivation.

## Reproduction

Python 3, NumPy, SymPy and mpmath:

    python decay_branch_probe.py

The script reruns the included prior reconstruction and writes `decay_branch_results.json` and `local_fault_to_product_branch.json`. Exact algebra is used for the pair-map identities and scalar weight formulas; raw large-matrix checks use floating point with explicit tolerances.
