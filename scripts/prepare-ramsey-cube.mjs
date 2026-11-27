import path from 'node:path'
import fs from 'node:fs/promises'
import {fileURLToPath} from 'node:url'
import {build} from 'vite'
import vue from '@vitejs/plugin-vue'
export async function prepareRamseyCube(root){
  const base=path.join(root,'website/public/experiments');await build({configFile:false,root:path.join(root,'examples/ramsey-cube'),base:'./',plugins:[vue()],build:{outDir:path.join(base,'ramsey-cube'),emptyOutDir:true,target:'es2022'}})
  const old=path.join(base,'ramsey38-cube');await fs.mkdir(old,{recursive:true});await fs.writeFile(path.join(old,'index.html'),'<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=../ramsey-cube/index.html?case=3-8"><title>Viewer moved</title><a href="../ramsey-cube/index.html?case=3-8">Ramsey witness cubes</a>')
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))await prepareRamseyCube(fileURLToPath(new URL('../',import.meta.url)))
