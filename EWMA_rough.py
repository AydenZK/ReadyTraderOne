bid_prices = [5,4,3,2,1]
ask_prices = [5,6,7,8,9]

EWMA = 0.
riskLambda = .94
periodicReturns = []
periodicVariance = []


executed = (np.array(bid_prices) >= np.array(ask_prices))
print(executed)

# check if the best bid price exceeds the best ask price

if(variation[0]>=0):
    if(periodicReturns):
        periodicReturns.append(bid_prices[0]/periodicReturns[periodicReturns.len-1])
    else:
        periodicReturns.append(bid_prices[0])
        
    periodicVariance.append(np.var(periodicReturns))
    
    print(periodicVariance)