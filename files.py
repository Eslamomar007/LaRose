import os 
import datetime

day =(datetime.datetime.now()-datetime.timedelta(hours=3)).strftime("%Y-%m-%d") 

def create_files():
    files = ['photos', 'logo','frame']
    try:
        os.mkdir('import')
    except:
        pass
    
    
    for i in files:
        try:    
            os.mkdirs('import/'+i)
        except:
            pass

# os.getcwd()