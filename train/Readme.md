## Training

This part of code will train a model to choose proper bitrates for future video chunks.

### To Run
1) Put training data and testing data (optional) in `cooked_traces` and `cooked_test_traces` respectively.
2) Run `python3 get_video_sizes.py`
3) Choose proper parameters in `main.py`, such as `workers`, `gpu`, `lr`, `NN_MODEL` and etc.
4) Run `python3 main.py`
