from elasticsearch import Elasticsearch
from RPA.Robocorp.Vault import Vault

class ElasticLibrary:

    def __init__(self):
        self.es = None

    def elastic_authenticate(self):
        secrets = Vault().get_secret("elastic")
        self.es = Elasticsearch(
            cloud_id=secrets["cloud_id"],
            http_auth=(secrets["username"], secrets["password"])
        )
        response = self.es.info()
        return response

    def elastic_index(self, name:str, document:dict):
        response = self.es.index(
            index=name,
            document=document
        )
        return response

    def elastic_refresh_index(self, name:str):
        response = self.es.indices.refresh(index=name)
        return response

    def elastic_search(self, index:str, query:dict):
        response = self.es.search(
            index=index,
            query={
                'match': query
            }
        )
        return response