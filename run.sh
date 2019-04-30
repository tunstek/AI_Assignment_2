#!/bin/sh
conda create -n ai_assignment python=2.7
source activate ai_assignment
conda install -y -c pytorch pytorch==0.3.1
conda install -y -c menpo ffmpeg
conda install -y -c conda-forge opencv
python -m pip install -y gym==0.9.3
python -m pip install -y gym[atari]

#python DQL/main.py &> DQL/out.log & disown
#python DCQL/main.py &> DCQL/out.log & disown
#python A3C/main.py &> A3C/out.log & disown
