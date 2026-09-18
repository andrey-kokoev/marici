#!/usr/bin/env python3
"""Audit constructor coverage of all 14 source-classified N2MHV invariants."""
import ast,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
f=json.loads((ROOT/'research/nima/fixtures/n2mhv-yangian-invariant-constructor-coverage.v1.json').read_text());rows=f['cyclic_classes'];mapping=f['constructor_mapping']
modules=(ROOT/'research/nima/momentum_twistor_constructors.py').read_text()+(ROOT/'research/nima/momentum_twistor_super.py').read_text();defined={n.name for tree in [ast.parse(modules)] for n in ast.walk(tree) if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
required={name for names in mapping.values() for name in names};kinds=Counter(r['kind'] for r in rows)
checks={'fourteen_rows':len(rows)==14,'ids_exactly_1_through_14':[r['id'] for r in rows]==list(range(1,15)),'all_four_constructor_kinds_present':set(kinds)==set(mapping),'all_mapped_public_constructors_defined':required<=defined,'unique_quadratic_four_mass_class':kinds['four-mass-psi']==1,'unique_phi_class':kinds['plane-line-phi']==1,'three_plain_classes':kinds['plain']==3,'nine_ordinary_line_plane_classes':kinds['line-plane']==9}
out={'schema':'marici.nima.n2mhv-yangian-invariant-constructor-coverage.v1','source_fixture':'research/nima/fixtures/n2mhv-yangian-invariant-constructor-coverage.v1.json','kind_counts':dict(kinds),'required_public_constructors':sorted(required),'missing_public_constructors':sorted(required-defined),'checks':checks,'passed':all(checks.values()),'scope':'Syntactic constructor coverage of all 14 source formulas; not independent componentwise evaluation of every row.'}
p=ROOT/'research/nima/results/n2mhv-yangian-invariant-constructor-coverage.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
