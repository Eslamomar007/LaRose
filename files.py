import os 
import datetime

day =(datetime.datetime.now()-datetime.timedelta(hours=3)).strftime("%Y-%m-%d") 

def create_files():
    files = ['','photos', 'logo','frame']
    for i in files:
        try:
            os.mkdir('import')
        except:
            pass
        try:    
            os.mkdirs('import/'+i)
        except:
            pass

# os.getcwd()