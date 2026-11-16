# Minimal Hall–triangle composition obstruction atlas

Computed for the 95 non-immediate instances among 478 reduced six-label contact systems.

A vertex x has contact set C(x). An eligible A-edge xy requires C(x) ∩ C(y) = ∅.
A Hall clause is a positive disjunction of eligible A-edges inside a deficient vertex set T.
A triangle clause prohibits simultaneously choosing all three A-edges of an eligible triangle.
Every representative core is minimally unsatisfiable: deleting any clause makes it Boolean satisfiable.
Isomorphism identifies edge variables and clause nodes, preserving clause type and size; it does not preserve ambient label embeddings.

| Type | Cases | Hall clauses | Triangle clauses | Forcing rounds |
|---:|---:|---:|---:|---|
| 1 | 23 | 7 | 3 | 0 |
| 2 | 17 | 3 | 1 | 0 |
| 3 | 8 | 7 | 3 | 1 |
| 4 | 7 | 7 | 5 | 1 |
| 5 | 4 | 6 | 3 | 0 |
| 6 | 4 | 12 | 9 | 3 |
| 7 | 2 | 7 | 4 | 1 |
| 8 | 2 | 10 | 6 | 1 |
| 9 | 2 | 11 | 9 | 2 |
| 10 | 2 | 8 | 5 | 1 |
| 11 | 2 | 12 | 10 | 3 |
| 12 | 2 | 16 | 15 | 2 |
| 13 | 2 | 8 | 6 | 2 |
| 14 | 2 | 7 | 5 | 1 |
| 15 | 2 | 18 | 15 | 6 |
| 16 | 2 | 7 | 4 | 1 |
| 17 | 2 | 8 | 5 | 1 |
| 18 | 2 | 7 | 3 | 2 |
| 19 | 1 | 11 | 7 | 2 |
| 20 | 1 | 8 | 5 | 0 |
| 21 | 1 | 16 | 14 | 4 |
| 22 | 1 | 15 | 14 | 2 |
| 23 | 1 | 15 | 12 | 3 |
| 24 | 1 | 12 | 12 | 4 |
| 25 | 1 | 16 | 14 | 3 |
| 26 | 1 | 16 | 14 | 3 |

## Type 1 — 23 instances

Core size: 7 Hall + 3 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:014`, `5:235`, `6:02`, `7:03`, `8:04`, `9:12`, `10:14`, `11:15`, `12:25`, `13:34`, `14:35`, `15:45`

Core A-edge variables (index: endpoint indices):

`e1:(0,3)`, `e2:(0,10)`, `e3:(1,3)`, `e4:(1,8)`, `e5:(1,12)`, `e6:(1,13)`, `e7:(3,8)`, `e8:(3,10)`, `e9:(12,13)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,3,7}` : e1
- `T={0,4,8,10}` : e2
- `T={1,3,10,13}` : e3 ∨ e6 ∨ e8
- `T={1,4,8,10}` : e4
- `T={1,9,11,12}` : e5
- `T={3,7,8,13}` : e7
- `T={5,12,13,14,15}` : e9

Triangle exclusions:

- `T={0,3,10}` : not all of e1, e2, e8
- `T={1,3,8}` : not all of e3, e4, e7
- `T={1,12,13}` : not all of e5, e6, e9

---

## Type 2 — 17 instances

Core size: 3 Hall + 1 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:012`, `6:012`, `7:345`, `8:03`, `9:04`, `10:13`, `11:15`, `12:24`, `13:25`, `14:35`, `15:45`

Core A-edge variables (index: endpoint indices):

`e1:(0,1)`, `e2:(0,2)`, `e3:(1,2)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,1,5,6}` : e1
- `T={0,2,5,6}` : e2
- `T={1,2,5,6}` : e3

Triangle exclusions:

- `T={0,1,2}` : not all of e1, e2, e3

---

## Type 3 — 8 instances

Core size: 7 Hall + 3 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:5`, `6:012`, `7:013`, `8:245`, `9:345`, `10:01`, `11:04`, `12:15`, `13:23`, `14:24`, `15:35`

Core A-edge variables (index: endpoint indices):

`e1:(0,2)`, `e2:(0,4)`, `e3:(1,3)`, `e4:(1,5)`, `e5:(2,3)`, `e6:(2,4)`, `e7:(2,10)`, `e8:(3,5)`, `e9:(3,10)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,2,6,10}` : e1 ∨ e7
- `T={0,4,11}` : e2
- `T={1,3,7,10}` : e3 ∨ e9
- `T={1,5,12}` : e4
- `T={2,3,13}` : e5
- `T={2,4,14}` : e6
- `T={3,5,15}` : e8

Triangle exclusions:

- `T={0,2,4}` : not all of e1, e2, e6
- `T={1,3,5}` : not all of e3, e4, e8
- `T={2,3,10}` : not all of e5, e7, e9

---

## Type 4 — 7 instances

Core size: 7 Hall + 5 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:012`, `6:034`, `7:135`, `8:02`, `9:04`, `10:14`, `11:15`, `12:23`, `13:25`, `14:35`, `15:45`

Core A-edge variables (index: endpoint indices):

`e1:(0,1)`, `e2:(0,2)`, `e3:(0,3)`, `e4:(0,4)`, `e5:(1,4)`, `e6:(1,8)`, `e7:(2,3)`, `e8:(2,4)`, `e9:(2,9)`, `e10:(3,9)`, `e11:(4,8)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,1,5,8}` : e1 ∨ e6
- `T={0,2,8}` : e2
- `T={0,3,6,9}` : e3 ∨ e10
- `T={0,4,9}` : e4
- `T={1,4,10}` : e5
- `T={2,3,12}` : e7
- `T={2,4,8,9}` : e8 ∨ e9 ∨ e11

Triangle exclusions:

- `T={0,1,4}` : not all of e1, e4, e5
- `T={0,2,3}` : not all of e2, e3, e7
- `T={0,2,4}` : not all of e2, e4, e8
- `T={1,4,8}` : not all of e5, e6, e11
- `T={2,3,9}` : not all of e7, e9, e10

---

## Type 5 — 4 instances

Core size: 6 Hall + 3 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:012`, `6:015`, `7:345`, `8:02`, `9:03`, `10:13`, `11:14`, `12:24`, `13:25`, `14:35`, `15:45`

Core A-edge variables (index: endpoint indices):

`e1:(0,2)`, `e2:(0,3)`, `e3:(0,13)`, `e4:(2,3)`, `e5:(2,4)`, `e6:(2,14)`, `e7:(3,13)`, `e8:(4,14)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,2,8}` : e1
- `T={0,3,9}` : e2
- `T={0,5,6,8,13}` : e3
- `T={2,3,13,14}` : e4 ∨ e6 ∨ e7
- `T={2,4,12}` : e5
- `T={4,7,14,15}` : e8

Triangle exclusions:

- `T={0,2,3}` : not all of e1, e2, e4
- `T={0,3,13}` : not all of e2, e3, e7
- `T={2,4,14}` : not all of e5, e6, e8

---

## Type 6 — 4 instances

Core size: 12 Hall + 9 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:5`, `6:012`, `7:013`, `8:045`, `9:145`, `10:02`, `11:13`, `12:23`, `13:24`, `14:35`, `15:45`

Core A-edge variables (index: endpoint indices):

`e1:(0,2)`, `e2:(0,4)`, `e3:(0,15)`, `e4:(1,3)`, `e5:(1,5)`, `e6:(1,15)`, `e7:(2,3)`, `e8:(2,4)`, `e9:(2,5)`, `e10:(2,14)`, `e11:(2,15)`, `e12:(3,4)`, `e13:(3,5)`, `e14:(3,13)`, `e15:(3,15)`, `e16:(4,5)`, `e17:(4,12)`, `e18:(4,14)`, `e19:(5,12)`, `e20:(5,13)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,2,10}` : e1
- `T={0,4,8,15}` : e2 ∨ e3
- `T={1,3,11}` : e4
- `T={1,5,9,15}` : e5 ∨ e6
- `T={2,3,12}` : e7
- `T={2,4,13}` : e8
- `T={2,5,12,14}` : e9 ∨ e10 ∨ e19
- `T={2,5,13,15}` : e9 ∨ e11 ∨ e20
- `T={3,4,12,13}` : e12 ∨ e14 ∨ e17
- `T={3,4,14,15}` : e12 ∨ e15 ∨ e18
- `T={3,5,14}` : e13
- `T={4,5,15}` : e16

Triangle exclusions:

- `T={0,2,4}` : not all of e1, e2, e8
- `T={0,2,15}` : not all of e1, e3, e11
- `T={1,3,5}` : not all of e4, e5, e13
- `T={1,3,15}` : not all of e4, e6, e15
- `T={2,3,4}` : not all of e7, e8, e12
- `T={2,3,5}` : not all of e7, e9, e13
- `T={2,4,14}` : not all of e8, e10, e18
- `T={3,5,13}` : not all of e13, e14, e20
- `T={4,5,12}` : not all of e16, e17, e19

---

## Type 7 — 2 instances

Core size: 7 Hall + 4 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:014`, `5:235`, `6:02`, `7:04`, `8:05`, `9:13`, `10:14`, `11:15`, `12:24`, `13:25`, `14:34`, `15:35`

Core A-edge variables (index: endpoint indices):

`e1:(0,2)`, `e2:(0,11)`, `e3:(1,2)`, `e4:(1,3)`, `e5:(1,7)`, `e6:(1,13)`, `e7:(2,7)`, `e8:(2,11)`, `e9:(3,13)`, `e10:(7,11)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,2,6}` : e1
- `T={0,4,7,8,11}` : e2 ∨ e10
- `T={1,2,11,13}` : e3 ∨ e6 ∨ e8
- `T={1,3,9}` : e4
- `T={1,4,7,10}` : e5
- `T={2,6,7,12}` : e7
- `T={3,5,13,15}` : e9

Triangle exclusions:

- `T={0,2,11}` : not all of e1, e2, e8
- `T={1,2,7}` : not all of e3, e5, e7
- `T={1,3,13}` : not all of e4, e6, e9
- `T={2,7,11}` : not all of e7, e8, e10

---

## Type 8 — 2 instances

Core size: 10 Hall + 6 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:012`, `6:013`, `7:245`, `8:03`, `9:05`, `10:14`, `11:15`, `12:23`, `13:25`, `14:34`, `15:45`

Core A-edge variables (index: endpoint indices):

`e1:(0,1)`, `e2:(0,2)`, `e3:(0,3)`, `e4:(0,4)`, `e5:(0,15)`, `e6:(1,2)`, `e7:(1,4)`, `e8:(1,9)`, `e9:(1,13)`, `e10:(1,15)`, `e11:(2,3)`, `e12:(2,15)`, `e13:(3,4)`, `e14:(4,9)`, `e15:(4,13)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,1,2,5}` : e1 ∨ e2 ∨ e6
- `T={0,3,8}` : e3
- `T={0,4,9,15}` : e4 ∨ e5 ∨ e14
- `T={1,4,10}` : e7
- `T={1,5,9,11,13}` : e8 ∨ e9
- `T={1,10,11,15}` : e10
- `T={2,3,12}` : e11
- `T={2,7,13,15}` : e12
- `T={3,4,14}` : e13
- `T={4,7,13,15}` : e15

Triangle exclusions:

- `T={0,1,15}` : not all of e1, e5, e10
- `T={0,2,3}` : not all of e2, e3, e11
- `T={0,3,4}` : not all of e3, e4, e13
- `T={1,2,15}` : not all of e6, e10, e12
- `T={1,4,9}` : not all of e7, e8, e14
- `T={1,4,13}` : not all of e7, e9, e15

---

## Type 9 — 2 instances

Core size: 11 Hall + 9 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:012`, `6:034`, `7:135`, `8:02`, `9:05`, `10:14`, `11:15`, `12:24`, `13:25`, `14:34`, `15:35`

Core A-edge variables (index: endpoint indices):

`e1:(0,2)`, `e2:(0,4)`, `e3:(0,12)`, `e4:(0,13)`, `e5:(0,14)`, `e6:(0,15)`, `e7:(1,2)`, `e8:(1,4)`, `e9:(1,8)`, `e10:(1,15)`, `e11:(2,4)`, `e12:(2,9)`, `e13:(2,14)`, `e14:(2,15)`, `e15:(4,8)`, `e16:(4,9)`, `e17:(4,15)`, `e18:(12,15)`, `e19:(13,14)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,2,8}` : e1
- `T={0,4,6,9,15}` : e2 ∨ e6 ∨ e16 ∨ e17
- `T={0,4,6,14}` : e2 ∨ e5
- `T={0,4,8,12}` : e2 ∨ e3 ∨ e15
- `T={0,8,9,13}` : e4
- `T={1,2,5,8}` : e7 ∨ e9
- `T={1,4,10}` : e8
- `T={1,7,11,15}` : e10
- `T={2,4,12}` : e11
- `T={2,8,9,13}` : e12
- `T={2,12,13,14,15}` : e13 ∨ e14 ∨ e18 ∨ e19

Triangle exclusions:

- `T={0,2,4}` : not all of e1, e2, e11
- `T={0,2,14}` : not all of e1, e5, e13
- `T={0,2,15}` : not all of e1, e6, e14
- `T={0,12,15}` : not all of e3, e6, e18
- `T={0,13,14}` : not all of e4, e5, e19
- `T={1,2,4}` : not all of e7, e8, e11
- `T={1,4,8}` : not all of e8, e9, e15
- `T={1,4,15}` : not all of e8, e10, e17
- `T={2,4,9}` : not all of e11, e12, e16

---

## Type 10 — 2 instances

Core size: 8 Hall + 5 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:012`, `6:035`, `7:145`, `8:02`, `9:03`, `10:13`, `11:15`, `12:24`, `13:25`, `14:34`, `15:45`

Core A-edge variables (index: endpoint indices):

`e1:(0,1)`, `e2:(0,2)`, `e3:(0,3)`, `e4:(1,3)`, `e5:(1,8)`, `e6:(1,15)`, `e7:(2,3)`, `e8:(2,9)`, `e9:(2,15)`, `e10:(3,8)`, `e11:(3,15)`, `e12:(9,15)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,1,5,8}` : e1 ∨ e5
- `T={0,2,8}` : e2
- `T={0,3,9}` : e3
- `T={1,3,10}` : e4
- `T={1,7,11,15}` : e6
- `T={2,3,8,9}` : e7 ∨ e8 ∨ e10
- `T={2,12,13,15}` : e9
- `T={3,6,9,14,15}` : e11 ∨ e12

Triangle exclusions:

- `T={0,1,3}` : not all of e1, e3, e4
- `T={0,2,3}` : not all of e2, e3, e7
- `T={1,3,8}` : not all of e4, e5, e10
- `T={1,3,15}` : not all of e4, e6, e11
- `T={2,9,15}` : not all of e8, e9, e12

---

## Type 11 — 2 instances

Core size: 12 Hall + 10 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:012`, `6:035`, `7:145`, `8:02`, `9:04`, `10:13`, `11:15`, `12:23`, `13:25`, `14:34`, `15:45`

Core A-edge variables (index: endpoint indices):

`e1:(0,2)`, `e2:(0,3)`, `e3:(0,4)`, `e4:(0,10)`, `e5:(0,11)`, `e6:(0,12)`, `e7:(0,14)`, `e8:(0,15)`, `e9:(1,2)`, `e10:(1,3)`, `e11:(1,8)`, `e12:(2,3)`, `e13:(2,4)`, `e14:(2,14)`, `e15:(3,4)`, `e16:(3,8)`, `e17:(3,11)`, `e18:(4,10)`, `e19:(4,11)`, `e20:(4,12)`, `e21:(10,15)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,2,8}` : e1
- `T={0,3,6,10,11}` : e2 ∨ e4 ∨ e5 ∨ e17
- `T={0,3,8,12}` : e2 ∨ e6 ∨ e16
- `T={0,4,9}` : e3
- `T={0,6,9,14,15}` : e7 ∨ e8
- `T={1,2,5,8}` : e9 ∨ e11
- `T={1,3,10}` : e10
- `T={2,3,12}` : e12
- `T={2,4,12,14}` : e13 ∨ e14 ∨ e20
- `T={3,4,14}` : e15
- `T={4,7,10,14,15}` : e18 ∨ e21
- `T={4,7,11,15}` : e19

Triangle exclusions:

- `T={0,2,3}` : not all of e1, e2, e12
- `T={0,2,4}` : not all of e1, e3, e13
- `T={0,2,14}` : not all of e1, e7, e14
- `T={0,4,10}` : not all of e3, e4, e18
- `T={0,4,11}` : not all of e3, e5, e19
- `T={0,4,12}` : not all of e3, e6, e20
- `T={0,10,15}` : not all of e4, e8, e21
- `T={1,2,3}` : not all of e9, e10, e12
- `T={1,3,8}` : not all of e10, e11, e16
- `T={3,4,11}` : not all of e15, e17, e19

---

## Type 12 — 2 instances

Core size: 16 Hall + 15 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:012`, `6:035`, `7:345`, `8:04`, `9:05`, `10:12`, `11:13`, `12:15`, `13:24`, `14:25`, `15:34`

Core A-edge variables (index: endpoint indices):

`e1:(0,1)`, `e2:(0,2)`, `e3:(0,3)`, `e4:(0,4)`, `e5:(0,10)`, `e6:(0,12)`, `e7:(0,13)`, `e8:(0,14)`, `e9:(1,2)`, `e10:(1,3)`, `e11:(1,4)`, `e12:(1,8)`, `e13:(1,9)`, `e14:(1,14)`, `e15:(2,3)`, `e16:(2,4)`, `e17:(2,6)`, `e18:(2,8)`, `e19:(2,12)`, `e20:(3,4)`, `e21:(3,8)`, `e22:(3,9)`, `e23:(3,14)`, `e24:(4,6)`, `e25:(4,9)`, `e26:(4,10)`, `e27:(4,12)`, `e28:(4,14)`, `e29:(8,12)`, `e30:(12,13)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,1,9,12}` : e1 ∨ e6 ∨ e13
- `T={0,2,3,6,14}` : e2 ∨ e3 ∨ e8 ∨ e15 ∨ e17 ∨ e23
- `T={0,2,5,10}` : e2 ∨ e5
- `T={0,2,8,13}` : e2 ∨ e7 ∨ e18
- `T={0,3,6,9}` : e3 ∨ e22
- `T={0,4,8}` : e4
- `T={1,2,10}` : e9
- `T={1,3,11}` : e10
- `T={1,4,8,9,12}` : e11 ∨ e12 ∨ e13 ∨ e25 ∨ e27 ∨ e29
- `T={1,10,12,14}` : e14
- `T={2,4,13}` : e16
- `T={2,10,12,14}` : e19
- `T={3,4,15}` : e20
- `T={3,6,7,8,15}` : e21
- `T={4,6,7,8,15}` : e24
- `T={4,10,12,13,14}` : e26 ∨ e27 ∨ e28 ∨ e30

Triangle exclusions:

- `T={0,1,14}` : not all of e1, e8, e14
- `T={0,2,4}` : not all of e2, e4, e16
- `T={0,3,4}` : not all of e3, e4, e20
- `T={0,4,10}` : not all of e4, e5, e26
- `T={0,4,14}` : not all of e4, e8, e28
- `T={0,12,13}` : not all of e6, e7, e30
- `T={1,2,3}` : not all of e9, e10, e15
- `T={1,2,4}` : not all of e9, e11, e16
- `T={1,3,8}` : not all of e10, e12, e21
- `T={1,3,9}` : not all of e10, e13, e22
- `T={1,3,14}` : not all of e10, e14, e23
- `T={2,4,6}` : not all of e16, e17, e24
- `T={2,4,12}` : not all of e16, e19, e27
- `T={2,8,12}` : not all of e18, e19, e29
- `T={3,4,9}` : not all of e20, e22, e25

---

## Type 13 — 2 instances

Core size: 8 Hall + 6 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:5`, `6:012`, `7:013`, `8:045`, `9:234`, `10:05`, `11:12`, `12:14`, `13:25`, `14:34`, `15:35`

Core A-edge variables (index: endpoint indices):

`e1:(0,1)`, `e2:(0,3)`, `e3:(0,5)`, `e4:(0,15)`, `e5:(1,3)`, `e6:(1,4)`, `e7:(1,10)`, `e8:(1,15)`, `e9:(3,4)`, `e10:(3,5)`, `e11:(3,10)`, `e12:(4,5)`, `e13:(4,10)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,1,3,7}` : e1 ∨ e2 ∨ e5
- `T={0,3,10,15}` : e2 ∨ e4 ∨ e11
- `T={0,5,10}` : e3
- `T={1,3,7,10,15}` : e5 ∨ e7 ∨ e8 ∨ e11
- `T={1,4,12}` : e6
- `T={3,4,14}` : e9
- `T={3,5,15}` : e10
- `T={4,5,8,10}` : e12 ∨ e13

Triangle exclusions:

- `T={0,1,15}` : not all of e1, e4, e8
- `T={0,3,5}` : not all of e2, e3, e10
- `T={1,3,4}` : not all of e5, e6, e9
- `T={1,4,10}` : not all of e6, e7, e13
- `T={3,4,5}` : not all of e9, e10, e12
- `T={3,4,10}` : not all of e9, e11, e13

---

## Type 14 — 2 instances

Core size: 7 Hall + 5 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:5`, `6:012`, `7:013`, `8:045`, `9:234`, `10:02`, `11:14`, `12:15`, `13:25`, `14:34`, `15:35`

Core A-edge variables (index: endpoint indices):

`e1:(0,1)`, `e2:(0,2)`, `e3:(0,3)`, `e4:(0,4)`, `e5:(0,5)`, `e6:(1,3)`, `e7:(1,4)`, `e8:(1,5)`, `e9:(2,5)`, `e10:(3,4)`, `e11:(4,5)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,1,3,7}` : e1 ∨ e3 ∨ e6
- `T={0,2,10}` : e2
- `T={0,4,5,8}` : e4 ∨ e5 ∨ e11
- `T={1,4,11}` : e7
- `T={1,5,12}` : e8
- `T={2,5,13}` : e9
- `T={3,4,14}` : e10

Triangle exclusions:

- `T={0,1,4}` : not all of e1, e4, e7
- `T={0,2,5}` : not all of e2, e5, e9
- `T={0,3,4}` : not all of e3, e4, e10
- `T={1,3,4}` : not all of e6, e7, e10
- `T={1,4,5}` : not all of e7, e8, e11

---

## Type 15 — 2 instances

Core size: 18 Hall + 15 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:5`, `6:012`, `7:013`, `8:045`, `9:234`, `10:02`, `11:13`, `12:15`, `13:25`, `14:34`, `15:45`

Core A-edge variables (index: endpoint indices):

`e1:(0,2)`, `e2:(0,3)`, `e3:(0,5)`, `e4:(0,11)`, `e5:(0,12)`, `e6:(0,15)`, `e7:(1,2)`, `e8:(1,3)`, `e9:(1,4)`, `e10:(1,5)`, `e11:(1,9)`, `e12:(1,13)`, `e13:(1,14)`, `e14:(1,15)`, `e15:(2,4)`, `e16:(2,5)`, `e17:(2,7)`, `e18:(2,11)`, `e19:(2,12)`, `e20:(2,14)`, `e21:(3,4)`, `e22:(3,5)`, `e23:(3,12)`, `e24:(3,15)`, `e25:(4,5)`, `e26:(4,11)`, `e27:(4,12)`, `e28:(5,7)`, `e29:(5,9)`, `e30:(5,11)`, `e31:(5,14)`, `e32:(13,14)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,2,10}` : e1
- `T={0,3,5,7,12}` : e2 ∨ e3 ∨ e5 ∨ e22 ∨ e23 ∨ e28
- `T={0,3,7,11}` : e2 ∨ e4
- `T={0,5,8,15}` : e3 ∨ e6
- `T={1,2,4,9,11}` : e7 ∨ e9 ∨ e11 ∨ e15 ∨ e18 ∨ e26
- `T={1,2,6,7,11}` : e7 ∨ e17 ∨ e18
- `T={1,2,12,13}` : e7 ∨ e12 ∨ e19
- `T={1,3,11}` : e8
- `T={1,4,11,14}` : e9 ∨ e13 ∨ e26
- `T={1,4,12,15}` : e9 ∨ e14 ∨ e27
- `T={1,5,12}` : e10
- `T={2,4,9,14}` : e15 ∨ e20
- `T={2,5,13}` : e16
- `T={3,4,14}` : e21
- `T={3,5,11,12}` : e22 ∨ e23 ∨ e30
- `T={3,5,14,15}` : e22 ∨ e24 ∨ e31
- `T={4,5,15}` : e25
- `T={5,9,13,14,15}` : e29 ∨ e31 ∨ e32

Triangle exclusions:

- `T={0,2,5}` : not all of e1, e3, e16
- `T={0,2,11}` : not all of e1, e4, e18
- `T={0,2,12}` : not all of e1, e5, e19
- `T={0,3,15}` : not all of e2, e6, e24
- `T={1,2,5}` : not all of e7, e10, e16
- `T={1,3,4}` : not all of e8, e9, e21
- `T={1,3,5}` : not all of e8, e10, e22
- `T={1,3,15}` : not all of e8, e14, e24
- `T={1,5,9}` : not all of e10, e11, e29
- `T={1,13,14}` : not all of e12, e13, e32
- `T={2,4,5}` : not all of e15, e16, e25
- `T={2,5,7}` : not all of e16, e17, e28
- `T={2,5,14}` : not all of e16, e20, e31
- `T={3,4,12}` : not all of e21, e23, e27
- `T={4,5,11}` : not all of e25, e26, e30

---

## Type 16 — 2 instances

Core size: 7 Hall + 4 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:5`, `6:012`, `7:013`, `8:045`, `9:245`, `10:04`, `11:13`, `12:15`, `13:23`, `14:25`, `15:34`

Core A-edge variables (index: endpoint indices):

`e1:(1,3)`, `e2:(1,5)`, `e3:(1,13)`, `e4:(2,3)`, `e5:(2,4)`, `e6:(3,4)`, `e7:(3,5)`, `e8:(3,14)`, `e9:(4,14)`, `e10:(5,13)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={1,3,11}` : e1
- `T={1,5,12}` : e2
- `T={1,6,7,11,13}` : e3
- `T={2,3,13}` : e4
- `T={2,4,9,14}` : e5 ∨ e9
- `T={3,4,15}` : e6
- `T={3,5,13,14}` : e7 ∨ e8 ∨ e10

Triangle exclusions:

- `T={1,3,5}` : not all of e1, e2, e7
- `T={1,5,13}` : not all of e2, e3, e10
- `T={2,3,4}` : not all of e4, e5, e6
- `T={3,4,14}` : not all of e6, e8, e9

---

## Type 17 — 2 instances

Core size: 8 Hall + 5 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:5`, `6:012`, `7:013`, `8:045`, `9:245`, `10:03`, `11:14`, `12:15`, `13:23`, `14:24`, `15:35`

Core A-edge variables (index: endpoint indices):

`e1:(0,1)`, `e2:(0,2)`, `e3:(0,3)`, `e4:(0,4)`, `e5:(0,5)`, `e6:(1,2)`, `e7:(1,4)`, `e8:(1,5)`, `e9:(2,3)`, `e10:(2,4)`, `e11:(3,5)`, `e12:(4,5)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,1,2,6}` : e1 ∨ e2 ∨ e6
- `T={0,3,10}` : e3
- `T={0,4,5,8}` : e4 ∨ e5 ∨ e12
- `T={1,4,11}` : e7
- `T={1,5,12}` : e8
- `T={2,3,13}` : e9
- `T={2,4,14}` : e10
- `T={3,5,15}` : e11

Triangle exclusions:

- `T={0,1,4}` : not all of e1, e4, e7
- `T={0,2,3}` : not all of e2, e3, e9
- `T={0,3,5}` : not all of e3, e5, e11
- `T={1,2,4}` : not all of e6, e7, e10
- `T={1,4,5}` : not all of e7, e8, e12

---

## Type 18 — 2 instances

Core size: 7 Hall + 3 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:5`, `6:012`, `7:013`, `8:045`, `9:245`, `10:02`, `11:13`, `12:14`, `13:23`, `14:35`, `15:45`

Core A-edge variables (index: endpoint indices):

`e1:(0,2)`, `e2:(0,4)`, `e3:(0,5)`, `e4:(0,15)`, `e5:(2,3)`, `e6:(2,5)`, `e7:(2,15)`, `e8:(3,5)`, `e9:(4,5)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,2,10}` : e1
- `T={0,4,8,15}` : e2 ∨ e4
- `T={0,5,8,15}` : e3 ∨ e4
- `T={2,3,13}` : e5
- `T={2,5,9,15}` : e6 ∨ e7
- `T={3,5,14}` : e8
- `T={4,5,15}` : e9

Triangle exclusions:

- `T={0,2,15}` : not all of e1, e4, e7
- `T={0,4,5}` : not all of e2, e3, e9
- `T={2,3,5}` : not all of e5, e6, e8

---

## Type 19 — 1 instances

Core size: 11 Hall + 7 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:015`, `6:025`, `7:345`, `8:03`, `9:04`, `10:13`, `11:14`, `12:15`, `13:23`, `14:24`, `15:25`

Core A-edge variables (index: endpoint indices):

`e1:(0,1)`, `e2:(0,2)`, `e3:(0,3)`, `e4:(0,4)`, `e5:(0,12)`, `e6:(0,15)`, `e7:(1,2)`, `e8:(1,3)`, `e9:(1,4)`, `e10:(1,13)`, `e11:(2,3)`, `e12:(2,4)`, `e13:(2,10)`, `e14:(4,10)`, `e15:(4,12)`, `e16:(4,13)`, `e17:(4,15)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,1,5,12}` : e1 ∨ e5
- `T={0,2,6,15}` : e2 ∨ e6
- `T={0,3,8}` : e3
- `T={0,4,9}` : e4
- `T={1,2,10,13}` : e7 ∨ e10 ∨ e13
- `T={1,3,10}` : e8
- `T={1,4,11}` : e9
- `T={2,3,13}` : e11
- `T={2,4,14}` : e12
- `T={4,7,10,11,12}` : e14 ∨ e15
- `T={4,7,13,14,15}` : e16 ∨ e17

Triangle exclusions:

- `T={0,1,3}` : not all of e1, e3, e8
- `T={0,2,3}` : not all of e2, e3, e11
- `T={0,4,12}` : not all of e4, e5, e15
- `T={0,4,15}` : not all of e4, e6, e17
- `T={1,2,3}` : not all of e7, e8, e11
- `T={1,4,13}` : not all of e9, e10, e16
- `T={2,4,10}` : not all of e12, e13, e14

---

## Type 20 — 1 instances

Core size: 8 Hall + 5 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:5`, `6:012`, `7:013`, `8:024`, `9:135`, `10:05`, `11:14`, `12:24`, `13:25`, `14:34`, `15:35`

Core A-edge variables (index: endpoint indices):

`e1:(0,2)`, `e2:(0,3)`, `e3:(0,5)`, `e4:(2,3)`, `e5:(2,4)`, `e6:(2,5)`, `e7:(2,7)`, `e8:(3,4)`, `e9:(3,5)`, `e10:(3,6)`, `e11:(4,6)`, `e12:(5,7)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,2,3,6,7}` : e1 ∨ e2 ∨ e4 ∨ e7 ∨ e10
- `T={0,5,10}` : e3
- `T={2,4,12}` : e5
- `T={2,5,13}` : e6
- `T={3,4,14}` : e8
- `T={3,5,15}` : e9
- `T={4,6,8,11,12}` : e11
- `T={5,7,9,10,15}` : e12

Triangle exclusions:

- `T={0,2,5}` : not all of e1, e3, e6
- `T={0,3,5}` : not all of e2, e3, e9
- `T={2,3,4}` : not all of e4, e5, e8
- `T={2,5,7}` : not all of e6, e7, e12
- `T={3,4,6}` : not all of e8, e10, e11

---

## Type 21 — 1 instances

Core size: 16 Hall + 14 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:5`, `6:012`, `7:013`, `8:024`, `9:135`, `10:04`, `11:15`, `12:23`, `13:25`, `14:34`, `15:45`

Core A-edge variables (index: endpoint indices):

`e1:(0,1)`, `e2:(0,2)`, `e3:(0,3)`, `e4:(0,4)`, `e5:(0,5)`, `e6:(0,14)`, `e7:(0,15)`, `e8:(1,2)`, `e9:(1,3)`, `e10:(1,4)`, `e11:(1,5)`, `e12:(1,13)`, `e13:(1,15)`, `e14:(2,3)`, `e15:(2,4)`, `e16:(2,5)`, `e17:(2,10)`, `e18:(2,11)`, `e19:(2,14)`, `e20:(3,4)`, `e21:(3,5)`, `e22:(3,10)`, `e23:(3,11)`, `e24:(3,13)`, `e25:(4,5)`, `e26:(4,11)`, `e27:(4,12)`, `e28:(5,10)`, `e29:(5,12)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,1,2,6}` : e1 ∨ e2 ∨ e8
- `T={0,1,3,7}` : e1 ∨ e3 ∨ e9
- `T={0,3,10,14}` : e3 ∨ e6 ∨ e22
- `T={0,4,10}` : e4
- `T={0,5,10,15}` : e5 ∨ e7 ∨ e28
- `T={1,2,11,13}` : e8 ∨ e12 ∨ e18
- `T={1,4,11,15}` : e10 ∨ e13 ∨ e26
- `T={1,5,11}` : e11
- `T={2,3,12}` : e14
- `T={2,4,8,10}` : e15 ∨ e17
- `T={2,4,12,14}` : e15 ∨ e19 ∨ e27
- `T={2,5,13}` : e16
- `T={3,4,14}` : e20
- `T={3,5,9,11}` : e21 ∨ e23
- `T={3,5,12,13}` : e21 ∨ e24 ∨ e29
- `T={4,5,15}` : e25

Triangle exclusions:

- `T={0,1,15}` : not all of e1, e7, e13
- `T={0,2,14}` : not all of e2, e6, e19
- `T={0,3,4}` : not all of e3, e4, e20
- `T={0,4,5}` : not all of e4, e5, e25
- `T={1,2,5}` : not all of e8, e11, e16
- `T={1,3,13}` : not all of e9, e12, e24
- `T={1,4,5}` : not all of e10, e11, e25
- `T={2,3,4}` : not all of e14, e15, e20
- `T={2,3,5}` : not all of e14, e16, e21
- `T={2,3,10}` : not all of e14, e17, e22
- `T={2,3,11}` : not all of e14, e18, e23
- `T={2,5,10}` : not all of e16, e17, e28
- `T={3,4,11}` : not all of e20, e23, e26
- `T={4,5,12}` : not all of e25, e27, e29

---

## Type 22 — 1 instances

Core size: 15 Hall + 14 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:5`, `6:012`, `7:013`, `8:024`, `9:135`, `10:05`, `11:14`, `12:23`, `13:24`, `14:35`, `15:45`

Core A-edge variables (index: endpoint indices):

`e1:(0,1)`, `e2:(0,2)`, `e3:(0,3)`, `e4:(0,4)`, `e5:(0,5)`, `e6:(0,11)`, `e7:(0,15)`, `e8:(1,2)`, `e9:(1,4)`, `e10:(1,5)`, `e11:(1,10)`, `e12:(1,15)`, `e13:(2,3)`, `e14:(2,4)`, `e15:(2,5)`, `e16:(2,10)`, `e17:(2,11)`, `e18:(3,4)`, `e19:(3,5)`, `e20:(3,10)`, `e21:(3,11)`, `e22:(4,5)`, `e23:(4,6)`, `e24:(4,7)`, `e25:(4,10)`, `e26:(5,6)`, `e27:(5,7)`, `e28:(5,11)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,1,2,6}` : e1 ∨ e2 ∨ e8
- `T={0,3,4,7,11}` : e3 ∨ e4 ∨ e6 ∨ e18 ∨ e21 ∨ e24
- `T={0,4,10,15}` : e4 ∨ e7 ∨ e25
- `T={0,5,10}` : e5
- `T={1,2,5,6,10}` : e8 ∨ e10 ∨ e11 ∨ e15 ∨ e16 ∨ e26
- `T={1,4,11}` : e9
- `T={1,5,11,15}` : e10 ∨ e12 ∨ e28
- `T={2,3,12}` : e13
- `T={2,4,13}` : e14
- `T={2,6,8,11,13}` : e17
- `T={3,5,14}` : e19
- `T={3,7,9,10,14}` : e20
- `T={4,5,15}` : e22
- `T={4,6,8,11,13}` : e23
- `T={5,7,9,10,14}` : e27

Triangle exclusions:

- `T={0,1,15}` : not all of e1, e7, e12
- `T={0,2,11}` : not all of e2, e6, e17
- `T={0,3,5}` : not all of e3, e5, e19
- `T={0,4,5}` : not all of e4, e5, e22
- `T={0,5,11}` : not all of e5, e6, e28
- `T={1,2,4}` : not all of e8, e9, e14
- `T={1,4,5}` : not all of e9, e10, e22
- `T={1,4,10}` : not all of e9, e11, e25
- `T={2,3,4}` : not all of e13, e14, e18
- `T={2,3,5}` : not all of e13, e15, e19
- `T={2,3,10}` : not all of e13, e16, e20
- `T={2,3,11}` : not all of e13, e17, e21
- `T={4,5,6}` : not all of e22, e23, e26
- `T={4,5,7}` : not all of e22, e24, e27

---

## Type 23 — 1 instances

Core size: 15 Hall + 12 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:5`, `6:012`, `7:013`, `8:024`, `9:145`, `10:03`, `11:15`, `12:24`, `13:25`, `14:34`, `15:35`

Core A-edge variables (index: endpoint indices):

`e1:(0,1)`, `e2:(0,2)`, `e3:(0,3)`, `e4:(0,4)`, `e5:(0,5)`, `e6:(0,12)`, `e7:(0,14)`, `e8:(0,15)`, `e9:(1,2)`, `e10:(1,3)`, `e11:(1,5)`, `e12:(1,10)`, `e13:(1,15)`, `e14:(2,3)`, `e15:(2,4)`, `e16:(2,5)`, `e17:(2,14)`, `e18:(3,4)`, `e19:(3,5)`, `e20:(3,11)`, `e21:(3,12)`, `e22:(4,5)`, `e23:(4,10)`, `e24:(4,11)`, `e25:(5,10)`, `e26:(10,11)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,1,2,6}` : e1 ∨ e2 ∨ e9
- `T={0,3,10}` : e3
- `T={0,4,8,12}` : e4 ∨ e6
- `T={0,4,10,14}` : e4 ∨ e7 ∨ e23
- `T={0,5,10,15}` : e5 ∨ e8 ∨ e25
- `T={1,3,7,10}` : e10 ∨ e12
- `T={1,3,11,15}` : e10 ∨ e13 ∨ e20
- `T={1,5,11}` : e11
- `T={2,3,12,14}` : e14 ∨ e17 ∨ e21
- `T={2,4,12}` : e15
- `T={2,5,13}` : e16
- `T={3,4,14}` : e18
- `T={3,5,15}` : e19
- `T={3,7,10,11,15}` : e20 ∨ e26
- `T={4,5,9,11}` : e22 ∨ e24

Triangle exclusions:

- `T={0,1,15}` : not all of e1, e8, e13
- `T={0,2,14}` : not all of e2, e7, e17
- `T={0,3,4}` : not all of e3, e4, e18
- `T={0,3,5}` : not all of e3, e5, e19
- `T={0,3,12}` : not all of e3, e6, e21
- `T={1,2,5}` : not all of e9, e11, e16
- `T={1,3,5}` : not all of e10, e11, e19
- `T={1,5,10}` : not all of e11, e12, e25
- `T={2,3,4}` : not all of e14, e15, e18
- `T={2,4,5}` : not all of e15, e16, e22
- `T={3,4,11}` : not all of e18, e20, e24
- `T={4,10,11}` : not all of e23, e24, e26

---

## Type 24 — 1 instances

Core size: 12 Hall + 12 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:5`, `6:012`, `7:013`, `8:024`, `9:145`, `10:05`, `11:13`, `12:23`, `13:24`, `14:35`, `15:45`

Core A-edge variables (index: endpoint indices):

`e1:(0,3)`, `e2:(0,4)`, `e3:(0,5)`, `e4:(0,12)`, `e5:(1,2)`, `e6:(1,3)`, `e7:(1,5)`, `e8:(1,8)`, `e9:(1,13)`, `e10:(1,15)`, `e11:(2,3)`, `e12:(2,4)`, `e13:(2,5)`, `e14:(2,14)`, `e15:(3,4)`, `e16:(3,5)`, `e17:(3,8)`, `e18:(3,13)`, `e19:(3,15)`, `e20:(4,5)`, `e21:(4,12)`, `e22:(4,14)`, `e23:(5,12)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,3,4,8,12}` : e1 ∨ e2 ∨ e4 ∨ e15 ∨ e17 ∨ e21
- `T={0,5,10}` : e3
- `T={1,2,6,8,13}` : e5 ∨ e8 ∨ e9
- `T={1,3,11}` : e6
- `T={1,5,9,15}` : e7 ∨ e10
- `T={2,3,12}` : e11
- `T={2,4,13}` : e12
- `T={2,5,12,14}` : e13 ∨ e14 ∨ e23
- `T={3,4,12,13}` : e15 ∨ e18 ∨ e21
- `T={3,4,14,15}` : e15 ∨ e19 ∨ e22
- `T={3,5,14}` : e16
- `T={4,5,15}` : e20

Triangle exclusions:

- `T={0,3,5}` : not all of e1, e3, e16
- `T={0,4,5}` : not all of e2, e3, e20
- `T={0,5,12}` : not all of e3, e4, e23
- `T={1,2,3}` : not all of e5, e6, e11
- `T={1,3,5}` : not all of e6, e7, e16
- `T={1,3,8}` : not all of e6, e8, e17
- `T={1,3,13}` : not all of e6, e9, e18
- `T={1,3,15}` : not all of e6, e10, e19
- `T={2,3,4}` : not all of e11, e12, e15
- `T={2,3,5}` : not all of e11, e13, e16
- `T={2,4,14}` : not all of e12, e14, e22
- `T={4,5,12}` : not all of e20, e21, e23

---

## Type 25 — 1 instances

Core size: 16 Hall + 14 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:5`, `6:012`, `7:013`, `8:024`, `9:345`, `10:03`, `11:14`, `12:15`, `13:24`, `14:25`, `15:35`

Core A-edge variables (index: endpoint indices):

`e1:(0,3)`, `e2:(0,4)`, `e3:(0,5)`, `e4:(0,14)`, `e5:(0,15)`, `e6:(1,2)`, `e7:(1,3)`, `e8:(1,4)`, `e9:(1,5)`, `e10:(1,8)`, `e11:(1,10)`, `e12:(1,13)`, `e13:(1,14)`, `e14:(2,3)`, `e15:(2,4)`, `e16:(2,5)`, `e17:(2,11)`, `e18:(2,12)`, `e19:(2,15)`, `e20:(3,5)`, `e21:(3,14)`, `e22:(4,5)`, `e23:(4,12)`, `e24:(4,14)`, `e25:(4,15)`, `e26:(5,8)`, `e27:(5,10)`, `e28:(5,11)`, `e29:(5,13)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,3,10}` : e1
- `T={0,4,5,8,14}` : e2 ∨ e3 ∨ e4 ∨ e22 ∨ e24 ∨ e26
- `T={0,5,10,15}` : e3 ∨ e5 ∨ e27
- `T={1,2,12,14}` : e6 ∨ e13 ∨ e18
- `T={1,3,7,10}` : e7 ∨ e11
- `T={1,4,11}` : e8
- `T={1,5,12}` : e9
- `T={1,6,8,11,13}` : e10 ∨ e12
- `T={2,3,14,15}` : e14 ∨ e19 ∨ e21
- `T={2,4,13}` : e15
- `T={2,5,14}` : e16
- `T={2,6,8,11,13}` : e17
- `T={3,5,15}` : e20
- `T={4,5,9,15}` : e22 ∨ e25
- `T={4,5,11,12}` : e22 ∨ e23 ∨ e28
- `T={4,5,13,14}` : e22 ∨ e24 ∨ e29

Triangle exclusions:

- `T={0,3,5}` : not all of e1, e3, e20
- `T={0,3,14}` : not all of e1, e4, e21
- `T={0,4,15}` : not all of e2, e5, e25
- `T={1,2,4}` : not all of e6, e8, e15
- `T={1,3,5}` : not all of e7, e9, e20
- `T={1,4,5}` : not all of e8, e9, e22
- `T={1,4,14}` : not all of e8, e13, e24
- `T={1,5,8}` : not all of e9, e10, e26
- `T={1,5,10}` : not all of e9, e11, e27
- `T={1,5,13}` : not all of e9, e12, e29
- `T={2,3,5}` : not all of e14, e16, e20
- `T={2,4,12}` : not all of e15, e18, e23
- `T={2,4,15}` : not all of e15, e19, e25
- `T={2,5,11}` : not all of e16, e17, e28

---

## Type 26 — 1 instances

Core size: 16 Hall + 14 triangle clauses.

Exterior vertices (index: contact):

`0:0`, `1:1`, `2:2`, `3:3`, `4:4`, `5:5`, `6:012`, `7:013`, `8:024`, `9:345`, `10:04`, `11:13`, `12:15`, `13:23`, `14:25`, `15:45`

Core A-edge variables (index: endpoint indices):

`e1:(0,3)`, `e2:(0,4)`, `e3:(0,5)`, `e4:(0,12)`, `e5:(0,15)`, `e6:(1,2)`, `e7:(1,3)`, `e8:(1,4)`, `e9:(1,5)`, `e10:(1,13)`, `e11:(1,14)`, `e12:(1,15)`, `e13:(2,3)`, `e14:(2,4)`, `e15:(2,5)`, `e16:(2,7)`, `e17:(2,10)`, `e18:(2,11)`, `e19:(2,12)`, `e20:(3,5)`, `e21:(3,12)`, `e22:(3,14)`, `e23:(3,15)`, `e24:(4,5)`, `e25:(4,12)`, `e26:(5,7)`, `e27:(5,10)`, `e28:(5,11)`, `e29:(5,13)`

Hall obligations (deficient vertex set; eligible edge variables):

- `T={0,3,5,7,12}` : e1 ∨ e3 ∨ e4 ∨ e20 ∨ e21 ∨ e26
- `T={0,4,10}` : e2
- `T={0,5,10,15}` : e3 ∨ e5 ∨ e27
- `T={1,2,12,14}` : e6 ∨ e11 ∨ e19
- `T={1,3,11}` : e7
- `T={1,4,12,15}` : e8 ∨ e12 ∨ e25
- `T={1,5,12}` : e9
- `T={1,6,7,11,13}` : e10
- `T={2,3,13}` : e13
- `T={2,4,8,10}` : e14 ∨ e17
- `T={2,5,14}` : e15
- `T={2,6,7,11,13}` : e16 ∨ e18
- `T={3,5,9,15}` : e20 ∨ e23
- `T={3,5,11,12}` : e20 ∨ e21 ∨ e28
- `T={3,5,13,14}` : e20 ∨ e22 ∨ e29
- `T={4,5,15}` : e24

Triangle exclusions:

- `T={0,3,15}` : not all of e1, e5, e23
- `T={0,4,5}` : not all of e2, e3, e24
- `T={0,4,12}` : not all of e2, e4, e25
- `T={1,2,3}` : not all of e6, e7, e13
- `T={1,3,5}` : not all of e7, e9, e20
- `T={1,3,14}` : not all of e7, e11, e22
- `T={1,3,15}` : not all of e7, e12, e23
- `T={1,4,5}` : not all of e8, e9, e24
- `T={1,5,13}` : not all of e9, e10, e29
- `T={2,3,12}` : not all of e13, e19, e21
- `T={2,4,5}` : not all of e14, e15, e24
- `T={2,5,7}` : not all of e15, e16, e26
- `T={2,5,10}` : not all of e15, e17, e27
- `T={2,5,11}` : not all of e15, e18, e28

---