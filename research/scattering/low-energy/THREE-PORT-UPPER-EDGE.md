# Three-port upper edge: source-audited scattering and packet corollary

[Exact checker](check_three_port_upper_edge.py) · [receipt](results/three-port-upper-edge.v1.json)

## Coverage finding, not another conjecture

The candidate upper-edge gap was partly already covered: the [C2 proof](THREE-PORT-COMPLETENESS-PROOF.md) and [bound-spectrum source](../../voevodsky/native-port-bound-spectrum.md) explicitly certify that `M4=4I-K-2P` has inertia (6,5,0). Thus upper-threshold nonsingularity was not missing. C9's no-singular-continuous statement alone would not supply it, and the statement of C2 alone does not imply absence of a threshold resonance.

The remaining scattering/packet consequence is a short derived result, made explicit below. It does not introduce C13, alter C1–C12, or reopen/renew C12's exhausted protocol. This is a coverage audit of a different branch.

## Exact finite input

Use exactly the eleven-state K, source metric H and visible projector P of the three-port model. The checker verifies the source hashes, H-self-adjointness, positivity of the metric, and independently constructs an exact two-sided inverse of M4 over Q(sqrt(151)). It also checks the inverse's H-adjoint identity and stores its port compression.

This is a direct full-core nonsingularity certificate, not a hidden-block inverse or a numerical E=4 sample. A negative control rejects omitting the second contact projector in M4.

## Uniform approach to E=4 from inside the band

The source coefficient convention is

```
E=2-2cos(k), eta=exp(ik), Gamma=2sin(k),
M(k)=E I-K-P+eta P,
S(k)=I3-i Gamma [M(k)^(-1)]_PP,   0<k<pi.
```

Put d=4-E and q=pi-k. Then `d=4sin(q/2)^2`, `eta=-exp(-iq)` and

```
M(k)-M4=-d I+(1+eta)P,
|1+eta|=sqrt(d),
||M(k)-M4||_H <= d+sqrt(d).
```

Whitening is unitary between the declared weighted spaces; P is an orthogonal projection in that metric. Let `a=||M4^(-1)||_H>0` and

```
epsilon0=min(1,1/(16a^2)).
```

For `0<d<epsilon0`, the Neumann defect is at most `a(d+sqrt(d))<1/2`. Therefore `||M(k)^(-1)||_H<=2a`. The port compression cannot increase this norm. Since `Gamma^2=d(4-d)<=4d`, the metric-whitened coefficient matrix satisfies

```
||S_hat(E)-I3|| <= 4a sqrt(4-E).
```

The receipt also gives fully explicit conservative constants without a floating eigensolver. Since the whitened inverse is Hermitian, `t=trace(M4^(-2))` is its squared Frobenius norm. The checker computes t exactly in Q(sqrt(151)) and finds a dyadic integer A with `A^2>t`. Thus `a<A`; replacing a by A gives the certified rational window `min(1,1/(16A^2))` and packet constant `16A^2` recorded in the receipt. For this pinned source, A=8: the window is `0<4-E<1/1024`, the coefficient bound is `32 sqrt(4-E)`, and the packet bound below is `1024 epsilon`.

This is a uniform bound on an entire one-sided energy interval, not just a limiting value or a sampled scan. Equivalently the defect is O(pi-k). No threshold atom, singular eliminated inverse or uncertified numerical constant is needed.

## Keep coefficient and endpoint amplitudes distinct

The source endpoint travelling-wave amplitude is `b=-eta^2 S a_in`. Hence

- coefficient limit: `S_hat -> I3`;
- endpoint-amplitude limit: `b_hat -> -a_hat_in`.

Confusing these gives the wrong sign. The common unit-modulus factor does not change any port probability. The group velocity Gamma tends to zero at E=4, so neither limit assigns a nonzero incoming flux at the exact band edge.

## Incoming-packet consequence

Fix one incoming port j. In whitened, energy-normalized coordinates prepare `f(E)e_j`, with `integral |f(E)|^2 dE=1` and support in `(4-epsilon,4)`, `0<epsilon<epsilon0`. Let Q_not_j project onto the other two outgoing ports. Since `Q_not_j e_j=0`,

```
integral ||Q_not_j S_hat(E)e_j f(E)||^2 dE
  <= 16a^2 epsilon.
```

All three declared leads have the same velocity Gamma(E); their currents are Gamma(E) h_j |a_j|^2. Multiplying amplitudes by sqrt(Gamma h_j) gives the unit-flux channel coordinates. The common sqrt(Gamma) cancels from the scattering map, leaving exactly the H_port-whitened S_hat above. Energy-normalized profiles therefore use the displayed dE norm, not an unweighted count of raw port coefficients.

The same inequality holds for endpoint travelling amplitudes, because their common phase has modulus one. The bound is uniform over the profile and phase and includes both other ports together; there is no missing factor of two. It does not define an unlabelled "transmission probability" for an arbitrary coherent superposition of input ports.

This is an asymptotic incoming packet, not release of an initially central excitation. C5's retained bound components and source-dependent preparation distinctions are unchanged. No physical decay-product interpretation is admitted.

## Verification boundary

The exact inverse and metric identities are replayable. The uniform spectral/norm and packet argument is documented mathematics, not a machine-formalized functional-analysis proof. The checker binds that proof and its finite inputs; it does not rerun the source stationary solver, infer physical species, or promote this auxiliary corollary into a new live proposition.

The upper-edge coverage question is now answered for this fixed three-port fixture. The rim's full bound/scattering sector remains a distinct audit question; no result is transported between their different dispersion laws.

```sh
python research/scattering/low-energy/check_three_port_upper_edge.py --check
python -m unittest discover -s research/scattering/low-energy -p test_three_port_upper_edge.py
```
