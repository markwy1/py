poem = r'''\
    (NO backslash)
    Programming is fun
    When the work is done
    if you wanna make your work also fun:
        use Python!
'''
# Open for 'w'riting
f = open('poem.txt', 'w')
# Write text to file
f.write(poem)
# Close the file
f.close()
