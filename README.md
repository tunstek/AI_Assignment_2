#AI Assignment 2

### Environment Setup
```
brew install boost boost-python sdl2

conda create -n ai_assignment python=2.7
source activate ai_assignment
conda install pytorch==0.3.1 -c pytorch
conda install -c conda-forge kivy
conda install -c menpo ffmpeg
python -m pip install gym==0.9.3
```

Then Downgrade the boost version to 1.64:
```
brew edit boost
```
Replace contents with: 
https://raw.githubusercontent.com/Homebrew/homebrew-core/3df9cdfc25f796ec8d3ffd0a0a12476cf6d413d5/Formula/boost.rb

Also downgrade boost-python:
```
brew edit boost-python
```
Replace with:
https://raw.githubusercontent.com/Homebrew/homebrew-core/d22f78c56a1c7d8e711a407c2dae5fc42f4ae6c2/Formula/boost-python.rb

If you receive an dependancy error for python from brew, try changing 'python3' to 'python' in the boost-python formula. if the error persists: remove the dependancy line but ensure python is installed

Then:

```
brew reinstall boost boost-python
python -m pip install ppaquette-gym-doom doom_py
```
