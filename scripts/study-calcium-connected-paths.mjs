import {readFileSync,writeFileSync} from 'node:fs';
import vm from 'node:vm';
import {studyConnectedCalcium} from '../examples/isotope-wiring/core/connected-path-trial.mjs';
const id=process.argv[2]||'Ca44';if(!['Ca44','Ca46'].includes(id))throw Error('Choose Ca44 or Ca46');
const context=vm.createContext({}),html=readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8');vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1],context);
const definition=JSON.parse(JSON.stringify(context.IsotopeWiring.fixtures()[id])),svg=context.IsotopeWiring.renderSVG(definition,{interactive:true}),result=studyConnectedCalcium(definition,svg);
if(process.argv[3])writeFileSync(process.argv[3],JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({definitionId:id,counts:result.binding.counts,branches:result.binding.branches.length,crossings:result.binding.crossings.length,gaugeControl:result.gaugeControl.status,twistedControl:result.twistedControl.status,status:result.status},null,2));
if(result.gaugeControl.status!=='verified'||result.twistedControl.status!=='refuted'||result.binding.counts.cycleRank!==result.binding.cycles.length)process.exitCode=1;
