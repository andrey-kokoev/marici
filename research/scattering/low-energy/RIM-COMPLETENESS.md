# Rim continuum: resolvent comparability and the outgoing decomposition

[Exact support checker](check_rim_completeness.py) · [receipt](results/rim-completeness.v1.json)

## Fixed scope and result

This is the same principal two-channel continuum point contact as the [full point-sector audit](RIM-BOUND-SECTOR.md), not the unequal-threshold control, a three-chain model, or a physical neutron Hamiltonian. The core has dimension 24 with physical metric M/3, two contact columns B, adjoint `S=B^T M/3`, and `SB=I2`. The free field is `L2(R,C2)` with threshold theta=1/2.

For this fixed supplied operator H:

- the singular-continuous subspace is zero;
- both wave operators from the entire free two-component field exist and have range H_ac(H);
- `I=P_point+P_ac`, with point rank **21**, as independently classified in the preceding audit;
- every non-point component has a free outgoing asymptote in norm.

The free field has four energy-fiber channels (two internal components times two momentum signs), not a rank-two fixed-energy fiber. Rank two below refers to the contact/resolvent correction, not the scattering multiplicity. Completeness does not silently identify wave-operator channel coordinates with the source's stationary endpoint frames, or enlarge C6's explicitly restricted shared-input/output comparison class.

These are auxiliary fixed-model results, not new numbered conjectures, a change to C1–C12, a renewal of C12, or evidence of physical capture or law selection.

## 1. Same-space reference and form resolvent

On the same Hilbert space set

```
H0=(-d^2/dx^2+theta) direct-sum K,
tau(psi,x)=psi(0)-Sx.
```

The source closed nonnegative form is exactly `h=h0+2||tau||^2`. Its domain is `H1(R,C2) direct-sum C24`. The trace is bounded in the H1 form norm; the positive contact form therefore defines the stated self-adjoint nonnegative H. It does not define a bounded operator difference H-H0 on the Hilbert space.

Use `(H-z)^(-1)` as the resolvent convention. For z<0 put `q=sqrt(theta-z)>0` and

```
g_q(x)=exp(-q|x|)/(2q),
J(z)=(K-z)^(-1),
R0(z)=(H0-z)^(-1),
Gamma(z)c=R0(z) tau* c=(g_q c, -J(z) B c),
A(z)=tau R0(z) tau*=I2/(2q)+S J(z) B,
C(z)=I2+2A(z).
```

Here tau* is interpreted as a form-dual map: its lead part is a delta source, not an L2 vector. Gamma is a bounded map from C2 into the Hilbert space. Since H0 is nonnegative, A(z) is positive and C(z) is invertible. Solving the form equation gives

```
R(z)=R0(z)-2 Gamma(z) C(z)^(-1) Gamma(z)*   (real z<0).
```

At nonreal z both resolvents exist and the final adjoint is `Gamma(conjugate(z))*`. The identity extends meromorphically, with the inverse formula used only where C is invertible. The signs follow from `tau=trace-S`: the correction's lead part is negative and its core part positive.

For completeness, the boundary check can be done without manipulating an unbounded delta operator. Given `t=tau R0(z)F`, set `c=C(z)^(-1)t`. The corrected state has mismatch `t-2A(z)c=c`. Since `g_q'(0+)-g_q'(0-)=-1`, its derivative jump is `2c`, exactly the source condition `2(psi(0)-Sx)`. Its core correction is `2J(z)Bc`, whose image under K-z cancels the contact term `-2Bc`. This proves the resolvent formula by uniqueness at z<0.

At z0=-1/2, q=1. The checker constructs J, A, C and C^(-1) over Q, verifies both-sided inversion and the mismatch/core identities, and verifies their positive Gram matrices. In particular

```
Gamma(z0)*Gamma(z0)=I2/4+S J(z0)^2 B > 0.
```

The first term is the full-line integral `||g_1||^2=1/4`. Thus Gamma is injective. The resolvent difference has **exact rank two**, is trace class, and has the negative sign required by the positive contact completion. No lead cutoff or numerical quadrature is used.

## 2. Complete wave operators: the resolvent-comparable theorem

Use the standard trace-class resolvent-comparability theorem for semibounded self-adjoint pairs: if, at a common real point below both spectra, their resolvent difference is trace class, then the ordinary wave operators exist and are complete on the absolutely continuous subspaces. One route is Kato–Rosenblum for the bounded resolvents followed by the Birman invariance principle. The resolvent function is decreasing, so that route reverses the intermediate time orientation; it still gives both ordinary limits below.

All hypotheses have just been verified for H,H0 at z0=-1/2. The Fourier transform makes the free field purely absolutely continuous; its threshold has no atom. The finite K summand has no ac part. If J_lead embeds the full free field with zero core component, it follows that

```
W_±=s-lim_(t->±infinity) exp(itH) J_lead exp(-itH_lead),
W_±* W_±=I_free,        Ran(W_±)=H_ac(H).
```

This theorem does not by itself rule out singular-continuous spectrum. That is a separate argument, not an inference from rank two.

## 3. No singular-continuous measure: a finite exceptional set

On `C\[theta,infinity)` choose `q(z)=sqrt(theta-z)` with Re(q)>0. For E>theta the upper boundary value is `q(E+i0)=-i sqrt(E-theta)`. The free Green kernel is

```
R_lead(x,y;z)=exp(-q|x-y|)/(2q).
```

For compactly supported smooth lead vectors, its integrated matrix elements, and those with g_q, extend analytically in q except for the possible q=0 pole. The fixed-vector conjugation in the inner product does not conjugate q. The finite core resolvent is rational in z, hence in q. The 2x2 C(q) and its inverse are rational in q away from finitely many poles.

The exceptional set is finite, not an assumption about zeros of an arbitrary analytic function. Indeed the full core secular numerator is the polynomial matrix

```
L(q)=(q+1)[K+(q^2-theta)I]+2q P,    P=BS.
```

Its cubic coefficient is I24, so `p(q)=det L(q)` is monic of degree 72. At q=1 it is nonsingular by positive congruence. With `A_core=K+(q^2-theta)I`, the determinant lemma, wherever the reference inverse exists, gives

```
p(q)=q^2 (q+1)^22 det(A_core) det C(q).
```

This identity extends as an identity of rational functions. Thus it is enough to exclude q=0,-1, the finitely many roots of p, and the finitely many roots of det(A_core). Some apparent poles cancel; they need not be located or declared spectral atoms. The checker verifies the polynomial coefficients, the determinant relation at exact regular rational points, and nonsingularity of L(1). The monic leading term, not those sample identities, proves global finiteness.

For every vector consisting of an arbitrary core vector and compactly supported smooth lead components, the full scalar resolvent formula is therefore meromorphic in q with only this finite possible pole set. On a compact real interval avoiding its real energy images and theta, the physical upper boundary values converge uniformly and smoothly. Stieltjes inversion gives an absolutely continuous spectral measure there. Outside the continuum the regular boundary value has zero imaginary part. Any singular part is supported on the finite exceptional set; an atomless singular-continuous measure cannot charge it.

These test vectors are dense in the full Hilbert space. Since P_sc is a bounded orthogonal projection, its vanishing on that dense set gives `P_sc(H)=0`. This reasoning also handles the threshold without claiming the resolvent is bounded there. Its absence as a point eigenvalue is supplied separately by the point-sector audit.

## 4. Arbitrary initial state and the outgoing asymptote

The point audit exhausts all square-integrable eigenstates: six zero-energy dark modes, thirteen embedded dark modes and two simple accessible modes below theta. Let P_point be their full-tail-normalized spectral projection. The two preceding arguments now imply

```
I=P_point+P_ac,       rank(P_point)=21.
```

For any initial state Psi, not only a named preparation, define

```
phi_out=W_+* (I-P_point) Psi.
```

Completeness and the defining strong limit give

```
||exp(-itH)(I-P_point)Psi - J_lead exp(-itH_lead)phi_out|| -> 0,
||phi_out||^2=||(I-P_point)Psi||^2,             t->+infinity.
```

The core component of the non-point state therefore vanishes in norm. The bound part remains separate; its core occupation can beat in time and is not its full-tail spectral weight. The exact dark-preparation lower bound from the point audit remains valid. Complete escape of every central preparation is false, and stationary incoming states do not capture into the orthogonal point sector.

## Verification and remaining programme scope

The fresh checker verifies the finite source/metric support, rank-two form-resolvent algebra and polynomial structure. The form-resolvent construction, resolvent-comparable scattering theorem, Stieltjes inversion/density argument and strong-limit consequence are documented analytic mathematics, **not machine-formalized analysis**. The source stationary solver and source-owner receipts are not rewritten or rerun.

This closes the fixed-rim spectral/outgoing audit, not the wider programme. Preparation-specific accessible bound weights, literal scalar-C/native comparison, richer retained constructions and independently justified physical states/laws/instruments remain separate. No existing no-go is extended to all operation classes and no physical explanation outcome is admitted.

```sh
python -S research/scattering/low-energy/check_rim_completeness.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_rim_completeness.py
```
