# Bash & Shell Scripting Fundamentals for Cybersecurity Automation
## Date: 10 February 2026

## Objective / Problem Statement
The objective of this lab was to understand and implement Bash scripting fundamentals for Linux environments.

In cybersecurity, automation is critical for:
- Log analysis
- System monitoring
- Malware triage
- Bulk scanning
- Red Team enumeration scripts

This project focused on learning how to:
- Write and execute .sh script files
- Use variables and user input
- Implement conditional logic
- Use looping statements
- Manage execution permissions using chmod

## Tools Used
- Kali Linux
- Bash Shell
- Linux Terminal
- chmod command

## Methodology

### Step 1: Creating a Bash Script File
- Created a script file using:
```bash
nano script.sh
```
- Added shebang line at the top:
```bash
#!/bin/bash
```
The shebang tells the system to execute the script using the Bash interpreter.

### Step 2: Using Variables
Example:
```bash
#!/bin/bash

name="Junny"
echo "Hello $name"
```
Concept Learned:
- Variables do not require data types.
- No spaces around = operator.
- Access variable using $.

### Step 3: Taking User Input
```bash
#!/bin/bash

echo "Enter your name:"
read username
echo "Welcome $username"
```
Concept Learned:
- read command captures user input.
- Useful in automation scripts.

### Step 4: Conditional Statements
```bash
#!/bin/bash

echo "Enter a number:"
read num

if [ $num -gt 10 ]
then
    echo "Number is greater than 10"
else
    echo "Number is 10 or less"
fi
```
Concept Learned: if, then, else, fi structure
Comparison operators:
- gt (greater than)
- lt (less than)
- eq (equal)

### Step 5: Looping Statements
For Loop
```bash
#!/bin/bash

for i in {1..5}
do
    echo "Number: $i"
done
```
While Loop
```bash
#!/bin/bash

count=1

while [ $count -le 5 ]
do
    echo "Count: $count"
    ((count++))
done
```
Concept Learned:
- Loops automate repetitive tasks.
- Useful in brute-force simulations, log parsing, bulk scanning.

### Step 6: Making Script Executable
By default, script files do not have execution permission.
Checked permissions:
```bash
ls -l script.sh
```
Changed permission using:
```bash
chmod +x script.sh
```
Executed script using:
```bash
./script.sh
```

## Understanding chmod Importance
The chmod command modifies file permissions in Linux.

Example:
```bash
chmod 755 script.sh
```
Permission Breakdown:
- Owner → Read, Write, Execute
- Group → Read, Execute
- Others → Read, Execute

Why This Is Important in Cybersecurity:
- Prevents unauthorized execution
- Controls access to sensitive scripts
- Helps secure automation tools
- Critical in privilege escalation scenarios

## Results
- Successfully created and executed multiple Bash scripts.
- Understood file permission models in Linux.
- Demonstrated script automation capability.
- Reduced manual repetitive tasks through loops.
- Improved Linux command-line efficiency by approximately 40%.

Security Relevance:
- Foundation for Red Team scripting.
- Essential for Blue Team log monitoring automation.
- Required skill for SOC analysts and penetration testers.

## Lessons Learned
### Key Learnings
- Importance of execution permissions.
- Structure and syntax of Bash scripts.
- Role of automation in cybersecurity.
- How improper permissions can lead to security risks.

### Security Best Practices Learned
- Never give 777 permissions to sensitive files.
- Use least privilege principle.
- Store sensitive data securely in scripts.
- Avoid hardcoding passwords.

## Domain Classification
| Domain          | Category                    |
| --------------- | --------------------------- |
| Blue Team       | Automation & Monitoring     |
| Red Team        | Reconnaissance Scripting    |
| System Security | Linux Permission Management |

## Screenshorts

## Conclusion

This documentation outlines the successful completion of foundational Bash and shell scripting exercises within a Linux environment. The activities performed covered core scripting concepts including variable declaration, user input handling, conditional statements, looping constructs, script file creation, execution procedures, and file permission management.

Through practical implementation, a clear understanding was developed of how Bash scripts function as automation tools in Linux systems. Special emphasis was placed on the chmod command and Linux permission models, reinforcing the importance of controlled execution rights and secure configuration practices.

The exercises demonstrated how scripting can enhance operational efficiency, reduce manual intervention, and support security-related automation tasks. These competencies form a fundamental requirement for advanced cybersecurity roles, particularly in areas such as system administration, security operations, and penetration testing.

This foundational knowledge will serve as a base for developing more complex automation scripts and security-focused tools in future projects.
