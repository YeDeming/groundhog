{
'target':['/home/ydm/data/binarized_text.title.shuf.h5'],
'source':['/home/ydm/data/binarized_text.article.shuf.h5'],
'indx_word':'/home/ydm/data/ivocab.article.pkl',
'indx_word_target':'/home/ydm/data/ivocab.title.pkl',
'word_indx':'/home/ydm/data/vocab.article.pkl',
'word_indx_trgt':'/home/ydm/data/vocab.title.pkl',
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
