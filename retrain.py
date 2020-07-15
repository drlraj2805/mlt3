# Let's read our input file into a variable

with open('/home/root/mlopstask/cnncode.py', 'r') as f:
    in_file = f.readlines()  						# in_file is now a list of lines

# Now we start building our output

out_file = []
for line in in_file:
    out_file.append(line)  						# copy each line, one by one
    if 'model.add(MaxPooling2D(pool_size = (2, 2)))' in line:  	# add a new entry, after a match
        out_file.append('\nmodel.add(Conv2D(50, (5, 5) )) \nmodel.add(Activation("relu")) \nmodel.add(MaxPooling2D(pool_size = (2, 2),strides = (2, 2)))')



# Now let's write all those lines to a new output file.
# You would re-write over the input file now, if you wanted!

with open('/home/root/mlopstask/new.py', 'w') as f:
    f.writelines(out_file)
