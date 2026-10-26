# 🤖 MCP Cloud SRE Agent (Model Context Protocol Server)

<div align="center">

[![Protocol: MCP](https://img.shields.io/badge/Protocol-Model_Context_Protocol-00F5FF?style=for-the-badge&logo=openai&logoColor=black)](https://modelcontextprotocol.io/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)](Dockerfile)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

**An autonomous AI Site Reliability Engineer (SRE) and DevSecOps diagnostic agent built on the Model Context Protocol (MCP). Connects frontier LLMs directly to live Kubernetes cluster events, Terraform drift detection, and FinOps spending telemetry.**

[Architecture Guide](docs/architecture.md) · [Client Config](mcp_config.json) · [Dockerfile](Dockerfile)

</div>

---

## ⚡ Key Capabilities

* **Kubernetes Crash Triage:** Automatically correlates `CrashLoopBackOff` events with cgroup memory limits, container exit codes (`OOMKilled exit code 137`), and generates KEDA autoscaling patches.
* **Terraform Infrastructure Drift Detection:** Pinpoints manual out-of-band console changes (e.g. unapproved port 3389/22 ingress openings) and generates automated reconciliation pull requests.
* **FinOps Cost Anomaly Detection:** Real-time heuristic monitoring detecting 20%+ abnormal daily cost surges in compute or Log Analytics ingestion tables.

---

## 🛠️ MCP Client Configuration

Add this server to your Claude Desktop or Antigravity IDE configuration:

```json
{
  "mcpServers": {
    "cloud-sre-agent": {
      "command": "python",
      "args": ["/path/to/mcp-cloud-sre-agent/server.py"]
    }
  }
}
```

---

## 🚀 Quickstart & Local Testing

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run unit test suite
pytest tests/

# 3. Start MCP Server locally
python server.py
```

---

## 🤝 Maintained by
**Rushikesh Bonde** · Licensed under MIT.