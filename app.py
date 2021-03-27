import base64
import numpy as np
import io
from PIL import Image
import keras
import re
from keras import backend as K
from keras.models import Sequential, load_model
from keras.preprocessing.image import ImageDataGenerator,img_to_array
from keras.preprocessing import image
from flask import Flask,request,jsonify,render_template
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
import cv2
import pickle


import tensorflow as tf

app=Flask(__name__)
def getModel():
    global model
   # model=pickle.load(open('PlantsClassification_FYP.pkl','rb'))
    model=load_model('PlantsClassification_FYP.h5')
    print('Model Loaded Successfully!!!')

def preprocessImage(image,targetSize):
    image=image.resize(targetSize)
    image=img_to_array(image)
    image=np.expand_dims(image,axis=0)
    return image
print('Loading Keras Model...............')
getModel()
@app.route('/')
def home():
    return render_template('index.html')
def convertImage(imgData1):
	imgstr = re.search(r'base64,(.*)',imgData1).group(1)
	#print(imgstr)
	with open('output.png','wb') as output:
		output.write(imgstr.decode('base64'))
@app.route('/predict', methods=['POST'])
def predict():
    file=request.files['file1']
    file.save('static/file.jpg')
    img = image.load_img('static/file.jpg', target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.hstack([x])
    prediction = model.predict(images, batch_size=126)
    print(prediction)
    max_index=np.argmax(prediction)
    print (max_index)
    if(max_index==0):
        response='Anemone_flower'
    elif(max_index==1):
        response='Asparagus'
    elif(max_index==2):
        response='Banana'
    elif(max_index==3):
        response='Chamomile'
    elif(max_index==4):
        response='Chickweed'
    elif(max_index==5):
        response= 'Daffodil_flower'
    elif(max_index==6):
        response= 'Daisy Fleabane'
    elif(max_index==7):
        response= 'Echinacea'                            
    elif(max_index==8):
        response='Hyacinth_flower'
    elif(max_index==9):
        response='Jonquil_flower'
    elif(max_index==10):
        response='Lisianthus_flower'
    elif(max_index==11):
        response='Madagascar_Periwinkle'
    elif(max_index==12):
        response='Mini-Carnation_purple'
    elif(max_index==13):
        response='Mustard'
    elif(max_index==14):
        response='Pickerelweed_flower' 
    elif(max_index==15):
        response= 'Poinsettia_flower'
    elif(max_index==16):
        response='Pompon_flower'
    elif(max_index==17):
        response='Primrose_blue'
    elif(max_index==18):
        response='Protea'
    elif(max_index==19):
        response='Purple_Deadnettle_flower'
    elif(max_index==20):
        response='Ranunculus_flower'
    elif(max_index==21):
        response='Rose_hips'
    elif(max_index==22):
        response='Trachelium_flower'
    elif(max_index==23):
        response='Vervain_Mallow_flower'
    elif(max_index==24):
        response='Waxflower'
    elif(max_index==25):
        response='Wild Grape Vine'
    elif(max_index==26):
        response='Wild Leek'
    elif(max_index==27):
        response='aeonium'
    elif(max_index==28):
        response='agapanthus'        
    elif(max_index==29):
        response='almond'
    elif(max_index==30):
        response='aloe_vera'
    elif(max_index==31):
        response='amaryllis_flower'
    elif(max_index==32):
        response='aster'
    elif(max_index==33):
        response='baby_breath_flower'
    elif(max_index==34):
        response='black_rose_flower'
    elif(max_index==35):
        response='blue_chicory'        
    elif(max_index==36):
        response='blue_vervain'
    elif(max_index==37):
        response='bougainvillea_flower'
    elif(max_index==38):
        response='bromeliad'
    elif(max_index==39):
        response='buttercup_flower'
    elif(max_index==40):
        response='calendula_flower'
    elif(max_index==41):
        response= 'canna'
    elif(max_index==42):
        response='cannabis_flower'        
    elif(max_index==43):
        response='carex'
    elif(max_index==44):
        response='cattails'
    elif(max_index==45):
        response='coconut'
    elif(max_index==46):
        response='cone_flower'
    elif(max_index==47):
        response='coronation_gold'
    elif(max_index==48):
        response='crimson_clover'
    elif(max_index==49):
        response='crocus_blue'
    elif(max_index==50):
        response='Daisy'
    elif(max_index==51):
        response='dandelion'
    elif(max_index==52):
        response='datura_flower'
    elif(max_index==53):
        response='delonix_regia_flower'
    elif(max_index==54):
        response='downy_yellow_violet'
    elif(max_index==55):
        response='elderberry_flower'
    elif(max_index==56):
        response='fireweed_flower'        
    elif(max_index==57):
        response='forget_me_not'
    elif(max_index==58):
        response='golden_champa_flower'
    elif(max_index==59):
        response='harebell_flower'
    elif(max_index==60):
        response='hibiscus_flower'
    elif(max_index==61):
        response='iris_flower'
    elif(max_index==62):
        response='jasmine_flower'
    elif(max_index==63):
        response='joe_pye_weed'        
    elif(max_index==64):
        response='knapweed'
    elif(max_index==65):
        response='larkspur_flower'
    elif(max_index==66):
        response='lily_flower'
    elif(max_index==67):
        response='lotus_flower'
    elif(max_index==68):
        response='mallow_flower'
    elif(max_index==69):
        response='marigold_flower'
    elif(max_index==70):
        response='milk_thistle_flower'                                                    
    elif(max_index==71):
        response='mullein_flower_yellow'
    elif(max_index==72):
        response='mushroom'
    elif(max_index==73):
        response='narcissistic_flower'
    elif(max_index==74):
        response='oleander_flower'
    elif(max_index==75):
        response='orchid_flower'
    elif(max_index==76):
        response='palash_flower'
    elif(max_index==77):
        response='parlor_palm'        
    elif(max_index==78):
        response='prickly_pear_cactus'
    elif(max_index==79):
        response='queen_anne_s_lace_flower'
    elif(max_index==80):
        response='red-hot_poker'
    elif(max_index==81):
        response='red_clover'
    elif(max_index==82):
        response='red_rose'
    elif(max_index==83):
        response='saffron_flower'
    elif(max_index==84):
        response='sedum_purple'        
    elif(max_index==85):
        response='solidago_flower'
    elif(max_index==86):
        response='st_john'
    elif(max_index==87):
        response='statice_flower'
    elif(max_index==88):
        response='sunflower'
    elif(max_index==89):
        response='teasel_flower'
    elif(max_index==90):
        response='touch_me_not_flower'
    elif(max_index==91):
        response='tuberose_flower'        
    elif(max_index==92):
        response='tulip_flower'
    elif(max_index==93):
        response='viola_flower'
    elif(max_index==94):
        response='white_yarrow'
    elif(max_index==95):
        response='wild_bee_balm_flowers'
    elif(max_index==96):
        response='yellow_sow_thistle'
    elif(max_index==97):
        response='yucca'
    elif(max_index==98):
        response='zinnia_flower_red'                    
    else:
         response = "No prediction"
         
    
    return '{Name:'+response+'}'





if __name__ == "__main__":
    app.run(debug=True)

