from configparser import ConfigParser


def dbconfig():
    config = ConfigParser()
    config.read('Tree_code/DB_CONFIG.ini')
    servername= str(config.sections()[0])
    conf_list = list(config[servername])
    db_username = config[servername][conf_list[0]]
    db_password = config[servername][conf_list[1]]
    db_host = config[servername][conf_list[2]]
    db_port = config[servername][conf_list[3]]
    db_service = config[servername][conf_list[4]]
    
    return(db_username,db_password,db_host,db_port,db_service)
