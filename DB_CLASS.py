from mandrill_mail import mandrillClass
import MySQLdb
import sys
from  logmonitor import logmonitor
import env

global environment
environment = env.environment

class DB_CLASS :

    global host,user,passwd,database


    if environment == 'development' :
        host = "127.0.0.1" # hostname
        user = "root" # username to be entered
        passwd = "root" # password to be entered
        database = "msg91_betatest" # name of the data base

                
    def connectMongoDb(self,hostName,userName,password,dbName):
        #from pymongo import MongoClient
        import pymongo
        try :
            hostName += ",mongo.localhost.com:10006"
            uri = "mongodb://"+str(userName)+":"+str(password)+"@"+str(hostName)+"/admin"
            conn = pymongo.MongoClient(uri)
            #conn = pymongo.MongoClient(hostName)        
            #auth = conn[dbName].authenticate(userName,password)

        except Exception as ins:
            print "Error" + str(ins)
            msgDic = {}
            msgDic['subject'] = "Exception Error"
            msgDic['from'] = "connectMongoDb@DBCLASS.com"
            msgDic['to'] = "kadamb@kaluskar"
            msgDic['message']  = ins
            mailObj = mandrillClass()
            mailObj.mandrillMail(msgDic)
            return False
            
        
        return conn[dbName]
    
    #- this function will connect with mysql
    def connectMysqlDb(self):
        try :
            db_var = MySQLdb.connect(host = hostName, # hostname
                user = userName, # username to be entered
                passwd = password, # password to be entered
                db = dbName # name of the data base
                )

        except Exception as ins:
            msgDic = {}
            msgDic['subject'] = "Exception Error"
            msgDic['from'] = "connectMongoDb@DBCLASS.com"
            msgDic['to'] = "kadamb@kaluskar.com"
            msgDic['message']  = ins
            mailObj = mandrillClass()
            mailObj.mandrillMail(msgDic)
            return False
        
        return db_var
