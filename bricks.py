import random 
bricks = [] 
difference_brick = random.randint(0,11)
fake = ''

#CREATE 11 SAME BRICKS AND ONE heavier or lighter
for i in range(12):  
    if i != difference_brick:
        bricks.append(100)
    else:
        bricks.append(random.choice([50,150]))   

#....................FUNCTIONs............................................
def heavier_is_fake(val1,val2,index_val1,index_val2):
    index_val1 = index_val1 + 1
    index_val2 = index_val2 + 1
    if val1 > val2: 
        return f'Fake brick is brick number {index_val1} and its HEAVER '
    if val2 > val1:  
        return f'Fake brick is brick number {index_val2} and its HEAVER '

def lighter_is_fake(val1,val2,index_val1,index_val2):
    index_val1 = index_val1 + 1
    index_val2 = index_val2 + 1
    if val1 < val2: 
        return f'Fake brick is brick number {index_val1} and its LIGHTER '
    if val2 < val1:  
        return f'Fake brick is brick number {index_val2} and its LIGHTER '      

print(f'Current bricks are:{bricks} kg')  

#SPLIT INTO THREE GROUPS
bricks_1_2_3_4 = bricks[0] + bricks[1] + bricks[2] + bricks[3]
bricks_5_6_7_8 = bricks[4] + bricks[5] + bricks[6] + bricks[7]
bricks_9_10_11_12 = bricks[8] + bricks[9] + bricks[10] + bricks[11]

# COMPARING BRICKS{1,2,3,4} AND {5,6,7,8}
if bricks_1_2_3_4 == bricks_5_6_7_8: 
    bricks_8_9 = bricks[7] + bricks[8]
    bricks_10_11 = bricks[9] + bricks[10]
    if bricks_8_9 == bricks_10_11:
        #WEIGHT BRICK 12 WITH ANY OTHER BRICK TO CHECK IF ITS A LIGHTER OR HEAVER 
        if bricks[0] > bricks[11]: 
            fake = f'Fake brick is brick number 12 and its LIGHTER'
        else: 
            fake = f'Fake brick is brick number 12 and its HEAVER '

    if bricks_8_9 > bricks_10_11:
        if bricks[9] == bricks[10]:
           fake = f'Fake brick is brick number 9 and its HEAVER '
        else: 
            fake = lighter_is_fake(bricks[9],bricks[10],9,10)              

    if bricks_8_9 < bricks_10_11:
        if bricks[9] == bricks[10]: 
            fake = f'Fake brick is brick number 9 and its LIGHTER'
        else:     
            fake = heavier_is_fake(bricks[9],bricks[10],9,10)

if bricks_1_2_3_4 > bricks_5_6_7_8:
    bricks_1_2_5 = bricks[0] + bricks[1] + bricks[4] 
    bricks_3_6_9 = bricks[2] + bricks[5] + bricks[8]

    if bricks_1_2_5 == bricks_3_6_9: 
        if bricks[6] == bricks[7]: 
            fake = f'Fake brick is brick number 4 and its HEAVER '
        else:
            fake = lighter_is_fake(bricks[6],bricks[7],6,7)              

    if bricks_1_2_5 > bricks_3_6_9:
        if bricks[0] == bricks[1]: 
            fake = f'Fake brick is brick number 6 and its LIGHTER'   
        else:
            fake = heavier_is_fake(bricks[0], bricks[1],0,1)              
                
    if bricks_1_2_5 < bricks_3_6_9: 
        if bricks[4] < bricks[8]:
            fake = f'Fake brick is brick number 5 and its LIGHTER'
        if bricks[4] == bricks[8]:
            fake = f'Fake brick is brick number 3 and its HEAVER'
       
if bricks_1_2_3_4 < bricks_5_6_7_8:
    bricks_5_6_1 = bricks[4] + bricks[5] + bricks[0]
    bricks_7_2_9 = bricks[6] + bricks[1] + bricks[8]

    if bricks_5_6_1 == bricks_7_2_9: 
        if bricks[2] == bricks[3]: 
            fake = f'Fake brick is brick number 8 and its HEAVER'
        else: 
            fake = lighter_is_fake(bricks[2],bricks[3],2,3)              

 
    if bricks_5_6_1 > bricks_7_2_9:
        if bricks[4] == bricks[5]:
            fake = f'Fake brick is brick number 2 and its LIGHTER'
        else: 
            fake = heavier_is_fake(bricks[4],bricks[5],4,5)

    if bricks_5_6_1 < bricks_7_2_9: 
        if bricks[0] == bricks[8]: 
            fake = f'Fake brick is brick number 7 and its HEAVER ' 
        else: 
            fake = f'Fake brick is brick number 1 and its LIGHTER ' 

print(fake)