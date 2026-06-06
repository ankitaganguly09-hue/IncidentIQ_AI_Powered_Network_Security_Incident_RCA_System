# 🧠 IncidentIQ — AI-Powered Network Security Incident Root Cause Analysis System

## Overview

IncidentIQ is an AI-powered incident analysis system designed for network security and production engineering environments. It helps engineers perform root cause analysis (RCA), log investigation, code correlation, and fix recommendation using Retrieval-Augmented Generation (RAG) and multi-agent reasoning powered by ChatMistralAI.

The system simulates real-world SRE and sustenance engineering workflows where production incidents must be diagnosed by analyzing logs, code changes, and historical incident patterns under strict time constraints.

---

## Problem Statement

In production systems, debugging incidents is difficult because:

- Logs are large, noisy, and unstructured  
- Root cause analysis is manual and slow  
- Engineers must correlate logs, code, and tickets manually  
- Knowledge is distributed across multiple systems  
- Time-to-resolution (MTTR) is critical  

---

## Solution

IncidentIQ solves this by acting as an intelligent debugging assistant that:

- Understands incident descriptions and logs  
- Retrieves relevant context using vector-based search (RAG)  
- Correlates logs with source code changes  
- Performs reasoning to identify root causes  
- Suggests fixes and mitigation strategies  
- Generates structured RCA reports  

---

## System Architecture

The system follows a Retrieval-Augmented Multi-Agent architecture:

- Incident input (logs, tickets, code) is ingested and processed  
- Text is chunked and converted into embeddings  
- Embeddings are stored in a vector database (ChromaDB)  
- Relevant context is retrieved at query time  
- Multiple AI agents process the context:

  - Log Analysis Agent → detects anomalies and patterns  
  - RCA Reasoning Agent → identifies root cause  
  - Code Correlation Agent → maps logs to code functions  
  - Fix Suggestion Agent → recommends fixes and mitigations  
  - Report Generation Agent → produces final RCA report  

---

## Core Functionalities

### Log Analysis
The system processes raw logs to detect anomalies, error spikes, and failure patterns while reconstructing the incident timeline.

### Root Cause Analysis
The system performs reasoning over retrieved logs and context to identify the most probable root cause along with supporting evidence and confidence estimation.

### Code Correlation
Logs and stack traces are mapped to relevant source code files, functions, or modules to identify where the issue originated in the codebase.

### Fix Recommendation
The system suggests actionable engineering solutions such as rollbacks, patches, configuration changes, or temporary mitigations.

### RCA Report Generation
A structured incident report is generated containing root cause, evidence, timeline, fix, and preventive measures.

---

## Tech Stack

- LangChain for LLM orchestration  
- ChatMistralAI (Mistral LLM API) for reasoning  
- ChromaDB for vector storage and retrieval  
- Python 3.14 as runtime  
- dotenv for environment configuration  

---

## Example Workflow

Input incident:

- Users experiencing 401 authentication errors after deployment v2.3  
- Logs show spike in authentication failures after a specific timestamp  
- Code changes include updates to authentication middleware  

System behavior:

- Retrieves relevant logs and historical incidents  
- Correlates errors with authentication module changes  
- Identifies likely root cause as token validation regression  
- Suggests rollback or patch fix  
- Generates structured RCA report with evidence and prevention steps  

---

## Value Proposition

This system demonstrates enterprise-level AI engineering capabilities and closely mirrors real-world systems used in:

- Network Security sustenance engineering teams  
- AWS SRE workflows  
- Large-scale distributed system observability pipelines  

It reduces Mean Time To Resolution (MTTR) by automating log analysis, context retrieval, and reasoning.

---

## Skills Demonstrated

- Retrieval-Augmented Generation (RAG) systems  
- Multi-agent AI architecture  
- LLM application design  
- Log analysis and observability concepts  
- Code understanding and correlation systems  
- Production AI engineering design  

---

## Future Enhancements

- Real-time log streaming (Kafka integration)  
- AST-based deep code analysis  
- Incident timeline visualization  
- Slack / PagerDuty integration  
- Evaluation framework for RCA accuracy  
- Docker and Kubernetes deployment  

---

## Disclaimer

This system is a decision-support tool for engineers. It is not intended to replace human judgment in production environments.

---

## Author

Ankita Ganguly