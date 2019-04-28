# AI Assignment 2

### Environment Setup
```
conda create -n ai_assignment python=2.7
source activate ai_assignment
conda install -c pytorch pytorch==0.3.1 
conda install -c menpo ffmpeg
conda install -c conda-forge opencv
python -m pip install gym==0.9.3
python -m pip install gym[atari]
```

### Running
To run A3C and DCQL cd to the respective directory and run: 
```
python main.py
```

### Details
Both algorithms are evaluated using 
