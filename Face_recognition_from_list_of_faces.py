import face_recognition
import glob

# path of the picture to intended to be compared
path_all_pics=r"C:\Users\gcris\Documents\MEGA\MEGAsync\Programming\Python\Learning topics\Opencv_"

#loading my pic and encoding it
picture_of_me = face_recognition.load_image_file("picture.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]


# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

# return a list with all files .jpg , to be used after in order to compare each file
def list_images_names_folder(folder):
    list_of_faces = []
    for img in glob.glob("{}/*.jpg".format(folder)):
        list_of_faces.append(img)
    return list_of_faces


# eloading each picture and encoing it from a specif folder
def list_face_encoded_pic_name(list_Of_Pictures_Path):
    list_unknown_face_encoding=[] #lisf of unkonwn encoded faces
    list_pictures=list_images_names_folder(list_Of_Pictures_Path) # path of each pic in the folder
    for x in list_pictures:
        unknown_picture = face_recognition.load_image_file(x) #load image
        try:
            unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0] ## encoding the immage

            list_unknown_face_encoding.append(unknown_face_encoding)  # append each encoded pic to the list
        except: continue
    return list_unknown_face_encoding,list_pictures

# Now we can see the two face encodings are of the same person with `compare_faces`
def compare_faces(list_Of_Pictures_Path):
    i=0 # the conter is used to travers the list of files path (name of the file)
    for x in list_face_encoded_pic_name(list_Of_Pictures_Path)[0]: # for each encoded picture
        result = face_recognition.compare_faces([my_face_encoding], x) #comparing the my picture encoded with each one from the folder
        print(result,list_face_encoded_pic_name(list_Of_Pictures_Path)[1][i])
        i=i+1
    return  result,list_face_encoded_pic_name(list_Of_Pictures_Path)[1][i]

# if results[0] == True:
#     print("It's a picture of me!")
# else:
#     print("It's not a picture of me!")
compare_faces(path_all_pics)

# print(list_face_encoded_pic_name(path_all_pics))
# print(len(list_images_names_folder(path_all_pics)))

