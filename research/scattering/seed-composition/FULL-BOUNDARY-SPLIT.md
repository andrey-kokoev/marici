# The twelve-occurrence selected sector has rank four; rank two also selects correlation parity

**Iteration 10 of the requested ten-turn work-net run.**

**Strength:** exact full-boundary characteristic, corrected algebraic projectors and a commuting graph-reflection decomposition. Not native preparation or independent physical photon outputs.

[Previous projector](ALGEBRAIC-PROJECTOR.md) · [Checker](check_full_boundary_split.py) · [Receipt](results/full-boundary-split.v1.json)

## 1. Return to the original carrier

The preceding algebraic projector acts on a four-dimensional correlated subspace H of the twelve displayed boundary occurrences. This turn checks the larger carrier rather than assuming that its spectral multiplicities are the same.

For the original boundary family F(z)=zA+z^2C, each six-occurrence pair block has characteristic polynomial

    lambda^2 chi(lambda,z),

where chi is the checked quartic from the moving-plane analysis. The two blocks are related by an explicit source-graph relabelling. The full characteristic polynomial is therefore

    lambda^4 chi(lambda,z)^2.

Coefficientwise matrix arithmetic also verifies the stronger annihilator

    F chi(F)=0.

Since chi(0,z)=-z^5 is nonzero for z>0, the zero sector is semisimple. The twelve-dimensional space decomposes into three sectors of dimensions

    zero: 4,    selected pair: 4,    complementary nonzero pair: 4.

The selected rank four consists of two copies of the selected quadratic sector. It is not yet a statement about independently prepared physical states or a tensor-product two-particle space.

## 2. Correct the lift by retaining the zero sector

The four-carrier formula Pi=g(M)h(M)/R was derived modulo chi. It must not be applied blindly to F on the larger space, where zero eigenvalues are also present.

Define

    Z0 = chi(F)/chi(0),
    N  = I-Z0,
    P_selected = N g(F)h(F)/R,
    P_other    = I-Z0-P_selected.

The checker proves all three idempotence, mutual-annihilation and annihilator identities modulo lambda chi. They commute with F, sum to I, and have ranks four each on the positive axis. The zero record is retained rather than removed from the input without accounting.

A useful false-positive control: the uncorrected formula vanishes at lambda=0 exactly at z=1, so a base-point-only test would miss the problem. Along the actual algebraic branch, its value on the zero sector has derivative **-3/4** at z=1. Thus the old formula does not remain a projector there. The N correction is necessary.

## 3. Identify the additional correlation selector

The already-audited directed glued graph has the reflection

    A <-> C, D <-> Ep, E <-> Dp, B fixed.

It exchanges the two displayed triangle pairs and induces the occurrence permutation

    (9,10,11,6,7,8,3,4,5,0,1,2)

in the existing zero-based order. Its matrix J satisfies

    J^2=I, JA=AJ, JC=CJ.

Consequently the even and odd projectors

    E_plus=(I+J)/2, E_minus=(I-J)/2

commute with every spectral projector above. Each of the three spectral sectors splits into an even rank-two and an odd rank-two part. Keeping all six records recovers the original input by summation.

The earlier graded four-carrier is exactly the **odd nonzero sector**:

    JH=-H,
    im H = im(E_minus K),    K=F(1).

Its moving selected two-plane is therefore

    im(P_selected E_minus).

This locates the correlation assumption explicitly. The full selected projector has rank four; recovering the previously studied rank two additionally selects odd parity.

## 4. Spectral selection alone cannot choose the odd copy

The two parity copies have the same spectral quadratic. A scalar polynomial, rational function or scalar analytic spectral function of the block-diagonal F alone remains block diagonal across the two displayed pairs.

By contrast, P_selected E_minus has nonzero cross-pair blocks: it imposes a correlation through the reflection J. Therefore it cannot be selected by a scalar spectral function of F alone. The commuting reflection observable supplies extra mathematical structure; choosing its odd sector remains another preparation condition.

This is not an arbitrary fitted symmetry: J comes from the explicit glued-graph relabelling and preserves primitive-length blocks. But symmetry compatibility does not mean the source prepares a particular parity. The even sector is equally present in the decomposition.

At z=1 the checker also evaluates the original prefix-copy map Q. It finds

    rank(P_selected Q)=4,
    rank(E_plus P_selected Q)=2.

Thus generic prefix-copy input reaches the even selected sector as well. Odd selection is not already enforced by that source readout.

## 5. Ten-turn checkpoint

The batch establishes a detailed conditional mathematical construction and its boundaries:

- retained path incidence is faithful before lossy readouts;
- all-parse continuation preserves equal-copy source coefficients, without uniquely selecting macro-events;
- length-graded transport has a four-dimensional correlated invariant carrier;
- its selected plane continues analytically, including through an internal Jordan collision;
- positive normalized metrics exist only below that collision and degenerate there;
- exact selection/gain require algebraic rather than finite rational coefficient operations;
- on the full boundary carrier, the selected sector has rank four, and the synchronized rank-two sector additionally requires odd correlation parity.

None of these finite/algebraic results constructs independently emitted photons. In particular, they do not supply a native operation preparing the odd sector, macro parsing/control, the gain, or the correlated inputs while preserving the rejected records and physical metric.

The work-net root and physical-channel gate remain open. The next nonredundant construction is a source-authorized odd-parity preparation with the even and zero records retained. The separate atlas/seed source-correspondence branch also remains executable. Completing this ten-turn batch is not completion of the scientific objective.

## Reproduce

```sh
python research/scattering/seed-composition/check_full_boundary_split.py
python research/scattering/seed-composition/check_full_boundary_split.py --check
python research/scattering/seed-composition/check_algebraic_projector.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The checker computes the six-block characteristic exactly, verifies the annihilator coefficientwise, checks universal corrected-projector identities and exercises the full twelve-dimensional base maps. It writes only its own receipt; `--check` is read-only. Existing pinned work-net contracts and formal outcomes are unchanged.
