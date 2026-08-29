# Analytic endpoint traces are not arithmetic incidence lifts

## Source re-audit

The local analytic history already has explicit endpoint traces:

[
Gamma_{P,p}psi=W_{log p}psi,
qquad
Gamma_{Q,p}psi=W_{2log p}psi.
]

Both are contractions on (L^2(mathbb R,dq)), and

[
Gamma_{Q,p}-Gamma_{P,p}
=
D_p
=
int_{log p}^{2log p}partial_tW_t,dt.
]

Therefore the analytic trace theorem is closed.

However, these maps begin and end in the analytic (q)-Hilbert carrier. They
are not the arithmetic endpoint lifts needed to turn

[
p^{-1/2}delta_{log p},
qquad
rac12p^{-1}delta_{2log p}
]

into arguments of one relative Green form.

## Correct factorization

Introduce source-authorized comparison maps

[
J_{P,p}:mathcal P_{sigma,p}longrightarrowmathcal H_{q,p}^{	imes},
qquad
J_{Q,p}:mathcal Q_plongrightarrowmathcal H_{q,p}^{	imes},
]

where the target may be a rigged analytic history space rather than (L^2)
itself.

The mixed form must factor as

[
b_p(x,y)
=
leftlangle
J_{Q,p}y,,
D_pJ_{P,p}x
ightangle_{mathrm{rel}}
]

or by the adjoint convention forced by the Green pairing.

The earlier notation (L_{P,p},L_{Q,p}) conflated the already solved analytic
traces (Gamma_{P,p},Gamma_{Q,p}) with these still-missing
arithmetic--analytic comparison maps.

## Why the distinction matters

A delta incidence at (log p) is not an (L^2(q)) vector. Multiplication by
(W_{log p}) does not itself embed that delta into the analytic state space.
Likewise, knowing the endpoint difference (D_p) does not specify how the
primitive and square source fibers pair against it.

The comparison maps must supply:

1. the rigged meaning of each delta incidence;
2. the primitive exponential and square tempered topologies;
3. prime and grade labels;
4. the source normalization coefficients;
5. radical descent into the relative Green quotient;
6. reciprocal adjoint orientation.

## Boundary-triple formulation

Let (mathcal G_p) be the closed history graph and

[
Gamma_p=(Gamma_{P,p},Gamma_{Q,p})
]

its analytic boundary trace. A source realization is a map

[
J_p:mathcal P_{sigma,p}oplusmathcal Q_p
longrightarrow
operatorname{ran}Gamma_p
]

or into its rigged extension, satisfying

[
Gamma_pJ_p
=
egin{pmatrix}
I_{1,p}&0\
0&I_{2,p}
end{pmatrix}
]

after the authorized identifications.

The Green boundary form on (operatorname{ran}Gamma_p) then pulls back along
(J_p). This is the exact constructor-level meaning of the desired mixed
form.

## New earliest theorem

Construct (J_p) from the source Fourier--Tate or comoving correspondence and
prove:

[
operatorname{Green}_{partial,p}(J_p(x,0),J_p(0,y))
=
b_p(x,y).
]

The theorem must also establish:

- continuity into the rigged trace range;
- cutoff naturality;
- prime-idempotent preservation;
- wall and reciprocal compatibility;
- closability of the pulled-back form;
- the lift growth budget below the exponent threshold (1/2).

## Minimal hostile

Take the correct analytic history and traces, then choose two different rigged
embeddings of the same arithmetic delta packet. They have identical endpoint
locations and scalar Euler weights but induce different pulled-back Green
forms. This shows that solved analytic traces do not determine the arithmetic
mixed edge.

## Frontier

The earliest missing data are not the endpoint trace operators; they are
already explicit. The missing constructor is the source comparison

[
	ext{valuation/Fock incidence}
longrightarrow
	ext{rigged analytic boundary trace range}.
]

Once that map is source-derived, the contractive adjacent cell supplies the
analytic propagation and the Green form can be pulled back without fitting.
