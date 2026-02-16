# Research Roadmap

## Phase 1: Documentation Hardening (Current)

- Establish architecture-level narrative with primary-source citations.
- Define evaluation posture without fabricated benchmarks.
- Publish mathematical foundations and constraints.

## Phase 2: Evaluation Harness

- Implement reproducible benchmark protocols.
- Add objective metrics for reasoning integrity and planning horizons.
- Build failure taxonomy across retrieval, planning, and synthesis.
- Anchor benchmark design to referenced work in `docs/ACADEMIC_LINEAGE.md`.

## Phase 3: Deep Reasoning Integration

- Integrate advanced reasoning model candidate for Planner-heavy tasks.
- Compare Planner+Executor performance under long-horizon missions.
- Validate self-correction loops and CoT verification gates.

## Phase 4: Real-World Testbeds

- Evaluate reasoning latency and quality in:
  - Eidetic Clipboard
  - Kairon Whisper
- Track user-facing quality under real interaction constraints.

## Phase 5: Publication-Grade Benchmarking

- Release benchmark report with reproducible setup.
- Provide ablation studies:
  - with/without graph expansion,
  - with/without metacognitive hydration,
  - with/without recursive routing.
