count=0
count1=0
count2=0
count3=0
count4=0
while True:
 count=count
 count1=count1
 count2=count2
 count3=count3
 count4=count4
 proceed_or_quit=input('enter anything to proceed, q to quit:')
 if proceed_or_quit!='q':
   passed_credit=input('enter your passed credit:')
   try:
    passed_credit=int(passed_credit)
    if passed_credit in range(0,121,20):
      defered_credit=input('enter your defered credit:')
      try:
          defered_credit=int(defered_credit)
          if defered_credit in range(0,121,20):
            failed_credit=input('enter your failed credit:')
            try:
                failed_credit=int(failed_credit)
                if failed_credit in range(0,121,20):
                  count=count+1
                  if (passed_credit+defered_credit+failed_credit)!=120:
                    print('total incorrect')
                  elif passed_credit==120:
                    print('progress')
                    count1=count1+1
                  elif passed_credit==100:
                    print('progress - module trailer')
                    count2=count2+1
                  elif failed_credit>=80:
                    print('exclude')
                    count3=count3+1
                  else:
                    print('do not progress - module retriever')
                    count4=count4+1
                else:
                  print('range error')
            except:
               print('integers required')
          elif defered_credit not in range(0,121,20):
            print('range error')
      except:
         print('integers required')
    else:
      print('range error')
   except:
    print('integers required')
 else:
   break
print('\n')
print('Progress',count1,':',count1*'*')
print('Trailing',count2,':',count2*'*')
print('Retriever',count4,':',count4*'*')
print('Excluded',count3,':',count3*'*')
print('\n')
print(count,'outcomes in total.')

