# Product scope

[简体中文](README.zh-CN.md) · English · [Home](../../README.md) · [Documentation](../README.md)

## Purpose

KetupaMK organizes PCB, package, and interconnect engineering workflows through CIR configuration. It helps engineers prepare inputs, configure modeling tasks, coordinate external tools, and review traceable outputs. The public repository distributes packaged products and documentation; it does not expose current proprietary core source.

## Published 1.0.2 capabilities

| Capability | Scope and required inputs |
| --- | --- |
| CIR execution | `ketupa run -sh main.cir`; global settings in CIR and project details in include files |
| Existing workflow entries | Fifteen entries across existing protocols and PKG/PCB/Merge combinations; queues and network workers have separate resource controls |
| PKG and Merge configuration | Bump, solderball, chip orientation, and port impedance; actual geometry follows layout, stackup, and project parameters |
| Sweep units | Hz, kHz, MHz, and GHz may be mixed within a sweep |
| DDR `.tap` reports | Touchstone, specifications, and explicit port mapping produce S21 delay and relative-skew Excel reports; missing signal or reference-plane approval does not automatically yield PASS |
| Traceability | Timestamped batches and project/scenario/channel/PKG/PCB identifiers in outputs |
| AI input preparation | Network inventory review, classification mapping, and Excel preprocessing; PKG/PCB need their layout and XML, Merge needs both layouts and both XML files, and connectors need their real models |
| Client integration | Optional configuration for detected Skill/Agent/MCP clients, preservation of user settings, editable workspace `ai` materials; MCP is read-only by default in the published description |
| Web integration | Authenticated local HTTPS interfaces and a frontend SDK; no production website integration is asserted |
| GDS Interposer | Import-only assistance, without solver execution or electrical signoff |
| Platforms | Windows Launcher and Linux CLI; valid version-scoped licensing is required |

These capabilities are described in the [1.0.2 release notes](../releases/openketupamk-v1.0.2.md). They are not assumed to exist in older versions. The fifteen entries are not evidence that every scenario has completed physical acceptance.

## Inputs, dependencies, and outputs

Workflow inputs may include CIR/include files, layouts, stackups/XML, network selections, connector models, Touchstone data, and specification templates. Supply the items required by the selected workflow and confirm data rights before use.

External Ansys, Cadence, MATLAB, Polar, or other vendor software requires separate compatible installations and vendor entitlements where applicable. Product installation does not supply those commercial rights. Outputs require engineering review for the actual project and reference planes.

## Distribution types

KetupaMK product releases and the historical Runtime 1.0.0 distribution have separate release tags and installers. The historical Beta is a separate pre-release. Version numbers and names alone do not establish interchangeable interfaces or compatibility. Use the [release index](../releases/README.md) and [installation guide](../installation/README.md).

## Foundation

[Ketupa_v0.0.3](../../history/README.md) is the original foundational project. It preserves research in HFSS antennas, transmission lines, MATLAB/CNN, LLM interaction, and desktop automation. It is retained as a complete historical project; its old setup instructions are not current-product installation instructions.
