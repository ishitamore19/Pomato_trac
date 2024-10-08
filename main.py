import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model


#Tensor flow model Prediction
def model_prediction(test_image):
    loaded_model = load_model(r"C:\Users\ishit\OneDrive\Desktop\Project\Plant_disease_detector_copy/trainn_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image into batch
    prediction = loaded_model.predict(input_arr)
    result_index = np.argmax(prediction)
    return result_index




#Sidebar:

st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","About","Disease Recognition","Prevention"])

#Home page
if(app_mode=="Home"):
    st.header("POMATO TRAC")
    image_path = "home_bg.jpg"
    st.image(image_path,use_column_width=True)
    st.markdown(""" Welcome to the Plant Disease Recognition System! 🌿🔍
    
    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    ### How It Works
    1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results:** View the results and recommendations for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Disease Recognition** page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
                """ )
    

 #About page
elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
                #### About Dataset
                This dataset is recreated using offline augmentation from the original dataset.The original dataset can be found on this github repo.
                This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 10 different classes.The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure.
                
                """) 
    st.header("About our website")
    st.markdown("""
                 
                Introducing a cutting-edge platform for efficient potato and tomato leaf detection. Our website utilizes advanced image processing algorithms to swiftly identify and classify plant leaves, aiding farmers and researchers in crop management and disease diagnosis. Harnessing the power of artificial intelligence, our user-friendly interface delivers rapid and accurate results, empowering users to make informed decisions for optimal agricultural outcomes
                
                """)
#Prediction Page:
elif(app_mode=="Disease Recognition"):
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")
    if(st.button("Show Image")):
        st.image(test_image,width=4,use_column_width=True)
    #Predict button
    if(st.button("Predict")):
        st.write("Our Prediction")
        result_index = model_prediction(test_image)

        #define class:
        class_name = [ 'Potato___Late_blight',
 'Potato___healthy',
 'Tomato_Bacterial_spot',
 'Tomato_Early_blight',
 'Tomato_Late_blight',
 'Tomato_Leaf_Mold',
 'Tomato_Septoria_leaf_spot',
 'Tomato_Spider_mites_Two_spotted_spider_mite',
 'Tomato__Tomato_YellowLeaf__Curl_Virus',
 'Tomato_healthy']
        st.success("Model is Predicting it's a {}".format(class_name[result_index]))       

elif(app_mode=="Prevention"):
    st.header("1)Potato Late Blight")
    st.markdown("""
                 Crop Rotation: Rotate potato crops with non-host plants to reduce the buildup of the pathogen in the soil.
                Fungicide Application: Regularly apply fungicides approved for late blight control, following label instructions and local regulations. Fungicides containing active ingredients such as copper compounds, mancozeb, or chlorothalonil are commonly used.
                """)
    st.header("2)Tomato Bacterial spot")
    st.markdown("""
                 Healthy Seedlings: Start with healthy seedlings from reputable sources. Avoid purchasing or planting seedlings with symptoms of bacterial spot.
                Sanitation: Practice good sanitation in the greenhouse and field. Remove and destroy any infected plant debris promptly to reduce the survival and spread of the bacterium.
                """)
    st.header("3)Tomato Early blight")
    st.markdown("""
                 Spacing and Pruning: Proper spacing between plants and pruning to improve airflow can reduce humidity around the plants, making conditions less favorable for fungal growth.
                Weed Control: Keep the area around tomato plants free from weeds, as they can harbor fungal spores and increase humidity.
                """)
    st.header("4)Tomato Late blight")
    st.markdown("""
                 Cultural Practices: Avoid working in the garden when foliage is wet, as this can spread late blight spores. Additionally, stake or cage tomato plants to keep them off the ground and reduce contact with soil-borne pathogens.
                Weather Monitoring: Be vigilant during periods of cool, wet weather, as these conditions are favorable for late blight development. Monitor weather forecasts and disease prediction models to time fungicide applications effectively.
                """)
    st.header("5)Tomato Leaf Mold")
    st.markdown("""
                 Fungicide Application: Apply fungicides preventatively, especially during periods of high humidity or when leaf mold is known to be prevalent in your area. Fungicides containing active ingredients such as chlorothalonil or copper can help protect tomato plants from leaf mold.
                Weather Monitoring: Be aware of weather conditions that favor the development of leaf mold, such as high humidity and warm temperatures. Monitor weather forecasts and disease prediction models to time fungicide applications effectively.
                """)
    st.header("6)Tomato Septoria leaf spot")
    st.markdown("""
                Sanitation: Remove and destroy infected plant debris promptly to reduce the source of inoculum. This includes fallen leaves and any other infected plant material.
                Fungicide Application: Apply fungicides preventatively, especially during periods of high humidity or when septoria leaf spot is known to be prevalent in your area. Fungicides containing active ingredients such as chlorothalonil or copper can help protect tomato plants from this disease.
                """)
    st.header("7)Tomato Spider mites Two spotted spider mite")
    st.markdown("""
                Quarantine New Plants: Inspect new plants before introducing them into the garden to prevent introducing spider mites or other pests.
                Crop Rotation: Rotate tomato crops with non-host crops to disrupt the life cycle of spider mites and reduce the buildup of populations in the soil. 
                """)
    st.header("8)Tomato Tomato YellowLeaf Curl_Virus")
    st.markdown("""
            Insecticide Application: In severe cases, consider applying insecticides labeled for use against whiteflies to reduce their populations. Follow label instructions carefully and avoid harming beneficial insects.
            Integrated Pest Management (IPM): Implement an integrated approach to pest management that combines cultural practices, biological control, and chemical control methods to effectively manage TYLCV and whiteflies. 
                """)
    