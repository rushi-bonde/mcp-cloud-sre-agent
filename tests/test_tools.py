from server import MCPAgentTools

def test_diagnose_pod_failures():
    result = MCPAgentTools.diagnose_pod_failures("production", "api-gateway-7b89f-x12")
    assert result.status == "CrashLoopBackOff"
    assert "OOMKilled" in result.root_cause

def test_analyze_terraform_drift():
    result = MCPAgentTools.analyze_terraform_drift("azurerm_network_security_group", "nsg-app-prod")
    assert result.drift_detected is True
    assert result.risk_level == "CRITICAL"

def test_detect_finops_anomalies():
    anomalies = MCPAgentTools.detect_finops_anomalies(20.0)
    assert len(anomalies) >= 2