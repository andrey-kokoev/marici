import {readFileSync,writeFileSync} from 'node:fs';
import vm from 'node:vm';
import {buildLayeredCalcium} from '../examples/isotope-wiring/core/layered-neutron-transport.mjs';
import {buildStackedCellInterface} from '../examples/isotope-wiring/core/stacked-cell-interface.mjs';
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),model=buildLayeredCalcium(d,c.IsotopeWiring.renderSVG(d,{interactive:true}));
const results=['direct','neutron-mediated'].map(mode=>buildStackedCellInterface(model,{mode}));
if(process.argv[2])writeFileSync(process.argv[2],JSON.stringify(results,null,2)+'\n');
console.log(JSON.stringify(results.map(r=>({mode:r.mode,status:r.status,counts:r.counts,interface:r.interface,transfer:r.transfer.forwardVertices,bypassInOriginalModel:r.bypassInOriginalModel,frameReturn:r.frameReturn,limits:r.limits})),null,2));
