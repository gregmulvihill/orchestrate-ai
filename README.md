# Orchestrate-AI

An orchestrated AI system for accelerating project development through self-improving infrastructure.

## Overview

Orchestrate-AI is designed as a self-improving infrastructure that rapidly iterates on both technology and business strategy. By establishing an early revenue stream, it aims to create a sustainable engine for growth, ensuring long-term success in the evolving AI landscape.

Orchestrate-AI is part of a larger ecosystem:
- It provides strategic direction and task prioritization to [Automated-Dev-Agents (ADCA)](https://github.com/gregmulvihill/automated-dev-agents)
- It leverages [Multi-Tiered Memory Architecture (MTMA)](https://github.com/gregmulvihill/multi-tiered-memory-architecture) for persistent memory and knowledge management

## Ecosystem Architecture

Orchestrate-AI functions as the strategic/business layer in a three-tier architecture:

```
┌─────────────────────────────────────────────────┐
│ ORCHESTRATE-AI (This Repository)                │
│ (Strategic Orchestration & Business Logic)      │
└────────────────────────┬────────────────────────┘
                         │
┌────────────────────────▼────────────────────────┐
│ AUTOMATED-DEV-AGENTS                            │
│ (Tactical Task Execution & Agent Management)    │
└────────────────────────┬────────────────────────┘
                         │
┌────────────────────────▼────────────────────────┐
│ MULTI-TIERED MEMORY ARCHITECTURE                │
│ (Persistence, Context Preservation, Knowledge)  │
└─────────────────────────────────────────────────┘
```

## Core Framework

### Value Optimization
- Self-improving systems with automated testing
- Intent preservation in LLM operations
- n8n.io pipeline efficiency

### Implementation Approach
- Prioritize tasks by value/risk/time metrics
- Deploy incremental improvements
- Maintain comprehensive monitoring

### Risk Management
- Regular validation and logging
- Incremental feature deployment
- System architecture reviews

## Integration Points

### Integration with Automated-Dev-Agents
- Provides high-level tasks and priorities to ADCA
- Receives task execution status and results from ADCA
- Sets strategic direction for development activities

### Integration with MTMA
- Uses MTMA for persistent memory across workflows
- Stores strategic decisions and business metrics
- Retrieves historical data for trend analysis and optimization

## Architecture

The system architecture follows these design patterns:
- Observer (system analysis)
- Strategy (task prioritization)
- Chain of Responsibility (intent checks)
- Factory (agent creation)

For a detailed view of the system architecture, see [ARCHITECTURE.md](./docs/ARCHITECTURE.md).

## Getting Started

### Prerequisites
- Node.js v18 or higher
- Redis database
- n8n.io installed and configured

### Installation

```bash
npm install
npm run setup
```

### Configuration

Copy the example configuration file and update it with your settings:

```bash
cp .env.example .env
# Edit .env with your configuration values
```

### Running the System

```bash
npm run start
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](./docs/CONTRIBUTING.md) for guidelines.

## Related Projects

- [Automated-Dev-Agents (ADCA)](https://github.com/gregmulvihill/automated-dev-agents) - The tactical execution layer that implements specialized agents for development tasks
- [Multi-Tiered Memory Architecture (MTMA)](https://github.com/gregmulvihill/multi-tiered-memory-architecture) - The memory system that enables persistence and knowledge sharing

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.