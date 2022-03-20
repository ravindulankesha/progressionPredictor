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
                  if (passed_credit+defered_credit+failed_credit)!=120:
                    print('total incorrect')
                  elif passed_credit==120:
                    print('progress')  
                  elif passed_credit==100:
                    print('progress - module trailer')
                  elif failed_credit>=80:
                    print('exclude')
                  else:
                    print('do not progress - module retriever')
                else:
                  print('range error')
            except:
               print('integers required')
          else:
            print('range error')
      except:
         print('integers required')
    else:
      print('range error')
except:
   print('integers required')
