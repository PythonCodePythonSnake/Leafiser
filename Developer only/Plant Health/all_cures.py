"""This file contains a dictionary cures which contains cure for the diseases as predicted in the model."""

def add_cure(name, method):
    global cures
    cures[name] = method


def get_cure(name):
    """Returns the cures of a disease <name> as a string"""
    global cures
    if name not in cures: return ""
    return_str = ""
    for i in range(len(cures[name])):
        return_str = return_str + str(i+1)+") " + cures[name][i]+ "\n"
    return_str = return_str[:-1]
    return return_str

#Make empty dictionary
cures = {}

#Keep adding cures like
#add_cure("<name of disease>", [<methods as individual strings. Each element of list is one method>])
add_cure("Apple___Apple_scab", ["Remove and destroy affected leaves", 
                                "Apply zinc and urea(or some other notrogen source)", 
                                "Make sure that leaves stay dry for as long as possible", 
                                "In rainy or humid season, use fetilizers like fixed copper or simple materials like neem(or mineral) oil"])
add_cure("Apple___Black_rot", ["Since, this disease spreads due to dead and decaying material, prune out dead or diseased branches", 
                               "Remove infected plant material from the area",
                               "Captan and sulfur products are labeled for control of black rot. However, these sprays will not control or prevent infection of branches."])
add_cure("Apple___Cedar_apple_rust", ["Dispose of fallen leaves from under the trees", 
                                      "Rust on infected trees can be controlled by spraying plants with a weak copper solution", 
                                      "Apply preventative, disease-fighting fungicides labeled for use on apples weekly, starting with bud break"])
add_cure("Cherry___Powdery_mildew", ["Keep short irrigation sets such that leaves do not get wet", 
                                     "Remove and destroy sucker shoots", 
                                     "Bicarbonate-based products will help in chemical control"])
add_cure("Corn___Cercospora_leaf_spotGray_leaf_spot", ["Crop rotation will help in reducing amount of inoculum", 
                                                       "Fungicides containing pyraclostrobin will surely help",
                                                        "Weed control will allow airflow"])
add_cure("Corn___Common_rust", ["Fungicides can be beneficial, especially if applied early", "Best management practice is to use resistant varieties"])
add_cure("Corn___Northern_Leaf_Blight", ["Use of resistant hybrids", 
                                         "Fungicides may be warranted on inbreds for seed production during the early stages of this disease", 
                                         "Make sure the crop does not stay wet for long periods of time"])
add_cure("Grape___Black_rot", ["Infected prunings and mummified berries should be removed, burned, and/or buried in the soil before new growth begins", 
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