# Minecraft World Profile Generator (Prototype Version)

added Minecraft-Overviewer-master/overviewer_core/sw_analysis.py

modified Minecraft-Overviewer-master/overviewer_core/nbt.py

modified Minecraft-Overviewer-master/build/scripts-3.7/overviewer.py

## Abstract

This thing repeats the following tasks: 
1. Generates a minecraft world by starting a server.
2. Stops the server automatically
3. Starts a modified overviewer that produce a world profile image

It includes a modified minecraft server and a modified overviewer.

This is a prototype version. The full version is at another repo.

## To make change to the overviewer script:
### After an overviewer is compiled, go to it's directory (Minecraft-Overviewer-master), and the same folder in this repository.
### Replace two files and add one file: 
- build/scripts-3.7/overviewer.py    replacing the file at build/scripts_generated_for_your_system/overviewer.py;
- overviewer_core/nbt.py    replacing the file in the same place at destination; 
- overviewer_core/sw_analysis.py    should be put in the same folder at destination.
- overviewer_core/tileset.py     replacing the file in the same place at destination

## TextOverlay is at the same folder with Minecraft-Overviewer-master
