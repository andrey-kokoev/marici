"""Read-only symbol closure; outputs only the Nima dependency manifest."""
import argparse
import hashlib
import json
import re
from pathlib import Path

parser=argparse.ArgumentParser()
parser.add_argument('--module',choices=['15-integer-hom-indexing','16-integer-coefficient-complex','17-integer-hom-square','18-finite-coefficient-presentations','19-loaded-polynomial-cech-modules','20-loaded-coefficient-square','21-loaded-finite-cech-chain','22-endpoint-relative-cech-complex','23-endpoint-relative-cech-square','24-endpoint-quotient-projection','25-setoid-coefficient-interface','26-supported-local-coefficient-complex','27-supported-local-residue','28-supported-augmentation-boundaries','29-supported-top-normalization','30-physical-source-comparison','31-normalization-conductor-roof','32-conditional-conductor-morse-exactness','33-relative-physical-fibre','34-formal-endpoint-lines','35-relative-sparse-comparison','36-corrected-morse-fibre-evaluation','37-six-direction-first-conductor-map','38-endpoint-relative-source-fibre','39-endpoint-pullback-homotopy','40-reduced-seven-state-q-cell','41-q-occurrence-tensor','42-seven-triangle-morse-primitive','43-morse-filling-attachment','44-endpoint-normal-annihilators','45-alternating-rees-annihilator','46-repeated-normal-excess-source','47-d03-resonance-compatibility','48-q-lift-naturality-obstruction','49-branch-rees-excess-and-occurrence-line','50-finite-dual-transgression','51-d03-fixed-beta-specialization','52-x35-strict-occurrence-summand','53-d03-specialization-map','54-d03-supported-cartier-cone','55-d03-three-carrier-separation','56-d03-native-endpoint-q-vectors','57-central-rees-gysin-channel','58-q-three-pair-supported-section','59-beta-zero-supported-difference','60-common-spatial-correspondence-gate','61-regulator-vertex-decomposition','62-orbit-source-assembly-gate','63-beta-endpoint-q-transgression','64-cubical-supported-dual-critical-edge','65-union-recollement-obstruction-persistence','66-first-conductor-framed-deformations','67-coherent-endpoint-q-primary-frame','68-divisor-complement-lift-torsor','69-occurrence-linear-reverse-pairing','70-first-conductor-coherent-ranks','71-normalization-endpoint-extension','72-occurrence-supported-conductor-trace','73-endpoint-complete-descent-duality','74-conductor-symbol-lifting-symmetry','75-endpoint-multiplier-coherence','76-endpoint-complete-reverse-cone','77-conductor-ideal-source-relations','78-joint-conductor-dual-endpoints','79-native-conductor-dual-endpoint-attachment','80-normalization-ideal-descent','81-reverse-endpoint-gysin','82-intrinsic-conductor-resolution','83-normalization-sheet-extension-obstruction','84-joint-conductor-spatial-cap','85-native-short-face-comparison','86-coherent-normalization-sheet-extensions','87-native-spatial-three-extension','88-mixed-short-edge-generic-attachment','89-milnor-totalization-conductor-costalk','90-global-endpoint-transformations','91-full-conductor-square-d03-support','92-completed-normal-dual-comparison','93-conductor-yoneda-global-frames','94-conductor-costalk-regulator-continuation','95-toric-punctured-conductor-comparisons','96-completed-toric-descent-and-w03-excess','97-native-excess-punctured-reciprocal','98-native-overlap-relative-interval','99-w03-cech-support-trace-descent','100-occurrence-bridge-short-rees-defects','101-derived-normalization-duality-dilation','102-all-degree-endpoint-scalar-pairing'],default='15-integer-hom-indexing')
args=parser.parse_args()
root=Path.cwd()
core=root/'research/grothendieck/rzk/.check-tmp-1788576911/marici-rzk-check-52a441cc4aaa03f3fe94ee94f70bb2874e26a6a2/source/sHoTT-52a441cc4aaa03f3fe94ee94f70bb2874e26a6a2/src/hott'
if not core.is_dir(): raise SystemExit('Pinned sHoTT core missing; do not silently change dependencies')
files=[core/'00-common.rzk.md',core/'01-paths.rzk.md']+sorted((root/'research/grothendieck/rzk/src').glob('*.rzk.md'))+sorted(p for p in (root/'research/nima/rzk').glob('*.rzk.md') if p.name[:2].isdigit() and int(p.name[:2])>=11)
code={p:'\n'.join(re.findall(r'```rzk\s*\n(.*?)```',p.read_text(encoding='utf-8-sig'),re.S)) for p in files}
owners={}
for p,text in code.items():
    names=re.findall(r'^\s*#(?:define|def|data)\s+([A-Za-z][\w-]*)',text,re.M)
    for block in re.findall(r'#data\b[^#]*',text):
        names+=re.findall(r'(?:\:=|\|)\s*([A-Za-z][\w-]*)',block)
    for name in names:
        if name in owners and owners[name]!=p: raise RuntimeError(f'Duplicate declaration {name}: {p}, {owners[name]}')
        owners[name]=p
start=root/f'research/nima/rzk/{args.module}.rzk.md'
visited=set();active=set();ordered=[]
def visit(p):
    if p in visited:return
    if p in active:raise RuntimeError(f'File-level dependency cycle at {p}')
    active.add(p)
    deps={owners[t] for t in re.findall(r'[A-Za-z][\w-]*',code[p]) if t in owners and owners[t]!=p}
    for d in sorted(deps):visit(d)
    active.remove(p);visited.add(p);ordered.append(p)
visit(start)
manifest={'target':start.relative_to(root).as_posix(),
          'files':[{'path':p.relative_to(root).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                    'declared_assumptions':re.findall(r'^\s*#assume\s+([^\n]+)',code[p],re.M),
                    'parameter_declarations':re.findall(r'^\s*#variables?\s+([^\n]+)',code[p],re.M)} for p in ordered],
          'scope':'Fresh transitive code-symbol file closure; read-only other-owner inputs; no source provenance authentication; literal assumption and parameter scans, not an axiom classification'}
out=root/f'research/nima/results/{args.module}.closure.json'
out.write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'files':len(ordered),'manifest':out.relative_to(root).as_posix(),'assumptions':[(f['path'],f['declared_assumptions']) for f in manifest['files'] if f['declared_assumptions']]}))
