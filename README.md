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
Both algorithms are evaluated using the "PongDeterministic-v4" gym environment

### Results
A3C - Top performance in 1 hour 40

<details><summary>Output:</summary>
<p>

```
(ai_assignment3)[ec2-user@ip-172-31-43-253 A3C]$ python main.py 
[2019-04-29 10:19:07,024] Making new env: PongDeterministic-v4
[2019-04-29 10:19:07,321] Making new env: PongDeterministic-v4
[2019-04-29 10:19:07,321] Making new env: PongDeterministic-v4
[2019-04-29 10:19:07,321] Making new env: PongDeterministic-v4
[2019-04-29 10:19:07,322] Making new env: PongDeterministic-v4
[2019-04-29 10:19:07,336] Making new env: PongDeterministic-v4
[2019-04-29 10:19:07,603] Creating monitor directory test
[2019-04-29 10:19:07,827] Starting new video recorder writing to /home/ec2-user/AI_Assignment_2/A3C/test/openaigym.video.0.6408.video000000.mp4
Time 00h 00m 02s, episode reward -21.0, episode length 764
[2019-04-29 10:19:10,348] Starting new video recorder writing to /home/ec2-user/AI_Assignment_2/A3C/test/openaigym.video.0.6408.video000001.mp4
Time 00h 01m 05s, episode reward -21.0, episode length 764
Time 00h 02m 06s, episode reward -21.0, episode length 783
Time 00h 03m 09s, episode reward -21.0, episode length 764
Time 00h 04m 11s, episode reward -21.0, episode length 812
Time 00h 05m 13s, episode reward -21.0, episode length 812
Time 00h 06m 16s, episode reward -21.0, episode length 764
Time 00h 07m 18s, episode reward -21.0, episode length 811
[2019-04-29 10:26:26,757] Starting new video recorder writing to /home/ec2-user/AI_Assignment_2/A3C/test/openaigym.video.0.6408.video000008.mp4
Time 00h 08m 25s, episode reward -21.0, episode length 1324
Time 00h 09m 28s, episode reward -21.0, episode length 824
Time 00h 10m 33s, episode reward -21.0, episode length 1964
Time 00h 11m 40s, episode reward -19.0, episode length 2144
Time 00h 12m 55s, episode reward -21.0, episode length 4384
Time 00h 13m 57s, episode reward -21.0, episode length 824
Time 00h 15m 04s, episode reward -21.0, episode length 2120
Time 00h 16m 12s, episode reward -20.0, episode length 2696
Time 00h 17m 23s, episode reward -4.0, episode length 3318
Time 00h 18m 32s, episode reward -16.0, episode length 3322
Time 00h 25m 20s, episode reward -1.0, episode length 100000
Time 00h 26m 22s, episode reward -21.0, episode length 764
Time 00h 27m 25s, episode reward -21.0, episode length 764
Time 00h 28m 27s, episode reward -21.0, episode length 764
Time 00h 29m 30s, episode reward -21.0, episode length 764
Time 00h 30m 33s, episode reward -21.0, episode length 764
Time 00h 31m 35s, episode reward -21.0, episode length 764
Time 00h 32m 37s, episode reward -21.0, episode length 764
Time 00h 33m 40s, episode reward -21.0, episode length 764
[2019-04-29 10:52:48,010] Starting new video recorder writing to /home/ec2-user/AI_Assignment_2/A3C/test/openaigym.video.0.6408.video000027.mp4
Time 00h 34m 44s, episode reward -21.0, episode length 764
Time 00h 35m 47s, episode reward -21.0, episode length 764
Time 00h 36m 50s, episode reward -21.0, episode length 764
Time 00h 37m 52s, episode reward -21.0, episode length 764
Time 00h 38m 55s, episode reward -21.0, episode length 764
Time 00h 39m 58s, episode reward -21.0, episode length 764
Time 00h 41m 01s, episode reward -21.0, episode length 764
Time 00h 42m 04s, episode reward -21.0, episode length 764
Time 00h 43m 06s, episode reward -21.0, episode length 764
Time 00h 44m 09s, episode reward -21.0, episode length 764
Time 00h 45m 12s, episode reward -21.0, episode length 764
Time 00h 46m 14s, episode reward -21.0, episode length 764
Time 00h 47m 30s, episode reward -21.0, episode length 764
Time 00h 48m 45s, episode reward -21.0, episode length 764
Time 00h 50m 06s, episode reward -21.0, episode length 824
Time 00h 51m 08s, episode reward -21.0, episode length 764
Time 00h 52m 22s, episode reward -21.0, episode length 764
Time 00h 53m 38s, episode reward -21.0, episode length 764
Time 00h 54m 53s, episode reward -21.0, episode length 764
Time 00h 56m 00s, episode reward -21.0, episode length 764
Time 00h 57m 15s, episode reward -21.0, episode length 764
Time 00h 58m 29s, episode reward -21.0, episode length 764
Time 00h 59m 46s, episode reward -21.0, episode length 764
Time 01h 00m 59s, episode reward -21.0, episode length 764
Time 01h 02m 13s, episode reward -21.0, episode length 764
Time 01h 03m 28s, episode reward -21.0, episode length 764
Time 01h 04m 44s, episode reward -21.0, episode length 764
Time 01h 05m 58s, episode reward -21.0, episode length 764
Time 01h 07m 15s, episode reward -21.0, episode length 764
Time 01h 08m 31s, episode reward -21.0, episode length 764
Time 01h 09m 46s, episode reward -21.0, episode length 764
Time 01h 11m 02s, episode reward -21.0, episode length 1730
Time 01h 12m 59s, episode reward -14.0, episode length 3018
Time 01h 15m 05s, episode reward -21.0, episode length 3224
Time 01h 16m 16s, episode reward -21.0, episode length 3224
Time 01h 18m 10s, episode reward -20.0, episode length 2742
Time 01h 19m 46s, episode reward 21.0, episode length 1698
[2019-04-29 11:38:54,061] Starting new video recorder writing to /home/ec2-user/AI_Assignment_2/A3C/test/openaigym.video.0.6408.video000064.mp4
Time 01h 21m 07s, episode reward 20.0, episode length 1849
Time 01h 22m 43s, episode reward 21.0, episode length 1819
Time 01h 24m 16s, episode reward 21.0, episode length 1697
Time 01h 25m 50s, episode reward 21.0, episode length 1697
Time 01h 27m 22s, episode reward 21.0, episode length 1697
Time 01h 28m 57s, episode reward 21.0, episode length 1697
Time 01h 30m 30s, episode reward 21.0, episode length 1697
Time 01h 32m 03s, episode reward 21.0, episode length 1697
Time 01h 33m 37s, episode reward 21.0, episode length 1697
Time 01h 35m 12s, episode reward 21.0, episode length 1697
Time 01h 36m 17s, episode reward 21.0, episode length 1697
Time 01h 37m 52s, episode reward 21.0, episode length 1697
Time 01h 39m 26s, episode reward 21.0, episode length 1697
```

</p>
</details>