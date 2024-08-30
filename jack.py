try: 
  	shirt = input("What is the color of your shirt?")
      ear = input('What object is closest to your ear right now?')
      elbow = input('What object is closest to your elbow right now?')
      time = input('What were you doing at 5pm yesterday?')
      sock = ('How many pairs of socks do you own? (Enter as a number)')
      sock * 10
except:
    print('User entered an invalid number')
else:
    print('There is no problem')
finally:
    print('Your exception handling is complete')