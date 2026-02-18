
# Burp Suite Intruder – Attack Type Methodology & Decision Framework

---

# 0. Summary

1. [Objective](#objective)
2. [Pre-Execution Controls & Safeguards](#pre-execution-controls--safeguards)
3. [Attack Escalation Strategy](#attack-escalation-strategy)
4. [Attack Selection Decision Tree](#attack-selection-decision-tree)
5. [Attack Type Definitions & Execution Models](#attack-type-definitions--execution-models)

---

# 1. Objective

This document defines a methodology for selecting and executing Intruder attack types during **authorized** web application security assessments.

---

# 2. Pre-Execution Controls & Safeguards

Before selecting an attack type:

1. Estimate request count.
2. Confirm brute-force authorization.
3. Assess rate limiting.
4. Monitor for account lockout.
5. Log evidence properly.
6. Configure appropriate request throttling settings.

---

# 3. Attack Escalation Strategy

Methodology recommends escalation:

1. Begin with Sniper to **identify response behavior**.
2. Use Battering Ram when **duplication logic** is suspected.
3. Apply Pitchfork for **known credential pairs**.
4. Escalate to Cluster Bomb only when justified and authorized, as this mode may **significantly increase request volume**.

---

# 4. Attack Selection Decision Tree

```
                        ┌────────────────────────────┐
                        │  What are you testing?     │
                        └──────────────┬─────────────┘
                                       │
                    ┌──────────────────┴──────────────────┐
                    │                                     │
        ┌───────────▼───────────┐             ┌──────────▼──────────┐
        │ Single parameter only?│             │ Multiple parameters? │
        └───────────┬───────────┘             └──────────┬──────────┘
                    │ Yes                                  │ Yes
                    ▼                                      ▼
           ┌───────────────────┐              ┌────────────────────────────┐
           │ Use SNIPER        │              │ Do parameters need         │
           │                   │              │ identical values?          │
           └───────────────────┘              └──────────────┬─────────────┘
                                                             │
                                            ┌────────────────┴───────────────┐
                                            │                                │
                                           Yes                               No
                                            │                                │
                                            ▼                                ▼
                                ┌────────────────────┐        ┌────────────────────────────┐
                                │ Use BATTERING RAM  │        │ Are values correlated?     │
                                │ (same payload      │        │ (e.g., known pairs)        │
                                │ everywhere)        │        └──────────────┬─────────────┘
                                └────────────────────┘                       │
                                                                      ┌───────┴────────┐
                                                                      │                │
                                                                     Yes               No
                                                                      │                │
                                                                      ▼                ▼
                                                         ┌──────────────────┐   ┌─────────────────────┐
                                                         │ Use PITCHFORK    │   │ Use CLUSTER BOMB    │
                                                         │ (parallel lists) │   │ (all combinations)  │
                                                         └──────────────────┘   └─────────────────────┘
```

---

# 5. Attack Type Definitions & Execution Models

---

## 5.1 Sniper Attack

### Purpose

Tests a **single injection position** sequentially using one payload set.

### Target Example

```
username=§user§
```

### Payload Set (Single List)

```
payload1
payload2
payload3
payload4
payload5
payload6
```

### Execution Model

|Request|Payload|Request Sent|
|---|---|---|
|1|payload1|username=payload1|
|2|payload2|username=payload2|
|3|payload3|username=payload3|
|4|payload4|username=payload4|
|5|payload5|username=payload5|
|6|payload6|username=payload6|

### Request Volume Formula

N

### Use Cases

 - Testing single parameter behavior
 - Username enumeration
 - Initial response pattern analysis

### Operational Risk

Low (linear execution)

---

## 5.2 Battering Ram Attack

### Purpose

Injects the **same payload** into **multiple positions** simultaneously.

### Target Example

```
username=§user§&password=§password§
```

### Execution Model

|Request|Payload|Request Sent|
|---|---|---|
|1|payload1|username=payload1&password=payload1|
|2|payload2|username=payload2&password=payload2|
|3|payload3|username=payload3&password=payload3|
|4|payload4|username=payload4&password=payload4|
|5|payload5|username=payload5&password=payload5|
|6|payload6|username=payload6&password=payload6|

### Request Volume Formula

N

### Use Cases

 - Testing identical credentials
 - Scenarios where parameters are expected to match

### Operational Risk

Low

---

## 5.3 Pitchfork Attack

### Purpose

Iterates through **multiple payload sets in parallel** (index-based).

### Target Example

```
username=§user§&password=§password§
```

### Payload Sets

**Set 1**

```
set1_item1
set1_item2
set1_item3
```

**Set 2**

```
set2_item1
set2_item2
set2_item3
```

### Execution Model

|Request|Username|Password|
|---|---|---|
|1|set1_item1|set2_item1|
|2|set1_item2|set2_item2|
|3|set1_item3|set2_item3|

### Request Volume Formula

min(N1, N2, ..., Nn)

### Use Cases

 - Testing known username/password pairs
 - Validating parameter dependencies

### Operational Risk

Moderate

---

## 5.4 Cluster Bomb Attack

### Purpose

Tests **all possible combinations** across multiple payload sets (cartesian product).

### Target Example

```
username=§user§&password=§password§
```

### Execution Model (Example)

|Request|Username|Password|
|---|---|---|
|1|set1_item1|set2_item1|
|2|set1_item1|set2_item2|
|3|set1_item1|set2_item3|
|4|set1_item2|set2_item1|
|5|set1_item2|set2_item2|
|6|set1_item2|set2_item3|

### Request Volume Formula

N1 × N2

### Use Cases

 - Assessment of authentication control robustness

### Operational Risk

High (exponential growth potential)