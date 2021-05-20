# 1. TASK: print "Hello World"
print( "Hello World" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Allen"
print( "Hello", name )	# with a comma
print( "Hello " + name )	# with a +
# 3. print "Hello 42!" with the number in a variable
num = 42
print( "Hello", num, "!" )	# with a comma
print( "Hello " + str(num) + "!")	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "curry"
fave_food2 = "ramen"
print( "I love to eat {} and {}.".format(fave_food1, fave_food2) ) # with .format()
print( f"I love to eat {fave_food1} and {fave_food2}." ) # with an f string

# EXTRAS:
# With %-formatting
print( "I love to eat %s and %s." % (fave_food1, fave_food2) )
# Upper-casing
print( "hello world".upper() )
# Lower-casing
print( "HELLO WORLD".lower() )
# Counting substrings
content = "Hello world, I am Allen A Nagtalon!"
aCount = content.count('e')
print( "\"{}\" has {} \'e\'s.".format(content, aCount))