``` mermaid
flowchart TD

    A([User Logged In])

    A --> B{Outstanding Fee Notification Enabled?}

    B -->|Yes| C{Overdue Fee Exists?}
    B -->|No| F

    C -->|Yes| D[Display Reminder Message]
    C -->|No| F

    D --> F[Membership Fees Menu]

    F --> G[View Outstanding and Upcoming Fees]

    G --> H{Manage Notifications?}

    H -->|Enable| I[Activate Notifications]
    H -->|Skip| J

    I --> J[Fee Processing]

    J --> K{Annual Fee Review Date Reached?}

    K -->|No| N
    K -->|Yes| L{Outstanding Fees Exist?}

    L -->|No| N
    L -->|Yes| M[Add 10% Late Fee Once Per Year]

    M --> N

    N --> O{Member for 5+ Years?}

    O -->|No| R([End])
    O -->|Yes| P[Apply Discount to Upcoming Fees]

    P --> Q[Ensure Discount Applied Only Once]

    Q --> R([End])
```
