##
### Opening a file
##file = open('Demo.txt', 'r')
##
### Reading from a file
##content = file.read()
##print(content)
##
### Closing a file
##file.close()

# Writing to a file
with open('Impana.txt', 'a') as file:
    file.write('Python Training')

# Reading from a file again
with open('Impana.txt', 'r') as file:
    content = file.read()
    print(content)
