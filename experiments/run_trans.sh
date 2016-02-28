#!/bin/sh
set -ex

if [ $# -ne 6 ];
then
	echo "usage: $0 [source input] [output] [model_state] [model file] [beam size] [cpu|gpu0|gpu1|..]"
	exit 1
fi

SOURCE=$1
OUTPUT=$2
MODEL_STATE=$3
MODEL=$4
BEAM_SIZE=$5
GPU=$6
CODE=/home/meepo/summary/GroundHog-master

PYTHONPATH=$CODE THEANO_FLAGS=floatX=float32,device=$GPU python $CODE/experiments/nmt/sample.py --state $CODE/experiments/nmt/$MODEL_STATE --beam-search --beam-size $BEAM_SIZE --source $CODE/experiments/nmt/$SOURCE --trans $CODE/experiments/nmt/$OUTPUT $CODE/experiments/nmt/$MODEL --ignore-unk
