txt = open('2readWriteFile.txt')
print('Content of file:\n',txt.read())

# after 'read()', read cursor will be at end of file so we need to open it again.
# we can also do it with 'seek()'
txt = open('2readWriteFile.txt')
print('\nreading with \'readline\'')
print(txt.readline())
print(txt.readline())

# trying seek()
txt.seek(0) # seek at 0th char we can say

print(txt.read())

print('------------file in read mode------------')
filename = '2readWriteFile.txt'
target = open(filename, 'r')
for each in target:
    print(each)
target.close()

target = open(filename, 'a')

target.write("\nline written")
target.close()

target = open(filename, 'r')

print('------------file after write------------')
for each in target:
    print(each)
    
# other file related exercises : 20,23