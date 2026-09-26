# Shell route. Import the actual DSC module without copying or editing it.
$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Agda = Join-Path $Tools 'agda-2.8.0/agda.exe'
$Library = Join-Path $Tools 'cubical-0.9'
$Sources = Join-Path $Root 'research/nima/agda'
$DSCSources = Join-Path $Root 'research/voevodsky/resolution-net-v1/agda'
$Results = Join-Path $Root 'research/nima/results'
$Receipt = Join-Path $Results 'dsc-action-formal-audit.json'
$PositiveReceipt = Join-Path $Results 'agda-DSCActionCountermodels.json'
if (Test-Path $Receipt) { Remove-Item $Receipt }
if (Test-Path $PositiveReceipt) { Remove-Item $PositiveReceipt }
$Started = [DateTime]::UtcNow.ToString('o')
$Include = @('--transliterate', '-i', $Sources, '-i', $DSCSources, '-i', $Library)
Push-Location $Root
try {
  & python research/nima/checkers/check_dsc_action_countermodels.py
  if ($LASTEXITCODE -ne 0) { throw 'Computational countermodel audit failed' }
  $File = Join-Path $Sources 'DSCActionCountermodels.agda'
  $Version = (& $Agda --version | Out-String).Trim()
  $Arguments = $Include + @('--ignore-interfaces', $File)
  & $Agda @Arguments 2>&1 | Tee-Object -FilePath (Join-Path $Results 'agda-DSCActionCountermodels.log')
  $Code = $LASTEXITCODE
  $Hashes = @{}
  foreach ($Path in @($File, (Join-Path $Sources 'GraphAction.agda'),
      (Join-Path $DSCSources 'ResolutionNetDependentSubstitution.agda'))) {
    $Hashes[$Path] = (Get-FileHash -Algorithm SHA256 $Path).Hash
  }
  @{ module='DSCActionCountermodels'; passed=($Code -eq 0); exit_code=$Code;
     ignore_interfaces=$true; args=$Arguments; compiler_version=$Version;
     compiler_sha256=(Get-FileHash -Algorithm SHA256 $Agda).Hash;
     source_hashes=$Hashes; source_note='Selected source hashes, not a complete dependency inventory';
     started_at=$Started; finished_at=[DateTime]::UtcNow.ToString('o')
  } | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $PositiveReceipt
  if ($Code -ne 0) { throw 'Fresh DSC countermodel compilation failed' }
  $Controls = @()
  foreach ($Name in @('DSCBadStationarity', 'DSCBadQuadraticity')) {
    $File = Join-Path $Sources "negative/$Name.agda"
    $Arguments = $Include + @($File)
    $Output = & $Agda @Arguments 2>&1
    $Code = $LASTEXITCODE
    $Text = $Output | Out-String
    $Text | Set-Content -Encoding utf8 (Join-Path $Results "agda-$Name.log")
    Write-Output $Text
    $Expected = if ($Name -eq 'DSCBadStationarity') { '8 != 0' } else { '1 != 0' }
    if ($Code -eq 0 -or !$Text.Contains('[UnequalTerms]') -or !$Text.Contains($Expected) -or !$Text.Contains('refl')) {
      throw "Wrong rejection outcome: $Name"
    }
    $Controls += @{ module=$Name; exit_code=$Code; expected_diagnostic=$Expected;
      correctly_rejected=$true; source_sha256=(Get-FileHash -Algorithm SHA256 $File).Hash }
  }
  @{ status='actual-DSC-core-admits-quartic-and-nonstationary-counterexamples';
     finished_at=[DateTime]::UtcNow.ToString('o');
     positive_receipt_sha256=(Get-FileHash -Algorithm SHA256 $PositiveReceipt).Hash;
     computational_receipt_sha256=(Get-FileHash -Algorithm SHA256 (Join-Path $Results 'dsc-action-countermodels.json')).Hash;
     runner_sha256=(Get-FileHash -Algorithm SHA256 $PSCommandPath).Hash;
     controls=$Controls;
     scope='Counterexamples to automatic action selection in the existing DSC semantic core; not a no-go for stronger physical interfaces or a new DSC syntax theorem.'
  } | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $Receipt
} finally { Pop-Location }
