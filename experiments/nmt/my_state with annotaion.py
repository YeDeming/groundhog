{
'target':['/home/meepo/summary/GroundHog-master/experiments/nmt/preprocess/binarized_text.cs.shuf.h5'],
'source':['/home/meepo/summary/GroundHog-master/experiments/nmt/preprocess/binarized_text.en.shuf.h5'],
'indx_word':'/home/meepo/summary/GroundHog-master/experiments/nmt/preprocess/ivocab.en.pkl',
'indx_word_target':'/home/meepo/summary/GroundHog-master/experiments/nmt/preprocess/ivocab.cs.pkl',
'word_indx':'/home/meepo/summary/GroundHog-master/experiments/nmt/preprocess/vocab.en.pkl',
'word_indx_trgt':'/home/meepo/summary/GroundHog-master/experiments/nmt/preprocess/vocab.cs.pkl',
'null_sym_source':3500,
'null_sym_target':3500,
'n_sym_source':3501,                  # n_in
'n_sym_target':3501,
'seqlen':140,
'bs':1,
'dim':500,
'rank_n_approx':400,                  #n_hids
'prefix':'search_',
'reload':True,
'hookFreq':500,
'minerr':-11,
'copy_model_freq':10000,
'copy_model_path':'./model/models',
'n_samples':1,
'n_examples':1,
}
