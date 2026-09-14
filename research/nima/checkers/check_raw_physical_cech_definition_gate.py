"""Audit whether rawCech has a concrete physical definition rather than an interface parameter."""
import json
from pathlib import Path
root=Path('research/nima/rzk');hits=[];definitions=[]
for path in root.glob('*.rzk.md'):
 text=path.read_text(encoding='utf-8')
 if 'rawCech' in text:
  hits.append(str(path))
  for line in text.splitlines():
   if '#define' in line and 'rawCech' in line: definitions.append({'file':str(path),'line':line.strip()})
assert hits
assert not definitions
out={'schema':'marici.nima.raw-physical-cech-definition-gate.v1','status':'raw_physical_Cech_is_interface_only',
'files_mentioning_rawCech':hits,'concrete_rawCech_definitions':definitions,
'countermodel':'the polymorphic interface permits rawCech to be either the selected target or zero while all constructed road data are unchanged',
'consequence':'rawCech=Čech(v) cannot be proved until a physical chart/residue formula defines rawCech',
'required_input':'one occurrence-labelled local qG12 raw defect formula in the same ramified filtered Q target'}
Path('research/nima/results/raw-physical-cech-definition-gate.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
