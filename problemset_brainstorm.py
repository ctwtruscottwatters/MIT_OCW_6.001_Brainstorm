# -*- coding: utf-8 -*-
import random
import sys
" Charles Truscott is happily sitting a unit at MIT through edX :-) "
" Woohooo!! Lifelong dream come TRUE of sitting a unit from MIT "
" Consistently rated the highest performing Higher Learning Institution in International Rankings as #1"

words = ["apple", "pear", "banana", "peach"]


y = words[random.randint(1, len(words))]
p, q, r, s = 0, 0, 0, 0
d = {}

for n in y:
        d.get(s)
        d[p] = n
        p += 1
        
print(d)
copy_dict = d

for n in y:
    print(n, end='\n')


print(y)


fin = False
choices = []
not_chosen = []
correct_answers = []
wrong_answers = []
not_found_letters = []
z = y
z_copy = z
not_found = True
for n in y:
    not_chosen.append(n)
while(not fin):
    found = False
    choice = input('Pick a letter: ')
    for n in y:
            if choice == n:
                correct_answers.append(choice)
                for x in not_chosen:
                    if x == choice:
                        not_chosen.remove(choice)
                        found = True

    if found == True:
        print("Correct! {} is in the word.".format(choice))
    elif found == False:
        print("Incorrect, {} is not in the word".format(choice))
    found = False

    temp = []
    for q in z:
        for r in correct_answers:
            if q is r:
                temp.append(r)
                break

    print(temp)
    
    show_letter = False
    letter_fact = {}
    letter_show = {}
    zz = 0
    yy = 0
    for q in z:
        for r in correct_answers:
            if q is r:
                letter_show[zz] = True
                zz += 1
                break
            if q != r:
                letter_show[yy] = False
                yy += 1
                break
    
    hide_letter = True
    xx = 0
    for q in range(0, len(z)):
        letter_fact[xx] = hide_letter
        xx += 1
    print(letter_fact)
#    temp = []
 #   for q in z:
  #      for r in not_chosen:
   #         if q != r:
    #            temp.append(q)
     #           break
      #      if q == r:
       #         temp.append("_")
        #        break
   # for i in temp:
    #    print(i, end='')
 #   for q in z:
  #      for x in correct_answers:
   #         if q == x:
    #            print(q, end='')
     #           continue
      #      elif q != x:
       #         print('_', end='')
        #        continue
 #   for n in z:
  #      for x in not_chosen:
   #         if x is n:
    #            z_copy = z.replace(str(x), str('_'))
    
    print("I love MIT :-D, Charles T.W. Truscott")
    if len(not_chosen) is 0:
        print("End of Game")
        sys.exit()
    print(not_chosen)
    

                
         
    
            

                
            
