# History-conditioned feedback restores plus information but is outside native symmetry words

**Fourth batch, iteration 3 of 20.**

**Strength:** exact unitary plus-polar correction, an identity extension on minus, and a finite-library obstruction. Not an implemented feedback pulse or deterministic preparation.

[Previous retry channel](RETAINED-SELECTOR-RETRIES.md) · [Checker](check_selector_failure_feedback.py) · [Receipt](results/selector-failure-feedback.v1.json)

## 1. Fresh branch correction

For each recorded failure branch, R_g=sqrt(p_g)(sign(a_g)T_g-(3/5)P_plus). The two central branches already act as positive scalar identity on plus, so their feedback is identity.

For the sixteen half-quaternion branches let S_g=sign(a_g)T_g P_plus. Exact identities give

    S_g+S_g*=P_plus,
    W_g=5S_g*-3P_plus,
    W_g* W_g=19P_plus.

Here * denotes adjoint.

The feedback unitary is

    C_g=P_minus+(5S_g*-3P_plus)/sqrt(19).

It is the inverse unitary polar factor on plus and identity on minus. The checker verifies both unitarity directions over exact matrix pairs X+sqrt(19)Y, and verifies

    C_g R_g P_plus=sqrt(p_g)*sqrt(19)/5 P_plus

for the half-quaternion branches. This is not a claim to undo the minus branch. Its records remain, and its operation is unchanged by the chosen identity extension.

## 2. Corrected retry instrument

Every corrected plus failure branch is scalar identity. Summing the actual branches therefore gives

    Phi_corrected(X_plus)=(16/25)X_plus.

Feedback is unitary, so all failure effects are unchanged. At depth n the accepted plus channel is [1-(16/25)^n]X_plus, not a depolarized state. In the eventual-success limit the channel is

    X -> P_plus X P_plus.

This preserves the original plus logical state and does not convert minus input. The success probability is still the initial plus weight, not one for arbitrary input. Along plus histories, branch probabilities do not depend on the plus logical state; fresh controller records factor from that state after correction. The history and minus sector are retained rather than deleted.

The feedback uses a branch readout after the coherent selector's failure event. It does not replace that selector with a group label measured before coherent recombination, and it does not require a measurement of the plus/minus sector.

## 3. Native finite-library obstruction

The tested native library consists of finite products of the twenty-four joint symmetry unitaries. Group closure reduces every such product to another native element, irrespective of word length. On plus its trace is 2a, so the phase-insensitive squared trace has values

    |tr(T_native P_plus)|² in {0,1,4}.

For each half-quaternion correction,

    tr(C_g P_plus)=-1/sqrt(19),
    |tr(C_g P_plus)|²=1/19.

Thus none of these sixteen corrections equals a native word on plus, even up to an arbitrary global phase. The two central corrections are native identity.

This excludes only the stated finite symmetry library. It does not exclude continuous Hamiltonian controls, ancillas, coherent linear combinations, or a larger separately controlled swap/phase library. Those possibilities require their own input and synthesis analysis.

## 4. Gauge-compatible extension without implicit hardware

The prior individually gauge-preserving representation U_hat_g has fundamental central projector P_full. A bounded extension is

    C_full=(I-P_full)+(5 sign(a_g) U_hat_g* -3I)P_full/sqrt(19).

On every fundamental copy sign(a_g)U_hat_g has real scalar quaternion part one half; its sum with its adjoint is identity, giving numerator norm squared nineteen. On all other isotypic sectors the feedback is identity. The finite-group representation theorem therefore establishes full unitarity.

All factors commute with each G_i, and the operation preserves total charge and the physical ground. On the physical model it is compatible with H. No off-kernel Hamiltonian commutation or device synthesis is claimed. A central-sector operator formula is not a physical sector measurement, source pulse, or work-supply specification.

## 5. Next continuous-control gate

Express the correction as a continuous rotation with an explicit bounded Hermitian generator on the fundamental central sector and zero generator on its complement. Test the generator's gauge/ground compatibility and the required rotation angle. Separate those mathematical controls from the native fixed Hamiltonian and specify feedback/phase/work inputs.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. No physical spin, charge conjugation, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_selector_failure_feedback.py
python research/scattering/seed-composition/check_selector_failure_feedback.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The local checker freshly recomputes the predecessor channel and native action. Exact square-root-extension arithmetic verifies all branch feedbacks and effects. Full-isotypic extension and all-depth corrected retries are stated mathematical arguments, not new formal or physical admission.
