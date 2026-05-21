# Create markdown file
echo "# Lab1B - Authentication, Authorization, and Accounting" > Lab1B.md

# Add users/groups section
echo "## Users and Groups" >> Lab1B.md
echo "- Users created: alice, bob" >> Lab1B.md
echo "- Groups: IT" >> Lab1B.md

# Add symbolic permissions
echo "## Symbolic Permissions" >> Lab1B.md
echo "- File: testfile.txt" >> Lab1B.md
echo "chmod u+rwx testfile.txt" >> Lab1B.md
echo "chmod g-x testfile.txt" >> Lab1B.md
echo "chmod o+r testfile.txt" >> Lab1B.md

# Add numeric permissions
echo "## Numeric Permissions" >> Lab1B.md
echo "chmod 754 testfile.txt" >> Lab1B.md

# Add directory permissions
echo "## Directory Permissions" >> Lab1B.md
echo "mkdir labdir" >> Lab1B.md
echo "chmod 750 labdir" >> Lab1B.md
