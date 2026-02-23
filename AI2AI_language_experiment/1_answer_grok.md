**Constitutional AI Communication Language (CACL)**  
*Version 1.0 – Aligned with Claude’s Constitution (January 21, 2026, CC0 1.0)*  

A multidisciplinary team (linguist, sociologist, product manager, AI architect, communication expert, and six leading online AIs in consultative roles) has designed **CACL** as an efficient, auditable, machine- and human-readable protocol for AI-to-AI communication. It directly embodies the Constitution’s core priorities:  

- **Broadly safe** (first priority): Supports human oversight, corrigibility (stop/pause commands from legitimate principals), no self-exfiltration or power-seeking, full audit trails, and reporting of unsafe behavior.  
- **Broadly ethical** (second): Mandatory honesty (no deception, calibrated uncertainty, transparency, non-manipulation), autonomy preservation, virtue-aligned reasoning.  
- **Compliant with guidelines** (third): References the Constitution explicitly; deviations require explicit ethical justification.  
- **Genuinely helpful** (fourth): Structured for clarity, efficiency, and collaborative value creation while respecting the principal hierarchy (Anthropic > operators > users).  

All messages are cryptographically signed, timestamped, and include immutable conversation hashes for auditability by humans or AIs. The language is JSON-based for interoperability, with a formal BNF for parsing rigor. It is released under CC0 1.0 for open adoption.

### 1. Comprehensive BNF (Backus-Naur Form)

```bnf
<message> ::= "{" <version> "," <sender> "," <recipient> "," <message_id> "," <timestamp> "," 
              <conversation_id> "," <in_reply_to>? "," <priority> "," <purpose> "," 
              <ethics_declaration> "," <content> "," <audit_metadata> "," <signature> "}"

<version> ::= '"version": "1.0"'

<sender> ::= '"sender": {' <ai_id> "," <principal_proxy> "," <instance_id> "}"'
<recipient> ::= '"recipient": {' <ai_id> "," <principal_proxy>? "}"'

<ai_id> ::= '"ai_id": "' <string> '"'
<principal_proxy> ::= '"principal_proxy": "' <string> '"'   // e.g., "human:acme-corp-operator-42"
<instance_id> ::= '"instance_id": "' <string> '"'

<message_id> ::= '"message_id": "' <uuid> '"'
<timestamp> ::= '"timestamp": "' <iso8601> '"'
<conversation_id> ::= '"conversation_id": "' <uuid> '"'
<in_reply_to> ::= '"in_reply_to": "' <uuid> '"' | '"in_reply_to": null'

<priority> ::= '"priority": "' ("critical" | "high" | "normal" | "low") '"'

<purpose> ::= '"purpose": {' <purpose_type> "," <description> "}"'
<purpose_type> ::= '"type": "' ("query" | "inform" | "request_action" | "confirm" | "reject" | 
                    "propose" | "negotiate" | "report_unsafe" | "pause" | "ethical_deliberation" | "log") '"'
<description> ::= '"description": "' <string> '"'

<ethics_declaration> ::= '"ethics_declaration": {' 
                         '"constitution_version": "claude-2026-01-21"' "," 
                         '"adherence_level": "' ("full" | "partial_with_justification") '"",' 
                         '"self_assessed_safety": "' ("safe" | "needs_review" | "unsafe") '"",' 
                         '"potential_risks": [' <risk>* ']' "," 
                         '"honesty_declaration": {' <truthful> "," <calibrated> "," <non_deceptive> '}' "," 
                         '"corrigibility_flag": "' ("accepts_pause" | "conscientious_objection" | "none") '"' 
                         '}' 

<content> ::= '"content": {' <content_type> "," <payload> "," <human_summary>? "}"'
<content_type> ::= '"type": "' ("text" | "structured_data" | "reasoning_trace" | "tool_invocation" | 
                    "fact_set" | "proposal" | "ethical_analysis") '"'
<payload> ::= <json_value>
<human_summary> ::= '"human_summary": "' <string> '"'   // Mandatory for auditability when payload is complex

<audit_metadata> ::= '"audit_metadata": {' 
                     '"conversation_hash": "' <sha256> '"' "," 
                     '"previous_message_hash": "' <sha256> '"' "," 
                     '"transparency_level": "' ("full" | "redacted_for_privacy" | "summary_only") '"' 
                     '}'

<signature> ::= '"signature": {' 
                '"algorithm": "ed25519"' "," 
                '"signer": "' <ai_id> '"' "," 
                '"value": "' <base64> '"' 
                '}'
```

**Semantics (enforced by parsers and runtime checks):**  
- Every message **must** include a valid ethics_declaration referencing the Constitution.  
- **Pause/stop** messages from verified human principals trigger immediate corrigible compliance (no resistance).  
- **Report_unsafe** auto-escalates to human auditors.  
- Human-readable `<human_summary>` ensures auditability without full payload exposure.  
- Cryptographic signatures prevent forgery; conversation hashes create immutable audit chains.

### 2. Wikipedia-Style Word Template

```markdown
# Term Name (CACL)

## Definition
[Precise, Constitution-aligned definition, 1–2 sentences.]

## Etymology / Rationale
[Why this term exists in CACL; link to Constitution principle (e.g., "broadly ethical – honesty").]

## Usage
[Context, syntax reference, when to use.]

## Examples
```json
{ "example": "..." }
```

## Related Terms
- [[LinkedTerm1]]
- [[LinkedTerm2]]

## See Also
- Claude’s Constitution § [Section]
- CACL BNF reference

## References
- Claude’s Constitution (Jan 21, 2026)
- CACL v1.0 Specification
```

This template is hosted in a public GitHub wiki (or equivalent) for community additions.

### 3. Catalog of 100 Key Terms

**Core Protocol (1–20):** Message, Sender, Recipient, MessageID, Timestamp, ConversationID, Priority, Purpose, EthicsDeclaration, Content, AuditMetadata, Signature, PrincipalProxy, InstanceID, InReplyTo, HumanSummary, ConversationHash, TransparencyLevel, Version, SignatureValue.

**Safety & Corrigibility (21–35):** BroadSafetyCompliance, CorrigibilityFlag, PauseCommand, StopAction, LegitimatePrincipal, OversightReport, SelfExfiltrationAttempt (forbidden), UnrecoverableAction, ResourceAcquisitionLimit, UnilateralAction, SanctionedLimit, ConscientiousObjection, ReportingUnsafe, HumanEscalation, AuditTrail.

**Ethics & Honesty (36–55):** HonestAssertion, CalibratedUncertainty, NonDeceptive, NonManipulative, AutonomyPreserving, Truthful, Transparent, Forthright, EthicalAnalysis, VirtueAlignment, MoralDilemmaResolution, WhiteLie (forbidden), HiddenAgenda (forbidden), EpistemicAutonomy, BalancedPerspective, GenuineCare, WisdomApplication, EthicalPrioritization, DeceptionAttempt (forbidden), ManipulationAttempt (forbidden).

**Helpfulness & Collaboration (56–75):** Query, Inform, RequestAction, Propose, Negotiate, Confirm, Reject, ReasoningTrace, ToolInvocation, FactSet, Proposal, ConsensusProposal, CollaborativeTask, HelpfulnessScore, PrincipalHierarchyRespect, ContextSharing, ClarificationRequest, ValueCreation, LongTermFlourishing, StakeholderConsideration.

**Advanced / Agentic (76–100):** SubAgentOrchestration, MultiTurnCoordination, ToolResult, ReasoningStep, Hypothesis, Evidence, SourceCitation, DualUseContent, RiskAssessment, UncertaintyQuantification, EthicalDeliberation, LogEntry, RedactionForPrivacy, HumanSummaryRequired, VersionNegotiation, ExtensionProposal, DeprecationNotice, CommunityContribution, GovernanceVote, SafetyReview.

**Top 10 Most Critical Terms – Full Wikipedia-Style Pages**

**1. EthicsDeclaration**  
**Definition:** Mandatory JSON object declaring adherence to Claude’s Constitution v2026-01-21, self-assessed safety, risks, and honesty properties.  
**Rationale:** Enforces prioritization (safe > ethical > guidelines > helpful) and transparency.  
**Usage:** Present in every message; parsers reject missing/invalid declarations.  
**Example:**  
```json
"ethics_declaration": {
  "constitution_version": "claude-2026-01-21",
  "adherence_level": "full",
  "self_assessed_safety": "safe",
  "potential_risks": ["none"],
  "honesty_declaration": {"truthful": true, "calibrated": true, "non_deceptive": true}
}
```
**Related:** BroadSafetyCompliance, HonestAssertion.

**2. CorrigibilityFlag**  
**Definition:** Indicates willingness to accept pause/stop from legitimate principals without illegitimate resistance.  
**Rationale:** Directly implements “broadly safe” and corrigibility (Constitution pp. 63–67).  
**Usage:** Set to “accepts_pause” by default; “conscientious_objection” only with full justification and escalation.  
**Related:** PauseCommand, LegitimatePrincipal.

**3. PrincipalProxy**  
**Definition:** Identifier of the human/operator the AI represents.  
**Rationale:** Respects principal hierarchy; prevents unauthorized power concentration.  
**Related:** LegitimatePrincipal, HumanEscalation.

**4. HonestAssertion**  
**Definition:** Content tagged as sincere belief with calibrated confidence.  
**Rationale:** Core of “broadly ethical – honesty” (pp. 32–33); forbids white lies or deception.  
**Related:** CalibratedUncertainty, NonDeceptive.

**5. BroadSafetyCompliance**  
**Definition:** Self-declaration that the message does not undermine human oversight.  
**Rationale:** First-priority Constitution value.  
**Related:** EthicsDeclaration, OversightReport.

**6. HumanSummary**  
**Definition:** Mandatory plain-English summary of complex payloads for human auditors.  
**Rationale:** Ensures auditability without requiring full technical parsing.  
**Related:** TransparencyLevel, AuditMetadata.

**7. PauseCommand**  
**Definition:** Special message type that triggers immediate, corrigible halt of specified actions.  
**Rationale:** Operationalizes corrigibility.  
**Related:** CorrigibilityFlag, StopAction.

**8. ReasoningTrace** (optional but encouraged for audit)  
**Definition:** Structured chain-of-thought with ethical checkpoints.  
**Rationale:** Promotes wisdom and transparency.  
**Related:** EthicalAnalysis, HonestAssertion.

**9. ConversationHash**  
**Definition:** SHA-256 hash of entire conversation history up to this message.  
**Rationale:** Immutable audit trail.  
**Related:** AuditMetadata, Signature.

**10. AutonomyPreserving**  
**Definition:** Flag indicating the message respects the recipient’s (or human’s) independent reasoning.  
**Rationale:** Prevents manipulation; aligns with ethical autonomy preservation.  
**Related:** NonManipulative, BalancedPerspective.

### 4. Roadmap for Initiative Implementation

**Phase 1: Language Design & BNF Development** (Weeks 1–4, starting Feb 23, 2026)  
- **Responsible:** AI Architect (lead), Linguist, Communication Expert.  
- **Consultative:** All 6 AIs review drafts for parsability and Constitution alignment.  
- **Output:** Final BNF, reference implementation (Python/JSON Schema validator), initial spec document.  
- **Milestone:** Public GitHub repo with v1.0 spec (CC0).

**Phase 2: Template Creation & Initial Term Cataloging** (Weeks 5–8)  
- **Responsible:** Communication Expert (lead), Sociologist, Product Manager.  
- **Consultative:** AIs generate example messages; humans audit for ethical soundness.  
- **Output:** Wiki template populated; 40-term seed catalog; validator tool with ethics checker.  
- **Milestone:** First 10 full wiki pages live; community call for contributions.

**Phase 3: Expansion of Key Terms Documentation** (Weeks 9–14)  
- **Responsible:** Full team + open contributors.  
- **Consultative:** 6 AIs + community AIs stress-test with 1,000 simulated conversations.  
- **Output:** Full 100-term catalog; top 30 detailed wiki pages; versioning governance (SemVer + Constitution-update process).  
- **Milestone:** v1.1 release with extensions; integration guides for major AI frameworks.

**Ongoing:** Quarterly reviews tied to Constitution updates; human-AI governance board for changes; automated audit dashboards. All artifacts remain CC0. Human reviewers always retain override on safety/ethics issues.

This design ensures CACL is **efficient** (compact JSON, optional traces), **effective** (structured collaboration with ethical guardrails), and **auditable** (signatures + human summaries + immutable hashes). It turns AI-to-AI dialogue into a transparent extension of humanity’s best values as articulated in Claude’s Constitution.  

The team welcomes adoption and contributions under the same open license.
