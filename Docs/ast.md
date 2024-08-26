flowchart TD
A(["Start"]) --> B["Initialize AssemblyGenerator"]
B --> C["Parse Source Code"]
C --> D["Visit AST Nodes"]
D --> E{"Node Type"}
E --> F["Function Definition"] & G["Assignment"] & H["Expression"] & I["Other Nodes"]
F --> F1["Add Kernel Begin"]
F1 --> F2["Visit Function Body"]
F2 --> F3["Add Kernel End"]
G --> G1["Check Target Type"]
G1 --> G2["Is Target scamp5 Object?"]
G2 --> G3["Check Target Attribute"]
G3 --> G4["Is Supported Register?"]
G4 --> G5["Check Value Type"]
G5 --> G6["Is Function Call?"]
G6 --> G7["Check Function Name"]
G7 --> G8["Add Load Value Code"] & G10["Add Get Image Code"] & G12["Add Movement Code"]
H --> H1["Check Function Name"]
H1 --> H2["Handle Where Condition"] & H18["Handle mov Instruction"] & H20["Handle all Instruction"]
H2 --> H3["Check Comparison Type"]
H3 --> H4["Add Subtraction and Where Code"]
H4 --> H5["Store Flag and Handle Condition"]
I --> J["Call Generic Visit"]
J --> K["Return Assembly Code"]
style A stroke:#000000
style B stroke:#000000
style C stroke:#000000
style D stroke:#000000
style E stroke:#000000
style F stroke:#000000
style G stroke:#000000
style H stroke:#000000
style I stroke:#000000
style F1 stroke:#000000
style F2 stroke:#000000
style F3 stroke:#000000
style G1 stroke:#000000
style G2 stroke:#000000
style G3 stroke:#000000
style G4 stroke:#000000
style G5 stroke:#000000
style G6 stroke:#000000
style G7 stroke:#000000
style G8 stroke:#000000
style G10 stroke:#000000
style G12 stroke:#000000
style H1 stroke:#000000
style H2 stroke:#000000
style H18 stroke:#000000
style H20 stroke:#000000
style H3 stroke:#000000
style H4 stroke:#000000
style H5 stroke:#000000
style J stroke:#000000
style K stroke:#000000
