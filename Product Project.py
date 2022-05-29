import random
import math
# Money making game, Lemonade Stand style!

# Initial variables
cash = float (10.00)
raw_material = 0
raw_material_max = 5
finished_product = 5
finished_product_max = 30
day = 0
day_num = 1

# Introduction
print('Hi, in this game, your goal is to make as much money by the end of 10 days as possible.')
print('At the 9th and 10th day, you will not be able to buy raw material.')
print('At the end of each day, all your raw material will be processed into finished product.')
print('Best of luck & become a millionaire!')
print('')


# While loop (Condition of days before game ends)
while day < 10 : 
    # First week!
    if day <= 7:
        
        # Random prices set for all 
        raw_material_price =  float('{:.2}' .format(random.uniform(1.00,12.00)))
        finished_product_price = float('{:.2}' .format(random.uniform(1.00,12.00)))
        
        # Selling finished product and you can choose not to sell
        print('-----Day', day_num,'-----')
        print('')

        print('Here is how much money you have:', str(cash))

        print('How much finished product would you like to sell? (max:',str(finished_product)+')')
        print('Right now, one finished product sells for: $', finished_product_price)
        finished_product_sell = int(input())

        if finished_product_sell < finished_product:
            cash = cash + (finished_product_sell * float(finished_product_price))
            finished_product = finished_product - finished_product_sell 
        elif finished_product_sell >= finished_product:
            cash = cash + (finished_product * float(finished_product_price))
            finished_product = 0
        elif finished_product_sell == 0:
            finished_product = finished_product
            cash = cash

        # Raw material purchasing 
        raw_material_can = int(cash/raw_material_price)
        if raw_material_can > raw_material_max:
         print('How much raw material do you want to buy? (max:', str(raw_material_max)+')')
        elif raw_material_can < raw_material_max:
            print('How much raw material do you want to buy? (max:', str(raw_material_can)+')')
        print('Right now, one raw material costs: $',raw_material_price)

        raw_material_buy = int(input())

        if raw_material_buy >= raw_material_can:
            raw_material = raw_material_max
            cash += - (raw_material_can * float(raw_material_price))
        elif raw_material_buy < raw_material_can:
            raw_material += raw_material_buy
            cash += - (raw_material_buy * float(raw_material_price))
        elif raw_material_buy == 0:
            raw_material = raw_material

        if cash >= 0:
            if raw_material >= 2:
                finished_product += raw_material*2
                raw_material = 0 
            elif raw_material==1:
                finished_product += raw_material*2 
                raw_material = 0
            elif raw_material == 0:
                finished_product = finished_product
            if finished_product > finished_product_max:
                finished_product = finished_product_max
                
            # Summary 
            raw_mats_used = raw_material_buy
            finished_product_produced = raw_mats_used * 2
            print('raw materials used:',raw_mats_used)
            print('Finished product produced:', finished_product_produced)
            

            print(raw_material,'raw material available')
            print(finished_product,'finished product available')
            print('$'+ '{:.200}' .format(str(cash)))

            day += 1
            day_num +=1
            print ('')
        else:
            print('You cannot have negative money.')
            
    
    # Last few days raw material cannot be purchased, similar to above part 
    elif day > 7:

        raw_material_price = '{:.2}' .format(random.uniform(1.00,12.00))
        finished_product_price = '{:.2}' .format(random.uniform(1.00,12.00))

        print('-----Day', day_num,'-----')
        print('')

        print('Here is how much money you have:', str(cash))

        print('How much finished product would you like to sell? (max:',str(finished_product)+')')
        print('Right now, one finished product sells for: $', finished_product_price)
        finished_product_sell = int(input())

        if finished_product_sell < finished_product:
            cash = cash + (finished_product_sell * float(finished_product_price))
            finished_product = finished_product - finished_product_sell 
        elif finished_product_sell >= finished_product:
            cash = cash + (finished_product * float(finished_product_price))
            finished_product = 0
        elif finished_product_sell == 0:
            finished_product = finished_product
            cash = cash

        if cash>=0:
            if raw_material>=2:
                finished_product += raw_material*2
                raw_material = raw_material - finished_product/2
            elif raw_material==1:
                finished_product += raw_material*2
                raw_material = 0
            elif raw_material == 0:
                finished_product = finished_product              
                
            raw_mats_used = raw_material_buy
            finished_product_produced = raw_mats_used*2
            
            print('raw materials used:',raw_mats_used)
            print('Finished product produced:', finished_product_produced)
            

            print(raw_material,'raw material available')
            print(finished_product,'finished product available')
            print('$'+ '{:.200}' .format(str(cash)))

            day += 1
            day_num +=1
            print ('')
            
        else:
            print('You cannot have negative money.')
            
    # Last day everything from your stock is used. 
    elif day == 9 :

            print ('-----Day 10-----')
            finished_product_thrown = finished_product_max-finished_product
            raw_mats_used = finished_product/2
            finished_product_produced = finished_product + finished_product_thrown
            print('raw materials used:',raw_mats_used)
            print('Finished product produced:', finished_product_produced)
            
#Results 
print('Your entrepreneural adventure is over friend. Here is your total cash amount. Good job!')
print('$'+ '{:.200}' .format(str(cash)))