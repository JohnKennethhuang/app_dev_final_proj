    for client in customers:
        # sets a variable to the time recorded in each client 
        purchaseHour = client.time
       
       #Grabbing the first and second character from the string that time comes out two and adding them together  
       
        first = purchaseHour[0]
        second = purchaseHour[1]
        hour = first + second 
        hour = int(hour)
        
        # basically a long winded way of adding a point to each of the counters 
        
        if hour == 11:
            amElleven = amElleven + 1 
        elif hour == 12:
            pmTwelve = pmTwelve + 1 
        elif hour == 13:
            pmOne = pmOne + 1 
        elif hour == 14:
            pmTw0 = pmTwo+ 1 
        elif hour == 15:
            pmThree = pmThree+ 1 
        elif hour == 16:
            pmFour = pmFour + 1 
        elif hour == 17:
            pmFive = pmFive + 1 
        elif hour == 18:
            pmSix = pmSix + 1 
        elif hour == 19:
            pmSeven = pmSeven + 1 
        elif hour == 20:
            pmEight = pmEight + 1
        elif hour == 21:
            pmNine = pmNine + 1 
        elif hour == 22:
            pmTen = pmTen + 1      
            
            
    # adding all the variables to a list 
    HOURS = [ "Elleven","Twelve","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]
    hourCounts = [amElleven,pmTwelve,pmOne,pmTwo,pmThree,pmFour,pmFive,pmSix,pmSeven,pmEight,pmNine,pmTen]
    
    currentChamp = 0 
    hourList = ""
    otherChamps = ""
    secondaryChamp = 0
    positionCounter = 0 
    
    for time in HOURS:    
        currentContender = hourCounts[positionCounter]
        if currentContender > currentChamp:
            currentChamp = currentContender
            hourList = time 
            if currentContender > secondaryChamp:
                otherChamps = ""
        elif currentContender == currentChamp:
            secondaryChamp = currentContender
            otherChamps = otherChamps + time + " "
        positionCounter = positionCounter + 1 
            
    print ("\nThe busiest hour of the day is ",hourList,"\nWith other equally as busy hours being: ",otherChamps)
