# Support, Coefficient Novelty, and Readout Form a Dependent Tower

Entry 2054 repairs Carrier-level failure typing to a multi-axis signature.
Coefficient faithfulness should not be appended as an independent fourth bit.
It is only defined after a Carrier port is permitted, and physical activation
is only defined after a coefficient realization exists.

The resulting structure is a dependent tower:

\[
\boxed{
H_1(\operatorname{Cl}G)
\longrightarrow
\Omega_{\mathcal A_s/\mathcal B_s}
\longrightarrow
\operatorname{Hom}(\mathcal V_s,\mathcal O_{\rm phys}).
}
\]

Here:

- \(H_1\) types the Carrier-permitted supported ports;
- \(\mathcal A_s\to\mathcal B_s\) is the sector coefficient space over its
  lower invariants, and the relative tangent/cotangent rank measures genuinely
  new coefficient information;
- the final pairing measures which retained directions the physical readout
  actually observes.

A minimal exact model reproduces the amplitude/Gaussian separation.  The same
chordless \(C_4\) has \(H_1\) dimension one.  An amplitude-like chart
\((x,y)\to x\) retains one relative cycle direction.  A Gaussian-like graph
\(y=x^2\) projected to \(x\) has relative tangent dimension zero: the cycle is
nonzero but composite.  An additional readout can either detect or annihilate
the retained amplitude direction without changing either upstream stage.

Therefore

\[
\boxed{
\text{permitted}
\not\Rightarrow
\text{coefficient-independent}
\not\Rightarrow
\text{physically observed}.
}
\]

The Deutsch–Popperian conjecture is that these stages and their dependency are
functorial under legal presentations.  A counterexample would exhibit a
physical readout direction without a typed coefficient antecedent, or a
coefficient novelty direction without a permitted support port.

The exact checker passes 7/7 gates.

Artifacts:

- `research/nima/support-coefficient-readout-dependent-tower.md`
- `research/nima/checkers/check_support_coefficient_readout_tower.py`
- `research/nima/results/support-coefficient-readout-tower.json`

Sequence claim: `seqclaim-9a3cef24de83b0eb0c4a6e5d`.
