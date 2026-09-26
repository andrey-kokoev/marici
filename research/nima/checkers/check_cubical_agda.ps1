param(
  [Parameter(Mandatory=$true)][ValidatePattern('^[A-Za-z][A-Za-z0-9]*$')][string]$Module,
  [switch]$Fresh
)
$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Agda = Join-Path $Tools 'agda-2.8.0/agda.exe'
$Library = Join-Path $Tools 'cubical-0.9'
$Source = Join-Path $Root "research/nima/agda/$Module.agda"
$Results = Join-Path $Root 'research/nima/results'
$Log = Join-Path $Results "agda-$Module.log"
$Receipt = Join-Path $Results "agda-$Module.json"
if (!(Test-Path $Source)) { throw "Source not found: $Source" }
$Argv = @('--transliterate', '-i', (Join-Path $Root 'research/nima/agda'), '-i', $Library)
if ($Fresh) { $Argv += '--ignore-interfaces' }
$Argv += $Source
$Started = [DateTime]::UtcNow.ToString('o')
$Version = (& $Agda --version | Out-String).Trim()
Push-Location $Root
try {
  & $Agda @Argv 2>&1 | Tee-Object -FilePath $Log
  $Code = $LASTEXITCODE
} finally { Pop-Location }
$SourceFiles = Get-ChildItem (Join-Path $Root 'research/nima/agda') -Filter '*.agda'
$Hashes = @{}
foreach ($File in $SourceFiles) {
  $Hashes[$File.Name] = (Get-FileHash -Algorithm SHA256 $File.FullName).Hash.ToLowerInvariant()
}
[ordered]@{
  schema = 'marici.nima.agda-check.v1'
  module = $Module
  started_at = $Started
  finished_at = [DateTime]::UtcNow.ToString('o')
  command = $Agda
  args = $Argv
  compiler_version = $Version
  compiler_sha256 = (Get-FileHash -Algorithm SHA256 $Agda).Hash.ToLowerInvariant()
  library = $Library
  exit_code = $Code
  passed = ($Code -eq 0)
  ignore_interfaces = [bool]$Fresh
  source_sha256 = (Get-FileHash -Algorithm SHA256 $Source).Hash.ToLowerInvariant()
  owner_source_inventory_sha256 = $Hashes
  inventory_note = 'Hash inventory of owner Agda sources; not a dependency graph.'
  log = $Log
} | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $Receipt
exit $Code
