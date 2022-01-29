import os 
import datetime

day =(datetime.datetime.now()-datetime.timedelta(hours=3)).strftime("%Y-%m-%d") 

def create_files():
    files = [ 'logo','frame']
    try:
        os.mkdir('import')
        os.mkdir('photos')
    except:
        pass
    
    
    for i in files:
        try:    
            os.mkdirs('import/'+i)
        except:
            pass

# os.getcwd()