#!/usr/bin/env bash
import requests
from hdbcli import dbapi

class mdundo_hana():
    def __init__(self):
        self.key='pyraxuserkey'
        self.fetch_data()
        
    def hana_conn(self):
        try:
            conn = dbapi.connect(key=self.key)
            print('connected')
        except Exception as e:
            print(e)
        finally:
            return conn
    
    def fetch_data(self):
        """Fetches the data from the database."""
        cursor = self.hana_conn().cursor()
        sql_command = "select * from hotel.customer;"
        
        try:
            cursor.execute(sql_command)
            rows = cursor.fetchall()
        except Exception as e:
            print ("Error fetching data from database: ", e.message)
        finally:
            for row in rows:
                for col in row:
                    print ("%s" % col, end=" ")
                print(" ")
                
            cursor.close()
            print ("\n")

if __name__=='__main__':
    mdundo_hana()