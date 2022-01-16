#!C:\Users\yangm\Anaconda3\python.exe
import os
from PIL import Image
import numpy as np
import copy


##biome keyword
kw_snow = ['snow','jagged','ice','frozen']
kw_dry = ['savanna','desert','badland']


# to percentage string
def topercentage(n,r=2):
    return str(round(n*100,r))+'%'

def ntorgb(li):
    for i in range(len(li)):
        n = li[i][1]
        if n == 0:
            c = (255,255,255)
        elif n == 1:
            c = (51,255,51)
        elif n == 2:
            c = (0,128,255)
        elif n == 3:
            c = (255,51,255)
        elif n == 4:
            c = (255,128,0)
        elif n >= 5:
            c = (255,0,0)
        li[i][1] = c
    return li

index = 5

f1 = open(f'saved/worldsummary{index}.txt','r').readlines()
f2 = open(f'saved/worldrarity{index}.txt','r').readlines()
'BIOMES,EB,GB,SP,CS,Ustructure,ore_types,am/tot_ore,dm/tot_ore,gd/tot_ore,em/tot_ore,bn/tot_ore,cp/tot_ore,ir/tot_ore,cl/tot_ore,lp/tot_ore,rs/tot_ore,stone/tot_surf,soil/tot_surf,veggies/tot_surf,water/tot_surf,ores/tot_surf,sandy/tot_surf,snow/tot_surf'

sindex = ['Biomes','','','Spawner','Chest','Structures','Ores','Amethyst','Diamond','Gold','Emerald','Bone','Copper','Iron','Coal','Lapis','Redstone','a_stone','a_soil','a_veggies','a_water','a_ores','a_sand','a_snow']
summary = []
for f in f1:
    summary.append(eval(f))



d_summary = {}
'''for i in range(len(summary)):
    if type(summary[i])!= list:
        d_summary[summary[i]] = sindex[i]'''
for i in range(len(summary)):
    if i in range(3,5) or i > 7: 
        d_summary[summary[i]] = sindex[i]

rindex = []
rarity = []
for f in f2:
    i = 0
    space = f.find(' ')
    rindex.append(f[:space])
    rarity.append(eval(f[space:]))


# area\n land ratio\n water ratio\n another ratio\n ALL biomes with rarity colored
area = (21*21*16*16)
waterratio = summary[20]
#print(area,waterratio,area*waterratio)

others = summary[17:20]+summary[21:]
a_print = [[['area',f'{area}m\u00b2'],0],[['land coverage',topercentage(1-waterratio)],0],[['water coverage',topercentage(waterratio)],0],[[d_summary[max(others)][2:]+' coverage',topercentage(max(others))],0]]


for i in range(7,24):
    summary[i] = topercentage(summary[i])

coral = 0
b_print = []
summary0_cp = copy.deepcopy(summary[0])
for b in rarity[0]:
    b_print.append([b[0],b[1]])
    summary0_cp.remove(b[0])
    if 'warm_ocean' in b[0]:
        coral = 1

for b in summary0_cp:
    b_print.append([b,0])






'''res_print = list(zip(list(zip(sindex[7:17],summary[7:17])),rarity[4:14]))
print(res_print)'''
res_print = []
for i in range(10):
    res_print.append([[sindex[i+7],summary[i+7]],rarity[i+4]])



s_print = []
summary5_cp = copy.deepcopy(summary[5])
for s in rarity[1]:
    s_print.append([s[0],s[1]])
    summary5_cp.remove(s[0])

for s in summary5_cp:
    s_print.append([s,0])

#print(s_print)
# simple biome rarity score and structure rarity score, could use sum(1/p[i])
r_n = [len(rarity[0]),len(rarity[1])]

# sort biomes by season
snow,dry = 0,0
for bio in summary[0]:
    for k in kw_snow:
        if k in bio:
            snow = 1
    for k in kw_dry:
        if k in bio:
            dry = 1

# simple season rarity score
#print(snow+dry)


# simple ore rarity score
metal_r = 0
gem_r = 0
for type in res_print:
    if type[1] > 0:
        if type[0][0] in 'AmethystDiamondEmeraldRedstoneLapis':
            gem_r += 1
        if type[0][0] in 'GoldIronCopper':
            metal_r += 1
#print(metal_r,gem_r)


# sum up for column 3:

f_print = copy.deepcopy(s_print)
if metal_r > 0:
    f_print.append(['more metal',metal_r])
if gem_r > 0:
    f_print.append(['more gem',gem_r])
if (snow+dry) > 0:
    f_print.append(['multiclimate',snow+dry])
if rarity[14] > 0:
    f_print.append(['biome diversity',rarity[14]])
if rarity[2] > 0:
    f_print.append(['more spawners',rarity[2]])
if rarity[3] > 0:
    f_print.append(['more chests',rarity[3]])
if len(rarity[0]) >= 2:
    f_print.append(['uncommon biomes',len(rarity[0])-1])
if len(rarity[1]) >= 2:
    f_print.append(['uncommon structures',len(rarity[1])-1])
if coral == 1:
    f_print.append(['corals',2])

biorarity = 0
cb = 3
for b in rarity[0]:
    biorarity += cb**b[1]

print(biorarity,int(round(np.log(biorarity)/np.log(cb))),[cb**i for i in range(7)])

print(rarity[0])
'''print('')
print(ntorgb(a_print))
print('')
print(ntorgb(b_print))
print('')
print(ntorgb(res_print))
print('')
print(ntorgb(f_print))
print('')'''


# if coral biome + coral


'''image = Image.open('textures/test_map.png')

image = image.resize((6000,6000))

image.save('textures/test_map_sm.png','PNG')'''


'''image = Image.new('RGBA',(400,400))

array = np.asarray(image)

for i in range(400):
    for j in range(400):
        a = abs(1-min((i/200-1)**2+(j/200-1)**2,1))
        array[i,j] += np.array((255,255,255,int(round(a*255,0))),dtype='uint8')

image = Image.fromarray(array)

image.save('textures/glow_circle.png','PNG')


image = Image.new('RGBA',(400,400))

array = np.asarray(image)

for i in range(400):
    for j in range(400):
        a = 1-abs(j-200)/200
        array[i,j] += np.array((255,255,255,int(round(a*255,0))),dtype='uint8')

image = Image.fromarray(array)

image.save('textures/glow_wall.png','PNG')'''