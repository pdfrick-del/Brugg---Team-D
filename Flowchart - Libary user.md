```mermaid

flowchart TD

1.1([Start])
1.1 --> 2.1
2.1{Ask for user type}
2.1 -->|librarian| 2.2([Different path])
2.1 -->|library user| 3.1[/Type in username/]
3.1 --> 3.2
3.2{Username exists?}
3.2 -->|No| 3.1[\Error\]
3.4 --> 1.1
3.2 -->|Yes| 3.3{Choose Option}
3.3 -->|Fees| 4.1[\Show Fees\]
3.3 -->|Deadlines| 5.1[\Show Deadlines\]
3.3 -->|Books| 6.1[\Show Books\]
