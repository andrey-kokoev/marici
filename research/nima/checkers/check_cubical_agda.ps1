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
function Get-SourceInventory([string]$Directory) {
  $Inventory = [ordered]@{}
  foreach ($File in (Get-ChildItem $Directory -Recurse -File -Filter '*.agda' | Sort-Object FullName)) {
    $Key = [IO.Path]::GetRelativePath($Directory, $File.FullName).Replace('\', '/')
    $Inventory[$Key] = (Get-FileHash -Algorithm SHA256 -LiteralPath $File.FullName).Hash.ToLowerInvariant()
  }
  return ,$Inventory
}
$OwnerDirectory = Join-Path $Root 'research/nima/agda'
$OwnerBefore = Get-SourceInventory $OwnerDirectory
$LibraryBefore = Get-SourceInventory $Library
$CompilerBefore = (Get-FileHash -Algorithm SHA256 $Agda).Hash.ToLowerInvariant()
$Started = [DateTime]::UtcNow.ToString('o')
$Version = (& $Agda --version | Out-String).Trim()
Push-Location $Root
try {
  & $Agda @Argv 2>&1 | Tee-Object -FilePath $Log
  $Code = $LASTEXITCODE
} finally { Pop-Location }
$Hashes = Get-SourceInventory $OwnerDirectory
$LibraryAfter = Get-SourceInventory $Library
$CompilerAfter = (Get-FileHash -Algorithm SHA256 $Agda).Hash.ToLowerInvariant()
$InputsStable = (($OwnerBefore | ConvertTo-Json -Compress) -ceq ($Hashes | ConvertTo-Json -Compress)) -and
  (($LibraryBefore | ConvertTo-Json -Compress) -ceq ($LibraryAfter | ConvertTo-Json -Compress)) -and
  ($CompilerBefore -ceq $CompilerAfter)
if (!$InputsStable) { $Code = 43 }
[ordered]@{
  schema = 'marici.nima.agda-check.v1'
  module = $Module
  started_at = $Started
  finished_at = [DateTime]::UtcNow.ToString('o')
  command = $Agda
  args = $Argv
  compiler_version = $Version
  compiler_sha256 = $CompilerAfter
  inputs_stable_during_check = $InputsStable
  library = $Library
  library_source_inventory_sha256 = $LibraryAfter
  library_inventory_note = 'Full Cubical .agda inventory, stable before/after checking; compiler built-in data remains a separate trust boundary.'
  exit_code = $Code
  passed = ($Code -eq 0)
  ignore_interfaces = [bool]$Fresh
  source_sha256 = (Get-FileHash -Algorithm SHA256 $Source).Hash.ToLowerInvariant()
  owner_source_inventory_sha256 = $Hashes
  inventory_note = 'Hash inventory of owner Agda sources; not a dependency graph.'
  log = $Log
} | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $Receipt
exit $Code
