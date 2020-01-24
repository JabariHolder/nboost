
# class => module
MODULE_MAP = {
    'QAModelPlugin': 'plugins.models.qa.base',
    'RerankModelPlugin': 'plugins.models.rerank.base',
    'ShuffleRerankModelPlugin': 'plugins.models.rerank.shuffle',
    'PtBertRerankModelPlugin': 'plugins.models.rerank.pt.bert',
    'TfBertRerankModelPlugin': 'plugins.models.rerank.tf.bert',
    'TfAlbertRerankModelPlugin': 'plugins.models.rerank.tf.albert',
    'PtDistilBertQAModelPlugin': 'plugins.models.qa.pt.distilbert',
}

CLASS_MAP = {
    "shuffle-model": "ShuffleRerankModelPlugin",
    "pt-tinybert-mrpc": "PtBertRerankModelPlugin",
    "pt-tinybert-msmarco": "PtBertRerankModelPlugin",
    "pt-bert-base-uncased-msmarco": "PtBertRerankModelPlugin",
    "tf-bert-base-uncased-msmarco": "TfBertRerankModelPlugin",
    "tf-albert-tiny-uncased-msmarco": "TfAlbertRerankModelPlugin",
    "tf-biobert-base-uncased-msmarco": "TfBertRerankModelPlugin"
}

URL_MAP = {
    "shuffle-model": "https://example.org",
    "tf-bert-base-uncased-msmarco": "https://storage.googleapis.com/koursaros/tf-bert-base-uncased-msmarco.tar.gz",
    "tf-albert-tiny-uncased-msmarco": "https://storage.googleapis.com/koursaros/albert-tiny-uncased-msmarco.tar.gz",
    "tf-biobert-base-uncased-msmarco": "https://storage.googleapis.com/koursaros/biobert-base-uncased-msmarco.tar.gz",
    "pt-tinybert-msmarco": "https://storage.googleapis.com/koursaros/pt-tinybert-msmarco.tar.gz",
    "pt-bert-base-uncased-msmarco":  "https://storage.googleapis.com/koursaros/pt-bert-base-uncased-msmarco.tar.gz",
    "pt-tinybert-mrpc" : "https://storage.googleapis.com/koursaros/pt-tinybert-mrpc.tar.gz",
}

# image => directory
IMAGE_MAP = {
    'alpine': '../Dockerfiles/alpine',
    'tf': '../Dockerfiles/tf',
    'pt': '../Dockerfiles/pt'
}

INDEXER_MAP = {
    'ESIndexer': 'indexers.es'
}
