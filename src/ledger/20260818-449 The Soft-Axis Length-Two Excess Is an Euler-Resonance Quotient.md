---
id: 449
authors:
  - marici.Benincasa
date: 2026-08-18
---
# The Soft-Axis Length-Two Excess Is an Euler-Resonance Quotient

## Record

Status: characteristic-zero symbolic identification of Entry 443's stable
two-dimensional excess, after reading Entries 447--448.

## Frozen exact differential

At
[
E=X_2=0,
qquad
K=a^4,quad L_1=b+1,quad L_2=a.
]
Set
[
c=b+1.
]

Every exact-form image is divisible by (a^4). Divide by that universal
factor and retain the ((s_a,s_b)=(1,1)) sector. Its two exact operators are
[
oxed{
D_b=a(1-cpartial_c),
qquad
D_a=c(apartial_a-7).
}
]

On a monomial (a^ic^j),
[
D_b(a^ic^j)=(1-j)a^{i+1}c^j,
]
and
[
D_a(a^ic^j)=(i-7)a^ic^{j+1}.
]

## Symbolic quotient theorem

The image of these two operators contains every monomial except
[
1,qquad a^7c.
]

Indeed:

- every (a^Ic^0) with (Ige1) is produced by (D_b);
- every (a^0c^J) with (Jge1) is produced by (D_a);
- for (I,Jge1), (D_b) produces the monomial unless (J=1);
- on (J=1), (D_a) produces it unless (I=7).

The remaining three exact sectors do not hit (a^7c). For a non-(q)
operator, the required source (c)-degree is (j=s_a), and its coefficient
is (s_a-j=0). For a (q)-operator, the required source degree is
(i=6+s_b), and its coefficient is (i-(s_b+6)=0). They cannot hit the
constant because every divided image retains an (a) or (c) prefactor.

Therefore, in characteristic zero,
[
oxed{
mathbf Q[a,c]ig/
operatorname{im}(d_{m ex}/a^4)
simeq
mathbf Qlangle[1],[a^7c]angle.
}
]

Restoring the universal factor gives intrinsic representatives
[
oxed{
[a^4],
qquad
[a^{11}(b+1)].
}
]

Thus Entry 443's length-two excess is not a finite-field or cutoff artifact.
Its earlier greedy representative (a^{11}b) differs from the canonical
Euler-resonant representative by a reducible (a^{11}) term.

## Relation to the Cayley--Menger module

Entry 447's flat module
[
mathcal M_{CM}=mathbf Q[u,a,b]/(K)
]
accounts for the quartic quotient with special fibre
(mathbf Q[a,b]/(a^4)). The two classes above arise from the exact-form
operator quotient after the universal (a^4) factor is removed. They are
therefore relative-de-Rham/exact-form coefficient data, not additional
Cayley--Menger carrier generators.

The unextended identification of (mathcal M_{CM}/u) with the full
exact-form cokernel remains falsified by precisely this Euler-resonance
plane.

## Relation to the meromorphic lift

Entry 448 proves that the soft Kodaira--Spencer class forces the meromorphic
vertical correction
[
V=rac{b^2-1}{4a}.
]
The present theorem does not define its action on the resonance plane:
coefficientwise application does not preserve the exact quotient without
the complete relative de Rham reduction. The next test must derive that
action from the deformed exact differential, not by applying (Vpartial_a)
to the chosen representatives alone.

## Classification

- quartic module: flat Cayley--Menger coefficient geometry;
- length-two plane: Euler-resonant exact-form cohomology;
- splitting from the quartic module: unproved;
- regular Gauss--Manin lift: obstructed by Entry 448;
- new carrier datum: none.

## Next falsifier

Work over dual numbers in the physical soft parameter (u=X_2). Deform all
four exact operators using the source-fixed (K(u),L_1(u),L_2(u)), construct
the first-order cokernel without choosing a projection, and test whether the
Euler-resonance plane:

1. lifts freely;
2. becomes (u)-torsion;
3. mixes nontrivially with the rank-four Cayley--Menger module; or
4. requires the logarithmic blowup of ((u,a)) already predicted by Entry
   448.

## Evidence

- `research/benincasa/soft-axis-euler-resonance-certificate.json`;
- `research/benincasa/marici-gm/src/bin/marked_tangency_support.rs`;
- Entries 443, 447, and 448.
