# Hostile test: which policy selects the returning phase?

## Question

Freshly read the closed phase-moment observer result. Its fifteen readouts close for the declared record swap. Test whether conservation and reproduction of the source's first projected output force that law, or whether its first-moment return depends on another policy.

Keep the same mean projector P, the zero-mean record sector Pw=0 and the same initially empty record. Test the family

    x_next=P x+eta*w,
    w_next=(I-P)x,
    |eta|=1.

These are controlled rivals, not modifications to the original source implementation.

## What is unchanged

Every member has the same first output (Px,(I-P)x) from an empty record. Orthogonality of readable and contrast sectors gives the same conserved norm. Every member is invertible, with inverse

    x_previous=P x_next+w_next,
    w_previous=conjugate(eta)*(I-P)x_next.

The family commutes with simultaneous permutations of the twelve carrier/record slots because P does and eta is a scalar. Thus relabelling covariance also fails to select eta.

## What differs

From the previous preparation u+d, the second active output is u+eta*d. Its center is

    (1/12, Re(eta)/42, -Re(eta)/42).

Exact three-advance controls compare:

| Return phase | Second active center |
|---|---|
| 1 | (1/12,1/42,-1/42) |
| -1 | (1/12,-1/42,1/42) |
| exp(2*pi*i/3) | (1/12,-1/84,1/84) |

The memory-mediated distinction remains, but its return sign and magnitude are not fixed by norm conservation or the initial projection alone.

## The existing agreement policy does select the original member

Require the complete state to remain unchanged whenever the stored contrast already agrees with the carrier contrast:

    w=(I-P)x  =>  update(x,w)=(x,w).

For the family above this demands eta*w=w for every contrast w, hence eta=1. The original swap passes; the two nontrivial phase controls fail.

This makes an earlier assumption operationally visible: the original return is selected by full-state agreement fixing, not by conservation alone. It is a conditional selection within this family, not a new unrestricted uniqueness theorem. The source's physical reason for requiring agreement fixing remains a separate question; mere equality of a scalar readout would not imply this stronger policy.

## The observer closure is law-dependent

For a nonreal eta, next first moments depend on the imaginary as well as real mean-record correlations. Write

    c_x=(S+i*sqrt(3)*V)/2,
    c_w=(R+i*sqrt(3)*W)/2,
    eta=a+i*sqrt(3)*b.

Per spatial axis the correlation update is

    S_next=a R-3b W,  V_next=b R+a W,
    R_next=S,         W_next=V.

Together with the two first moments, their exact observable orbit has dimension four for eta=+/-1 and six for the nonreal control. This is an algebraic observable-orbit calculation, not an authorization for longer physical execution.

An explicit counterexample strengthens that result. The states (u,+i*sqrt(3)*d) and (u,-i*sqrt(3)*d) agree on all fifteen previous real-phase readouts. With eta=exp(2*pi*i/3), their next active centers differ:

    (7/36,-1/36,1/36),   (7/36,1/36,-1/36).

So the earlier observer is not universally sufficient after changing the interaction law. This does not contradict its exact closure under eta=1.

## Disposition

The return experiment is informative but not assumption-free. Conservation, the source projection and slot covariance leave a return phase free. The stated agreement-fixing policy selects the original return and its observer closure.

The next physical question is therefore not whether another trajectory can be plotted, but whether the actual retained source interprets agreement as a no-intervention condition on the whole state. No electric charge, mass, recoil or physical frame is selected by this test.

## Verification

`python research/nima/checkers/check_memory_return_phase_policy.py` passes exact Q(i*sqrt(3)) budget, inverse, three-advance, agreement and phase-sensitive counterexample controls. Receipt: `results/memory-return-phase-policy.json`. The general norm/covariance identities are written above; no universal physical claim is inferred from the three sampled phases. Existing source dynamics and prior receipts were not changed.
