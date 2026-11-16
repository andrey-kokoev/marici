import {readFileSync,writeFileSync} from 'node:fs';
import vm from 'node:vm';
import {fileURLToPath} from 'node:url';
import {resolve} from 'node:path';
import {bindCalciumLocalPaths} from '../examples/isotope-wiring/core/diagram-path-trial.mjs';
import {buildLayeredCalcium} from '../examples/isotope-wiring/core/layered-neutron-transport.mjs';
import {buildStackedFullInterface} from '../examples/isotope-wiring/core/stacked-full-interface.mjs';
import {solveTetrahedralDepths} from '../examples/isotope-wiring/core/tetrahedral-depth-constraints.mjs';
import {auditTetrahedralPacking} from '../examples/isotope-wiring/core/tetrahedral-packing-audit.mjs';
import {renderStackedVisual} from '../examples/isotope-wiring/core/render-stacked-visual.mjs';
export function prepareCa46StackedVisual({check=false}={}) {
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),svg=c.IsotopeWiring.renderSVG(d,{interactive:true});bindCalciumLocalPaths(d,svg);
const full=buildStackedFullInterface(buildLayeredCalcium(d,svg)),depths=solveTetrahedralDepths(full,{allowContactTranslation:true}),packing=auditTetrahedralPacking(depths);
if(packing.status!=='verified-for-cell-geometry')throw Error('Refusing to publish a visual claiming overlap-free geometry');
const html=renderStackedVisual({depths,packing,referenceSVG:c.IsotopeWiring.renderSVG(d,{standalone:true,interactive:false})}),path=new URL('../examples/isotope-wiring/ca46-stacked-trial.html',import.meta.url);
if(check){if(readFileSync(path,'utf8')!==html)throw Error('Generated Ca46 visual is stale');}
else{writeFileSync(path,html);}
return {path:fileURLToPath(path),html};
}
if(process.argv[1]&&resolve(process.argv[1])===fileURLToPath(import.meta.url)){
  const check=process.argv.includes('--check');
  prepareCa46StackedVisual({check});
  console.log(check?'Ca46 stacked visual is current':'Updated examples/isotope-wiring/ca46-stacked-trial.html');
}
