# Errata

This file lists the known errors in the paper by Mert Torun, "Ensuring Functional Equivalence in Retrofitted Anti-Skid Systems for European Public Transportation: A Hybrid Two-Layer Verification Methodology", Kölner Beiträge zur technischen Informatik (Cologne Contributions to Computer Engineering), Band 2/2026, TH Köln, published on Cologne Open Science, DOI [10.57684/COS-1494](https://doi.org/10.57684/COS-1494), URN urn:nbn:de:hbz:832-cos4-14942.

This repository keeps the deposited file, byte-identical with the one the library holds (10 pages, SHA-256 `bcf68b4b845c68ab48b43c1d91c855af7f8aac18f7a7a0846a43210ca66a3ebf`). It stays unchanged; the corrections apply through this list only. Page numbers are those printed on the pages and equal the PDF page numbers; pages 1 and 2 are the series cover and the imprint and carry no number. [n] is reference n of the paper. Among the cited sources, [10], [11] and [28] are unpublished project reports: [10], an internship documentation of 2023; [11], the report of the follow-on student project dated 8 August 2025, cited by its own printed page numbers; [28], the report on the test fixture of 2023. "Project files" are the unpublished design files and records of the project: the schematics, board files and bills of materials of Rev 0.0 and Rev 1.0, the VHDL sources and test benches and the STM32 firmware sources of 2023, and the original schematic of the legacy board with a firmware image kept with it.

Each entry quotes the deposited text verbatim; words divided at a line end are joined, and the narrow space the print sets between a number and its unit is written as a space. The class is one of: typographical; factual, not affecting results; affecting a result; attribution; reference could not be traced; claim not supported by the work's evidence. Errors not listed here can be reported with the issue form Correction or by e-mail to info@mtorun0x7cd.com, the address printed on page 3 of the paper, giving the page and the passage.

## 1. Errata

### P-E001

- **Location:** p. 3 (PDF p. 3), Abstract.
- **Quoted text:**
  - p. 3: "a two-layer verification methodology was developed, derived from the V-model as defined in IEC 61508 and IEEE 1012"
- **Correction:** IEEE 1012 is no longer named as a source of the V-model. Read: "derived from the V-model of IEC 61508, with verification and validation processes following IEEE 1012".
- **Class:** factual, not affecting results
- **Evidence:** IEEE Std 1012-2016, clause 1.1 (Scope), describes the standard as compatible with all life cycle models; the edition defines no V-model, and the term does not occur in it. The 2024 edition cited as [24] was not read; the IEEE SA page of that edition describes the working group's active project P1012 with the same sentence.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E002

- **Location:** p. 3 (PDF p. 3), Abstract; p. 7 (PDF p. 7), Section V-A, opening sentence and closing paragraph.
- **Quoted text:**
  - p. 3: "Through convergence of three independent evidence lines—simulation, oscilloscope measurement, and integrated scenario testing—functional equivalence of the safety-critical core was demonstrated for all documented fault codes, self-test sequences, and user interactions."
  - p. 7: "Functional equivalence of the safety-critical core was demonstrated through three converging lines of evidence:"
  - p. 7: "The convergence of these three independent lines of evidence—each addressing a distinct aspect of correctness (logical, physical, behavioural)—provides robust assurance of functional equivalence for the safety-critical core."
- **Correction:** The three lines are not independent evidence about the rebuilt unit. The oscilloscope captures date from 2023, before the rebuild ([P-E033](#p-e033)). The archived simulations are those of the 2023 design, whose test benches leave the NVRAM_ble signal unconnected and so could not show defect B1 ([P-E030](#p-e030)); no simulation after the correction of B1 is documented ([P-E038](#p-e038)). On the rebuilt unit, the follow-on project ran the fixture's test suite without an archived log, and several scenarios, among them the self-test, are not documented for that unit ([P-E035](#p-e035)). The three lines indicate functional equivalence of the safety-critical core; "was demonstrated" and "robust assurance" are not supported. Read in the Abstract: "Three lines of evidence (simulation, oscilloscope measurement and integrated scenario testing) indicate functional equivalence of the safety-critical core, but the evidence for the rebuilt unit is incomplete."
- **Class:** claim not supported by the work's evidence
- **Evidence:** the paper's own Fig. 3 (on-screen date 15 Aug 2023) and pp. 6 to 8; [10], Sections 4.6 and 4.10; [11], pp. 13 to 15; the archived VHDL test benches of 2023 (project files).
- **Found:** 2026-09-27
- **Reported:** not reported
- **Status:** Open. Held back until the author has informed the series editor (data provenance).

### P-E003

- **Location:** p. 3 (PDF p. 3), Section I, first paragraph; p. 4 (PDF p. 4), Section II-C; p. 9 (PDF p. 9), Section V-E, last sentence.
- **Quoted text:**
  - p. 3: "operators must simultaneously extend the operational life of proven infrastructure and comply with increasingly stringent safety standards [1], [2]."
  - p. 4: "further demonstrate the economic rationale for modernising safety-critical rolling stock [1]."
  - p. 9: "Board-level retrofits also align with UIC findings [1] that refurbishment reduces embodied CO2 compared to new manufacture."
- **Correction:** [1] carries none of the three statements and is withdrawn at all three places. The UIC report compares methods for calculating the carbon footprint of railway infrastructure; it contains no finding on refurbishment against new manufacture, nothing on safety standards and nothing on modernising rolling stock. On p. 3, [2] carries only the compliance with safety standards; on p. 4, the economic rationale stands with [19]; the sentence on p. 9 is withdrawn unless a source that makes this comparison is cited.
- **Class:** claim not supported by the work's evidence
- **Evidence:** [1] itself: UIC, "Carbon Footprint of Railway Infrastructure", subtitle "Comparing existing methodologies on typical corridors. Recommendations for harmonized approach", June 2016, ISBN 978-2-7461-2500-1. Its text contains none of "refurbish", "retrofit", "moderni", "upgrad" or "safety", and "embodied" occurs only for infrastructure projects in Great Britain. [19] reports the fleet owner's view that re-equipping the Class 455 fleet has a sound business case.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E004

- **Location:** p. 3 (PDF p. 3), Section I, second paragraph.
- **Quoted text:**
  - p. 3: "This paper addresses these challenges through a case study of a legacy anti-skid protection system [5], widely deployed across European urban rail networks."
- **Correction:** The only source given, [5], is the manual of the anti-skid system for the 1992/93 series of one light-rail vehicle, Stadtbahnwagen B; the work cites no source for a wide deployment across European networks. Read: "a legacy anti-skid protection system [5], documented for the 1992/93 series of a German light-rail vehicle".
- **Class:** claim not supported by the work's evidence
- **Evidence:** [5] as printed on p. 10 names a single vehicle series ("Serie 1992/93"); the manual itself is dated April 1992. [10], Section 1, dates the development of the system to the early 1980s.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E005

- **Location:** p. 3 (PDF p. 3), Section I, second paragraph.
- **Quoted text:**
  - p. 3: "Hardware-in-the-Loop (HIL) testing of complete braking systems [8]"
- **Correction:** In [8], only the bogie brake control unit is physical hardware; the vehicle, its running environment, the electric brake unit and the pneumatic valve unit are simulated. Read: "HIL testing of braking and anti-skid control units [8]".
- **Class:** claim not supported by the work's evidence
- **Evidence:** [8], p. 155 (abstract): an industrial PC provides a virtual train vehicle, running environment, electric brake unit and pneumatic valve unit around the physical brake control unit.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E006

- **Location:** pp. 3 to 4 (PDF pp. 3 to 4), Section I, contributions (a) to (c); p. 8 (PDF p. 8), Section V-B; p. 9 (PDF p. 9), Section VI.
- **Quoted text:**
  - p. 3: "failing to detect latent state anomalies (such as inactive memory interfaces)"
  - p. 3: "We prove that relying on either paradigm in isolation compromises safety-critical assurance."
  - p. 3: "By establishing mathematical and temporal correspondence between pre-synthesis simulation, JTAG boundary-scan, physical measurements, and automated, YAML-defined system-level scenario execution, the framework systematically closes the diagnostic blind spot."
  - p. 3: "(c) Empirical Proof via Bug Classification: We provide a detailed taxonomic classification of five distinct classes of hardware, firmware, and logical integration defects discovered during validation. This serves as an empirical validation of the diagnostic capabilities"
  - p. 8: "The results empirically demonstrate that neither verification layer alone is sufficient to ensure safety-critical functional equivalence."
  - p. 8: "Structural verification and boundary-scan diagnostics (Layer 1) successfully isolated the NVRAM chip-enable error (B1), the incorrect SWD pin routing (B2), and the FPGA solder joint assembly defects (B3)."
  - p. 8: "Layer 1 verifies structural correctness and exposes latent bugs that escape functional testing"
  - p. 9: "the methodology establishes the rigorous diagnostic depth required to definitively prove functional equivalence with the original legacy system."
- **Correction:** The proof claims are withdrawn. They rest on the assignment of defects B1 to B3 in Table II, which the cited source [11] does not support: B1 showed on the test fixture, that is in Layer 2 ([P-E030](#p-e030)); B2 concerns the test fixture, not the retrofitted board ([P-E011](#p-e011)); for B3, [11] names neither JTAG nor boundary scan and does not say how the solder faults were noticed ([P-E010](#p-e010)). The example in contribution (a), inactive memory interfaces that system-level testing fails to detect, is B1, which the fixture test showed at the board boundary; the statement in Section V-B that Layer 1 exposes latent bugs that escape functional testing is withdrawn with it. The defects documented in [11] were found in 2025 by the follow-on project while bringing up and debugging the test fixture and the rebuilt board, partly with tools of the method, not in a planned run of the two-layer method; on B4 and B5 see [P-E042](#p-e042). What remains is the weaker observation that no single method found all of the documented defects. Contribution (b) no longer names boundary scan as a tool against the solder faults and claims no mathematical correspondence; formal methods are outside the scope of the work (p. 9). Table II becomes a retrospective classification of the findings in [11], giving for each defect who found it, when and how; Section V-B and the Conclusion rest on that classification, and insofar as the lesson on design for debuggability (p. 9) rests on B2, it rests on a defect of the test fixture.
- **Class:** affecting a result
- **Evidence:** [11], pp. 10 to 14 and 21; the paper's own p. 9 ("Residual Scope Gaps"); the entries named above.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open. Held back until the author has informed the series editor (data provenance).

### P-E007

- **Location:** p. 3 (PDF p. 3), Section I, contribution (b); p. 7 (PDF p. 7), Section IV-C.
- **Quoted text:**
  - p. 3: "automated, YAML-defined system-level scenario execution"
  - p. 7: "A Python application orchestrates test execution in a semi-automated workflow"
- **Correction:** In contribution (b), read "semi-automated". The workflow prompts the operator for manual checks, as Section IV-C states.
- **Class:** factual, not affecting results
- **Evidence:** the paper's own p. 7 (the application "prompts the operator for manual checks").
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E008

- **Location:** p. 3 (PDF p. 3), Section I, contribution (c); p. 8 (PDF p. 8), Section V-B, first paragraph, and Table II.
- **Quoted text:**
  - p. 3: "five distinct classes of hardware, firmware, and logical integration defects"
  - p. 8: "revealed five distinct integration bugs across the hardware, firmware, and logical design domains"
- **Correction:** The list is incomplete. [11] documents a further defect of the rebuilt board: the two 7-segment displays were swapped, and this was corrected in the VHDL top level; a loose contact at both displays was recorded as unresolved. Of the five defects listed, B2 does not concern the device under test ([P-E011](#p-e011)). Correction: the display defect is added to Table II with source [11], and the count follows.
- **Class:** factual, not affecting results
- **Evidence:** [11], p. 13 (section on the 7-segment displays).
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E009

- **Location:** p. 4 (PDF p. 4), Section II-A.
- **Quoted text:**
  - p. 4: "Foundational reverse engineering by Ayoub [9] demonstrated the feasibility of FPGA emulation for the MCS-48 CPU."
- **Correction:** The work report that fits [9] ([P-E047](#p-e047)) used, on the comparator card, an FPGA-emulated 8-bit CPU taken over from an earlier project; it does not name the MCS-48, and at the time of the report the card was still in basic function testing. Read: "[9] used an FPGA emulation of the comparator card's 8-bit CPU, taken over from an earlier project". That these boards, the comparator card included, are based on the MCS-48 is stated in [10].
- **Class:** claim not supported by the work's evidence
- **Evidence:** the work report, pp. 5 and 10; [10], Section 1.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E010

- **Location:** p. 4 (PDF p. 4), Section II-A; p. 6 (PDF p. 6), Section IV-B 2); p. 7 (PDF p. 7), Section V-A 2); p. 8 (PDF p. 8), Table II (row B3) and Section V-B; p. 9 (PDF p. 9), Section VI.
- **Quoted text:**
  - p. 4: "approximately 40 FPGA pins required re-soldering"
  - p. 6: "This technique proved particularly valuable for diagnosing the approximately 40 FPGA pins that required re-soldering: boundary scan could rapidly identify open or bridged connections without requiring functional firmware execution."
  - p. 7: "This phase included extensive rework—approximately 40 FPGA pins required re-soldering for stable operation [11]."
  - p. 8: "B3 Assembly Approx. 40 FPGA pins open or shorted L1 JTAG / Scope Reworked"
  - p. 8: "the physical assembly faults (B3) caused intermittent system crashes that were impossible to isolate or root-cause without Layer 1 boundary-scan tools."
  - p. 9: "the re-soldering of roughly 40 FPGA pins"
- **Correction:** According to [11], during bring-up of the rebuilt board in 2025 the CPU did not respond to the reset signal and the flash addresses did not count up. Four poorly soldered FPGA pins were noticed during testing and re-soldered; when the addresses still did not count, about 40 more pins were re-soldered, after which the board could be switched on. The oscilloscope confirmed supply and clock; [11] does not say how the solder faults were noticed, and mentions neither JTAG, boundary scan nor short circuits. The symptom was a board that did not start, not intermittent crashes. The author's research report as submitted in 2025 states that the JTAG checks could not detect the poor solder joints. Correction: B3 was noticed while testing during bring-up, source [11]; "JTAG", "shorted", the sentence on the value of boundary scan for these pins and the sentence on intermittent crashes are withdrawn; "approximately 40", and "roughly 40" in Section VI, read "four, then about 40 more".
- **Class:** affecting a result
- **Evidence:** [11], p. 13; [11] contains no occurrence of "JTAG", "boundary" or "scan"; the author's research report as submitted in August 2025 (unpublished), Chapter 5, on the JTAG checks.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open. Held back until the author has informed the series editor (data provenance).

### P-E011

- **Location:** p. 4 (PDF p. 4), Section II-A; p. 8 (PDF p. 8), Table II (row B2), Section V-B and Section V-D.
- **Quoted text:**
  - p. 4: "the STM32 debug interface was blocked by a pin assignment error"
  - p. 8: "B2 Layout STM32 SWD debug pins routed incorrectly L1 Boundary-Scan Reworked"
  - p. 8: "After re-routing the STM32 Serial Wire Debug (SWD) pins and debugging the firmware state machine [11], diagnostic data routing was validated via USB serial streaming"
- **Correction:** In [11], the STM32 project that could not be debugged because PA13 and PA12 were assigned as GPIOs, and the fault in the firmware state machine, both belong to the test fixture [28]. The project is named "test-diagnosekarte-2024" in [11], but it is described under the heading on debugging the test fixture, together with the fixture's own firmware functions, and the only PCB redesigned was the fixture's. [28] assigns PA12, PA13 and PA14 of the fixture's STM32 board to fixture signals. On the retrofitted board, PA13 and PA14 of the STM32 run to its SWD header in Rev 0.0 and in Rev 1.0 alike. B2 is therefore not a defect of the device under test. Nor could the boundary scan the paper describes, that of the FPGA on the Base Board (p. 4), observe the STM32, which sits on the galvanically isolated diagnostics board (Fig. 1). Correction: B2 is marked as a defect of the test fixture or removed from Table II; Sections II-A and V-D accordingly.
- **Class:** affecting a result
- **Evidence:** [11], pp. 10 and 12, and p. 22, item 9 (only the fixture's PCB redesigned); [28], Table 7 (p. 23); schematics of Rev 0.0 as ordered and of Rev 1.0 (project files): nets SWD_TMS on PA13 and SWD_TCK on PA14 to the header X14, labelled "SWD".
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open. Held back until the author has informed the series editor (data provenance).

### P-E012

- **Location:** p. 4 (PDF p. 4), Section II-B, last item.
- **Quoted text:**
  - p. 4: "Combined approaches: Practice typically dictates layered strategies [15], [16], using white-box techniques for component verification and black-box methods for system validation."
- **Correction:** [16] reviews how a formal specification can be used to support testing; it does not carry a layered practice of white-box component tests and black-box system tests. [15] could not be traced ([P-E046](#p-e046)). The sentence stands without these two references, or with a work that carries it.
- **Class:** claim not supported by the work's evidence
- **Evidence:** [16], abstract, which states the article's subject as the ways in which a formal specification can assist testing; DOI 10.1145/1459352.1459354.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E013

- **Location:** p. 4 (PDF p. 4), Section II-C.
- **Quoted text:**
  - p. 4: "The Wabtec/SNCF adaptive wheel-slide protection project [17] achieved certification against EN 15595 [18] through HIL testing."
- **Correction:** The press release [17] of 6 December 2022 reports laboratory tests at an accredited laboratory, trials on a test bench that simulated very low adhesion, and tests in operation on an SNCF train; it does not mention hardware-in-the-loop testing. Read: "achieved certification against EN 15595 [18] after laboratory tests, test-bench trials and tests in operation [17]".
- **Class:** claim not supported by the work's evidence
- **Evidence:** [17] at <https://www.wabteccorp.com/newsroom/press-releases/wabtec-s-innovative-adaptive-wheel-slide-protection-solution-gains-certification>, read on 2026-09-24.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E014

- **Location:** p. 4 (PDF p. 4), Section II-C.
- **Quoted text:**
  - p. 4: "Fleet-level electronics upgrades such as the UK Class 455 [19] and Greater Anglia Class 317 [20] further demonstrate the economic rationale for modernising safety-critical rolling stock [1]."
- **Correction:** The article [20] reports a refresh of the Class 317 interiors (seat covers, flooring, carpets, paint, signage and cleaning) and the operator's plan to replace its entire fleet with new trains; it is not an example of an electronics upgrade. [20] is withdrawn from this sentence, which stands with [19]; on [1] see [P-E003](#p-e003).
- **Class:** claim not supported by the work's evidence
- **Evidence:** [20] at its current address (see [Updates](#3-updates)); [19] in its archived copy of April 2013 ([P-E049](#p-e049)).
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E015

- **Location:** p. 4 (PDF p. 4), Section II-D; p. 8 (PDF p. 8), Table III.
- **Quoted text:**
  - p. 4: "EN 50716 [22] (software/HDL modification)"
  - p. 8: "EN 50716 [22] SW/HDL modification L1 + L2"
- **Correction:** EN 50716 applies exclusively to software and, for the development of user-programmable integrated circuits such as FPGAs, refers to EN 50129:2018, Annex F. "HDL" is withdrawn at both places; the unchanged firmware running on the emulated core stays within the scope of EN 50716.
- **Class:** factual, not affecting results
- **Evidence:** EN 50716:2023, clauses 1.2 and 1.10 (scope).
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E016

- **Location:** p. 4 (PDF p. 4), Section II-D, last sentence, and Section III-A, first paragraph.
- **Quoted text:**
  - p. 4: "Using FPGAs in safety-critical applications introduces certification considerations including tool confidence, verification depth, and IP core validation [3], [25]."
  - p. 4: "chosen for its flash-based non-volatile configuration (inherent resistance to soft errors compared to SRAM alternatives [25])"
- **Correction:** [25] could not be traced ([P-E046](#p-e046)). For the flash-based FPGA, [3] carries the statement, restricted to the configuration memory: in flash-based FPGAs the configuration memory is insensitive to radiation effects, while the user memory can be affected. [3] does not address tool confidence, verification depth or certification; it carries only the need to show that FPGA-emulated components reach the dependability of the components they replace. Correction: in Section III-A, [3] with this restriction; in Section II-D, the sentence limited to what [3] carries.
- **Class:** claim not supported by the work's evidence
- **Evidence:** [3], its classification of FPGA technologies and its introduction.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E017

- **Location:** p. 4 (PDF p. 4), Section III and Section III-A; p. 5 (PDF p. 5), Section III-C.
- **Quoted text:**
  - p. 4: "four-Printed Circuit Board (PCB) architecture"
  - p. 4: "An Serial Peripheral Interface (SPI) master"
  - p. 4: "brown-out detection (Brown-Out Detection (BOD)) supervision"
  - p. 5: "The subsystem features an Real-Time Clock (RTC)"
  - p. 5: "a Secure Digital I/O (Secure Digital Input/Output (SDIO)) interface"
- **Correction:** Read "four-PCB architecture"; "A Serial Peripheral Interface (SPI) master"; "brown-out detection (BOD) supervision"; "a Real-Time Clock (RTC)"; "a Secure Digital Input/Output (SDIO) interface".
- **Class:** typographical
- **Evidence:** the paper's own text.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E018

- **Location:** p. 4 (PDF p. 4), Section III-A.
- **Quoted text:**
  - p. 4: "The FPGA runs an MCS-48 emulation core (adapted from the OpenCores t48_core)"
- **Correction:** The core is taken over without changes. Read: "an MCS-48 emulation core (the OpenCores t48 core, release rel_1_2, integrated without changes to the core)".
- **Class:** factual, not affecting results
- **Evidence:** comparison of the project's VHDL sources (project files) with OpenCores t48, release rel_1_2: in one archived version of the design, 47 of the 48 files it shares with the release are byte-identical, and the one that differs is a system-level RAM model with an added reset port; in the later version, all 46 shared files are identical. [10], Section 2.10, states that the code was taken from OpenCores.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E019

- **Location:** p. 4 (PDF p. 4), Section III-A.
- **Quoted text:**
  - p. 4: "executing the original 2 kB firmware binary from external flash ROM"
- **Correction:** The size is not established. The original schematic shows an MM2716 EPROM of 2 KiB, but [10] speaks of the EPROMs of the original board in the plural, and the firmware image kept in the project files contains data up to address 0x0B8E, beyond 2 KiB; whether that image is exactly the firmware of the original board can no longer be confirmed. Read: "the original firmware binary", without a size.
- **Class:** claim not supported by the work's evidence
- **Evidence:** the original schematic of the test-diagnosis board (project files); [10], Section 2.4; the archived flash image (project files), stored with every byte twice: a 4096-byte image whose last byte other than 0xFF lies at 0x0B8E, with 663 such bytes above 0x07FF.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E020

- **Location:** p. 4 (PDF p. 4), Section III-A.
- **Quoted text:**
  - p. 4: "In functional safety terms, this binary constitutes Software of Unknown Pedigree (SOUP), justified for integration via the IEC 61508 “Proven-in-Use” argument based on decades of safe field operation."
- **Correction:** No operating data, such as operating hours or failure records, were available to the work, and none is cited. The sentence claims no field experience that is not documented; it may say that the reuse of the binary would have to be argued along the proven-in-use route of IEC 61508, whose statistical evidence lies beyond this work.
- **Class:** claim not supported by the work's evidence
- **Evidence:** the paper cites no source for the operating history, and no operating records are among the project files.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E021

- **Location:** p. 5 (PDF p. 5), Fig. 1 and Section III-B.
- **Quoted text:**
  - p. 5, Fig. 1, PCB 1: "Watchdog"; "+ BOD"
  - p. 5, Fig. 1, PCB 2: "Debounce"; "+ Level Shift"
  - p. 5: "through debouncing and level-shifting circuitry"
- **Correction:** In Rev 1.0 the watchdog (a CD4518 counter with its clock and a transistor stage) sits on the Upper Board, together with the debouncing; the level shifters (CD4050) and the brown-out supervisor (TPS3307) sit on the Base Board. Fig. 1 and Section III-B show the watchdog and the level shifting the other way round. Correction: in Fig. 1, "Watchdog" moves to PCB 2 and "Level Shift" to PCB 1, while "BOD" stays on PCB 1; Section III-B reads "through debouncing circuitry".
- **Class:** factual, not affecting results
- **Evidence:** board files of Rev 1.0 (project files): the Upper Board carries CD40106, CD4518 and BCY59, and no CD4050 or TPS3307; [10], Section 4.6, describes the watchdog as a clock and a 4518 counter.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E022

- **Location:** p. 5 (PDF p. 5), Fig. 1 and Section III-C.
- **Quoted text:**
  - p. 5, Fig. 1, PCB 3: "RTC"; "DS3231SN"
  - p. 5: "Real-Time Clock (RTC) (DS3231SN) with battery backup for timestamped logging"
- **Correction:** Neither the schematic of Rev 0.0 as ordered nor that of Rev 1.0 contains a DS3231SN. Timestamps come from the STM32's internal real-time clock, with a 32.768 kHz crystal and a coin-cell holder on the diagnostics board; the DS3231SN appears only in an early draft schematic and in the inherited bill of materials. Read: "the STM32's internal real-time clock (RTC) with a 32.768 kHz crystal and coin-cell battery backup for timestamped logging"; in Fig. 1, "RTC (STM32 internal)".
- **Class:** factual, not affecting results
- **Evidence:** schematics of Rev 0.0 as ordered and of Rev 1.0 (project files): no DS3231, crystal Q8 of 32.768 kHz and battery holder U1; STM32 firmware of 2023 (project files), which initialises and reads the internal RTC.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E023

- **Location:** p. 5 (PDF p. 5), Fig. 1; p. 8 (PDF p. 8), Table II (row B4); p. 9 (PDF p. 9), Section V-E and Section VI.
- **Quoted text:**
  - p. 5, Fig. 1: "MicroSD"; "(FatFS)"
  - p. 8: "B4 Firmware FatFS timing starvation blocking SPI Rx"
  - p. 9: "SD Card Storage (FatFS Timing Starvation): The FatFS implementation on the STM32"
  - p. 9: "resolving the FatFS timing starvation"
- **Correction:** The library is called FatFs. Read "FatFs" throughout.
- **Class:** typographical
- **Evidence:** the library's own documentation at <http://elm-chan.org/fsw/ff/>.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E024

- **Location:** p. 5 (PDF p. 5), Section III-C.
- **Quoted text:**
  - p. 5: "Four optocouplers (SFH601-3) isolate the SPI communication link, with separate isolated DC/DC converters maintaining the power barrier."
- **Correction:** The four optocouplers carry the three SPI lines (data, clock and chip select) and the reset line of the STM32; one isolated DC/DC converter is fitted, and a second footprint is marked as not to be fitted. Read: "Four optocouplers (SFH601-3) isolate the three SPI lines and the STM32 reset line, and an isolated DC/DC converter maintains the power barrier."
- **Class:** factual, not affecting results
- **Evidence:** schematic of Rev 1.0 (project files): optocouplers OK5 to OK8 on the nets of SPI data, SPI clock, chip select and the STM32 reset; bill of materials of Rev 1.0, sheet of the STM32 board: Y22 marked as not fitted, Y23 fitted.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E025

- **Location:** p. 5 (PDF p. 5), Section III-C.
- **Quoted text:**
  - p. 5: "the FPGA’s emulated SPI master clock frequency is set to fSPI = 100 kHz by division of the 6 MHz system clock (30 clock cycles per half-period)"
- **Correction:** In the archived VHDL source of the 32-bit SPI master, the clock output toggles every 31 cycles of the 6 MHz system clock, since the counter runs from 0 to 30; this gives an SPI clock of about 96.8 kHz and a half-period of about 5.2 µs. A comment in the source states 30 cycles, and [11] states 30 cycles per edge for its own 24-bit transmitter of 2025, whose source is not among the project files. Read: "set to about 97 kHz by division of the 6 MHz system clock (31 clock cycles per half-period)". On Equation (2) see [P-E026](#p-e026).
- **Class:** factual, not affecting results
- **Evidence:** VHDL source of the SPI master of 2023 (project files), state "send": the clock toggles when the counter exceeds 29, and the counter is then reset to 0; [11], p. 20.
- **Found:** 2026-09-27
- **Reported:** not reported
- **Status:** Open.

### P-E026

- **Location:** p. 5 (PDF p. 5), Section III-C, Equation (2) and the sentences around it.
- **Quoted text:**
  - p. 5: "Given that the SFH601-3 optocoupler has a typical propagation delay of tprop ≈ 3 µs, this configuration leaves a timing margin of:"
  - p. 5: "tmargin = thalf − tprop = 5 µs − 3 µs = 2 µs, (2)"
  - p. 5: "which guarantees error-free signal transmission under typical operating temperatures."
- **Correction:** The 3 µs of the SFH601-3 are its typical turn-on and turn-off times at a load resistance of 100 Ω, not a propagation delay. The board fits 10 kΩ collector pull-ups, for which the datasheet's typical curve of switching time against load resistance shows a turn-off time well above the half-period of about 5 µs. Equation (2) holds only for a 100 Ω load and is marked as such; the timing margin at the SPI clock used has not been verified, and "guarantees error-free signal transmission" is withdrawn. [11] reports an oscilloscope check of the diagnostics board that showed no unstable communication; it did not measure a margin.
- **Class:** claim not supported by the work's evidence
- **Evidence:** SFH601 datasheet (document number 83663): switching characteristics (turn-on and turn-off time typically 3 µs at VCC = 5 V, IC = 2 mA, RL = 100 Ω) and Fig. 14 (switching time against load resistance); schematic of Rev 1.0 (project files): collector resistors R107 to R110 of 10 kΩ; [11], p. 22, item 7.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E027

- **Location:** p. 5 (PDF p. 5), Section III-E, item (2).
- **Quoted text:**
  - p. 5: "Key safety features include:"
  - p. 5: "(2) BOD supervision on all critical power rails (5 V, 3.3 V, 1.5 V)"
- **Correction:** The supervisor, a TPS3307-18 on the Base Board, senses all three rails, but on the 1.5 V core rail its trip point lies below the range in which the FPGA core is specified. It senses that rail directly and resets only when the rail falls below 1.22 to 1.29 V (typically 1.25 V), while the core of the A3P1000 is specified from 1.425 V to 1.575 V; between about 1.29 V and 1.425 V the core can run outside its specified range without a reset. On the 5 V rail, sensed through a divider of 2.4 kΩ and 6.8 kΩ, the reset comes at about 3.96 V, a fifth below the nominal value; [10] reports a reset below 4.1 V on the prototype in 2023. The work does not show that the parts on the 5 V rail work down to this value. On the 3.3 V rail, sensed through 4.7 kΩ and 5.6 kΩ, the reset comes at about 3.09 V, inside the 3.0 to 3.6 V range of the FPGA's 3.3 V supply. Read: "(2) brown-out supervision of the 5 V, 3.3 V and 1.5 V rails, with trip points of about 3.96 V, 3.09 V and 1.25 V; on the 1.5 V core rail the trip point lies below the specified core supply".
- **Class:** claim not supported by the work's evidence
- **Evidence:** schematic of Rev 1.0 (project files): supervisor Y3 (TPS3307-18), SENSE1 between R103 (2.4 kΩ, from the 5 V rail) and R105 (6.8 kΩ), net label 3.700 V; SENSE2 between R102 (4.7 kΩ, from the 3.3 V rail) and R104 (5.6 kΩ), net label 1.794 V; SENSE3 on the 1.5 V core rail; the bill of materials of Rev 1.0, sheet of the Base Board, with the same values; Texas Instruments SLVS199C (TPS3307-18, -25, -33), Electrical Characteristics: negative-going input thresholds 2.93 V (SENSE1), 1.68 V (SENSE2) and 1.25 V, 1.22 to 1.29 V (SENSE3); Microsemi DS0106 (Military ProASIC3/EL), Revision 6.0, Table 7: 1.5 V core supply of the A3P1000 1.425 to 1.575 V, 3.3 V I/O supply 3.0 to 3.6 V; [10], Section 4.7.
- **Found:** 2026-09-28
- **Reported:** not reported
- **Status:** Open.

### P-E028

- **Location:** p. 5 (PDF p. 5), Section III-E, item (3); p. 8 (PDF p. 8), Section V-D; p. 9 (PDF p. 9), Section V-E, paragraph beginning "Crucially".
- **Quoted text:**
  - p. 5: "(3) galvanic isolation preventing fault propagation from non-safety (STM32) to safety (FPGA) domains"
  - p. 8: "diagnostic data routing was validated via USB serial streaming, confirming isolation integrity"
  - p. 9: "This architectural separation—enforced by optocoupler isolation and independent power domains—ensures that diagnostic subsystem faults cannot propagate to the safety-critical domain."
- **Correction:** The barrier runs through the diagnostics board, not around it. The four optocouplers carry signals only from the Base Board to the STM32 side ([P-E024](#p-e024)), and the STM32 side is powered through an isolated DC/DC converter with short-circuit protection; faults on the STM32 side therefore cannot feed back into the FPGA domain through the signal path, and an overload there is limited by the converter. The parts of the diagnostics board on the primary side of the barrier are not covered. The six-pin connector X12 brings the Base Board's 5 V supply and ground onto the board (the schematic notes that this ground, GND3, is connected to GND); across this supply lie the suppressor diode D16 (SMBJ5.0A) and the input of the converter Y23, and on the same side the LEDs of the optocouplers with their series resistors R82 to R85. A short circuit of D16 or of the converter input would pull down the 5 V rail of the Base Board, whether or not the solder jumper SJ2, which can bridge the two grounds, is open. No test of the isolation is documented, and streaming diagnostic data over USB does not test it; [11] reports only that the diagnostics board showed no short circuit. Read on p. 5: "(3) galvanic isolation preventing signal feedback from the non-safety (STM32) side to the safety (FPGA) domain"; on p. 9: "This separation, by one-way optocouplers and an isolated supply, keeps faults on the isolated side of the diagnostic subsystem out of the safety-critical domain; its parts on the primary side of the barrier (the suppressor diode, the converter input and the optocoupler LEDs) share the 5 V supply of the Base Board." In Section V-D, "confirming isolation integrity" is withdrawn.
- **Class:** claim not supported by the work's evidence
- **Evidence:** schematic of Rev 1.0 (project files): connector X12 brings the Base Board's 5 V supply (pin 6) and ground (pin 1, named GND3 on the sheet of the diagnostics board) onto that board; the header X13 of the Base Board carries the same signals pin for pin, and the sheet notes "GND3 ist verbunden mit GND"; D16 (SMBJ5.0A) and the input pins of Y23 lie between these two nets; R82 to R85 (360 Ω) feed the LEDs of OK5 to OK8, whose cathodes lie on GND3; SJ2 lies between GND3 and the isolated ground GND2; the bill of materials of Rev 1.0 fits Y23 (MGDS-04-C-C); Gaia Converter, MGDM-04 series datasheet (FC97-008.05/23, Revision T): galvanic isolation, permanent short-circuit protection, input current in short-circuit mode at most 50 mA for the 5 V input models; [11], p. 22, item 7.
- **Found:** 2026-09-28
- **Reported:** not reported
- **Status:** Open.

### P-E029

- **Location:** p. 6 (PDF p. 6), Fig. 3 (caption); p. 8 (PDF p. 8), paragraph before Section V-B; p. 9 (PDF p. 9), Fig. 5 (caption).
- **Quoted text:**
  - p. 6: "Fig. 3. Oscilloscope capture from Layer 1 verification showing the watchdog circuit timing. CH1 (yellow): FPGA servicing pulses. CH2 (blue): watchdog reset response."
  - p. 8: "Fig. 5 provides direct visual evidence of functional equivalence for the frequency sweep—a key anti-skid diagnostic function."
  - p. 9: "Fig. 5. Frequency sweep comparison: original system (left half of each panel, LeCroy oscilloscope) vs. FPGA emulation (right half)."
- **Correction:** Both figures are reproduced from [10] without naming the source. Fig. 3 is a crop of [10], Fig. 9, a capture taken on 15 August 2023; the two images of Fig. 5 are [10], Figs. 11 and 12. The caption of Fig. 3 adds "Reproduced from [10], Fig. 9 (capture by M. Leyer, 15 August 2023)"; the caption of Fig. 5 adds "Reproduced from [10], Figs. 11 and 12 (measurements by M. Leyer, 2023)"; the sentence on p. 8 cites [10]. On the dating of these measurements see [P-E033](#p-e033).
- **Class:** attribution
- **Evidence:** [10], Section 4.6 (Fig. 9) and Section 4.10 (Figs. 11 and 12). The capture in Fig. 3 shows the same cursor readouts and the same on-screen time stamp (15:48:36, 15 Aug 2023) as [10], Fig. 9; the two images of Fig. 5 are identical in their pixel data with those of [10], Figs. 11 and 12.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open. Held back until the author has informed the series editor (attribution).

### P-E030

- **Location:** p. 6 (PDF p. 6), Section IV-B 1); p. 7 (PDF p. 7), Section V-A 1); p. 8 (PDF p. 8), Table II (row B1) and Section V-B.
- **Quoted text:**
  - p. 6: "A critical finding during simulation was the discovery of the NVRAM control logic bug"
  - p. 6: "This defect had remained undetected through previous development phases because the NVRAM was only exercised during fault storage and recall sequences—functions that were never systematically tested in isolation prior to this work."
  - p. 6: "but its discovery illustrates the diagnostic value of dedicated component-level testbenches in catching design faults that persist through integration."
  - p. 8: "B1 Logical NVRAM chip enable (NVRAM_ble) held high L1 Simulation Resolved"
  - p. 8: "during functional testing, the system’s internal RAM cache temporarily satisfied transient read/write commands, rendering the disabled NVRAM (B1) latent and invisible at the external board boundary."
- **Correction:** According to [11], the source the paper cites, B1 was not found in simulation: when the follow-on project tested the rebuilt board on the test fixture in 2025, the board did not respond to the fixture's tests, the clear function had no effect and the NVRAM was not cleared, and pressing STW displayed fault codes that do not exist; while debugging, the project then found NVRAM_ble set to 1 and corrected it, after which the board passed the fixture's tests. The fault was thus visible at the board boundary, in Layer 2, and its cause was located by debugging. The archived test benches of the 2023 design leave NVRAM_ble unconnected, so these simulations could not show the fault. The NVRAM had been tested in isolation before this work: [10] tested it in 2023 with dedicated test designs, including a power cycle, with success. Correction: Table II gives B1 as found on the test fixture (Layer 2), cause located by debugging, source [11]; Section V-A 1) says the same; the claims that these functions were never tested in isolation, on the value of the testbenches and on the RAM cache hiding the fault are withdrawn.
- **Class:** affecting a result
- **Evidence:** [11], p. 14; [10], Section 4.4; the archived VHDL test benches of 2023 (project files), in which the port NVRAM_ble is left open.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open. Held back until the author has informed the series editor (data provenance).

### P-E031

- **Location:** p. 6 (PDF p. 6), Section IV-B 1); p. 7 (PDF p. 7), Section V-A 1); p. 8 (PDF p. 8), Table II (row B1) and Section V-B.
- **Quoted text:**
  - p. 6: "the NVRAM_ble signal (active-low chip enable) was erroneously held at logic high in the inherited Rev 0.0 design, effectively disabling the non-volatile memory entirely [11]."
  - p. 7: "(NVRAM_ble was erroneously held high, disabling the chip [11])"
  - p. 8: "the NVRAM chip-enable error (B1)"
- **Correction:** NVRAM_ble is the byte-low enable of the nvSRAM (active low), which controls the lower data byte; the chip enable is a separate signal. [11] states only that NVRAM_ble was set to 1 although it has to be 0 in a low-active system, and that the clear function failed; that the memory or the chip was disabled entirely is not in [11]. Read: "the NVRAM_ble signal (byte-low enable, active low) was erroneously held high, preventing correct access to the NVRAM [11]", and "byte-low enable" for "chip enable" in Table II and Section V-B.
- **Class:** factual, not affecting results
- **Evidence:** pin definitions in the datasheet of the CY14B101LA/CY14B101NA, a smaller member of the nvSRAM family of the fitted CY14B104NA: BLE is the byte low enable, active low, for data lines DQ0 to DQ7, and CE the separate chip enable input; [11], p. 14.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E032

- **Location:** p. 6 (PDF p. 6), Section IV-B 2); p. 8 (PDF p. 8), Table I (row "JTAG scan").
- **Quoted text:**
  - p. 6: "IEEE 1149.1 boundary scan confirmed FPGA identification (A3P1000), successful bitstream programming, and I/O pin connectivity."
  - p. 8: "JTAG scan L1 Libero SoC Pass"
- **Correction:** The paper does not cite [10], which documents these checks for the prototype in 2023. In [10], the FPGA's device identification was read and its programming verified over JTAG; the I/O pins were checked with a pin-toggling test design and a multimeter, not by boundary scan; boundary scan was used, through a JTAG tool, to read and program the flash ROM, and the two cold solder joints that blocked this test were found by manual inspection. Read: "JTAG access confirmed the FPGA identification (A3P1000) and its programming on the prototype in 2023 [10]; the I/O pins were checked with a pin-toggling test design and a multimeter [10]." On the re-soldered pins see [P-E010](#p-e010).
- **Class:** attribution
- **Evidence:** [10], Sections 4.1 to 4.3.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open. Held back until the author has informed the series editor (attribution).

### P-E033

- **Location:** p. 6 (PDF p. 6), Section IV-B 3); p. 7 (PDF p. 7), Section V-A 2); p. 8 (PDF p. 8), Table I (row "HW timing: sweep").
- **Quoted text:**
  - p. 6: "Oscilloscope measurements on the assembled Rev 1.0 hardware validated critical real-world timing parameters: watchdog pulse periodicity and the frequency sweep profile (850 Hz to 1550 Hz)."
  - p. 6: "confirming that the actual RC networks, crystal tolerances, and signal integrity meet design expectations"
  - p. 7: "Post-rework oscilloscope measurements (Fig. 3) confirmed critical timing parameters"
  - p. 8: "HW timing: sweep L1 Oscilloscope 850 Hz–1550 Hz"
- **Correction:** The oscilloscope measurements shown are those of [10], taken in 2023 on the Rev 0.0 prototype, which the paper itself names as the result of [10] (p. 4); the capture in Fig. 3 carries the on-screen date 15 Aug 2023, while the re-soldering is documented in 2025 [11]. No oscilloscope measurement of the watchdog or of the frequency sweep on the reworked board is documented; before the re-soldering, [11] reports oscilloscope checks of the supply and the clock and that the watchdog reset the CPU correctly, and it reports an oscilloscope check of the communication on the diagnostics board. That the measurements confirm the RC networks, crystal tolerances and signal integrity is withdrawn: [10] doubts the watchdog's 1.2 s reset interval, because a capacitor of the watchdog clock measured 100 nF where the original schematic shows 1 µF, and the value was changed for Rev 1.0. Read in Section IV-B 3): "Oscilloscope measurements on the Rev 0.0 prototype in 2023 [10] checked the watchdog behaviour and the frequency sweep profile (850 Hz to 1550 Hz)"; in Section V-A 2): "Oscilloscope measurements on the Rev 0.0 prototype in 2023 [10] (Fig. 3)"; in Table I, the result of the sweep row reads "Pass (Rev 0.0, 2023 [10])".
- **Class:** affecting a result
- **Evidence:** the paper's own Fig. 3 (time stamp) and p. 4; [10], Sections 4.6, 4.10 and 9.2; [11], p. 13 and p. 22, item 7.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open. Held back until the author has informed the series editor (data provenance).

### P-E034

- **Location:** p. 7 (PDF p. 7), Section IV-C.
- **Quoted text:**
  - p. 7: "The fixture (Fig. 4) provides physical connections via the main 64-pin system connector"
- **Correction:** The system connector has 48 contacts, DIN 41612 type F. Read: "via the main 48-pin DIN 41612 (type F) system connector".
- **Class:** factual, not affecting results
- **Evidence:** schematics of Rev 0.0 and Rev 1.0 (project files): connector X4 is a 48-pin type F connector with rows b, d and z; the paper's own Listing 1 (p. 7) addresses contacts 18z and 24d, and [28], Table 7 (p. 23), contacts in rows z, b and d.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E035

- **Location:** p. 7 (PDF p. 7), Section IV-C ("Coverage") and Section V-A 3); p. 8 (PDF p. 8), Table I (rows "Faults (20 codes)", "Buttons (4 cases)" and "Self-test") and Section V-C.
- **Quoted text:**
  - p. 7: "Coverage: The test suite covered: (1) complete fault memory cycles (trigger → display → store → recall → clear) for all documented fault codes, (2) self-test activation and frequency sweep, (3) button interaction equivalence"
  - p. 7: "All Layer 2 test scenarios passed after resolving integration bugs. The test suite covered all 20 documented fault conditions"
  - p. 7: "the full self-test sequence with frequency sweep, all four operator button interactions (Test, STW, Lösch, Tür/V)"
  - p. 8: "Faults (20 codes) L2 Fixture/YAML 20/20"
  - p. 8: "Buttons (4 cases) L2 Fixture/YAML 4/4"
  - p. 8: "Self-test L2 Fixture/YAML Pass"
  - p. 8: "The generated artifacts under Git version control establish the evidence base for formal safety assessment."
- **Correction:** The results are stated beyond the record. [11] reports that the follow-on project ran the fixture's test suite on the rebuilt board in 2025 and that all tests passed, and that a run of tests 1 to 19 showed the expected fault codes. Which scenarios the suite contained, and which fault codes, self-test steps and button interactions it exercised, is not recorded, and no log of these runs was archived. The counts 20/20 and 4/4 and the self-test result are withdrawn; Section V-A 3) and Table I state what [11] reports. The sentence in Section V-C on the evidence base for formal safety assessment is withdrawn as far as test results are concerned, since no log of the Layer 2 runs was archived. On the fault categories see [P-E040](#p-e040); on power cycles, [P-E036](#p-e036).
- **Class:** claim not supported by the work's evidence
- **Evidence:** [11], p. 15; [5], sheet 20/25 (21 fault codes).
- **Found:** 2026-09-27
- **Reported:** not reported
- **Status:** Open. Held back until the author has informed the series editor (data provenance).

### P-E036

- **Location:** p. 7 (PDF p. 7), Section IV-C ("Coverage", item 4) and Section V-A 3); p. 8 (PDF p. 8), Table I (row "Power stability").
- **Quoted text:**
  - p. 7: "(4) power-cycle stability"
  - p. 7: "and power-cycle stability across multiple iterations."
  - p. 8: "Power stability L2 Fixture/YAML Pass"
- **Correction:** There is no record of this test; whether, how often and when it was run can no longer be established. The statement is withdrawn at all three places.
- **Class:** claim not supported by the work's evidence
- **Evidence:** [11] does not mention power cycles, and no test record for them is among the project files.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E037

- **Location:** p. 7 (PDF p. 7), Listing 1.
- **Quoted text:**
  - p. 7: "Listing 1. Example YAML test scenario: Geber 3 fault memory cycle."
- **Correction:** Listing 1 is Listing 3 of [28], with the descriptions rewritten in English and comments added; its caption does not name the source. Read: "Listing 1. Example YAML test scenario: Geber 3 fault memory cycle. Adapted from [28], Listing 3 (descriptions in English, comments added)."
- **Class:** attribution
- **Evidence:** [28], Listing 3 (p. 44): the same test names, pin settings ({18z: 1, 24d: 0}), expected codes (31 and 95), stored sequence (03 31 09) and delete flags.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open. Held back until the author has informed the series editor (attribution).

### P-E038

- **Location:** p. 7 (PDF p. 7), Section V-A 1).
- **Quoted text:**
  - p. 7: "all Layer 1 simulations confirmed correct memory interface timing, peripheral logic behaviour, and watchdog interaction."
- **Correction:** That Layer 1 simulations after the correction of B1 confirmed the memory interface timing, the peripheral logic and the watchdog interaction is not documented. The sentence claims no simulations after the correction; on B1 itself see [P-E030](#p-e030) and [P-E031](#p-e031).
- **Class:** claim not supported by the work's evidence
- **Evidence:** no simulation run after 2023 is among the project files; [11] documents simulation only of its own SPI transmitter (p. 21).
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E039

- **Location:** p. 7 (PDF p. 7), Section V-A 2); p. 8 (PDF p. 8), Table I (row "HW timing: watchdog").
- **Quoted text:**
  - p. 7: "including a watchdog service period of ∆t = 3.85 s at V = 3.36 V (expected ≈ 5 s from the VHDL test model; the shorter measured period is attributable to the voltage-dependent RC time constant of the external watchdog circuit)"
  - p. 8: "HW timing: watchdog L1 Oscilloscope 3.85 s"
- **Correction:** ∆t = 3.85 s and V = 3.36 V are the readouts of two manually placed cursors (∆V = 0.00 V): the time between the cursors and the signal level at their positions. The first cursor lies within a service phase, so the time between them is not a measured service period, and 3.36 V is not a supply voltage. According to [10], the test design services the watchdog 256 times, for some five seconds, and then withholds service for another 256 timer cycles; the watchdog is then expected to pull the reset line low every 1.2 s, a value [10] itself doubts because of a capacitor value. The explanation by the RC time constant has no basis, and neither has the value 3.85 s in Table I. Correction: Fig. 3 is described as [10] explains the capture, with the cursor values marked as cursor readouts; Table I gives "Pass (Rev 0.0, 2023 [10])".
- **Class:** affecting a result
- **Evidence:** the capture itself (Fig. 3: cursors at t1 = -1.72 s and t2 = 2.13 s, both at 3.36 V); [10], Section 4.6.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open. Held back until the author has informed the series editor (data provenance).

### P-E040

- **Location:** p. 7 (PDF p. 7), Section V-A 3); p. 8 (PDF p. 8), Table I (row "Faults (20 codes)").
- **Quoted text:**
  - p. 7: "The test suite covered all 20 documented fault conditions (five categories—sensor fault, short circuit, wire break, monitoring timeout, and watchdog—across four axle cards)"
- **Correction:** The diagnosis table of [5] has no watchdog category. It lists 21 fault codes in five categories: sensor, solenoid-valve short circuit, solenoid-valve wire break and bogie monitoring time, each for four positions, and computer card 01 to 05. Read: "(five categories: sensor, solenoid-valve short circuit, solenoid-valve wire break, bogie monitoring time and computer card)"; which of the codes were run is not recorded ([P-E035](#p-e035)).
- **Class:** factual, not affecting results
- **Evidence:** [5], sheet 20/25 (diagnosis table).
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E041

- **Location:** p. 8 (PDF p. 8), Table I (rows "SPI (32-bit)" and "SD card" with their notes), Table II (status of B4 and B5) and Section V-D; p. 9 (PDF p. 9), Section V-E, opening sentence, and Section VI, "Future work".
- **Quoted text:**
  - p. 8: "SPI (32-bit) L2 Fixture/USB Pass∗"
  - p. 8: "SD card L2 Firmware Pass†"
  - p. 8: "Originally truncated to 16 bits; resolved by resizing the SPI reception buffer configuration to 32 bits (4 bytes) in the STM32 firmware."
  - p. 8: "Originally blocked due to filesystem mounting delays; resolved by mounting once at initialization and optimizing the main logging loop."
  - p. 8: "confirming isolation integrity, error-free 32-bit SPI packet reception, and robust SD logging."
  - p. 9: "To ensure absolute safety integrity, these issues were subsequently resolved:"
  - p. 9: "Future work: Immediate priorities involve correcting the STM32 firmware’s SPI receiver buffer configuration to 32 bits and resolving the FatFS timing starvation with a non-blocking queue."
- **Correction:** The paper reports B4 and B5 as resolved and, in its Future work, as still to be corrected; on the findings and their dates see [P-E042](#p-e042). Both defects were open when the follow-on project reported in August 2025 [11]: the SD-card logging froze, and in simulation the VHDL transmitter transmitted the third byte of each frame incorrectly. A fix of the STM32 firmware of 2023 was applied afterwards; whether the VHDL transmitter was changed after the finding of 2025 is not documented. In early 2026 the author, his supervisor and members of the project team observed the rebuilt unit operating as a whole in the test setup; the diagnostic path itself, that is the SD-card logging and the complete SPI frames, was not verified separately, and no log or capture of that run was archived. Correction: in Tables I and II, the status of B4 reads "fix applied; diagnostic path not verified separately" and the status of B5 "receiver: fix applied; transmitter: change not documented; diagnostic path not verified separately", with a note that says the above; in Section V-D, "error-free" and "robust" are withdrawn, and on "isolation integrity" see [P-E028](#p-e028); the Future work sentence is superseded by this status.
- **Class:** claim not supported by the work's evidence
- **Evidence:** [11], pp. 19, 21 and 22 (items 5 and 13); the author's research report as submitted in August 2025 (unpublished), which lists both defects as unresolved and states that successful logging tests bypassed the SD card.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open. Held back until the author has informed the series editor (data provenance).

### P-E042

- **Location:** p. 8 (PDF p. 8), Table II (rows B4 and B5) and Section V-B; pp. 8 to 9 (PDF pp. 8 to 9), Section V-E.
- **Quoted text:**
  - p. 8: "B4 Firmware FatFS timing starvation blocking SPI Rx L2 Fixture/YAML Resolved"
  - p. 8: "B5 Interface SPI payload truncation (16-bit vs 32-bit buffer) L2 Fixture/USB Resolved"
  - p. 8: "it could not expose firmware-level timing starvation (B4) or SPI buffer truncation issues (B5). Conversely, system-level validation using the dedicated test fixture (Layer 2) stimulated the system through its external connector pins and successfully captured the runtime integration errors B4 and B5."
  - p. 8: "The discovery of the following integration issues during Layer 2 testing validates the necessity of the scenario-based approach; these faults would not have been detected"
  - p. 9: "by Layer 1 simulation alone."
  - p. 9: "which introduced a 50 ms to 200 ms blocking overhead"
- **Correction:** No record shows that the test fixture (Layer 2) found B4 or B5. [11] reports the SD-card freeze from running the diagnostics board with the follow-on project's own firmware, which read the SPI data bit by bit, three bytes per frame; the fixture does not appear in that part of [11]. [11] also documents a second SPI finding, which it made in simulation: the project's three-byte VHDL transmitter transmitted the third byte of each frame incorrectly. The causes stated in the paper match the STM32 firmware of 2023, which received two bytes per SPI interrupt against a 32-bit frame and mounted and unmounted the SD card in every loop cycle; who found them, and when, is not documented, and no measurement of "50 ms to 200 ms" was found. Correction: B4 and B5 are described with each finding dated: in the firmware of 2023, the 16-bit reception and the mounting in every loop cycle; in 2025, the SD-card freeze in the follow-on firmware and the transmitter fault found in simulation [11]. The instruments "Fixture/YAML" and "Fixture/USB" and the figure "50 ms to 200 ms" are withdrawn. The statements that Layer 1 could not expose B5 and that these faults would not have been detected by Layer 1 simulation alone do not hold for the transmitter fault, which [11] found in simulation; on the transmitter see [P-E043](#p-e043).
- **Class:** affecting a result
- **Evidence:** [11], pp. 16, 17, 19 and 21; the STM32 firmware of 2023 and the VHDL logger of 2023 (project files).
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open. Held back until the author has informed the series editor (data provenance).

### P-E043

- **Location:** p. 9 (PDF p. 9), Section V-E, item "SPI Payload Truncation and Alignment" and the paragraph beginning "Crucially".
- **Quoted text:**
  - p. 9: "The VHDL SPI master correctly transmits a 32-bit diagnostic frame (consisting of a 2-bit prefix, 6-bit button state, and 24-bit error code)."
  - p. 9: "Crucially, both the SPI bug and the FatFS issue reside exclusively in the non-safety-critical diagnostic subsystem, which is galvanically isolated from the FPGA core."
- **Correction:** That the VHDL SPI master transmits this frame correctly is not documented. [10] states that the FPGA side of this logging, two 16-bit messages introduced by a 2-bit marker, was implemented but not tested (Section 3.3); the test of the isolated link in [10] used reused test programs and a modified SPI master (Section 4.11). In 2025 the follow-on project simulated a three-byte version of the transmitter and found the third byte of each frame transmitted incorrectly, a fault it left open [11]; which transmitter runs on the rebuilt unit is not documented. "correctly transmits" is withdrawn. The second sentence holds only for the STM32 side: the 16-bit reception and the FatFs issue lie in the STM32 firmware of the diagnostic subsystem, but the transmitter fault documented in 2025 lies in the VHDL of the FPGA design. Read: "The VHDL SPI master sends a 32-bit diagnostic frame (a 2-bit prefix, the 6-bit button state and the 24-bit error code); its transmission has not been verified." and "Both the SPI reception fault and the FatFs issue lie in the STM32 firmware of the diagnostic subsystem, which is galvanically isolated from the FPGA core; the transmitter fault found in simulation in 2025 lies in the FPGA design [11]." On B4 and B5 see [P-E041](#p-e041) and [P-E042](#p-e042); on the isolation, [P-E028](#p-e028).
- **Class:** claim not supported by the work's evidence
- **Evidence:** [10], Sections 3.3 and 4.11; [11], pp. 3, 16, 20 and 21, and p. 22, items 11 to 13; the VHDL logger of 2023 (project files), which builds the frame from a 2-bit prefix, the six button states and 24 error lines and hands it to the SPI core as two 16-bit words.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open. Held back until the author has informed the series editor (data provenance).

### P-E044

- **Location:** p. 10 (PDF p. 10), reference [2].
- **Quoted text:**
  - p. 10: "[2] A. S. Losada, “Functional Safety Approaches for Rail Traffic Technology Specified Embedded Systems,” TH Köln – University of Applied Sciences, Research Report, 2021, internal Report."
- **Correction:** The year 2021 cannot be supported. The document carries no date, its most recent source is from 2015, and the file was created in 2016; 2021 is only the date on which the file was last modified. Read "n.d." for "2021".
- **Class:** factual, not affecting results
- **Evidence:** the copy of [2] available to the author: no date in the document, most recent cited year 2015, file created on 3 June 2016 and last modified on 23 March 2021.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E045

- **Location:** p. 10 (PDF p. 10), references [4], [18], [21] to [24], [26] and [29].
- **Quoted text:**
  - p. 10: "[18] CENELEC, “Railway applications – Braking – Wheel slide protection,” CENELEC, Tech. Rep. EN 15595:2018, 2018."
  - p. 10: "[21] CENELEC, “Railway applications – Safety related electronic systems for signalling,” CENELEC, Tech. Rep. EN 50129:2018, 2018."
- **Correction:** EN 15595 [18] is a standard of CEN, prepared by its technical committee CEN/TC 256, not of CENELEC. The title of EN 50129 [21] lacks the part "Communication, signalling and processing systems", which stands between "Railway applications" and "Safety related electronic systems for signalling". The standards among the references ([4], [18], [21] to [24], [26], [29]) are standards, not technical reports; "Tech. Rep." reads "Standard".
- **Class:** factual, not affecting results
- **Evidence:** EN 15595:2018, European foreword (prepared by Technical Committee CEN/TC 256 "Railway applications"); national catalogue entries for EN 50129:2018, which give the full title.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E046

- **Location:** p. 10 (PDF p. 10), references [6], [7], [13], [15], [25] and [27]; cited on pp. 3, 4, 5 and 9.
- **Quoted text:**
  - p. 10: "[6] M. Bozzano, A. Cimatti, J.-P. Katoen, T. Noll, and S. Tjell, “Formal verification and validation for safety-critical systems,” in Leveraging Applications of Formal Methods (ISoLA 2016). Springer, 2016, pp. 3–20."
  - p. 10: "[7] L. Chen, R. Liu, Y. Liu, and W. Zhang, “Formal Verification Methods for Railway Signaling Safety-Critical Software: A Survey,” IEEE Trans. Intell. Transp. Syst., vol. 24, no. 1, pp. 264–283, 2023."
  - p. 10: "[13] E. Cascone, A. Sorniotti, and P. Gruber, “Development and Validation of a Hardware-in-the-Loop Test Rig for Railway Primary Suspensions,” in Proc. 11th Int. Conf. Simulation and Testing for Vehicle Technology (VEHITS 2023), 2023, pp. 137–146."
  - p. 10: "[15] N. Scheithauer, R. Müller, and U. Goltz, “Safety cases for legacy systems in the railway domain,” in Proc. 6th Int. Conf. Model-Driven Engineering and Software Development, 2018, pp. 511–518."
  - p. 10: "[25] G. Latif-Shabgahi, “A survey on dependable design techniques for FPGAs,” IET Computers & Digital Techniques, vol. 3, no. 5, pp. 433–447, 2009."
  - p. 10: "[27] H. Chen, B. Jiang, and S. X. Ding, “Data-Driven Fault Diagnosis for Traction Drive Systems in High-Speed Trains: A Survey, Challenges, and Potential Solutions,” IEEE Transactions on Systems, Man, and Cybernetics: Systems, vol. 50, no. 5, pp. 1627–1638, 2020."
- **Correction:** These six references could not be traced to any published work as cited. They were carried over from the bibliography of the author's research report as submitted in August 2025 into the version of the paper submitted on 28 June 2026, and they had not been checked against the original works. The statements that cite them ([6] and [7] on pp. 3 and 4, [13] on pp. 4 and 9, [15] and [25] on p. 4, [27] on p. 5) stand without a source until a work that carries them is cited; on [15] see also [P-E012](#p-e012), on [25] [P-E016](#p-e016). For [27], a survey with a similar title by H. Chen, B. Jiang, S. X. Ding and a fourth author exists (IEEE Transactions on Intelligent Transportation Systems, vol. 23, no. 3, pp. 1700-1716, 2022, DOI 10.1109/TITS.2020.3029946); its title, journal, volume, year and author list differ from the printed entry, and it is not established that it is the work meant.
- **Class:** reference could not be traced
- **Evidence:** at least three queries for each reference in at least two bibliographic sources, among them Crossref (2026-09-24; Crossref repeated on 2026-09-28); where the author's earlier bibliography recorded a DOI for one of them, it is not registered or leads to a different work; in the proceedings of ISoLA 2016, Part I (LNCS 9952), pp. 3 to 15 hold a different chapter, and neither part contains a chapter by the authors of [6].
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E047

- **Location:** p. 10 (PDF p. 10), reference [9]; cited on p. 4.
- **Quoted text:**
  - p. 10: "[9] S. Ayoub, “Reverse Engineering von Steuerkarten – Vorarbeit,” TH Köln – University of Applied Sciences, Internal Report, 2014."
- **Correction:** No document under the printed title with "Vorarbeit" could be traced. The only document found that fits the passage on p. 4 is a work report (Arbeitsbericht) of Fachhochschule Köln dated 4 June 2014, with the title "Reverse Engineering von Steuerkarten" and the subtitle "Vergleicher Karte und Stromsollwert Karte". Read, with title, type and institution as in that report: S. Ayoub, "Reverse Engineering von Steuerkarten: Vergleicher Karte und Stromsollwert Karte", work report (Arbeitsbericht), Fachhochschule Köln, June 2014.
- **Class:** reference could not be traced
- **Evidence:** the work report itself (unpublished), title page; it treats an emulated CPU on an FPGA (pp. 5 and 10) and does not contain the word "Vorarbeit".
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E048

- **Location:** p. 10 (PDF p. 10), reference [16].
- **Quoted text:**
  - p. 10: "[16] R. M. Hierons, K. Bogdanov, J. P. Bowen, R. Cleaveland, J. Derrick, J. Dick, M. Gheorghe, M. Harman, K. Karatkevich, M. Kuluvan et al., “Using formal specifications to support testing,” ACM Computing Surveys (CSUR), vol. 41, no. 2, pp. 1–76, 2009."
- **Correction:** "K. Karatkevich" and "M. Kuluvan" are not among the article's 15 authors. Read: R. M. Hierons, K. Bogdanov, J. P. Bowen, R. Cleaveland, J. Derrick, J. Dick, M. Gheorghe, M. Harman et al., "Using formal specifications to support testing," ACM Computing Surveys, vol. 41, no. 2, pp. 1-76, 2009, DOI 10.1145/1459352.1459354.
- **Class:** factual, not affecting results
- **Evidence:** DOI 10.1145/1459352.1459354: Crossref lists 15 authors, and neither printed name is among them; the author line of the article agrees.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

### P-E049

- **Location:** p. 10 (PDF p. 10), references [17] and [19].
- **Quoted text:**
  - p. 10: "available: https://www.wabteccorp.com/newsroom."
  - p. 10: "available: https://www.railwaygazette.com."
- **Correction:** Both addresses lead only to the entry page of the website, not to the item cited. [17]: <https://www.wabteccorp.com/newsroom/press-releases/wabtec-s-innovative-adaptive-wheel-slide-protection-solution-gains-certification> (press release of 6 December 2022). [19]: the article of April 2013 is available as an archived copy at <http://web.archive.org/web/20130430163301/http://www.railwaygazette.com/news/single-view/view/south-west-trains-emus-to-get-ac-traction-equipment.html>.
- **Class:** factual, not affecting results
- **Evidence:** the addresses above, read on 2026-09-24 and 2026-09-28; both answered again on 2026-10-01.
- **Found:** 2026-09-24
- **Reported:** not reported
- **Status:** Open.

## 2. Properties of the record and the deposited file

These are not errors of the author's text. They concern the catalogue record of Cologne Open Science, the DOI metadata at DataCite, the copy of the record at the German National Library, and the container that the editors built around the paper. The record, the DOI metadata and the copy were last checked on 2026-10-01.

- **Series cover (p. 1).** The editors' cover sets the title as "Public Trans-", "portation:A Hybrid Two-Layer Verification Me-", "thodology": without a space after the colon, and with "Methodology" divided after "Me". The paper's own title page (p. 3) prints the title correctly: "Ensuring Functional Equivalence in Retrofitted Anti-Skid Systems for European Public Transportation: A Hybrid Two-Layer Verification Methodology". Found 2026-09-24; not reported.
- **Catalogue record.** On the author's request of 2026-09-27, the library corrected the record on 2026-09-30: the title now has the space after the colon, the abstract reads "cost-effective" as p. 3 does, and the subject classes, the GND subject headings and the index terms were revised; the record now carries all nine index terms of p. 3. Checked on 2026-10-01. The DOI metadata and the copy at the German National Library still show the earlier state.
- **DOI metadata at DataCite.** The DataCite record of the DOI has not been changed since its registration on 2026-09-22. It still gives the title as "…Transportation:A Hybrid…", without the space after the colon, and the abstract with "more costeffective"; it lists the publisher as "(:unav)", carries no affiliation for the author and classifies the paper only under the main class 000 of the Dewey Decimal Classification. Citations generated from the DOI carry this title and this publisher. Reported to the library on 2026-09-27; unchanged when checked on 2026-10-01.
- **Record at the German National Library.** The German National Library took the record over on 2026-09-29, before the correction. Its copy still gives the title without the space after the colon, together with the earlier subject headings and three of the nine index terms (checked on 2026-10-01). Not reported.
- **Licence.** The record gives CC BY-NC-ND 4.0; the published policy of Cologne Open Science names CC BY-NC-ND 3.0 DE; the imprint (p. 2) names the licence terms without a version. The question which version applies was put to the library on 2026-09-27 and is open; the record was unchanged when checked on 2026-10-01.
- **PDF/A conformance.** The file declares PDF/A-1a in its XMP metadata (part 1, conformance A) but does not conform: it has no structure tree and no MarkInfo entry, so it is not tagged; it contains soft-masked images and transparency groups (pp. 6 and 9); it uses DeviceCMYK colour without a CMYK output intent; and one annotation lacks the print flag. Validation with veraPDF 1.30.2 against PDF/A-1a and PDF/A-1b fails on these rules (2026-09-28 and 2026-10-01). Found 2026-09-27; not reported.
- **Document metadata.** The document information dictionary has no Title and no Author entry, and the XMP metadata carry no title or creator. Found 2026-09-24; not reported.
- **DOI in the file.** The DOI 10.57684/COS-1494 is printed nowhere in the file. Found 2026-09-27; not reported.

## 3. Updates

- **[20] (p. 10).** The printed address `https://www.railtechnologymagazine.com/articles/greater-anglia-1m-class-317-refurb-completed` returns HTTP 404 (checked on 2026-09-24, 2026-09-28 and 2026-10-01). The article is available at <https://www.railtechnologymagazine.com/Rolling-stock/greater-anglia-class-317-refurb-completed>.
- **Author's website (p. 3).** The web address printed in the author note does not open: the TLS handshake fails (checked on 2026-09-28 and 2026-10-01), and over plain HTTP the hosting provider's placeholder page appears. The author can be reached at the e-mail address printed beside it.
