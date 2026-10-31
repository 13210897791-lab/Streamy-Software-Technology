# Streamy Video Streaming Backend Platform
## Software Technology Course Laboratory Node
* **Student Identity:** [填入你的姓名]
* **Neptun System Code:** [填入你的 Neptun 代码]
* **Course Section Reference:** GEIAL314-B2a
---
## Workspace Environment Architecture
The diagram below maps out how our development environment connects local code authoring to remote version tracking, using a **Diagrams-as-Code** design pipeline.

```mermaid
---
title: Streamy Production Architecture Proof
---
flowchart TD
    %% Base Diagram Configurations and Properties
    
    UserNode["💻 Workstation Client <br> (Terminal CLI / Web Browser)"]
    LiveSandbox{"🌐 Cloud Sandbox <br> (mermaid.live)"}
    LocalIDE["⚙️ VS Code IDE <br> (Markdown Preview Extension)"]
    GitStage["📦 Local Git Index <br> (Staging Ledger)"]
    RemoteHub["☁️ GitHub Remote Cloud <br> (Streamy Repository Workspace)"] 
    UserNode -- 1. Sandbox Syntax --> LiveSandbox
    LiveSandbox -- 2. Verified Block Migration --> LocalIDE
    LocalIDE -- 3. git add CLI Operations --> GitStage
    GitStage -- 4. git push Pipeline Push --> RemoteHub
```
## Domain Model (UML Class Diagram)

```mermaid
classDiagram
    %% Step 1: Association (松散关联，无主从关系)
    Title -- Genre

    %% Step 2: Composition (强组合，父在左，子随父销毁)
    Title *-- Season
    Title *-- Review
    Season *-- Episode

    %% Step 3: Aggregation (聚合，演员可脱离作品独立存在)
    Title o-- Actor
```
## Domain Model (UML Class Diagram)

```mermaid
---
title: Streamy Domain Model
---
classDiagram
    Title: \n\n
    link Title "[https://example.com/titles](https://example.com/titles)" _blank
    
    %% Relationships with Multiplicity, Direction, and Labels
    Title "1..*" -- "1..*" Genre: is associated with
    Title "1" *-- "0..*" Season: has
    Title "1" *-- "0..*" Review: has
    Title "0..*" o-- "1..*" Actor: features
    
    %% Generalization / Inheritance
    TVShow --> Title: implements
    Short --> Title: implements
    Film --> Title: implements
    
    Viewer "0..*" --> "0..*" Title: watches
    Season "1" *-- "0..*" Review: has
    Season "1" *-- "1..*" Episode: contains
    Episode "1" *-- "0..*" Review: has