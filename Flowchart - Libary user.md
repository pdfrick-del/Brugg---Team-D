```mermaid

flowchart TD

1.1([Start])
1.1 --> 2.1
2.1{Ask for user type}
2.1 -->|librarian| 2.2([Different path])
2.1 -->|library user| 3.1[/Type in username/]  
3.2{Check username.py}
