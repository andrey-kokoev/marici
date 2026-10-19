# Interaction continuation — iteration 5: asymptotic port channels and flux

## Spectral follow-up

Iteration 6, `native-port-bound-spectrum.md`, certifies five above-band bound
modes and nonzero overlap for the named internal preparations. The stationary
incoming-flux result below remains valid; it is not a theorem that all initially
central states eventually escape.

## Result

The certified eleven-state interface now has three explicit semi-infinite
asymptotic leads. A positive contact construction, stationary scattering matrix
and normalized probabilities are supplied. All **54 exact checks** pass.

For an incoming belt-channel wave, at dimensionless model energy E=2:

| Outcome | Probability |
|---|---:|
| Reflection into the belt lead | 0.1179162817062031 |
| Transmission into the lower/proton-port lead | 0.4410418591468984 |
| Transmission into the upper/electron-port lead | 0.4410418591468984 |

The exact probabilities sum to one. The displayed decimals are evaluations of
retained exact algebraic numbers, not floating-point normalization tests.

These are **port-scattering probabilities**, not survival/2gamma/3gamma branching
fractions. The lead/contact laws are declared mathematical inputs. Full spinor
coupling, physical scale and a multi-object asymptotic dictionary remain open.

## 1. Fresh state and retained hidden sector

Freshly read `native-joint-generator-resolvent.md` and its source-bound receipt.
The calculation uses its exact eleven-state K, diagonal metric and eight-state
hidden self-energy. All predecessor hashes are verified before use.

The three visible vectors are the native belt return, the proton attachment-port
character and the electron's currently registered attachment-port character.
Their metric diagonal is

    h = (1196/15, 20, 20).

They are not unit vectors in the retained coefficient coordinates. Treating all
three raw amplitudes as if they had equal norm gives incorrect probabilities.

## 2. Explicit positive leads and contacts

For each port j attach a semi-infinite chain indexed by n=1,2,..., with metric
weight h_j at every site. Declare the total quadratic form

    <x,Kx>_H
      + sum_j h_j |x_j-psi_(j,1)|^2
      + sum_(j,n>=1) h_j |psi_(j,n+1)-psi_(j,n)|^2.

All terms are nonnegative. The nearest-neighbor leads and contacts give a
bounded self-adjoint operator in the inherited weighted Hilbert space. No
unbounded negative-energy wide-band approximation is required.

The central contact adds +1 on each of the three visible diagonal entries.
Each lead has onsite value 2 and hopping -1; its first node couples to its port
with -1. The contact shift is part of the operator, not silently omitted from
its self-energy.

A finite two-site-per-lead assembly is independently checked against these
positive edge-difference terms and the correct metric adjoint. A Dirichlet end
term supplies the final diagonal in that finite control; the scattering leads
are semi-infinite, not those finite truncations.

This is one supplied channel model with identical contacts. It is not claimed
that the geometric source uniquely selects chains, hopping strengths or a
physical spatial interpretation of the lead index.

## 3. Asymptotic states and retarded boundary condition

For 0<k<pi, write

    E = 2-2cos(k),
    eta = exp(ik),
    Gamma = 2sin(k) > 0.

A lead wave is

    psi_(j,n) = a_j exp[-ik(n-1)] + b_j exp[ik(n-1)].

The incoming component travels toward the central system; the outgoing component
travels away. The lead surface resolvent is

    g(E) = -eta,
    g(E) [E-2-g(E)] = 1,
    Im g(E) < 0.

This chooses the retarded, outgoing branch. Including the positive contact
shift, the full central response is

    G(E) = [E I-K-P+eta P]^(-1),

where P projects onto the three visible coordinates.

Only 0<E<4 supports nonzero propagating flux in this lead model. Band edges
need a limiting analysis; outside-band solutions are evanescent. The checker
rejects threshold and outside-band inputs rather than assigning them propagating
probabilities by dividing by zero velocity.

## 4. Scattering matrix derived from the endpoint equations

Let G_PP be the visible block of the full open response. Define

    S = I-i Gamma G_PP.

In the displayed endpoint-wave convention, the actual outgoing amplitudes are

    b = -eta^2 S a.

The extra factor is a common unit-modulus phase, so it does not change fluxes.
The internal response is

    x = i Gamma eta G V a,

where V includes the visible coordinates into the eleven-state central space.

For each of three independent incoming channels, the checker verifies both

    (E I-K-P)x = -V psi_1,
    (E-2)psi_1 + psi_2 + V^sharp x = 0.

Thus the scattering formula is checked against the actual contact and endpoint
equations, not introduced solely as a probability ansatz.

## 5. Flux normalization and the general conservation identity

Each lead carries flux magnitude

    Gamma h_j |amplitude_j|^2.

All three leads share Gamma, hence the probability from incoming channel j to
outgoing channel i is

    Prob(i <- j) = (h_i/h_j) |S_ij|^2.

The coefficient scattering matrix satisfies

    S* H_port S = H_port.

Equivalently, H_port^(1/2) S H_port^(-1/2) is unitary in ordinary orthonormal
channel coordinates. Both orders of metric unitarity are checked exactly.

The all-energy argument follows from the resolvent identity. In the full metric,

    M-M^sharp = i Gamma P,
    G-G^sharp = -i Gamma G^sharp P G.

Taking visible blocks gives the optical identity that cancels the quadratic
term in S^sharp S, proving flux conservation throughout the open band wherever
the response exists. This is not an extrapolation from three numerical samples.

In the coupled eleven-state space, a singular M at a real interior-band energy
would imply a K eigenvector with zero visible component: take the imaginary
part of <x,Mx>. The previous cyclic-closure certificate says the three visible
vectors generate all eleven coordinates under K, excluding such a nonzero
invisible eigenvector. Thus the coupled open response has no such real pole
inside the band. Decoupled spectator modes of a larger retained model are not
silently identified with these incoming port states.

## 6. Exact sample energies

Rational half-angle parameters tan(k/2)=1/2,1,2 give exact test energies and lead
phases in Q(i). The central field is Q(sqrt(151)), so the full calculation uses
Q(sqrt(151),i), without numerical matrix inversion or rank thresholds.

| E | Reflection from belt input | Each carrier-port transmission |
|---:|---:|---:|
| 4/5 | 0.1464951287210261 | 0.4267524356394870 |
| 2 | 0.1179162817062031 | 0.4410418591468984 |
| 16/5 | 0.1084042440695491 | 0.4457978779652254 |

At each energy, all three incoming columns are normalized, every probability is
nonnegative, and normalized probabilities obey reciprocity. The receipt retains
the complete 3-by-3 matrices, exact algebraic probabilities and decimal views.

## 7. The eight hidden coordinates remain necessary

Two independent calculations agree:

1. Solve the full eleven-coordinate open linear system for all three visible
   inputs, including its hidden response coordinates.
2. Evaluate the previously certified polynomial self-energy

       Sigma_hidden(E) = K_PQ (E I-K_QQ)^(-1) K_QP

   and solve the three-coordinate visible equation with the same lead/contact
   self-energy.

The sample energies avoid the hidden-block poles. At such poles one must use
the full response or an appropriate limit, not substitute a divergent eliminated
formula blindly.

Deleting the hidden block instead gives a different scattering matrix and
different normalized probabilities. That smaller, altered model can still be
unitary. **Probability conservation alone does not certify faithful elimination
of the retained interaction structure.**

Likewise, omitting the channel metric gives incorrect probability sums even
when the underlying scattering solution is correct. Both negative controls
are checked at every sample energy.

## 8. Output symmetry survives opening identical leads

The closed visible resolvent commutes with exchange of the two carrier ports;
this is checked coefficient by coefficient in its exact numerator polynomial.
The identical lead/contact self-energies preserve that exchange symmetry, and
the two output metric weights are equal. Consequently

    Prob(proton-port <- belt) = Prob(electron-port <- belt)

throughout the propagating band, not just at the sampled energies. Their ratio
is one wherever the transmissions are nonzero.

This does not falsify or derive the supplied 372 comparison: these ports have
not been identified with two- and three-photon sectors. It does show that a
bias cannot be obtained merely by calling two symmetric holes different channel
names. Different asymptotic spaces, thresholds, couplings, spinor dynamics or
preparations must be admitted and tested explicitly.

## 9. What is and is not completed

A complete **conditional stationary port-scattering construction** now exists:
retained finite operators, a native local adapter, hidden-space closure, a joint
positive generator, explicit asymptotic waves and flux-normalized probabilities.

This does not complete the physical shape-interaction program:

- the channels are one-excitation port waves, not a constructed tensor/Fock
  decomposition into two- and three-object output shapes;
- full electron spinor coupling and physical energy calibration remain open;
- the interface is stationary at a registered configuration, not an autonomous
  implementation of the moving-port schedule;
- normalized incoming scattering does not describe every initially excited
  central state; out-of-band bound components may remain;
- finite packets, threshold behavior and bound-state content are not yet audited.

The next nonredundant executable test is the spectral/asymptotic audit: determine
whether this positive lead-coupled fixture has bound modes outside [0,4], and
which central preparations overlap them. Distinguish stationary unit-flux
scattering from eventual release or retention of initially internal records.
This is directly relevant to the proposed indication/attachment function and
prevents a scattering identity from being mistaken for a storage theorem.

## Reproduction

```sh
python research/voevodsky/checkers/check_native_port_scattering.py
```

Receipt: `results/native_port_scattering.json`, with current source hashes,
contact conventions, exact S matrices, flux probabilities and erasure controls.
