# Academic Lineage

This document positions the system against external research it is inspired by, and maps those ideas to literal architecture choices.

## 1. Google-Aligned Agentic Research

1. **DS-STAR: Data Science Agent via Iterative Planning and Verification** (Nam et al., 2025)
   - [arXiv:2509.21825](https://arxiv.org/abs/2509.21825)
2. **MLE-STAR: Machine Learning Engineering Agent via Iterative Refinement** (Nam et al., 2025)
   - [arXiv:2506.15692](https://arxiv.org/abs/2506.15692)
3. **Towards an AI co-scientist** (Google Research, 2025)
   - [arXiv:2502.18864](https://arxiv.org/abs/2502.18864)
4. **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (Wei et al., 2022)
   - [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
5. **Self-Consistency Improves Chain of Thought Reasoning in Language Models** (Wang et al., 2022)
   - [arXiv:2203.11171](https://arxiv.org/abs/2203.11171)

## 2. Advanced RAG and Graph Retrieval

1. **From Local to Global: A GraphRAG Approach to Query-Focused Summarization** (Edge et al., 2024)
   - [arXiv:2404.16130](https://arxiv.org/abs/2404.16130)
2. **HippoRAG: Neurobiologically Inspired Long-Term Memory for LLMs** (Gutierrez et al., 2024)
   - [arXiv:2405.14831](https://arxiv.org/abs/2405.14831)
3. **ReAct: Synergizing Reasoning and Acting in Language Models** (Yao et al., 2022)
   - [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)

## 3. Metacognition, Reflection, and Memory for Agents

1. **Reflexion: Language Agents with Verbal Reinforcement Learning** (Shinn et al., 2023)
   - [arXiv:2303.11366](https://arxiv.org/abs/2303.11366)
2. **Tree of Thoughts: Deliberate Problem Solving with Large Language Models** (Yao et al., 2023)
   - [arXiv:2305.10601](https://arxiv.org/abs/2305.10601)
3. **Graph of Thoughts: Solving Elaborate Problems with Large Language Models** (Besta et al., 2023)
   - [arXiv:2308.09687](https://arxiv.org/abs/2308.09687)
4. **MemGPT: Towards LLMs as Operating Systems** (Packer et al., 2023)
   - [arXiv:2310.08560](https://arxiv.org/abs/2310.08560)

## 4. Knowledge Graph Execution Substrate (Cypher, Neo4j, GDS)

1. Neo4j Cypher Manual
   - [Cypher Manual](https://neo4j.com/docs/cypher-manual/current/)
2. Cypher `MERGE` for idempotent graph writes
   - [MERGE clause](https://neo4j.com/docs/cypher-manual/current/clauses/merge/)
3. Neo4j GDS Leiden community detection
   - [Leiden Algorithm (Neo4j GDS)](https://neo4j.com/docs/graph-data-science/current/algorithms/leiden/)

## 5. Literal Mapping: Research Idea -> System Implementation

| Research idea | Literal reflection in your system | Evidence path(s) |
| --- | --- | --- |
| Iterative planning + verification loop (DS-STAR) | Explicit Analyze -> Plan -> Code -> Verify -> Route -> Finalize lifecycle | `src/agents/ds_star/orchestrator.py`, `Docs/1-Agents/DS_STAR_TECHNICAL_REFERENCE.md` |
| LLM-judge style sufficiency checks | Verifier agent checks semantic sufficiency, not only code execution success | `Docs/1-Agents/DS_STAR_TECHNICAL_REFERENCE.md` |
| Long-horizon multi-step execution | Iterative loop with routing, debugger fallbacks, and step refinement | `src/agents/ds_star/orchestrator.py` |
| Deep research mission decomposition | Explore -> Plan -> Batch -> Audit -> Synthesize with MapReduce deduplication | `Docs/1-Agents/RESEARCH_PLANNER.md` |
| GraphRAG global-context retrieval | Seed vector search + graph expansion via Personalized PageRank | `Docs/ALGORITHMS.md`, `src/retrieval/hierarchical_retriever.py` |
| Multimodal evidence grounding | OCR gate + semantic visual ranking + deep vision analysis | `Docs/2-Intelligence/VISUAL_INTERPRETER.md`, `src/retrieval/visual_interpreter.py` |
| Agent memory and metacognition | Persistent traces (`Thought`, `Critique`, `Hypothesis`, `AntiPattern`) with hydration | `Docs/0-Architecture/CORE_V5_V6_METACOGNITION.md`, `src/orchestration/metacognition.py`, `src/orchestration/context_hydration.py` |
| Procedural memory for actions/decisions | Thought graph schema linking intent, plan, function calls, outcomes | `Docs/0-Architecture/CORE_V5_V6_METACOGNITION.md` |
| Graph-native ontology implementation | Typed nodes and relations map naturally onto Neo4j + Cypher queries | `Docs/0-Architecture/KNOWLEDGE_SPACES.md`, `src/persistence/graph_loader.py` |
| Idempotent graph writes and session lineage | Cypher-style merge semantics + `session_id` mission lineage | `Docs/0-Architecture/KNOWLEDGE_SPACES.md`, `Docs/3-Reference/API_REFERENCE.md` |

## 6. Notes on Naming

- The original inspiration mentioned as "ML-STAR" aligns more directly with **MLE-STAR** in current public literature.
- The implementation in this repository uses **DS-STAR** naming and extends it with multimodal and metacognitive layers.
