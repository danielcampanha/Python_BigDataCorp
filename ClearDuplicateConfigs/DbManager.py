
## Read Me ##
## File of connection of file "ClearDuplicateConfigs", this code returns all Group Configurations that contais the object of other file ##

import pymongo
from bson.objectid import ObjectId


class DbManager:
    mongo_login = 'login'
    mongo_passwd = 'password'
    mongo_host = 'host-dsn'
    mongo_port = 'port'
    mongo_database = 'database'
    mongo_auth_db = 'auth_db'


    def get_all_groupsconfig():
        client = pymongo.MongoClient(
            'mongodb://' + DbManager.mongo_login + ':' + DbManager.mongo_passwd + '@' + DbManager.mongo_host + ':' + DbManager.mongo_port + "/" + DbManager.mongo_auth_db)

        db = client[DbManager.mongo_database]
        group_configs = db.GroupConfiguration

        # cursor = group_configs.find()
        #
        # groups = []
        #
        # for document in cursor:
        #     groups.append(document)

        groups = list(group_configs.find({}))

        return groups

    def update_group_config(group_id, questions, infotype_config):
        client = pymongo.MongoClient(
            'mongodb://' + DbManager.mongo_login + ':' + DbManager.mongo_passwd + '@' + DbManager.mongo_host + ':' +
            DbManager.mongo_port + "/" + DbManager.mongo_auth_db)

        db = client[DbManager.mongo_database]
        group_configs = db.GroupConfiguration

        group_configs.update({"_id": ObjectId(group_id)}, {'$set': {"QuestionsConfigurations": questions,
                                                              "InfoTypeConfigurations": infotype_config}})
