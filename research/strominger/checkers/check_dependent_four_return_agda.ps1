param(
  [ValidateSet('DependentFourReturn', 'CoherentFourReturn', 'TwistedRouteReturn')][string]$Module = 'DependentFourReturn',
  [switch]$Fresh
)
$ErrorActionPreference = 'Stop'
# Adapted from research/nima/checkers/check_cubical_agda.ps1.
if ($IsWindows -and (($env:PATHEXT -split ';') -notcontains '.EXE')) {
  $env:PATHEXT = if ($env:PATHEXT) { "$env:PATHEXT;.EXE" } else { '.EXE' }
}
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Agda = Join-Path $Tools 'agda-2.8.0/agda.exe'
$Library = Join-Path $Tools 'cubical-0.9'
$Source = Join-Path $Root "research/strominger/agda/$Module.agda"
$ResultName = switch ($Module) {
  'DependentFourReturn' { 'dependent-four-return-v1' }
  'CoherentFourReturn' { 'coherent-four-return-v1' }
  'TwistedRouteReturn' { 'su32-edge5-twisted-return-v1' }
}
$Results = Join-Path $Root "research/strominger/results/$ResultName"
$Log = Join-Path $Results 'agda.log'
$Receipt = Join-Path $Results 'agda.json'
foreach ($Path in @($Source, $Agda, $Library)) {
  if (!(Test-Path -LiteralPath $Path)) { throw "Required path not found: $Path" }
}
New-Item -ItemType Directory -Force -Path $Results | Out-Null
$Argv = @('--safe', '--cubical', '--guardedness', '--transliterate',
  '-i', (Join-Path $Root 'research/strominger/agda'),
  '-i', (Join-Path $Root 'research/nima/agda'), '-i', $Library)
if ($Fresh) { $Argv += '--ignore-interfaces' }
$Argv += $Source
function Get-SourceInventory([string]$Directory) {
  $Inventory = [ordered]@{}
  foreach ($File in (Get-ChildItem $Directory -Recurse -File -Filter '*.agda' | Sort-Object FullName)) {
    $Key = [IO.Path]::GetRelativePath($Directory, $File.FullName).Replace('\', '/')
    $Inventory[$Key] = (Get-FileHash -Algorithm SHA256 -LiteralPath $File.FullName).Hash.ToLowerInvariant()
  }
  return ,$Inventory
}
function Get-Evidence {
  return [ordered]@{
    checker = (Get-FileHash -Algorithm SHA256 -LiteralPath $PSCommandPath).Hash.ToLowerInvariant()
    compiler = (Get-FileHash -Algorithm SHA256 -LiteralPath $Agda).Hash.ToLowerInvariant()
    owner = Get-SourceInventory (Join-Path $Root 'research/strominger/agda')
    imported_owner = Get-SourceInventory (Join-Path $Root 'research/nima/agda')
    library = Get-SourceInventory $Library
  }
}
$Before = Get-Evidence
$Started = [DateTime]::UtcNow.ToString('o')
$Version = (& $Agda --version | Out-String).Trim()
if ($LASTEXITCODE -ne 0) { throw 'Agda version probe failed' }
$Code = 1
Push-Location $Root
try {
  & $Agda @Argv 2>&1 | Tee-Object -FilePath $Log
  $Code = $LASTEXITCODE
} finally { Pop-Location }
$CompilerExitCode = $Code
$After = Get-Evidence
$InputsStable = ($Before | ConvertTo-Json -Depth 8 -Compress) -ceq ($After | ConvertTo-Json -Depth 8 -Compress)
if (!$InputsStable) { $Code = 43 }
[ordered]@{
  schema = 'strominger.dependent-four-return.agda-check.v1'
  module = $Module
  started_at = $Started
  finished_at = [DateTime]::UtcNow.ToString('o')
  command = $Agda
  args = $Argv
  compiler_version = $Version
  compiler_exit_code = $CompilerExitCode
  inputs_stable_during_check = $InputsStable
  exit_code = $Code
  passed = ($Code -eq 0)
  ignore_interfaces = [bool]$Fresh
  source_sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $Source).Hash.ToLowerInvariant()
  source_inventory = $After
  inventory_note = 'Full included-directory .agda inventories, not a dependency graph; built-in compiler data is a separate trust boundary.'
  log = $Log
} | ConvertTo-Json -Depth 8 | Set-Content -Encoding utf8 $Receipt
exit $Code
