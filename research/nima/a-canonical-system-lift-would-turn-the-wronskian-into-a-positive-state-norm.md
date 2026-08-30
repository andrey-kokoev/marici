# A canonical-system lift would turn the Wronskian into a positive state norm

## Reduction

The previous audit showed that the raw one-sided transform has an oscillatory Wronskian. There is a standard structural mechanism that would repair this without fitting a sign: realize the completed theta-tail constructor as a positive canonical system.

Let

[
J=
egin{pmatrix}
0&-1\
1&0
end{pmatrix},
qquad
J,partial_uY(u,z)=zH(u)Y(u,z),
]

where (H(u)=H(u)^{*}ge0) is source-derived and (Y) satisfies the source endpoint condition. If the outgoing endpoint section is

[
E_L(z)=A_L(z)-iB_L(z),
]

the differentiated Lagrange identity gives, with a convention-dependent sign (sigmain{1,-1}),

[
sigma,
igl(A_L(x)B_L'(x)-A_L'(x)B_L(x)igr)
=
int_0^L
Y(u,x)^{*}H(u)Y(u,x),du
+
Q_{partial}(x).
]

Here (Q_{partial}) records any independently typed wall or endpoint energy. It must not be discarded or absorbed into (H) without a source identity.

Consequently,

[
sigma,W_{A_L,B_L}(x)>0
]

whenever the combined state is not in the radical of the interior and boundary energies. This is exactly the missing one-sign phase-velocity theorem. The positivity comes from the constructor metric, not from positivity of the scalar theta forcing.

## Required source theorem

The completed theta-tail system must supply:

1. a two-component state (Y) obtained from the tail history and its conjugate boundary channel;
2. a source-derived Hamiltonian (Hge0);
3. the canonical evolution law on a common dense domain;
4. an endpoint map producing the previously identified one-sided section (E_L);
5. a Green identity including the wall term (Q_{partial});
6. radical control proving that the right side cannot vanish on a zero candidate;
7. a limit (L	oinfty) preserving the identity and strictness on compact spectral sets.

Only after these steps does the outgoing section become Hermite–Biehler by construction.

## Why this is stronger than Wronskian estimation

A direct inequality for the oscillatory double integral could prove a sign accidentally and only in one scalar presentation. The canonical-system identity is representation-stable: it explains the sign as stored positive energy and simultaneously supplies the de Branges reproducing-kernel diagonal.

It also isolates the exact failure modes:

- (H) is indefinite;
- an untyped endpoint term is omitted;
- the state enters the common radical;
- the finite-(L) identity loses strictness at completion;
- the endpoint section produced by the system is not the proposed theta-tail (E).

## New earliest constructor

The immediate target is therefore the source intertwiner

[
	ext{closed theta-tail history}
longrightarrow
	ext{positive two-component canonical system}.
]

The first finite test should derive this system on one truncated tail cell and verify its Lagrange identity before taking prime, archimedean, or infinite-length completion.
