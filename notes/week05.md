# Week 5 notes

## Lecture 5: System Failures (L5) (PRIORITY)

### Definitions (L5 s4)
- System: a regularly interacting or interdependent group of items forming a unified whole
- Failure: the state or condition of not meeting a desirable or intended objective

### Reasons for information system implementation (L5 s5)
- to increase productivity in order to maintain competitive advantage
- to re-engineer a process for efficiency
- adapt to a change in existing process
- introduce a new process

### Classification of system failures (4) (L5 s6) (reference: Lyytinen and Hirschheim, 1987)
- Process failure: an information system project cannot be developed within an allocated budget and/or time schedule
- Correspondence failure: when the objectives/goals of the systems design are not met
- Interaction failure: attributed to the level of end-user usage or adoption or acceptance of the implemented information system
- Expectation failure: inability of a system to meet its stakeholders' requirement, expectations or values

### Types of system failures (3) (L5 s7)
- Partial: failure of one or more components to impede the operation of a system
- Total: failure of one or more components that causes a system to stop working temporarily or permanently
- Catastrophic: failure of one or more components that renders the system irrecoverable

### Normal Accident (L5 s9) (reference: Perrow, 1999, Normal Accidents: Living with High Risk Technologies)
- "Normal Accident": complexity + tight interaction = catastrophic potential
- Complex: linear is simple, one thing then another; complex has multiple routes
- Tightly Coupled: interacting elements with no 'buffer' or delay possible

### Causes of system failures (6) (L5 s10, s17; "six primary reasons" L5 s3)
- poor development practices
- incorrect assumptions
- poor user interface
- faulty hardware
- inadequate user training (or user error) (s10 wording; s17 says "inadequate user training")
- poor fit between system and organisation

### Detail per cause
- Poor Development Practices (L5 s11): complexity of projects means poor specification, poor design, poor testing. Links only: NY Times 1993 Titan lost payload spy satellite system worth 800 million (URL title, dated 1993/08/04); LA Times 1999/06/18 article
- Incorrect Assumptions (L5 s12): development team guess, or don't check. Link only: NASA JPL Mars (mars.jpl.nasa.gov/msp98/news/mco990930.html)
- Poor User Interface (L5 s13): if the interface is poorly designed, user errors get introduced
- Faulty Hardware (L5 s14): difficult to guard against faulty hardware; no excuse for faulty code
- Inadequate User Training (L5 s15):
  - if a user is improperly trained then the likelihood of them making serious errors is increased due to their lack of knowledge of the system
  - bad training = loss of data integrity
  - incorrect data input from a bad interface can be considered errors
  - failures due to a lack of training are not errors, they are mistakes by management
- Poor Fit Between System and Organisation (L5 s16): often driven by cost; poor specification

### Safety critical systems (L5 s19)
- fail-safe failure mode(s)
- graceful degradation on failure of sub-system
- multiple backups using dissimilar systems/hardware/software
- rigorous testing
- rigorous external independent oversight of: specification; design; testing; approval; implementation; operation processes; maintenance (especially any changes to above)

### Reasons for failure (L5 s20)
- People: Poor training; Not following procedures before / during / after; Stress / pressure before / during / after
- Organisational culture: blame / aggressive leadership who can't be queried; pressure / unreasonable deadlines / political deadlines; too expensive to contemplate (failure scenario / remedy); top management kept in dark
- No clear responsibility for dealing with failure: different agendas/skills/perspectives/reasons for 'cover-up'; who pays...?; unwillingness to take legal responsibility
- Large projects have a momentum of their own
- Failures/bureaucracy of internal/external 'independent' regulators

### Case study 1: Kegworth Aircrash (L5 s22)
- Evening of 8th January 1989; British Midland Airways flight BD092 (Boeing 737-400); took off from Heathrow
- Approx 5 minutes into flight, pilots noticed shaking of aircraft frame; unbeknown to the crew a fan blade in engine #1 had fractured
- Following procedure, captain took plane off autopilot, asked first officer which engine was causing the problem; after some hesitation first officer replied engine #2
- Engine #2 throttled back, resulting in shutdown of one of the functioning engines
- Cleared for emergency landing at East Midlands Airport; lost altitude rapidly; crashed into the M1 motorway
- Slide wording: "loss of 47 of the 126 passengers on board"

### Case study 2: Three Mile Island (L5 s23)
- Morning of 28th March 1979; secondary, non-nuclear part experienced a mechanical failure causing the main-feed water pump to stop running, firing a chain of events ending in partial nuclear meltdown
- Water cooling steam generators automatically shut down; reactor pressure rose
- No means of cooling (auxiliary water feeds shut for maintenance); entered emergency shutdown routine
- To relieve pressure an operator triggered the pilot-operated relief valve, which releases coolant; it also suffered mechanical failure, causing the valve to remain open
- The light indicating valve position (open/closed) only reflected the command sent, not the valve state

### Case study 3: Therac-25 (L5 s24)
- Radiation therapy machine; software bug resulted in massive radiation overdoses administered to 6 people
- A software "race condition" caused the mechanical interlock (which applies the x-ray filter) to fail
- When operator provided a manual input at a particular time the interlock would fail and the dose would not be recorded
- One session: machine paused displaying "HTILT"; display showed "NO DOSE"; operator pressed the "proceed" key; repeated 4 times, each time "NO DOSE"
- Patient complained of burning sensation in her hip; died a month later of the cancer they were trying to prevent; autopsy: would have needed full hip replacement due to radiation exposure

### Further reading / references (L5 s25-s26)
- Lyytinen, K. and Hirschheim, R., 1987. Information Systems Failures - A Survey and Classification of the Empirical Literature. Oxford Surveys in IT, Vol. 4, pp. 257-309
- Perrow, C., 1999. Normal Accidents Living with High Risk Technologies
- Meadowcroft, B., n.d. Why Systems Fail

### Slide wording notes
- L5 s3 says "six primary reasons"; s10 and s17 both list six. s10 adds "(or user error)" to inadequate user training.
- L5 s19 says "dissimilar" backups (a test option may say "similar", which is wrong).
- L5 s22: "loss of 47 of the 126 passengers" (slide wording; does not say crew).
- L5 s7: slide text "one of more" (typo for one or more).
- L5 s15 tension: bad interface input "can be considered errors" vs training failures "are not errors, they are mistakes by management".
- L5 s11 and s12 give no costs or dates in text; only URL titles hint at them.
