# Conditionalization Is the Missing Central-Loop-to-Sheet-Gate Morphism

## Exact synthesis

The endogenous sheet pair supplies the selector carrier, and Entry 3766 shows
that its reflection-odd involution descends projectively. The algebraic map
from the metaplectic central sign to that involution is conditionalization.

Let (P_0,P_1) be the two sheet-branch projectors. Conditionalizing the
central lift gives

\[
C_{-I}=P_0\otimes I+P_1\otimes(-I)=Z\otimes I.
\]

Thus the central phase, invisible on the magnetic target by itself, becomes a
relative sheet phase. This is exactly the transgression proved abstractly in
Entry 3711.

The complete mathematical chain is now:

```text
metaplectic phase-lifted central element -I
  -- conditionalization on the endogenous sheet pair -->
reflection-odd linear selector phase Z
  -- projective descent through sheet exchange -->
global projective gate [Z]
```

The metaplectic two-cocycle identity supplies the triple-composition filler,
so no new higher associativity anomaly appears.

## Executable no-go

The ordinary physical channel forgets the required input distinction:

\[
\mathcal U_I=\mathcal U_{-I}.
\]

But their controlled outputs are (I) and (Z), respectively. Therefore no
compiler receiving only the conjugation channel can construct the selective
sheet gate. Conditionalization is not a well-defined operation on the
projective channel quotient.

## Final missing constructor

No mathematical arrow remains unidentified. The sole missing constructor is
an executable phase-lifted sheet conditional:

```text
input authority
  a specified metaplectic lift or Hamiltonian path retaining the central sign

branch authority
  the endogenous sheet packet as a coherent control carrier

operation
  apply the lifted loop on one branch and identity on its complement

output
  the projective reflection-odd gate [Z]
```

Figueiredo WP869 and WP870 give the deformation and authority pattern: the
sheet projector and detector frame must be co-transported by one source
connection. They do not supply the magnetic controlled implementation.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/sheet_conditional_metaplectic_transgression_checks.py
```
