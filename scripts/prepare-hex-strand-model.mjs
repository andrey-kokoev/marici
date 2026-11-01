import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
export async function prepareHexStrandModel(root){
 const html=await fs.readFile(path.join(root,'public/experiments/hex-edge-grid.html'),'utf8');
 const helpers=await fs.readFile(path.join(root,'public/experiments/hex-edge-strands.js'),'utf8');
 const start=html.indexOf('function buildHexGrid'),end=html.indexOf('const svg=document');
 if(start<0||end<=start)throw Error('Hex experiment model boundaries changed');
 const generated='// Generated from public/experiments/hex-edge-grid.html and hex-edge-strands.js.\n// Regenerate with scripts/prepare-hex-strand-model.mjs; do not edit.\n'+helpers+'\n'+html.slice(start,end)+'\nexport {growSimplex,simplexScene,applyProcess1,auditStrands,calculateSeedStrands};\n';
 await fs.writeFile(path.join(root,'research/realization-tower/hex-edge-grid-model.generated.mjs'),generated);
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))await prepareHexStrandModel(path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..'));
