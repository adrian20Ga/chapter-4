#exercise_6
#adrian_G


def break_words(stuff): #Funtion will break the words
  words = stuff.split(' ')
  return words


def sort_words(words): #this funtion will sort the words
  return sorted(words)


def print_first_word(words): #funtion will print the first word

  word = words.pop(0) #Change poop for pop

  print(word) #print it

def print_last_word(words):#funtion will print the last word
  word = words.pop(-1) # Close it

  print(word) # this part will print it

def sort_sentence(sentence): #funtion will take a sentences the return the words sorted
    words = break_words(sentence)
    return sort_words(words) #will return words

def print_first_and_last(sentence): #funtion that print first word and last of sentences
    words = break_words(sentence)

    print_first_word(words)

    print_last_word(words)

def print_first_and_last_sorted(sentence):#funtion that sort and print words sorted

    words = sort_sentence(sentence)
    print_first_word(words)

    print_last_word(words)


print("Let's practice everything.") # put the message
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.') # messages print it

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""

print("--------------") # print the word

print(poem)
print("--------------") # Collocate parentesis
#below will do the operation
five = 10 -2 + 2 - 5

print(f"This should be five: %s" % five) # here will print the messages

def secret_formula(started): #funtion that do the operation
  jelly_beans = started * 500
  jars = jelly_beans / 1000 # using  "/" divitor
  crates = jars / 100 #division
  return jelly_beans, jars, crates #return the funtion


start_point = 10000 #a lonely var


beans, jars, crates = secret_formula(start_point) # usign operators "==" to equal

print("With a starting point of: %d" %start_point) # print a funtion
#below will print the messages
print("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates))


start_point = start_point / 10 #calling a funtion



print("We can also do that this way:")  # print a message
#below will change the funtion and replace it to other
print("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point))


#var sentences that correct the spelling of sentences
sentence =("All good things come to those who weight.")

words = break_words(sentence)
#var ex-25
sorted_words = sort_words(words) #
print_first_word(words) #print fisrt word
print_last_word(words) #print last word

print_first_word(sorted_words) # Print first word sorted
print_last_word(sorted_words) #print last word sorted

sorted_words = sort_sentence(sentence) # var ex-25 fix it

print(sorted_words) # print (sorted_word)

print_first_and_last(sentence) # fix the spelling

print_first_and_last_sorted(sentence) # put and fix the funtion