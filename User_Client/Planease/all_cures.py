"""This file contains a dictionary cures which contains cure for the diseases as predicted in the model."""

def add_cure(name, method):
    global cures
    cures[name] = method


def get_cure(name):
    """Returns the cures of a disease <name> as a string"""
    global cures
    if name not in cures: return ""
    return_str = """"""
    for i in range(len(cures[name])):
        return_str = return_str + str(i+1)+") " + cures[name][i]+ "\n"
    return_str = return_str[:-1]
    return return_str

#Make empty dictionary
cures = {}
classes = ['Apple-scab', 'Apple-Black rot', 'Apple-Cedar apple rust', 'Apple-healthy', 'Blueberry-healthy', 'Cherry-Powdery mildew', 'Cherry-healthy', 'Corn-Cercospora leaf spot Gray leaf spot', 'Corn-Common rust', 'Corn-Northern Leaf Blight', 'Corn-healthy', 'Grape-Black rot', 'Grape-Esca (Black Measles)', 'Grape-Leaf blight (Isariopsis Leaf Spot)', 'Grape-healthy', 'Orange-Haunglongbing (Citrus greening)', 'Peach-Bacterial spot', 'Peach-healthy', 'Pepper, bell-Bacterial spot', 'Pepper, bell-healthy', 'Potato-Early blight', 'Potato-Late blight', 'Potato-healthy', 'Raspberry-healthy', 'Soybean-healthy', 'Squash-Powdery mildew', 'Strawberry-Leaf scorch', 'Strawberry-healthy', 'Tomato-Bacterial spot', 'Tomato-Early blight', 'Tomato-Late blight', 'Tomato-Leaf Mold', 'Tomato-Septoria leaf spot', 'Tomato-Spider mites Two-spotted spider mite', 'Tomato-Target Spot', 'Tomato-Tomato Yellow Leaf Curl Virus', 'Tomato-Tomato mosaic virus', 'Tomato-healthy']
#Keep adding cures like
#add_cure("<name of disease>", [<methods as individual strings. Each element of list is one method>])
add_cure("Apple-scab", ["Remove and destroy affected leaves", 
                                "Apply zinc and urea(or some other notrogen source)", 
                                "Make sure that leaves stay dry for as long as possible", 
                                "In rainy or humid season, use fetilizers like fixed copper or simple materials like neem(or mineral) oil"])
add_cure("Apple-Black rot", ["Since, this disease spreads due to dead and decaying material, prune out dead or diseased branches", 
                               "Remove infected plant material from the area",
                               "Captan and sulfur products are labeled for control of black rot. However, these sprays will not control or prevent infection of branches."])
add_cure("Apple-Cedar apple rust", ["Dispose of fallen leaves from under the trees", 
                                      "Rust on infected trees can be controlled by spraying plants with a weak copper solution", 
                                      "Apply preventative, disease-fighting fungicides labeled for use on apples weekly, starting with bud break"])
add_cure("Cherry-Powdery mildew", ["Keep short irrigation sets such that leaves do not get wet", 
                                     "Remove and destroy sucker shoots", 
                                     "Bicarbonate-based products will help in chemical control"])
add_cure("Corn-Cercospora leaf spot Gray leaf spot", ["Crop rotation will help in reducing amount of inoculum", 
                                                       "Fungicides containing pyraclostrobin will surely help",
                                                        "Weed control will allow airflow"])
add_cure("Corn-Common rust", ["Fungicides can be beneficial, especially if applied early", "Best management practice is to use resistant varieties"])
add_cure("Corn-Northern Leaf Blight", ["Use of resistant hybrids", 
                                         "Fungicides may be warranted on inbreds for seed production during the early stages of this disease", 
                                         "Make sure the crop does not stay wet for long periods of time"])
add_cure("Grape-Black rot", ["Infected prunings and mummified berries should be removed, burned, and/or buried in the soil before new growth begins", 
                               "Early season fungicide sprays should be timed to prevent the earliest infections", 
                               "Captan, Copper fungicide or Neem oil can be used"])
add_cure("", ["", "", ""])
add_cure("", ["", "", ""])
add_cure("", ["", "", ""])
add_cure("", ["", "", ""])
add_cure("", ["", "", ""])
add_cure("", ["", "", ""])
add_cure("", ["", "", ""])
add_cure("", ["", "", ""])
add_cure("", ["", "", ""])
add_cure("", ["", "", ""])
add_cure("", ["", "", ""])
add_cure("", ["", "", ""])