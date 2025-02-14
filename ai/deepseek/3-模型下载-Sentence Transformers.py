from modelscope import snapshot_download

cache_root_dir = snapshot_download(model_id='sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2',
                                   cache_dir='/Users/hrenxiang/Documents/company/ai')

print(f'下载已完成，目录为：{cache_root_dir}')
