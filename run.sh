STATE=/home/ydm/GroundHog-master/experiments/nmt/my_state.py
CODE=/home/ydm/GroundHog-master
THEANO_FLAGS=floatX=float32,device=gpu3,mode=FAST_RUN python $CODE/experiments/nmt/train.py --proto prototype_search_state --state $STATE

