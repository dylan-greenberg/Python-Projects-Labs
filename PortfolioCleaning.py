#This is first midterm test. It combines some principles acquired from HW0-5 and homework 6
#We will try and build the "algorithmical" trader routine
#We will send certain commands to the function that will read the client's portfolio(clients.csv) and
#determine what action to take based on the command, stock and price.
#################################################################################
#If command is "SELL", you need to find all of the cleint's who hold that stock and return a dictionary,
#where key is a name and value is a number of shares
#if there is no shares to sell - empty dictionary should be returned.
#For example: if our "clients.csv" has only three entries:
#Vlas,GS,120
#Vlas,GS,180
#Valeriya,MSFT,200
# and we send a command ("SELL", "GS","200") our return should be {Vlas:300}
# if we send a command ("SELL", "MSFT","300" ) our return should be {Valeriya:200}
##########################################################################################
#If command is "BUY", you need to find "CASH" position for a client and return a dictionary,
#where key is a name of the client and value is a whole(not fraction) of shares bought(cash/price)
#For example: if our "clients.csv" has only four entries:
#Vlas,GS,120
#Vlas,GS,180
#Vlas,CASH, 10000
#Valeriya,MSFT,200
# and if  we se send a command ("BUY","GS","205") the return should be {Vlas:48}


def doAlgo(command,stock,price):
   result = {}

   inFile = open('clients.csv', 'r')
   lines = inFile.readlines()
   for line in lines[1:]:
      line = line.strip()
      columns = line.split(',')
      amount = columns[2]
      amount = float(amount)
      position = columns[1]
      name = columns[0]

      if command == 'SELL' and stock == position:
         if name in result:
            result[name] += amount
         else:
            result[name] = amount

      if command == 'BUY' and position == 'CASH':
         shares_to_buy = int(amount//price)
         if shares_to_buy > 0:
            result[name] = shares_to_buy

   return result



print(doAlgo("SELL","BRDG",200))
#that should return {'Vlas Lezin': 232.0}

print(doAlgo("SELL","AAPL",200))
# that should return {'Elizabeth Jones': 295.0, 'Robert Williams': 125.0, 'William Brown': 286.0}

print(doAlgo("SELL","SNAP",2000))
#{'James Jones': 387.0, 'Barbara Johnson': 836.0, 'Barbara Brown': 271.0, 'James Williams': 114.0}

print(doAlgo("SELL","GZPRM",300))
#that should return empty dictionary

print(doAlgo("BUY","GZPRM",30))
#that should return
# {'John Brown': 1032, 'William Smith': 362, 'Robert Smith': 769, 'Marry Johnson': 286, 'Robert Williams': 378, 'Marry Williams': 603}

print(doAlgo("BUY","MSFT",300))
#{'John Brown': 103, 'William Smith': 36, 'Robert Smith': 76, 'Marry Johnson': 28, 'Robert Williams': 37, 'Marry Williams': 60}





