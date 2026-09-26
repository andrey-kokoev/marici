# Run through an operator-authorized shell. Never interpret an empty wrapper
# exit as a compiler certificate; require a fresh positive check and specific
# type errors in the two negative controls.
$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Agda = Join-Path $Tools 'agda-2.8.0/agda.exe'
$Library = Join-Path $Tools 'cubical-0.9'
$Sources = Join-Path $Root 'research/nima/agda'
$Results = Join-Path $Root 'research/nima/results'
$Started = [DateTime]::UtcNow.ToString('o')
Push-Location $Root
try {
  & python research/nima/amplitudes/scalar_six_bridge.py
  if ($LASTEXITCODE -ne 0) { throw 'Live fixture consistency failed' }
  & (Join-Path $PSScriptRoot 'check_cubical_agda.ps1') -Module ScalarSixCertificate -Fresh
  if ($LASTEXITCODE -ne 0) { throw 'Fresh positive certificate failed' }
  $Positive = Get-Content (Join-Path $Results 'agda-ScalarSixCertificate.json') -Raw | ConvertFrom-Json
  if (!$Positive.passed -or !$Positive.ignore_interfaces) { throw 'Missing fresh successful receipt' }
  $Controls = @()
  foreach ($Name in @('ScalarSixBadResult','ScalarSixBadPropagator')) {
    $File = Join-Path $Sources "negative/$Name.agda"
    $Log = Join-Path $Results "agda-$Name.log"
    $Output = & $Agda --transliterate -i $Sources -i $Library $File 2>&1
    $Code = $LASTEXITCODE
    $Text = $Output | Out-String
    $Text | Set-Content -Encoding utf8 $Log
    Write-Output $Text
    # Reject missing-file, scope/import, and runner errors as false controls.
    $Expected = if ($Name -eq 'ScalarSixBadResult') { '3600 != 4200' } else { '8 != 9' }
    $Rejected = ($Code -ne 0 -and $Text.Contains($Expected) -and $Text.Contains('refl'))
    $Controls += [ordered]@{
      module = "negative.$Name"
      exit_code = $Code
      expected_diagnostic = $Expected
      correctly_rejected = $Rejected
      source_sha256 = (Get-FileHash -Algorithm SHA256 $File).Hash.ToLowerInvariant()
      log = $Log
    }
    if (!$Rejected) { throw "Negative control did not fail as expected: $Name" }
  }
  [ordered]@{
    status = 'fixed-sample-calculation-checked-with-negative-controls'
    started_at = $Started
    finished_at = [DateTime]::UtcNow.ToString('o')
    command = 'pwsh -NoProfile -File research/nima/checkers/check_scalar_six_bridge.ps1'
    execution_authority = 'Operator explicitly requested shell execution of the ps1 runner, not MCP'
    positive_receipt = 'research/nima/results/agda-ScalarSixCertificate.json'
    compiler = $Agda
    compiler_sha256 = (Get-FileHash -Algorithm SHA256 $Agda).Hash.ToLowerInvariant()
    controls = $Controls
    scope = 'One live six-scalar fixture; arithmetic certificate, not Python refinement or physical-rule derivation'
  } | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 (Join-Path $Results 'scalar-six-formal-audit.json')
} finally { Pop-Location }
