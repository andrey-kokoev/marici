import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {build} from 'vite';
export async function prepareRealizationLattice(root) {
  const output=path.join(root,'website/public/experiments/realization-lattice');
  await build({configFile:false,root:path.join(root,'examples/realization-lattice'),base:'./',logLevel:'warn',
    build:{outDir:output,emptyOutDir:true,target:'es2022'}});
  await fs.copyFile(path.join(root,'node_modules/three/LICENSE'),path.join(output,'THREE-LICENSE.txt'));
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))
  await prepareRealizationLattice(path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..'));
