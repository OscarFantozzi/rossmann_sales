import pickle
import pandas as pd
from flask             import Flask, request
from Rossmann import Rossmann
import os

# loading model
model = pickle.load( open( 'trained_model.pkl' , 'rb') )

# initialize api
app = Flask( __name__ )

@app.route( '/rossmann/predict', methods = ['POST'] )
def rossmann_predict():
    test_json = request.get_json()
    
    if test_json: # se tiver dados
        if isinstance( test_json, dict ): # se tiver chave - valor
            
            test_raw = pd.DataFrame( test_json, index = [0] ) # trato como única linha
            
        else:
            
            test_raw = pd.DataFrame( test_json, columns = test_json[0].keys() )
            
            # instancia classe rossmann
            pipeline = Rossmann()
            
            # data cleaning
            df1 = pipeline.data_cleaning( test_raw )
            
            # feature engineering
            df2 = pipeline.feature_engineering( df1 )
            
            # data preparation
            df3 = pipeline.data_preparation( df2 )
            
            # prediction
            df_response = pipeline.get_prediction( model, test_raw, df3 )
            
            return df_response
            
    else:
        return Response( '{}', status = 200, mimetype = 'application/json' )

if __name__ == '__main__':
    port = os.environ.get( 'PORT', 5000 ) 
    app.run( host = 'https://api-rossmann-384417.wm.r.appspot.com/', port = port )
