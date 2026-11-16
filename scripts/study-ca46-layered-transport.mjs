import {readFileSync,writeFileSync} from 'node:fs';
import vm from 'node:vm';
import {buildLayeredCalcium} from '../examples/isotope-wiring/core/layered-neutron-transport.mjs';
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),result=buildLayeredCalcium(d,c.IsotopeWiring.renderSVG(d,{interactive:true}));
if(process.argv[2])writeFileSync(process.argv[2],JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({definitionId:result.definitionId,status:result.status,counts:result.counts,inventory:result.inventory,transfer:result.transfer,policy:result.policy,residuals:result.residuals},null,2));
