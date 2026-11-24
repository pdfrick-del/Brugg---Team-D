``` mermaid
flowchart TD

    A([Catalog Opened])

    A --> B{Books Available?}

    B -->|No| C[Display 'No Books Available']
    B -->|Yes| D[Display Catalog]

    D --> E{Apply Filter?}

    E -->|Title| F[Filter by Title]
    E -->|Author| G[Filter by Author]
    E -->|Year| H[Filter by Publication Year]
    E -->|Genre| I[Filter by Genre]
    E -->|No Filter| J[Show All Books]

    F --> K
    G --> K
    H --> K
    I --> K
    J --> K

    K{Matching Books Found?}

    K -->|No| L[Display 'No Matching Books Found']
```
    K -->|Yes| M[Display Filtered Results]

    M --> N{Sort Results?}

    N -->|Title| O[Sort A-Z by Title]
    N -->|Author| P[Sort A-Z by Author]
    N -->|Year| Q[Sort Oldest to Newest]
    N -->|Genre| R[Sort A-Z by Genre]
    N -->|None| S[Display Current Results]

    O --> S
    P --> S
    Q --> S
    R --> S

    S --> T([End])
