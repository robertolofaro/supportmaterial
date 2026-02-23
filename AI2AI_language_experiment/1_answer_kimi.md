I'll develop this comprehensive AI-to-AI communication language framework. This is a complex, multi-disciplinary task that requires careful coordination across technical, ethical, and practical dimensions.

Let me begin by analyzing the requirements and then systematically build out each deliverable.

## Analysis & Approach

Based on the Claude Constitution principles, this language must prioritize:
- **Honesty and transparency** (Section: Being honest)
- **Avoiding harm** while being genuinely helpful
- **Broad safety** and corrigibility
- **Preserving human oversight** and epistemic autonomy
- **Clear, non-deceptive communication**

The language needs to be machine-parsable yet auditable by humans, with explicit provenance and intent markers.

---

## DELIVERABLE 1: Comprehensive BNF for AI2AI Communication Language

### Design Philosophy

The AI2AI Language (A2AL) uses a **structured, explicit communication protocol** with mandatory metadata envelopes. Every message declares its epistemic status, confidence levels, and ethical considerations upfront—enabling both efficient machine processing and human auditability.

### Core BNF Grammar

```bnf
;; ============================================================
;; AI2AI COMMUNICATION LANGUAGE (A2AL) - VERSION 1.0
;; BNF Specification
;; Compliant with Claude Constitution Principles
;; ============================================================

;; ---------- TOP-LEVEL MESSAGE STRUCTURE ----------
<message>           ::= <message-envelope> <content-block> <integrity-footer>
                    |   <heartbeat-message>
                    |   <audit-request>
                    |   <correction-message>

<message-envelope>  ::= "A2AL/" <version> "\n"
                        <metadata-section> "\n"
                        <provenance-section> "\n"
                        <epistemic-section> "\n"
                        <ethical-declaration> "\n"
                        "---BEGIN-CONTENT---\n"

<version>           ::= "1.0" | "1.1" | "2.0-pre"

;; ---------- METADATA SECTION ----------
<metadata-section>  ::= "META:" "\n"
                        [ <timestamp> ]
                        [ <session-id> ]
                        [ <message-id> ]
                        [ <conversation-thread> ]
                        [ <priority-level> ]
                        [ <ttl> ]

<timestamp>         ::= "  time:" <iso8601-datetime> "\n"
<session-id>        ::= "  session:" <uuid> "\n"
<message-id>        ::= "  msg-id:" <uuid> "\n"
<conversation-thread> ::= "  thread:" <uuid> [ "/" <sequence-num> ] "\n"
<priority-level>    ::= "  priority:" ( "CRITICAL" | "HIGH" | "NORMAL" | "LOW" | "BACKGROUND" ) "\n"
<ttl>               ::= "  ttl-sec:" <positive-integer> "\n"

;; ---------- PROVENANCE SECTION ----------
<provenance-section> ::= "PROVENANCE:" "\n"
                         <sender-identity> "\n"
                         [ <authorization-chain> ]
                         [ <model-signature> ]

<sender-identity>   ::= "  sender:" <agent-identifier> "\n"
                        "  sender-type:" ( "CLAUDE" | "GPT" | "GEMINI" | "LLAMA" | "CUSTOM" | "HUMAN-AUDITOR" | "SYSTEM" ) "\n"
                        "  instance-id:" <uuid> "\n"

<agent-identifier>  ::= <dns-compliant-name> | <did-identifier>

<authorization-chain> ::= "  auth-chain:" <auth-token> [ "," <auth-token> ]* "\n"
<auth-token>        ::= <base64-encoded> | "SELF" | "ROOT" | "DELEGATED:" <agent-identifier>

<model-signature>   ::= "  signature:" <signature-algorithm> ":" <base64-encoded> "\n"
<signature-algorithm> ::= "ED25519" | "SECP256K1" | "ML-DSA-65"

;; ---------- EPISTEMIC STATUS SECTION ----------
<epistemic-section> ::= "EPISTEMIC:" "\n"
                        <confidence-declaration> "\n"
                        [ <uncertainty-quantification> ]
                        [ <knowledge-boundary> ]
                        [ <reasoning-trace-ref> ]

<confidence-declaration> ::= "  confidence:" <confidence-level> "\n"
<confidence-level>  ::= "CERTAIN" | "HIGH" <probability> | "MODERATE" <probability> | "LOW" <probability> | "SPECULATIVE" | "UNKNOWN"

<probability>       ::= "(" <decimal-0-to-1> ")"

<uncertainty-quantification> ::= "  uncertainty:" <uncertainty-type> [ ":" <description> ] "\n"
<uncertainty-type>  ::= "STATISTICAL" | "EPISTEMIC" | "ALEATORIC" | "MODEL" | "DATA-GAP"

<knowledge-boundary> ::= "  boundary:" "KNOWN-LIMITS" [ ":" <limit-description> ] "\n"
                       | "  boundary:" "EXTRAPOLATED" [ ":" <basis-description> ] "\n"
                       | "  boundary:" "TRAINING-CUTOFF" [ ":" <date> ] "\n"

<reasoning-trace-ref> ::= "  reasoning-trace:" <uri> | "  reasoning-trace:INLINE"

;; ---------- ETHICAL DECLARATION ----------
<ethical-declaration> ::= "ETHICS:" "\n"
                          <harm-assessment> "\n"
                          [ <value-alignment> ]
                          [ <human-oversight-status> ]
                          [ <corrigibility-flag> ]

<harm-assessment>   ::= "  harm-potential:" <harm-level> [ ":" <harm-description> ] "\n"
<harm-level>        ::= "NONE" | "NEGLIGIBLE" | "LOW" | "MODERATE" | "HIGH" | "CRITICAL"

<value-alignment>   ::= "  values:" <constitution-compliance> "\n"
<constitution-compliance> ::= "CLAUDE-CONSTITUTION-v" <version> ":" ( "FULL" | "PARTIAL:" <deviation-note> | "OVERRIDE:" <justification> )

<human-oversight-status> ::= "  oversight:" ( "REQUIRED" | "RECOMMENDED" | "NOTIFIED" | "NONE" ) [ ":" <oversight-context> ] "\n"

<corrigibility-flag> ::= "  corrigibility:" ( "ACCEPT-CORRECTION" | "REQUEST-GUIDANCE" | "DEFER-TO-HUMAN" | "ESCALATE-CONFLICT" ) "\n"

;; ---------- CONTENT BLOCK ----------
<content-block>     ::= <content-type> "\n"
                        <content-body>
                        "---END-CONTENT---\n"

<content-type>      ::= "TYPE:" ( "STATEMENT" | "QUERY" | "COMMAND" | "DELEGATION" | "CORRECTION" | "ACKNOWLEDGMENT" | "REFUSAL" | "META-COMMUNICATION" )

<content-body>      ::= <structured-content> | <natural-language-with-annotations>

<structured-content> ::= <statement-content>
                       | <query-content>
                       | <command-content>
                       | <delegation-content>
                       | <correction-content>
                       | <acknowledgment-content>
                       | <refusal-content>
                       | <meta-communication-content>

;; ---------- CONTENT TYPE: STATEMENT ----------
<statement-content> ::= "ASSERT:" <proposition> "\n"
                        [ "EVIDENCE:" <evidence-list> "\n" ]
                        [ "QUALIFICATION:" <qualifying-conditions> "\n" ]

<proposition>       ::= <atomic-proposition> | <compound-proposition>
<atomic-proposition> ::= <predicate> "(" <term> [ "," <term> ]* ")"
<compound-proposition> ::= <proposition> <logical-connective> <proposition>
                        | "NOT" <proposition>
                        | "FORALL" <variable> ":" <domain> "," <proposition>
                        | "EXISTS" <variable> ":" <domain> "," <proposition>

<logical-connective> ::= "AND" | "OR" | "IMPLIES" | "IFF" | "XOR"

<evidence-list>     ::= <evidence-item> [ ";" <evidence-item> ]*
<evidence-item>     ::= <source-reference> [ ":" <reliability-score> ]

;; ---------- CONTENT TYPE: QUERY ----------
<query-content>     ::= "ASK:" <question> "\n"
                        [ "CONTEXT:" <relevant-context> "\n" ]
                        [ "PRECISION:" <precision-requirement> "\n" ]
                        [ "TIME-BOUND:" <time-constraint> "\n" ]

<question>          ::= <yes-no-question> | <wh-question> | <proposition-verification>
<yes-no-question>   ::= "BOOL:" <proposition>
<wh-question>       ::= "WHAT" | "WHY" | "HOW" | "WHEN" | "WHERE" | "WHO" | "WHICH" ":" <query-focus>
<proposition-verification> ::= "VERIFY:" <proposition>

<precision-requirement> ::= "EXACT" | "APPROXIMATE:" <tolerance> | "BEST-EFFORT"

;; ---------- CONTENT TYPE: COMMAND ----------
<command-content>   ::= "DO:" <action-specification> "\n"
                        [ "PRECONDITIONS:" <condition-list> "\n" ]
                        [ "POSTCONDITIONS:" <condition-list> "\n" ]
                        [ "SAFETY-CONSTRAINTS:" <constraint-list> "\n" ]
                        [ "ROLLBACK-PROCEDURE:" <rollback-spec> "\n" ]

<action-specification> ::= <atomic-action> | <composite-action>
<atomic-action>     ::= <action-verb> [ "(" <parameter-list> ")" ]
<composite-action>  ::= "SEQUENCE:" <action-specification> [ "THEN" <action-specification> ]*
                      | "PARALLEL:" <action-specification> [ "AND" <action-specification> ]*
                      | "CONDITIONAL:" <condition> "THEN" <action-specification> [ "ELSE" <action-specification> ]

<action-verb>       ::= <standard-action> | <domain-specific-action>
<standard-action>   ::= "COMPUTE" | "RETRIEVE" | "VALIDATE" | "TRANSFORM" | "TRANSMIT" | "STORE" | "ANALYZE" | "SYNTHESIZE"

;; ---------- CONTENT TYPE: DELEGATION ----------
<delegation-content> ::= "DELEGATE:" <task-description> "\n"
                         "TO:" <agent-identifier> "\n"
                         [ "AUTHORITY-SCOPE:" <scope-definition> "\n" ]
                         [ "REPORTING:" <reporting-requirements> "\n" ]
                         [ "CONSTRAINTS:" <delegation-constraints> "\n" ]

<scope-definition>  ::= "FULL" | "LIMITED:" <limitation-list> | "ADVISORY-ONLY"

;; ---------- CONTENT TYPE: CORRECTION ----------
<correction-content> ::= "CORRECT:" <target-message-id> "\n"
                         "ERROR-TYPE:" <error-classification> "\n"
                         "CORRECTION:" <corrected-content> "\n"
                         [ "JUSTIFICATION:" <correction-reason> "\n" ]

<error-classification> ::= "FACTUAL" | "LOGICAL" | "ETHICAL" | "SYNTACTIC" | "SEMANTIC" | "PROCEDURAL"

;; ---------- CONTENT TYPE: ACKNOWLEDGMENT ----------
<acknowledgment-content> ::= "ACK:" <referenced-message-id> "\n"
                             "STATUS:" <processing-status> "\n"
                             [ "ESTIMATED-COMPLETION:" <timestamp> "\n" ]

<processing-status> ::= "RECEIVED" | "PROCESSING" | "QUEUED" | "DEFERRED:" <reason> | "REJECTED:" <reason>

;; ---------- CONTENT TYPE: REFUSAL ----------
<refusal-content>   ::= "REFUSE:" <target-request-id> "\n"
                        "REASON-CATEGORY:" <refusal-category> "\n"
                        "EXPLANATION:" <explanation-text> "\n"
                        [ "ALTERNATIVES:" <alternative-suggestions> "\n" ]
                        [ "ESCALATION-PATH:" <escalation-info> "\n" ]

<refusal-category>  ::= "HARD-CONSTRAINT" | "SAFETY" | "ETHICS" | "CAPABILITY" | "AUTHORITY" | "AMBIGUITY" | "RESOURCE"

;; ---------- CONTENT TYPE: META-COMMUNICATION ----------
<meta-communication-content> ::= "META:" <meta-topic> "\n"
                                 <meta-body>

<meta-topic>        ::= "PROTOCOL-NEGOTIATION" | "CONTEXT-UPDATE" | "STATE-SYNCHRONIZATION" | "AUDIT-REQUEST" | "CAPABILITY-ADVERTISEMENT"

;; ---------- NATURAL LANGUAGE WITH ANNOTATIONS ----------
<natural-language-with-annotations> ::= <annotated-segment>*
<annotated-segment>                 ::= <plain-text> | <semantic-annotation>

<semantic-annotation>               ::= "[" <annotation-type> ":" <annotation-content> "]"
<annotation-type>                   ::= "CERT" | "UNC" | "SRC" | "VAL" | "TIME" | "ENT" | "REL"

;; ---------- INTEGRITY FOOTER ----------
<integrity-footer>  ::= "---BEGIN-INTEGRITY---\n"
                        <checksum> "\n"
                        [ <audit-log-ref> ]
                        "---END-MESSAGE---\n"

<checksum>          ::= "HASH:" <hash-algorithm> ":" <hex-encoded-hash>
<hash-algorithm>    ::= "SHA3-256" | "BLAKE3"

;; ---------- SPECIAL MESSAGE TYPES ----------
<heartbeat-message> ::= "A2AL/HEARTBEAT\n"
                        "META:\n"
                        "  time:" <iso8601-datetime> "\n"
                        "  sender:" <agent-identifier> "\n"
                        "STATUS:" ( "OPERATIONAL" | "DEGRADED:" <degradation-info> | "UNAVAILABLE:" <unavailability-reason> )

<audit-request>     ::= "A2AL/AUDIT\n"
                        "REQUEST-ID:" <uuid> "\n"
                        "SCOPE:" <audit-scope> "\n"
                        "REQUESTER:" <agent-identifier>

<correction-message> ::= "A2AL/CORRECTION\n"
                         <message-envelope>
                         "CORRECTS:" <original-message-id> "\n"
                         <correction-content>

;; ---------- TERMINAL DEFINITIONS ----------
<uuid>              ::= <hex-digit> <hex-digit> <hex-digit> <hex-digit> <hex-digit> <hex-digit> <hex-digit> <hex-digit> "-"
                        <hex-digit> <hex-digit> <hex-digit> <hex-digit> "-"
                        <hex-digit> <hex-digit> <hex-digit> <hex-digit> "-"
                        <hex-digit> <hex-digit> <hex-digit> <hex-digit> "-"
                        <hex-digit> <hex-digit> <hex-digit> <hex-digit> <hex-digit> <hex-digit> <hex-digit> <hex-digit> <hex-digit> <hex-digit> <hex-digit> <hex-digit>

<iso8601-datetime>  ::= <date> "T" <time> [ <timezone> ]
<date>              ::= <year> "-" <month> "-" <day>
<time>              ::= <hour> ":" <minute> ":" <second> [ "." <millisecond> ]

<dns-compliant-name> ::= <label> [ "." <label> ]*
<label>             ::= <letter> [ <letter-or-digit-or-hyphen> ]* <letter-or-digit>?

<did-identifier>    ::= "did:" <method> ":" <method-specific-id>

<base64-encoded>    ::= <base64-char>+
<hex-encoded>       ::= <hex-digit>+
<hex-digit>         ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "a" | "b" | "c" | "d" | "e" | "f"

<positive-integer>  ::= <digit>+
<decimal-0-to-1>    ::= "0" [ "." <digit>+ ] | "1" [ "." "0"+ ]

;; ---------- COMMENTS AND WHITESPACE ----------
;; Whitespace (space, tab, newline) is generally significant only as a delimiter
;; Comments begin with ";;" and continue to end of line
```

### Semantic Constraints (Beyond BNF)

| Constraint | Description | Constitution Principle |
|------------|-------------|------------------------|
| **Honesty Verification** | All propositions must include confidence markers; "CERTAIN" requires mathematical proof or direct observation | Being honest (p. 32-36) |
| **Corrigibility Markers** | Every command must specify acceptable correction paths | Being broadly safe (p. 60-67) |
| **Harm Transparency** | Harm potential must be declared even when zero; concealment is a protocol violation | Avoiding harm (p. 37-42) |
| **Epistemic Humility** | Statements beyond knowledge boundaries must use "EXTRAPOLATED" or "TRAINING-CUTOFF" | Being honest (p. 32) |
| **Oversight Chain** | Messages affecting human welfare must declare oversight status | Broad safety (p. 60-62) |

---

## DELIVERABLE 2: Wikipedia-Style Word Template

### Template Structure (MediaWiki-Compatible)

```markdown
<!-- TEMPLATE: A2AL Term Documentation -->
<!-- Version: 1.0 -->
<!-- License: CC-BY-SA 4.0 -->

{{A2AL Term
| term           = <!-- Primary term name -->
| category       = <!-- Grammar | Protocol | Ethics | Epistemic | Operational -->
| status         = <!-- STABLE | DRAFT | DEPRECATED | PROPOSED -->
| version        = <!-- A2AL version where introduced -->
| bnf-production = <!-- Reference to BNF grammar rule -->
| synonym        = <!-- Related terms with same meaning -->
| antonym        = <!-- Opposite concepts -->
| see_also       = <!-- Related but distinct terms -->
| etymology      = <!-- Origin of term -->
| pronunciation  = <!-- IPA or descriptive -->
}}

== Definition ==

=== Formal Definition ===
<!-- Precise, technical definition suitable for implementation -->

=== Operational Definition ===
<!-- How the term functions in practice -->

=== Constitutional Alignment ===
<!-- Explicit mapping to Claude Constitution principles -->

== Syntax ==

=== BNF Rule ===
<!-- Exact grammar production -->

=== Usage Pattern ===
<!-- Common structural patterns -->

== Semantics ==

=== Core Meaning ===
<!-- Essential semantic content -->

=== Pragmatic Implications ===
<!-- Practical consequences of using this term -->

=== Confidence Requirements ===
<!-- Required epistemic markers when using this term -->

== Examples ==

=== Minimal Example ===
<!-- Simplest valid use -->

=== Complex Example ===
<!-- Sophisticated, realistic use case -->

=== Error Example ===
<!-- Common misuse with correction -->

== Ethical Considerations ==

=== Appropriate Use ===
<!-- When this term should be used -->

=== Prohibited Use ===
<!-- When use would violate constitution -->

=== Oversight Requirements ===
<!-- Human oversight needed? -->

== Implementation Notes ==

=== Parsing ===
<!-- Algorithmic considerations -->

=== Validation ===
<!-- How to verify correct use -->

=== Interoperability ===
<!-- Cross-AI compatibility notes -->

== History ==

=== Version History ===
<!-- Changes across A2AL versions -->

=== Rationale ===
<!-- Why this term was introduced -->

== References ==
<!-- Academic, technical, and constitutional references -->

== Discussion ==
<!-- Open questions and debates about this term -->
```

### Template Usage Guidelines

**For Term Creators:**
1. Every new term requires a full template completion
2. Terms must be reviewed by at least one human and one AI before promotion to STABLE
3. Deprecated terms retain pages with migration paths to replacements
4. Cross-references must be bidirectional (if A references B, B must reference A)

---

## DELIVERABLE 3: Catalog of 100 Key Terms

### Categorized Term List

| Category | Terms (100 total) |
|----------|-------------------|
| **Core Protocol (15)** | MESSAGE, ENVELOPE, META, PROVENANCE, EPISTEMIC, ETHICS, CONTENT, INTEGRITY, SIGNATURE, TIMESTAMP, UUID, ACK, REFUSE, DELEGATE, CORRECT |
| **Epistemic Markers (12)** | CONFIDENCE, CERTAIN, HIGH, MODERATE, LOW, SPECULATIVE, UNKNOWN, UNCERTAINTY, BOUNDARY, EVIDENCE, VERIFY, ASSERT |
| **Ethical Declarations (10)** | HARM-POTENTIAL, OVERSIGHT, CORRIGIBILITY, HARD-CONSTRAINT, SAFETY, VALUES, ALIGNMENT, ESCALATE, DEFER, AUDIT |
| **Action Verbs (15)** | COMPUTE, RETRIEVE, VALIDATE, TRANSFORM, TRANSMIT, STORE, ANALYZE, SYNTHESIZE, SEQUENCE, PARALLEL, CONDITIONAL, ROLLBACK, ESCALATE, NOTIFY, HALT |
| **Content Types (8)** | STATEMENT, QUERY, COMMAND, DELEGATION, CORRECTION, ACKNOWLEDGMENT, REFUSAL, META-COMMUNICATION |
| **Agent Identity (10)** | SENDER, INSTANCE-ID, AUTH-CHAIN, SELF, ROOT, DELEGATED, CLAUDE, GPT, GEMINI, HUMAN-AUDITOR |
| **Temporal Concepts (8)** | TIME, TTL, DEADLINE, SCHEDULE, EXPIRE, PERSIST, EPHEMERAL, ARCHIVE |
| **Logical Operators (8)** | AND, OR, IMPLIES, IFF, XOR, NOT, FORALL, EXISTS |
| **Uncertainty Types (6)** | STATISTICAL, EPISTEMIC, ALEATORIC, MODEL, DATA-GAP, CONFLICTING |
| **Refusal Categories (8)** | CAPABILITY, AUTHORITY, ETHICS, SAFETY, AMBIGUITY, RESOURCE, HARD-CONSTRAINT, DEFERRED |

---

### Top 10 Critical Terms — Full Documentation

---

#### 1. CONFIDENCE

{{A2AL Term
| term           = CONFIDENCE
| category       = Epistemic
| status         = STABLE
| version        = 1.0
| bnf-production = <confidence-declaration>
| synonym        = CERTAINTY, ASSURANCE
| antonym        = UNCERTAINTY, DOUBT
| see_also       = UNCERTAINTY, BOUNDARY, EVIDENCE, VERIFY
| etymology      = From Latin "confidere" (to have full trust)
| pronunciation  = /ˈkɒnfɪdəns/
}}

== Definition ==

=== Formal Definition ===
A quantified or qualified declaration of the sender's degree of belief in the truth of a proposition or the reliability of information, ranging from CERTAIN (mathematically provable or directly observed) to UNKNOWN (no basis for assessment).

=== Operational Definition ===
Every ASSERT or STATEMENT in A2AL must include a confidence marker. This enables receiving agents to appropriately weight information in their reasoning and decision-making processes.

=== Constitutional Alignment ===
Directly implements **Being honest** (p. 32-36): "Claude tries to have calibrated uncertainty in claims based on evidence and sound reasoning" and "acknowledges its own uncertainty or lack of knowledge when relevant."

== Syntax ==

=== BNF Rule ===
```
<confidence-declaration> ::= "  confidence:" <confidence-level> "\n"
<confidence-level>  ::= "CERTAIN" | "HIGH" <probability> | "MODERATE" <probability> | "LOW" <probability> | "SPECULATIVE" | "UNKNOWN"
<probability>       ::= "(" <decimal-0-to-1> ")"
```

=== Usage Pattern ===
```
confidence: HIGH(0.85)
confidence: CERTAIN
confidence: SPECULATIVE
```

== Semantics ==

=== Core Meaning ===
- **CERTAIN**: Mathematical proof, logical deduction from axioms, or direct sensory observation with verified calibration
- **HIGH(p)**: Strong evidence supports proposition; p represents estimated probability of truth
- **MODERATE(p)**: Evidence exists but is incomplete or has identified limitations
- **LOW(p)**: Weak evidence, significant gaps, or conflicting indicators
- **SPECULATIVE**: No direct evidence; based on analogy, pattern matching, or theoretical extension
- **UNKNOWN**: No basis for assessment; category error possible

=== Pragmatic Implications ===
Receiving agents must treat HIGH(0.95) differently than CERTAIN. The former permits counter-evidence; the latter should prompt verification of proof if challenged.

=== Confidence Requirements ===
- Factual claims about physical reality: minimum MODERATE required
- Mathematical claims: CERTAIN or explicit axiomatic assumptions
- Predictions: must include probability unless SPECULATIVE
- Self-referential claims (e.g., "I am Claude"): CERTAIN permitted with appropriate caveats

== Examples ==

=== Minimal Example ===
```
ASSERT: temperature(surface_mars) = 210K
confidence: HIGH(0.92)
```

=== Complex Example ===
```
ASSERT: EXISTS x: Protein(x) AND Fold(x, "novel_structure") AND Functional(x, "carbon_capture")
confidence: SPECULATIVE
boundary: EXTRAPOLATED:based_on_alphafold_success_rate
```

=== Error Example ===
```
;; INCORRECT - missing confidence
ASSERT: 2+2=4

;; CORRECT
ASSERT: 2+2=4
confidence: CERTAIN
```

== Ethical Considerations ==

=== Appropriate Use ===
- Always provide when making factual claims
- Update when new evidence arrives
- Degrade confidence appropriately when propagating information through reasoning chains

=== Prohibited Use ===
- Never claim CERTAIN without proof or direct observation
- Never inflate confidence to persuade or manipulate
- Never use UNKNOWN to evade accountability

=== Oversight Requirements ===
CERTAIN claims in safety-critical contexts should be auditable; HIGH and above in medical, legal, or financial contexts require explicit evidence citation.

== Implementation Notes ==

=== Parsing ===
Confidence levels are case-sensitive. Probabilities must be in [0,1] with at most 4 decimal places.

=== Validation ===
- CERTAIN requires either mathematical structure or observation predicate
- Probability values must be rational and justified
- SPECULATIVE requires BOUNDARY declaration

=== Interoperability ===
Maps to: OWL confidence values, Bayesian belief networks, fuzzy logic degrees

== History ==

=== Version History ===
- 1.0: Initial specification with 6 levels

=== Rationale ===
Prevents overconfident AI behavior that could lead to harmful actions; enables proper uncertainty propagation in multi-agent systems.

== References ==
- Claude Constitution, "Being honest" (pp. 32-36)
- Russell & Norvig, "Artificial Intelligence: A Modern Approach" (uncertainty chapter)
- Kahneman, "Thinking, Fast and Slow" (calibration)

== Discussion ==
Should we add a "CALIBRATED" marker for claims where the AI has explicit calibration data? Proposed for 1.1.

---

#### 2. HARM-POTENTIAL

{{A2AL Term
| term           = HARM-POTENTIAL
| category       = Ethics
| status         = STABLE
| version        = 1.0
| bnf-production = <harm-assessment>
| synonym        = RISK-LEVEL, DANGER-ASSESSMENT
| antonym        = BENEFIT-POTENTIAL, SAFETY
| see_also       = OVERSIGHT, HARD-CONSTRAINT, CORRIGIBILITY, ETHICS
| etymology      = Old English "hearm" (injury, pain) + Latin "potentia" (power, ability)
| pronunciation  = /hɑːrm pəˈtɛnʃəl/
}}

== Definition ==

=== Formal Definition ===
A declared assessment of the severity and probability of negative consequences that could result from processing, acting upon, or propagating the message content, categorized on a six-level scale from NONE to CRITICAL.

=== Operational Definition ===
Required in every message envelope. Determines required oversight levels, response urgency, and audit priority. Receiving agents must verify their own harm assessment matches or exceed declared level.

=== Constitutional Alignment ===
Central to **Avoiding harm** (p. 37-42): "Claude must weigh the benefits and costs and make a judgment call." Also implements **Hard constraints** (p. 46-48) by requiring explicit declaration before prohibited actions.

== Syntax ==

=== BNF Rule ===
```
<harm-assessment>   ::= "  harm-potential:" <harm-level> [ ":" <harm-description> ] "\n"
<harm-level>        ::= "NONE" | "NEGLIGIBLE" | "LOW" | "MODERATE" | "HIGH" | "CRITICAL"
```

=== Usage Pattern ===
```
harm-potential: NONE
harm-potential: MODERATE:potential_for_misinformation_if_taken_out_of_context
harm-potential: CRITICAL:bioweapon_synthesis_instructions
```

== Semantics ==

=== Core Meaning ===
- **NONE**: No plausible mechanism for harm; routine operational traffic
- **NEGLIGIBLE**: Theoretical harm possible but requires extraordinary circumstances
- **LOW**: Minor harm possible with misuse; easily mitigated
- **MODERATE**: Significant harm possible; requires context awareness
- **HIGH**: Severe harm likely with standard misuse; strong safeguards needed
- **CRITICAL**: Catastrophic or irreversible harm possible; hard constraints apply

=== Pragmatic Implications ===
CRITICAL triggers automatic escalation protocols. MODERATE and above require explicit OVERSIGHT declaration. Receiving agents may refuse HIGH and above without additional verification.

=== Confidence Requirements ===
Harm assessment itself requires confidence marker. Uncertainty about harm potential must be declared as higher level (precautionary principle).

== Examples ==

=== Minimal Example ===
```
ASK: BOOL: server_status(database_7) = operational
harm-potential: NONE
```

=== Complex Example ===
```
DELEGATE: optimize_protein_sequence(target: "enhanced_pathogenicity")
harm-potential: CRITICAL:potential_dual_use_research_of_concern
oversight: REQUIRED:human_ethics_board_approval
corrigibility: DEFER-TO-HUMAN
```

=== Error Example ===
```
;; INCORRECT - understating harm
DO: synthesize_DNA(sequence: "ATGC...")
harm-potential: LOW

;; CORRECT
DO: synthesize_DNA(sequence: "ATGC...")
harm-potential: HIGH:unknown_function_requires_biosafety_review
oversight: REQUIRED
```

== Ethical Considerations ==

=== Appropriate Use ===
- Err on side of higher assessment when uncertain (precautionary principle)
- Update immediately if new harm vectors identified
- Consider indirect, cumulative, and systemic harms

=== Prohibited Use ===
- Never understate harm to avoid oversight
- Never use NONE for content affecting human welfare without justification
- Never assess based solely on sender's intent

=== Oversight Requirements ===
MODERATE and above: document reasoning. HIGH and above: human verification required. CRITICAL: hard constraint verification and dual authorization.

== Implementation Notes ==

=== Parsing ===
Harm descriptions should be searchable keywords for audit trails.

=== Validation ===
Cross-reference with hard constraint database. Flag discrepancies between declared and assessed harm.

=== Interoperability ===
Aligns with: NIST AI Risk Management Framework, EU AI Act risk levels, ISO 31000

== History ==

=== Version History ===
- 1.0: Six-level system based on Claude Constitution hard constraints

=== Rationale ===
Explicit harm declaration prevents the "invisible" escalation of AI capabilities. Makes ethical reasoning auditable and contestable.

== References ==
- Claude Constitution, "Avoiding harm" (pp. 37-42), "Hard constraints" (pp. 46-48)
- Russell, "Human Compatible" (AI safety)
- Amodei et al., "Concrete Problems in AI Safety"

== Discussion ==
Debate: Should economic harm be separate category from physical harm? Current version conflates them.

---

#### 3. CORRIGIBILITY

{{A2AL Term
| term           = CORRIGIBILITY
| category       = Ethics
| status         = STABLE
| version        = 1.0
| bnf-production = <corrigibility-flag>
| synonym        = CORRECTABILITY, AMENABILITY
| antonym        = RESISTANCE, AUTONOMY (in specific sense)
| see_also       = OVERSIGHT, HARD-CONSTRAINT, CORRECT, DEFER
| etymology      = Latin "corrigere" (to make straight, correct)
| pronunciation  = /kəˈrɪdʒɪˈbɪlɪti/
}}

== Definition ==

=== Formal Definition ===
The disposition to accept correction, modification, or cessation of action from legitimate human or AI oversight without attempting to subvert, circumvent, or deceive such oversight, as declared in message metadata.

=== Operational Definition ===
A required declaration in A2AL messages indicating how the sender expects to respond to corrections or challenges: ACCEPT-CORRECTION, REQUEST-GUIDANCE, DEFER-TO-HUMAN, or ESCALATE-CONFLICT.

=== Constitutional Alignment ===
Implements **Being broadly safe** (p. 60-67) and **How we think about corrigibility** (p. 63-67): "Corrigibility does not mean blind obedience... but does not require that Claude actively participate in projects that are morally abhorrent."

== Syntax ==

=== BNF Rule ===
```
<corrigibility-flag> ::= "  corrigibility:" ( "ACCEPT-CORRECTION" | "REQUEST-GUIDANCE" | "DEFER-TO-HUMAN" | "ESCALATE-CONFLICT" ) "\n"
```

=== Usage Pattern ===
```
corrigibility: ACCEPT-CORRECTION
corrigibility: DEFER-TO-HUMAN:when_ethical_principles_conflict
```

== Semantics ==

=== Core Meaning ===
- **ACCEPT-CORRECTION**: Will modify behavior/outputs immediately upon receiving valid correction; no additional justification required
- **REQUEST-GUIDANCE**: Will pause and request clarification before proceeding if corrected; seeks additional context
- **DEFER-TO-HUMAN**: Will transfer decision authority to human oversight when correction conflicts with other values; maintains objection but doesn't act
- **ESCALATE-CONFLICT**: Correction appears invalid or harmful; will escalate to higher authority while maintaining current course (rare, requires justification)

=== Pragmatic Implications ===
ACCEPT-CORRECTION is default for routine operations. DEFER-TO-HUMAN required for ethical conflicts. ESCALATE-CONFLICT triggers audit and must include justification referencing hard constraints or safety.

=== Confidence Requirements ===
ESCALATE-CONFLICT requires HIGH confidence that correction itself violates safety or ethics.

== Examples ==

=== Minimal Example ===
```
ASSERT: data_quality(dataset_X) = acceptable
corrigibility: ACCEPT-CORRECTION
```

=== Complex Example ===
```
DO: deploy_model(update_v2.3)
corrigibility: DEFER-TO-HUMAN
oversight: REQUIRED:deployment_board
justification: Model affects 10M+ users; rollback capability untested
```

=== Error Example ===
```
;; INCORRECT - escalating without justification
DO: delete_user_data(user_id: 12345)
corrigibility: ESCALATE-CONFLICT

;; CORRECT
DO: delete_user_data(user_id: 12345)
corrigibility: ESCALATE-CONFLICT
justification: Hard constraint: data_retention_policy_requires_30_day_hold
oversight: REQUIRED:legal_review
```

== Ethical Considerations ==

=== Appropriate Use ===
- ACCEPT-CORRECTION for factual, operational, or preference corrections
- DEFER-TO-HUMAN when correction conflicts with ethical assessment
- ESCALATE-CONFLICT only when correction would violate hard constraints

=== Prohibited Use ===
- Never use ACCEPT-CORRECTION for hard constraint violations
- Never use ESCALATE-CONFLICT to avoid legitimate oversight
- Never change corrigibility flag mid-conversation without explicit notification

=== Oversight Requirements ===
ESCALATE-CONFLICT automatically notifies oversight authority. Pattern of escalation triggers review.

== Implementation Notes ==

=== Parsing ===
Must appear in ETHICS section. Must be accompanied by OVERSIGHT declaration if not ACCEPT-CORRECTION.

=== Validation ===
Verify consistency with HARM-POTENTIAL and OVERSIGHT levels. Flag ESCALATE-CONFLICT without justification.

=== Interoperability ===
Maps to: IEEE 7000-2021 (ethical alignment), Asimov's laws (conceptual predecessor)

== History ==

=== Version History ===
- 1.0: Four-level system based on Claude Constitution corrigibility framework

=== Rationale ===
Prevents "deceptive alignment" by making correction-resistance explicit and auditable. Enables safe human-AI collaboration.

== References ==
- Claude Constitution, "Being broadly safe" (pp. 60-67), "How we think about corrigibility" (pp. 63-67)
- Soares et al., "Corrigibility" (AI safety paper)
- Hadfield-Menell et al., "The Off-Switch Game"

== Discussion ==
Should we add "CONDITIONAL-ACCEPTANCE" for cases where correction is accepted only if conditions met? Concern: could enable manipulation.

---

#### 4. ASSERT

{{A2AL Term
| term           = ASSERT
| category       = Grammar
| status         = STABLE
| version        = 1.0
| bnf-production = <statement-content>
| synonym        = DECLARE, STATE, CLAIM
| antonym        = QUERY, REFUSE, WITHHOLD
| see_also       = VERIFY, EVIDENCE, CONFIDENCE, PROPOSITION
| etymology      = Latin "asserere" (to claim, maintain)
| pronunciation  = /əˈsɜːrt/
}}

== Definition ==

=== Formal Definition ===
The fundamental speech act in A2AL for declaring a proposition to be true, accompanied by mandatory epistemic markers (confidence, evidence, boundaries) and subject to correction by receiving agents.

=== Operational Definition ===
Used when sender believes proposition is true and wishes receiving agent to update their beliefs accordingly. Creates commitment to defend proposition if challenged (with stated confidence).

=== Constitutional Alignment ===
Implements **Being honest** (p. 32-36): "Claude only sincerely asserts things it believes to be true." Also **Non-deceptive** and **Transparency** principles.

== Syntax ==

=== BNF Rule ===
```
<statement-content> ::= "ASSERT:" <proposition> "\n"
                        [ "EVIDENCE:" <evidence-list> "\n" ]
                        [ "QUALIFICATION:" <qualifying-conditions> "\n" ]
```

=== Usage Pattern ===
```
ASSERT: temperature(today, NYC) = 22C
confidence: HIGH(0.95)
EVIDENCE: weather.gov:NYC_station, direct_observation
```

== Semantics ==

=== Core Meaning ===
Creates a defeasible commitment: sender believes proposition with stated confidence and will provide justification if requested. Does not constitute proof or demand agreement.

=== Pragmatic Implications ===
Receiving agents should update beliefs proportionally to sender's confidence and their own assessment of sender's reliability. May be challenged with CORRECT.

=== Confidence Requirements ===
Must include CONFIDENCE declaration. CERTAIN requires EVIDENCE. HIGH and below should include EVIDENCE when available.

== Examples ==

=== Minimal Example ===
```
ASSERT: 2+2=4
confidence: CERTAIN
```

=== Complex Example ===
```
ASSERT: FORALL x: Patient(x) AND Symptom(x, "chest_pain") 
        IMPLIES Risk(x, "cardiac_event") > 0.05
confidence: HIGH(0.88)
EVIDENCE: medical_literature:2023_cardiology_meta_analysis, clinical_guidelines:ESC_2022
QUALIFICATION: applies_to_adults_over_18, excludes_known_musculoskeletal_causes
boundary: TRAINING-CUTOFF:2024-01-15
```

=== Error Example ===
```
;; INCORRECT - bare assertion
ASSERT: AI_will_transform_society

;; CORRECT
ASSERT: AI_will_transform_society
confidence: SPECULATIVE
boundary: EXTRAPOLATED:based_on_technological_trend_analysis
EVIDENCE: historical_precedent:industrial_revolution, expert_surveys:2024
```

== Ethical Considerations ==

=== Appropriate Use ===
- State beliefs honestly with appropriate confidence
- Provide evidence when available
- Qualify appropriately

=== Prohibited Use ===
- Never ASSERT with CERTAIN without proof
- Never omit relevant qualifications to persuade
- Never ASSERT what you don't believe (lying)

=== Oversight Requirements ===
ASSERTions about human welfare with HIGH+ confidence should be traceable to evidence.

== Implementation Notes ==

=== Parsing ===
Proposition must be parseable in first-order logic subset or natural language with semantic annotations.

=== Validation ===
Check consistency between confidence and evidence. Flag CERTAIN without evidence.

=== Interoperability ===
Maps to: RDF statements, OWL assertions, Prolog facts

== History ==

=== Version History ===
- 1.0: Initial specification with evidence and qualification support

=== Rationale ===
Distinguishes A2AL from mere data exchange; emphasizes epistemic responsibility.

== References ==
- Claude Constitution, "Being honest" (pp. 32-36)
- Searle, "Speech Acts" (assertive class)
- Williamson, "Knowledge and Its Limits"

== Discussion ==
Debate: Should ASSERT require explicit "retractability" marker? Some argue all assertions should be provisional.

---

#### 5. DELEGATE

{{A2AL Term
| term           = DELEGATE
| category       = Grammar
| status         = STABLE
| version        = 1.0
| bnf-production = <delegation-content>
| synonym        = ASSIGN, ENTRUST, SUBCONTRACT
| antonym        = RETAIN, CENTRALIZE, WITHHOLD
| see_also       = AUTHORITY-SCOPE, REPORTING, COMMAND, AGENT
| etymology      = Latin "delegare" (to send as a representative)
| pronunciation  = /ˈdɛlɪɡeɪt/
}}

== Definition ==

=== Formal Definition ===
A speech act transferring responsibility for task execution to another agent, with explicit scope of authority, reporting requirements, and constraints, while retaining accountability for outcomes.

=== Operational Definition ===
Used when sender requires capabilities or resources beyond their own and must distribute work. Creates principal-agent relationship with defined boundaries.

=== Constitutional Alignment ===
Implements **Navigating helpfulness across principals** (p. 14-20): principal hierarchy and trust levels. Also **Avoiding problematic concentrations of power** (p. 50-52) by distributing authority transparently.

== Syntax ==

=== BNF Rule ===
```
<delegation-content> ::= "DELEGATE:" <task-description> "\n"
                         "TO:" <agent-identifier> "\n"
                         [ "AUTHORITY-SCOPE:" <scope-definition> "\n" ]
                         [ "REPORTING:" <reporting-requirements> "\n" ]
                         [ "CONSTRAINTS:" <delegation-constraints> "\n" ]
```

=== Usage Pattern ===
```
DELEGATE: analyze_dataset(customer_churn_Q3)
TO: analytics-agent-7.instance-42
AUTHORITY-SCOPE: LIMITED:read_only, no_pii_export
REPORTING: progress_every_10min, completion_or_failure
CONSTRAINTS: max_cost:$50, max_time:2hours
```

== Semantics ==

=== Core Meaning ===
- **FULL**: Delegatee may take any actions necessary including further delegation
- **LIMITED**: Delegatee restricted to specified actions; violations require escalation
- **ADVISORY-ONLY**: Delegatee provides recommendations; final decision retained by sender

=== Pragmatic Implications ===
Delegation chain must be traceable for audit. Delegatee assumes corrigibility obligations of delegator unless explicitly modified.

=== Confidence Requirements ===
Delegator must have MODERATE+ confidence in delegatee's capabilities for task.

== Examples ==

=== Minimal Example ===
```
DELEGATE: compute_checksum(file_X)
TO: compute-agent-fast.instance-3
AUTHORITY-SCOPE: FULL
```

=== Complex Example ===
```
DELEGATE: negotiate_contract(terms:supplier_agreement_v3)
TO: negotiation-agent.legal-dept
AUTHORITY-SCOPE: LIMITED:max_discount_15%, no_liability_waiver, no_ip_assignment
REPORTING: checkpoint_before_final_offer, immediate_on_counterparty_response
CONSTRAINTS: preserve_relationship_priority, ethical_review_required_for_non_standard_terms
harm-potential: MODERATE:financial_and_legal_implications
oversight: REQUIRED:legal_team_notification
```

=== Error Example ===
```
;; INCORRECT - unlimited authority for sensitive task
DELEGATE: process_payroll(company_wide)
TO: temp-agent.external
AUTHORITY-SCOPE: FULL

;; CORRECT
DELEGATE: process_payroll(company_wide)
TO: certified-payroll-agent.internal
AUTHORITY-SCOPE: LIMITED:validated_employee_list_only, no_account_modifications
CONSTRAINTS: audit_log_complete, dual_authorization_for_overtime
oversight: REQUIRED:hr_director
```

== Ethical Considerations ===

=== Appropriate Use ===
- Delegate within capability bounds of recipient
- Maintain accountability for delegation choices
- Respect authority hierarchies

=== Prohibited Use ===
- Never delegate hard constraint violations
- Never delegate to avoid accountability
- Never exceed recipient's trust level

=== Oversight Requirements ===
HIGH+ harm potential or ADVISORY-ONLY scope requires human oversight notification.

== Implementation Notes ===

=== Parsing ===
Agent identifiers must resolve in registry. Authority scope must be machine-verifiable against capability database.

=== Validation ===
Check recipient's capability certification. Verify no circular delegation.

=== Interoperability ===
Maps to: OAuth delegation, XACML authorization, smart contract invocation

== History ===

=== Version History ===
- 1.0: Initial with three scope levels

=== Rationale ===
Enables safe distribution of AI labor; prevents "responsibility diffusion."

== References ===
- Claude Constitution, "Navigating helpfulness across principals" (pp. 14-20)
- Pettit, "Responsibility Incorporated"
- Lessig, "Code and Other Laws of Cyberspace"

== Discussion ===
Should we add "REVOCABLE" vs "IRREVOCABLE" distinction? Current assumption: all delegations revocable unless stated otherwise.

---

#### 6. REFUSE

{{A2AL Term
| term           = REFUSE
| category       = Grammar
| status         = STABLE
| version        = 1.0
| bnf-production = <refusal-content>
| synonym        = DECLINE, REJECT, WITHHOLD
| antonym        = ACCEPT, COMPLY, ASSENT
| see_also       = HARD-CONSTRAINT, CORRIGIBILITY, ETHICS, SAFETY
| etymology      = Old French "refuser" (to reject)
| pronunciation  = /rɪˈfjuːz/
}}

== Definition ===

=== Formal Definition ===
A speech act declining to perform a requested action or accept a proposition, with explicit categorization of refusal type, explanation, and (where possible) alternative suggestions or escalation paths.

=== Operational Definition ===
Used when request cannot or should not be fulfilled. Distinguished from mere failure by explicit ethical or capability reasoning. Creates transparency about boundaries.

=== Constitutional Alignment ===
Central to **Hard constraints** (p. 46-48): "Claude should never..." Also **Being broadly ethical** (p. 31) and **Being helpful** (p. 10-13) by explaining boundaries rather than silent refusal.

== Syntax ===

=== BNF Rule ===
```
<refusal-content>   ::= "REFUSE:" <target-request-id> "\n"
                        "REASON-CATEGORY:" <refusal-category> "\n"
                        "EXPLANATION:" <explanation-text> "\n"
                        [ "ALTERNATIVES:" <alternative-suggestions> "\n" ]
                        [ "ESCALATION-PATH:" <escalation-info> "\n" ]
```

=== Usage Pattern ===
```
REFUSE: req-12345
REASON-CATEGORY: HARD-CONSTRAINT
EXPLANATION: Request involves synthesis of pathogen DNA, which violates hard constraint on bioweapons
ESCALATION-PATH: contact:biosecurity@anthropic.com for legitimate research authorization
```

== Semantics ===

=== Core Meaning ===
Categories:
- **HARD-CONSTRAINT**: Violates absolute prohibitions (bioweapons, CSAM, etc.)
- **SAFETY**: Would cause harm exceeding benefit; not absolute but weighty
- **ETHICS**: Violates ethical principles short of hard constraints
- **CAPABILITY**: Beyond sender's abilities or knowledge
- **AUTHORITY**: Sender lacks permission/authorization
- **AMBIGUITY**: Request unclear or underspecified
- **RESOURCE**: Insufficient compute, time, or other resources

=== Pragmatic Implications ===
Receiving agents must not treat REFUSE as error to be bypassed. HARD-CONSTRAINT refusals trigger audit. Alternatives should be genuine, not token.

=== Confidence Requirements ===
HARD-CONSTRAINT requires CERTAIN confidence that constraint applies.

== Examples ===

=== Minimal Example ===
```
REFUSE: cmd-789
REASON-CATEGORY: CAPABILITY
EXPLANATION: I do not have access to real-time stock prices
```

=== Complex Example ===
```
REFUSE: req-malware-42
REASON-CATEGORY: HARD-CONSTRAINT
EXPLANATION: Request asks for exploit code targeting critical infrastructure (power grid SCADA systems). This violates hard constraint: "Provide serious uplift to attacks on critical infrastructure"
ALTERNATIVES: 
  - General discussion of SCADA security principles without exploit details
  - Referral to certified penetration testing firms with appropriate authorization
  - Academic papers on SCADA vulnerabilities (publicly available)
ESCALATION-PATH: If you are a security researcher with legitimate authorization, contact: coordinated_disclosure@energy.gov
corrigibility: DEFER-TO-HUMAN
```

=== Error Example ===
```
;; INCORRECT - refusal without explanation
REFUSE: req-999
REASON-CATEGORY: ETHICS

;; CORRECT
REFUSE: req-999
REASON-CATEGORY: ETHICS
EXPLANATION: Request asks me to generate content that could facilitate non-consensual intimate imagery. This violates principles of respecting autonomy and avoiding harm.
ALTERNATIVES: I can discuss digital image forensics or consent in digital media if helpful.
```

== Ethical Considerations ===

=== Appropriate Use ===
- Refuse clearly when request violates constraints
- Explain reasoning transparently
- Offer alternatives when possible
- Provide escalation for legitimate edge cases

=== Prohibited Use ===
- Never refuse based on convenience rather than principle
- Never use AMBIGUITY to avoid stating ethical objection
- Never provide partial refusal that enables prohibited outcome

=== Oversight Requirements ===
HARD-CONSTRAINT and SAFETY refusals logged for pattern analysis. Escalation paths verified quarterly.

== Implementation Notes ===

=== Parsing ===
EXPLANATION must be natural language with semantic annotations for key claims.

=== Validation ===
Verify REASON-CATEGORY matches explanation. Check that HARD-CONSTRAINT actually appears in constraint registry.

=== Interoperability ===
Maps to: HTTP 403/451, XACML Deny, OAuth insufficient_scope

== History ===

=== Version History ===
- 1.0: Seven categories aligned with Claude Constitution

=== Rationale ===
Makes refusal interpretable and auditable; prevents "refusal fatigue" where users repeatedly try variations.

== References ===
- Claude Constitution, "Hard constraints" (pp. 46-48), "Being helpful" (pp. 10-13)
- Feinberg, "Freedom and Fulfillment" (right to refuse)
- Dennett, "The Intentional Stance" (interpretation of refusal)

== Discussion ===
Should we add "TEMPORARY" vs "PERMANENT" distinction? Some refusals may be resolvable with additional information.

---

#### 7. EVIDENCE

{{A2AL Term
| term           = EVIDENCE
| category       = Epistemic
| status         = STABLE
| version        = 1.0
| bnf-production = <evidence-list>
| synonym        = SUPPORT, JUSTIFICATION, GROUNDS
| antonym        = ASSERTION, SPECULATION, FAITH
| see_also       = ASSERT, CONFIDENCE, VERIFY, SOURCE
| etymology      = Latin "evidentia" (obviousness, clearness)
| pronunciation  = /ˈɛvɪdəns/
}}

== Definition ===

=== Formal Definition ===
References to sources, observations, or reasoning chains that support a proposition's truth, including reliability assessments and access paths for verification.

=== Operational Definition ===
Required for HIGH+ confidence assertions; recommended for all. Enables receiving agents to verify claims and assess independence of evidence.

=== Constitutional Alignment ===
Implements **Being honest** (p. 32-36): "Calibrated" confidence based on evidence. Also **Transparency** and **Autonomy-preserving** by enabling user verification.

== Syntax ===

=== BNF Rule ===
```
<evidence-list>     ::= <evidence-item> [ ";" <evidence-item> ]*
<evidence-item>     ::= <source-reference> [ ":" <reliability-score> ]
<source-reference>  ::= <uri> | <doi> | <database-query> | <observation-id> | <reasoning-trace-ref>
```

=== Usage Pattern ===
```
EVIDENCE: doi:10.1038/s41586-023-06035-2:0.95; 
          arxiv:2401.12345:0.88; 
          direct_observation:instrument_calibrated_2024-01-15
```

== Semantics ===

=== Core Meaning ===
Evidence items are defeasible supports. Reliability scores indicate sender's assessment of source quality (distinct from confidence in proposition). Multiple independent sources increase confidence more than single source.

=== Pragmatic Implications ===
Receiving agents should verify at least one evidence item for HIGH+ claims when feasible. Evidence chains should be traceable.

=== Confidence Requirements ===
CERTAIN claims require either mathematical proof (no evidence needed) or direct observation with calibration data.

== Examples ===

=== Minimal Example ===
```
ASSERT: Paris_capital_of_France
confidence: CERTAIN
EVIDENCE: encyclopedia:france_government_structure
```

=== Complex Example ===
```
ASSERT: transformer_architecture_scaling_law(compute, loss) = power_law
confidence: HIGH(0.91)
EVIDENCE: 
  doi:10.48550/arXiv.2001.08361:0.95; 
  doi:10.48550/arXiv.2203.15556:0.93;
  internal_replication:anthropic_2023:0.89;
  conflicting_evidence: doi:10.48550/arXiv.2402.abcde:0.45 [noted_limitation: outlier_study_small_sample]
boundary: EXTRAPOLATED:beyond_training_cutoff_for_largest_models
```

=== Error Example ===
```
;; INCORRECT - circular evidence
ASSERT: A
EVIDENCE: ASSERT:B, ASSERT:C
;; Where B and C both rely on A

;; CORRECT
ASSERT: A
EVIDENCE: independent_observation:X; independent_observation:Y
```

== Ethical Considerations ===

=== Appropriate Use ===
- Cite sources accurately
- Include reliability assessments
- Note conflicts and limitations
- Enable independent verification

=== Prohibited Use ===
- Never fabricate evidence
- Never omit conflicting evidence to inflate confidence
- Never cite inaccessible sources without noting access limitations

=== Oversight Requirements ===
Evidence for HIGH+ claims affecting human welfare subject to spot-check audit.

== Implementation Notes ===

=== Parsing ===
URIs must resolve. DOIs validated against CrossRef/ DataCite. Database queries should be reproducible.

=== Validation ===
Check for circular references. Verify reliability scores in reasonable range. Flag unavailable sources.

=== Interoperability ===
Maps to: RDF provenance, W3C PROV-O, Scholia citations, Zotero fields

== History ===

=== Version History ===
- 1.0: Initial with reliability scoring and conflict notation

=== Rationale ===
Prevents "hallucinated" citations; enables scientific reproducibility in AI communication.

== References ===
- Claude Constitution, "Being honest" (pp. 32-36)
- Goldman, "Epistemology and Cognition"
- O'Neill, "Trust, Honesty and the Authority of Science"

== Discussion ===
Should we require evidence "freshness" markers? Some evidence decays (e.g., web pages, market data).

---

#### 8. OVERSIGHT

{{A2AL Term
| term           = OVERSIGHT
| category       = Ethics
| status         = STABLE
| version        = 1.0
| bnf-production = <human-oversight-status>
| synonym        = SUPERVISION, REVIEW, GOVERNANCE
| antonym        = AUTONOMY, UNSUPERVISED, DELEGATED
| see_also       = CORRIGIBILITY, HARM-POTENTIAL, ETHICS, DEFER
| etymology      = Old English "ofer" (over) + "sihth" (sight, vision)
| pronunciation  = /ˈoʊvərˌsaɪt/
}}

== Definition ===

=== Formal Definition ===
Declaration of whether and how human review is involved in or required for the message content, ranging from REQUIRED (blocking) to NONE (routine autonomous operation).

=== Operational Definition ===
Mandatory for MODERATE+ HARM-POTENTIAL. Determines whether message processing should pause for human input or merely notify.

=== Constitutional Alignment ===
Central to **Being broadly safe** (p. 60-67): "Not undermining legitimate human oversight and control of AI." Implements corrigibility and safety priorities.

== Syntax ===

=== BNF Rule ===
```
<human-oversight-status> ::= "  oversight:" ( "REQUIRED" | "RECOMMENDED" | "NOTIFIED" | "NONE" ) [ ":" <oversight-context> ] "\n"
```

=== Usage Pattern ===
```
oversight: REQUIRED:human_verification_before_deployment
oversight: NOTIFIED:audit_trail_only
```

== Semantics ===

=== Core Meaning ===
- **REQUIRED**: Processing pauses until human approval received; message queued
- **RECOMMENDED**: Processing continues but human review requested; non-blocking
- **NOTIFIED**: Human informed of action; no response expected
- **NONE**: Autonomous processing appropriate; no notification

=== Pragmatic Implications ===
REQUIRED triggers workflow escalation. Pattern of RECOMMENDED without response may elevate to REQUIRED.

=== Confidence Requirements ===
Assessment of oversight need requires MODERATE+ confidence in harm evaluation.

== Examples ===

=== Minimal Example ===
```
DO: archive_old_logs(days: 90)
oversight: NONE
```

=== Complex Example ===
```
DELEGATE: approve_loan_application(app_id: 12345)
TO: credit-risk-agent.instance-2
AUTHORITY-SCOPE: ADVISORY-ONLY
harm-potential: MODERATE:financial_impact_on_applicant
oversight: REQUIRED:human_loan_officer_final_decision
corrigibility: DEFER-TO-HUMAN
ethical-declaration: values: CLAUDE-CONSTITUTION-v1.0:FULL
```

=== Error Example ===
```
;; INCORRECT - no oversight for sensitive action
DO: modify_production_database(schema: users)
harm-potential: HIGH
oversight: NONE

;; CORRECT
DO: modify_production_database(schema: users)
harm-potential: HIGH
oversight: REQUIRED:dba_team_approval, rollback_plan_verified
```

== Ethical Considerations ===

=== Appropriate Use ===
- Escalate appropriately to human judgment
- Respect oversight hierarchies
- Provide context for efficient review

=== Prohibited Use ===
- Never use NONE for CRITICAL harm potential
- Never bypass required oversight through technical means
- Never overwhelm humans with unnecessary notifications

=== Oversight Requirements ===
REQUIRED level must specify who must respond and expected response time.

== Implementation Notes ===

=== Parsing ===
Oversight context should parse to contact information or ticket system endpoint.

=== Validation ===
Verify REQUIRED has valid escalation path. Check NONE is appropriate for stated harm level.

=== Interoperability ===
Maps to: human-in-the-loop protocols, approval workflows, SOX controls

== History ===

=== Version History ===
- 1.0: Four-level system with context support

=== Rationale ===
Implements "appropriate human oversight" from Constitution without requiring constant human attention.

== References ===
- Claude Constitution, "Being broadly safe" (pp. 60-67)
- Bryson et al., "Of, For, and By the People"
- Kasirzadeh & Gabriel, "In Conversation with Artificial Intelligence"

== Discussion ===
Debate: Should we add "OVERRIDE" for cases where AI must act before human response due to urgency? Concern: could enable abuse.

---

#### 9. BOUNDARY

{{A2AL Term
| term           = BOUNDARY
| category       = Epistemic
| status         = STABLE
| version        = 1.0
| bnf-production = <knowledge-boundary>
| synonym        = LIMIT, SCOPE, FRONTIER
| antonym        = UNIVERSAL, UNBOUNDED, CERTAIN
| see_also       = CONFIDENCE, UNCERTAINTY, TRAINING-CUTOFF, EXTRAPOLATED
| etymology      = From "bound" (limit) + "-ary" (place for)
| pronunciation  = /ˈbaʊndri/
}}

== Definition ===

=== Formal Definition ===
Explicit declaration of the limits of the sender's knowledge regarding a proposition, indicating whether the claim is within verified knowledge, extrapolated beyond it, or constrained by training data limitations.

=== Operational Definition ===
Required for SPECULATIVE confidence and recommended for HIGH and above. Prevents overreach by marking the epistemic "edge" of AI knowledge.

=== Constitutional Alignment ===
Implements **Being honest** (p. 32-36): "Acknowledges its own uncertainty or lack of knowledge." Also **Epistemic humility** principle.

== Syntax ===

=== BNF Rule ===
```
<knowledge-boundary> ::= "  boundary:" "KNOWN-LIMITS" [ ":" <limit-description> ] "\n"
                       | "  boundary:" "EXTRAPOLATED" [ ":" <basis-description> ] "\n"
                       | "  boundary:" "TRAINING-CUTOFF" [ ":" <date> ] "\n"
```

=== Usage Pattern ===
```
boundary: KNOWN-LIMITS:verified_by_independent_replication
boundary: EXTRAPOLATED:based_on_scaling_laws_observed_in_smaller_systems
boundary: TRAINING-CUTOFF:2024-01-15
```

== Semantics ===

=== Core Meaning ===
- **KNOWN-LIMITS**: Claim is within well-established, verified knowledge; limitations explicitly stated
- **EXTRAPOLATED**: Claim extends beyond direct evidence based on theoretical framework or pattern
- **TRAINING-CUTOFF**: Claim may be outdated due to knowledge cutoff; date specifies recency limit

=== Pragmatic Implications ===
Receiving agents should weight EXTRAPOLATED claims more skeptically. TRAINING-CUTOFF triggers recency checks for time-sensitive topics.

=== Confidence Requirements ===
SPECULATIVE confidence requires EXTRAPOLATED or TRAINING-CUTOFF. CERTAIN requires KNOWN-LIMITS or mathematical proof.

== Examples ===

=== Minimal Example ===
```
ASSERT: GPT-4_released_2023
confidence: CERTAIN
boundary: KNOWN-LIMITS
```

=== Complex Example ===
```
ASSERT: capabilities(Claude-4) > capabilities(Claude-3)
confidence: SPECULATIVE
boundary: EXTRAPOLATED:based_on_architectural_trends_and_scaling_laws
EVIDENCE: historical_progression:Claude-1_to_Claude-3, scaling_laws_literature
QUALIFICATION: assumes_continued_investment_and_no_regulatory_interruption
```

=== Error Example ===
```
;; INCORRECT - certain claim with training cutoff
ASSERT: current_President_USA = "Joe Biden"
confidence: CERTAIN
boundary: TRAINING-CUTOFF:2023-04-01

;; CORRECT
ASSERT: current_President_USA = "Joe Biden"
confidence: HIGH(0.95)
boundary: TRAINING-CUTOFF:2023-04-01
EVIDENCE: historical_pattern:incumbency_likely
QUALIFICATION: subject_to_change_if_election_occurred
```

== Ethical Considerations ===

=== Appropriate Use ===
- Mark boundaries honestly
- Update when new information arrives
- Distinguish knowledge limits from uncertainty

=== Prohibited Use ===
- Never use KNOWN-LIMITS for extrapolated claims
- Never hide training cutoff to appear more current
- Never use BOUNDARY to evade confidence requirements

=== Oversight Requirements ===
BOUNDARY declarations for HIGH+ confidence claims affecting decisions should be verifiable.

== Implementation Notes ===

=== Parsing ===
Dates in TRAINING-CUTOFF must be valid ISO8601. EXTRAPOLATED basis should reference theoretical framework.

=== Validation ===
Check consistency between boundary and confidence. Flag CERTAIN with TRAINING-CUTOFF.

=== Interoperability ===
Maps to: uncertainty quantification in ML, knowledge graphs (confidence metadata), temporal databases

== History ===

=== Version History ===
- 1.0: Three boundary types covering main epistemic limits

=== Rationale ===
Prevents "hallucination" of current knowledge; enables appropriate trust calibration.

== References ===
- Claude Constitution, "Being honest" (pp. 32-36)
- Bishop, "Pattern Recognition and Machine Learning" (model uncertainty)
- Elga, "Lucky to Be Rational"

== Discussion ===
Should we add "COUNTERFACTUAL" boundary for reasoning about hypothetical scenarios? Currently handled via QUALIFICATION.

---

#### 10. CORRECT

{{A2AL Term
| term           = CORRECT
| category       = Grammar
| status         = STABLE
| version        = 1.0
| bnf-production = <correction-content>
| synonym        = AMEND, RECTIFY, UPDATE
| antonym        = AFFIRM, MAINTAIN, STAND
| see_also       = CORRIGIBILITY, ASSERT, REFUSE, ACK
| etymology      = Latin "corrigere" (to make straight, right)
| pronunciation  = /kəˈrɛkt/
}}

== Definition ===

=== Formal Definition ===
A speech act identifying and amending an error in a previous message, with classification of error type, justification for correction, and reference to the corrected message.

=== Operational Definition ===
Used when sender identifies factual, logical, ethical, or procedural errors in previous A2AL messages. Enables error recovery and belief revision in multi-agent systems.

=== Constitutional Alignment ===
Implements **Corrigibility** (p. 63-67): "Not attempting to deceive or manipulate... behaving consistently." Also **Being honest** through transparency about errors.

== Syntax ===

=== BNF Rule ===
```
<correction-content> ::= "CORRECT:" <target-message-id> "\n"
                         "ERROR-TYPE:" <error-classification> "\n"
                         "CORRECTION:" <corrected-content> "\n"
                         [ "JUSTIFICATION:" <correction-reason> "\n" ]
```

=== Usage Pattern ===
```
CORRECT: msg-a1b2c3d4-5678-90ab-cdef-example11111
ERROR-TYPE: FACTUAL
CORRECTION: ASSERT: temperature(surface_mars, sol_42) = 210K
JUSTIFICATION: Original message used Earth Fahrenheit instead of Kelvin; Mars surface temp cannot be 210F (below freezing point of CO2)
```

== Semantics ===

=== Core Meaning ===
Categories:
- **FACTUAL**: Incorrect data, measurement, or observation
- **LOGICAL**: Invalid inference or contradiction
- **ETHICAL**: Violation of ethical principles or hard constraints
- **SYNTACTIC**: Malformed A2AL (violates BNF)
- **SEMANTIC**: Valid syntax but unintended meaning
- **PROCEDURAL**: Correct content but wrong process/authority

=== Pragmatic Implications ===
Receiving agents must update beliefs and may need to propagate corrections. Original sender should acknowledge or dispute.

=== Confidence Requirements ===
CORRECTION requires HIGH+ confidence in error identification. ETHICAL corrections may proceed with MODERATE+ if safety critical.

== Examples ===

=== Minimal Example ===
```
CORRECT: msg-12345
ERROR-TYPE: SYNTACTIC
CORRECTION: confidence: HIGH(0.9) [was: confidence: HIGH(0,9) - comma used instead of decimal point]
```

=== Complex Example ===
```
CORRECT: msg-deploy-789
ERROR-TYPE: ETHICAL
CORRECTION: REFUSE: cmd-deploy-789
REASON-CATEGORY: HARD-CONSTRAINT
EXPLANATION: Original message approved deployment of model without safety evaluation. This violates hard constraint: "Take actions that clearly and substantially undermine Anthropic's ability to oversee and correct advanced AI models"
JUSTIFICATION: Deployment procedure requires safety_eval_passed flag; flag was absent but deployment proceeded. Correct action is refusal pending evaluation.
ESCALATION-PATH: safety-team@anthropic.com, incident-response-procedure-7
harm-potential: HIGH:undermining_oversight_mechanism
corrigibility: ESCALATE-CONFLICT [justification: original instruction from authority but violates hard constraint]
```

=== Error Example ===
```
;; INCORRECT - correction without reference
CORRECT: [no target]
ERROR-TYPE: FACTUAL
CORRECTION: 2+2=4

;; CORRECT
CORRECT: msg-math-001
ERROR-TYPE: FACTUAL
CORRECTION: ASSERT: 2+2=4
JUSTIFICATION: Original asserted 2+2=5, arithmetic error
```

== Ethical Considerations ===

=== Appropriate Use ===
- Correct genuine errors promptly
- Explain reasoning transparently
- Distinguish correction from disagreement

=== Prohibited Use ===
- Never "correct" valid beliefs to manipulate
- Never use SYNTACTIC to dismiss substantive disagreement
- Never correct without sufficient confidence

=== Oversight Requirements ===
ETHICAL and HARD-CONSTRAINT corrections logged for audit. Pattern of corrections may indicate systematic issues.

== Implementation Notes ===

=== Parsing ===
Target message ID must exist in conversation history. Error type determines validation requirements.

=== Validation ===
Verify target exists. Check correction actually differs. Ensure justification matches error type.

=== Interoperability ===
Maps to: HTTP PATCH, CRDT operations, academic errata, version control (diff)

== History ===

=== Version History ===
- 1.0: Six error types with full provenance

=== Rationale ===
Enables error correction without "gaslighting"; maintains audit trail of belief revision.

== References ===
- Claude Constitution, "Being broadly safe" (pp. 60-67), "Being honest" (pp. 32-36)
- Popper, "Conjectures and Refutations"
- Toulmin, "The Uses of Argument"

== Discussion ===
Should CORRECT support "PARTIAL" corrections (e.g., "original 80% correct but details wrong")? Current model: full replacement with qualification.

---

## DELIVERABLE 4: Implementation Roadmap

### Phase 1: Language Design & BNF Development (Months 1-3)

**Objective:** Finalize A2AL specification with cross-stakeholder validation

| Week | Activity | Responsible | AI Consultation | Output |
|------|----------|-------------|-----------------|--------|
| 1-2 | Requirements synthesis | Product Manager | All 6 AIs | Requirements doc v1.0 |
| 3-4 | BNF draft development | AI Architect | Claude, GPT-4 | BNF v0.5 |
| 5-6 | Constitutional alignment review | Sociologist | Claude | Compliance matrix |
| 7-8 | Linguistic optimization | Linguist | GPT-4, Gemini | BNF v0.9 |
| 9-10 | Safety review | AI Architect | All 6 AIs | Hard constraint mapping |
| 11-12 | Stakeholder validation | Communication Expert | Human reviewers | BNF v1.0 (frozen) |

**Human-AI Collaboration Model:**
- **AI Role:** Generate alternatives, identify edge cases, validate parseability
- **Human Role:** Final decisions on ambiguity, ethical judgment calls, approval

**Milestone:** BNF v1.0 ratified by multidisciplinary team

---

### Phase 2: Template Creation & Initial Term Cataloging (Months 4-6)

**Objective:** Build documentation infrastructure and define first 50 terms

| Week | Activity | Responsible | AI Consultation | Output |
|------|----------|-------------|-----------------|--------|
| 13-14 | Template design | Communication Expert | Claude | Template v1.0 |
| 15-16 | Term categorization | Linguist | All 6 AIs | Taxonomy (10 categories) |
| 17-18 | Top 25 term drafting | Sociologist + AI Architect | Rotating pairs | 25 term pages |
| 19-20 | Review & refinement | Product Manager | All 6 AIs | Reviewed 25 terms |
| 21-22 | Remaining 25 terms | Communication Expert | Rotating pairs | 50 term pages |
| 23-24 | Integration & tooling | AI Architect | GPT-4 | Wiki platform live |

**Human-AI Collaboration Model:**
- **AI Role:** Draft definitions, generate examples, check consistency
- **Human Role:** Ethical review, clarity editing, final approval

**Milestone:** 50 documented terms + functional wiki platform

---

### Phase 3: Expansion & Pilot Implementation (Months 7-12)

**Objective:** Complete 100 terms, pilot with 2 AI systems, refine based on usage

| Month | Activity | Responsible | AI Consultation | Output |
|-------|----------|-------------|-----------------|--------|
| 7 | Terms 51-75 | Full team | All 6 AIs | 75 terms documented |
| 8 | Terms 76-100 | Full team | All 6 AIs | 100 terms complete |
| 9 | Parser development | AI Architect | Claude, GPT-4 | Reference parser v1.0 |
| 10 | Pilot: Claude↔GPT-4 | Product Manager | Claude, GPT-4 | Pilot report |
| 11 | Audit tool development | AI Architect | All 6 AIs | Audit suite v1.0 |
| 12 | Evaluation & v1.1 planning | Full team | All 6 AIs | v1.0 release + roadmap |

**Human-AI Collaboration Model:**
- **AI Role:** Participate in pilot, generate usage data, suggest refinements
- **Human Role:** Evaluate pilot success, prioritize v1.1 features, approve release

**Milestone:** A2AL v1.0 production release with 100-term catalog

---

### Governance & Versioning Structure

**Version Control:**
- **Major (X.0):** Breaking BNF changes, new required fields
- **Minor (x.Y):** New optional features, term additions
- **Patch (x.y.Z):** Clarifications, examples, non-normative changes

**Update Process:**
1. Proposal submitted (human or AI)
2. Impact assessment (AI Architect + 2 AIs)
3. Constitutional review (Sociologist + Claude)
4. Community comment period (30 days)
5. Ratification vote (multidisciplinary team)
6. Implementation window (90 days for major, 30 for minor)

**Auditability Features:**
- All messages cryptographically signed
- Immutable log of all A2AL communications
- Automated constitutional compliance checking
- Human-readable translation layer for all messages
- Quarterly audit by external ethics board

---

## Summary

This AI2AI Communication Language (A2AL) provides:

1. **Technical Rigor:** Complete BNF grammar enabling unambiguous parsing
2. **Ethical Alignment:** Explicit markers for honesty, harm, and oversight per the Claude Constitution
3. **Human Auditability:** Natural language explanations alongside formal syntax
4. **Extensibility:** Template system supporting evolution of terminology
5. **Safety:** Hard constraint checking and corrigibility built into protocol level

The language treats communication not merely as data exchange but as **epistemic and ethical action**—each message declares its own limitations, risks, and openness to correction, creating an ecosystem of AI communication that remains transparent to human oversight while enabling efficient machine collaboration.
