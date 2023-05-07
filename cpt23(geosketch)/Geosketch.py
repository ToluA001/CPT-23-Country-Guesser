# import statements
from tkinter import *
import customtkinter
from PIL import Image

global score 
score = 0 

# This is the dictionary that the images will be  pulled from via their keys 
im_dict = {
   # program segment done by collaborative partner 
   "U.S" : "us_outline.png",
   "Netherland" : "netherlands_outline.png",
   "Chad" : "chad_outline.png",
   "Suriname" : "suriname_outline.png",
   "Georgia" : "georgia_outline.png",
   "China" : "china_outline.png",
   "Srilanka" : "sri_lanka_outline.png",
   "Czech" : "czech_republic_outline.png",
   "Ireland" : "Ireland_ouline.png",
   "Lesotho" : "lesotho_outline.png" 
   }

   # Sources for images below:
   #USA map: https://www.burningcompass.com/countries/united-states/blank-map-of-us.html
   #Netherlands map: https://www.burningcompass.com/countries/netherlands/netherlands-outline-map.html
   #Chad map: https://www.burningcompass.com/countries/chad/chad-outline-map.html
   #Suriname map: https://commons.wikimedia.org/wiki/File:Guianas_location_map_with_disputed_boundaries.svg
   #Georgia map: https://commons.wikimedia.org/wiki/File:Georgia_(country)_EU.svg
   #China map: https://www.burningcompass.com/countries/china/china-outline-map.html
   #Sri Lanka map: https://www.burningcompass.com/countries/sri-lanka/sri-lanka-outline-map.html
   #Czech Republic map: https://pixabay.com/vectors/czech-republic-country-europe-flag-1758820/
   #Ireland map: https://simplemaps.com/resources/svg-ie
   #Lesotho map: https://www.burningcompass.com/countries/lesotho/lesotho-outline-map.htm
   

def save_score():
   # done by me 
   # This function will be called when the user clicks the save score button 
   global score # The score of the player
   global user_name_entry # This is the entry box the user typed their name in 
   global save_score_frame # The frame that the user_entry_box and enter button are, will be used to displaye the highest score 

   score_dict = {} 
   # the key will be the name of the user and the value wil be the score, the dictionary will be filled when the score.txt file is read

   user_name = user_name_entry.get() 
   # getting the name of the user 
   score_str = str(score) 
   # turning the score into a str, this must be done so the score can be saved in a file, causes no problems bc no math will be done with the score

   with open ('score.txt', 'a') as f: # opens the text file and sets it to append mode 
      f.write(user_name + "\n" + score_str + "\n") 
      # appends the user name and score to the file, seperating them by leaving a space in the middle 
   
   with open ('score.txt', 'r') as f:# opens the text file in read mode 
      contents = f.readlines() # sets the information read into a list

   for line in range (len(contents)):
      if line % 2 == 0:
         key = contents[line].strip()
      else:
         value = int(contents[line].strip())  # convert value to an integer
         score_dict[key] = value
   
   max_key = NONE # initialize max_key to None
   max_value = 0  # initialize max_value to negative infinity

   # sets the max value as the first value in the list, checks if the next value is greater than the current maximum value
   # If the value is greater than the current maximum value, it updates the maximum value and the key associated with that value.
   for key, value in score_dict.items():
      if value > max_value:
        max_value = value
        max_key = key

   # makes a new variable where the b=max value is a str so that it can  be displayed in the label 
   str_max_value = str(max_value) 

   # displays the highest score and the key/name associated with that value
   highest_score_label = customtkinter.CTkLabel(master = save_score_frame, 
                                                text = "Highest score is " + str_max_value + " by " + max_key)
   highest_score_label.grid(row = 2, column = 0 )

 
def score_win():
   # done by me 
   # the window where the user can see their score and has the option to save their score 
   global score 

   scorewin = customtkinter.CTkToplevel(main)
   scorewin.geometry("400x400")
   scorewin.title("Score")

   score_frame = customtkinter.CTkFrame(master = scorewin, width = 100, height = 100, corner_radius = 5)
   score_frame.grid(row = 0, column = 0, padx = 135, pady = 10 )

   scorelabel = customtkinter.CTkLabel(master = score_frame, text = "You got a score of: " + str(score), width = 50, height = 50)
   scorelabel.grid(row = 0, column = 0)

   global save_score_frame
   save_score_frame = customtkinter.CTkFrame( master = scorewin, width = 100, height = 100, corner_radius = 5)
   save_score_frame.grid(row = 1, column = 0)

   save_score_label = customtkinter.CTkLabel(master = save_score_frame, text = "Enter the name you would like to save your score as: ")
   save_score_label.grid(row = 0, column = 0 )

   global user_name_entry 
   user_name_entry = customtkinter.CTkEntry(master = save_score_frame, width = 150, height = 50 )
   user_name_entry.grid(row = 1, column = 0)

   
   save_score_btn = customtkinter.CTkButton(master = save_score_frame, 
                                            width = 20, height = 20, 
                                            text = "Save Score", command = save_score)
   save_score_btn.grid(row = 1, column = 1)
   
   the_countries_txt = "*The countries in the order they appeared in*\nUnited States\nNetherlands\nChad\nChina\nCzech republic\nGeorgia\nIreland\nLesotho\nSri Lanka\nSuriname"
   the_countries = customtkinter.CTkLabel(master = save_score_frame, text = the_countries_txt)
   the_countries.grid(row = 3, column = 0 )





def get_input(turn):
   # done by me 
   # this function is called when the enter button to submit their guess 
   # these globals are set so that the windows/toplevels can be accessed from the function, specifically to close them 
   global uclassic_gm_win
   global text_input_box # where the user is inputting their guess 
   global nclassic_gm_win
   global cclassic_gm_win
   global chin_gm_win
   global Czech_gm_win
   global georgia_gm_win
   global ireland_gm_win
   global lesotho_gm_win
   global sri_gm_win
   global suriname_gm_win
   global score 

   # checks what turn it is 
   if turn == 1: 
      # gets whetever the user inputted 
      user_input = text_input_box.get()

      # makes the input all lower case, makes the input easier to check later on 
      user_input.lower()

      # Checks the input 
      if user_input == "u.s.a" or user_input == "united states" or user_input == "u.s" or user_input == "united states of america":
         score += 1
         # if what the user inputted is correct their is increased by 1
      # Destroys the window and calls the next window 
      uclassic_gm_win.destroy()
      Neder_screen(im_dict)

   if turn == 2:
      user_input = text_input_box.get()
      user_input.lower()
      if user_input == "netherlands":
         score += 1
      nclassic_gm_win.destroy()
      Chad_screen(im_dict)
   
   if turn == 3:
      user_input = text_input_box.get()
      user_input.lower()
      if user_input == "chad":
         score += 1
      cclassic_gm_win.destroy()
      China_screen(im_dict)
   
   if turn == 4:
      user_input = text_input_box.get()
      user_input.lower()
      if user_input == "china":
         score += 1
      chin_gm_win.destroy()
      czech_screen(im_dict)
   
   if turn == 5:
      user_input = text_input_box.get()
      user_input.lower()
      if user_input == "czech" or user_input == "czech republic":
         score += 1
      Czech_gm_win.destroy()
      georgia_screen(im_dict)
   
   if turn == 6:
      user_input = text_input_box.get()
      user_input.lower()
      if user_input == "georgia":
         score += 1
      georgia_gm_win.destroy()
      ireland_screen(im_dict)

   if turn == 7:
      user_input = text_input_box.get()
      user_input.lower()
      if user_input == "ireland":
         score += 1
      ireland_gm_win.destroy()
      lesotho_screen(im_dict)

   if turn == 8:
      user_input = text_input_box.get()
      user_input.lower()
      if user_input == "lesotho":
         score += 1
      lesotho_gm_win.destroy()
      srilanka_screen(im_dict)
   
   if turn == 9:
      user_input = text_input_box.get()
      user_input.lower()
      if user_input == "sri lanka":
         score += 1
      sri_gm_win.destroy()
      suriname_screen(im_dict)
   
   if turn == 10:
      user_input = text_input_box.get()
      user_input.lower()
      if user_input == "suriname":
         score += 1
      suriname_gm_win.destroy()
      score_win()


def Chad_screen(im_dict):
   # done by collaborative partner 
   global turn 
   turn = 3
   global cclassic_gm_win
   cclassic_gm_win = customtkinter.CTkToplevel(main)
   cclassic_gm_win.geometry("600x600")
   cclassic_gm_win.title("Classic")

   image_frame =customtkinter.CTkFrame(master = cclassic_gm_win, width = 500, height = 500)
   image_frame.grid(row = 0, column = 0, padx = 100, pady = 10)

   chad_image_file =  (im_dict.get("Chad"))

   chad_button_image = customtkinter.CTkImage(Image.open(chad_image_file), size=(400, 500))
   chad_image_button = customtkinter.CTkLabel(master=image_frame, image=chad_button_image, text = " ", text_color = "black")
   chad_image_button.grid(row = 0, column = 0)

   text_input_frame = customtkinter.CTkFrame(master = cclassic_gm_win, width = 500, height = 300)
   text_input_frame.grid(row = 1, column = 0)

   global text_input_box
   text_input_box = customtkinter.CTkEntry(master = text_input_frame, width = 150, height = 50)
   text_input_box.grid(row = 0, column = 0, pady = 15)

   enter_btn = customtkinter.CTkButton(master = text_input_frame, text = "Enter", 
                                       width = 10, height = 10, 
                                       command = lambda: get_input(turn))
   enter_btn.grid(row = 0, column = 1, padx = 10)

def Neder_screen(im_dict):
   global nclassic_gm_win
   global turn 
   turn = 2
   nclassic_gm_win = customtkinter.CTkToplevel(main)
   nclassic_gm_win.geometry("600x600")
   nclassic_gm_win.title("Classic")

   image_frame =customtkinter.CTkFrame(master = nclassic_gm_win, width = 500, height = 300)
   image_frame.grid(row = 0, column = 0, padx = 150, pady = 10)

   neder_image_file =  (im_dict.get("Netherland"))

   neder_lable_image = customtkinter.CTkImage(Image.open(neder_image_file), size=(300, 300))
   neder_image_button = customtkinter.CTkLabel(master=image_frame, image=neder_lable_image, 
                                                text = " ", text_color = "black")
   neder_image_button.grid(row = 0, column = 0)

   text_input_frame = customtkinter.CTkFrame(master = nclassic_gm_win, width = 500, height = 300)
   text_input_frame.grid(row = 1, column = 0)

   global text_input_box
   text_input_box = customtkinter.CTkEntry(master = text_input_frame, width = 150, height = 50)
   text_input_box.grid(row = 0, column = 0, pady = 15)

   enter_btn = customtkinter.CTkButton(master = text_input_frame, 
                                       text = "Enter", width = 10, 
                                       height = 10, 
                                       command = lambda: get_input(turn))
   enter_btn.grid(row = 0, column = 1, padx = 10)

def UnitedStates_screen(im_dict):
   # This is the first screen that the main window will call when the classic button is clicked.
   global turn
   turn = 1 # this is turn 1, this will be the first screen 
   # Making the window 
   global uclassic_gm_win # global so it can be accesed in other functions 
   uclassic_gm_win = customtkinter.CTkToplevel(main)
   uclassic_gm_win.geometry("600x600")
   uclassic_gm_win.title("Classic")

   # An empty frame, this is where the image will go 
   image_frame =customtkinter.CTkFrame(master = uclassic_gm_win, width = 500, height = 300)
   image_frame.grid(row = 0, column = 0, padx = 150, pady = 10)

   # Access the dictionary and gets the value of the key 
   us_image_file =  (im_dict.get("U.S"))

   # Uses the value of the key(the path of the image) to find the image file
   # and creates the image object that will be used in the label 
   us_image = customtkinter.CTkImage(Image.open(us_image_file), size=(300, 200))

   # Due to the fact that there is no widget that only shows the image, I'm using a label to display the image
   us_image_label = customtkinter.CTkLabel(master=image_frame, 
                                           image=us_image, 
                                           text = " ", 
                                           text_color = "black")
   us_image_label.grid(row = 0, column = 0)

   # A frame for the input box 
   text_input_frame = customtkinter.CTkFrame(master = uclassic_gm_win, width = 500, height = 300)
   text_input_frame.grid(row = 1, column = 0)

   # The input box 
   global text_input_box
   text_input_box = customtkinter.CTkEntry(master = text_input_frame, width = 150, height = 50)
   text_input_box.grid(row = 0, column = 0, pady = 15)

   # The enter button
   enter_btn = customtkinter.CTkButton(master = text_input_frame, text = "Enter", 
                                       width = 10, height = 10, 
                                       command = lambda: get_input(turn))
   enter_btn.grid(row = 0, column = 1, padx = 10)

def China_screen(im_dict):
   global chin_gm_win
   global turn 
   turn = 4
   
   chin_gm_win = customtkinter.CTkToplevel(main)
   chin_gm_win.geometry("600x600")
   chin_gm_win.title("Classic")

   image_frame =customtkinter.CTkFrame(master = chin_gm_win, width = 500, height = 500)
   image_frame.grid(row = 0, column = 0, padx = 150, pady = 10)

   neder_image_file =  (im_dict.get("China"))

   neder_lable_image = customtkinter.CTkImage(Image.open(neder_image_file), size=(300, 300))
   neder_image_button = customtkinter.CTkLabel(master=image_frame, image=neder_lable_image, 
                                               text = " ", text_color = "black")
   neder_image_button.grid(row = 0, column = 0)

   text_input_frame = customtkinter.CTkFrame(master = chin_gm_win, width = 500, height = 300)
   text_input_frame.grid(row = 1, column = 0)

   global text_input_box
   text_input_box = customtkinter.CTkEntry(master = text_input_frame, width = 150, height = 50)
   text_input_box.grid(row = 0, column = 0, pady = 15)

   enter_btn = customtkinter.CTkButton(master = text_input_frame, text = "Enter", 
                                       width = 10, height = 10, 
                                       command = lambda: get_input(turn))
   enter_btn.grid(row = 0, column = 1, padx = 10)

def czech_screen(im_dict):
   global Czech_gm_win
   global turn 
   turn = 5

   
   Czech_gm_win = customtkinter.CTkToplevel(main)
   Czech_gm_win.geometry("600x600")
   Czech_gm_win.title("Classic")

   image_frame =customtkinter.CTkFrame(master = Czech_gm_win, width = 500, height = 500)
   image_frame.grid(row = 0, column = 0, padx = 100, pady = 10)

   neder_image_file =  (im_dict.get("Czech"))

   neder_lable_image = customtkinter.CTkImage(Image.open(neder_image_file), size=(450, 450))
   neder_image_button = customtkinter.CTkLabel(master=image_frame, image=neder_lable_image, text = " ", text_color = "black")
   neder_image_button.grid(row = 0, column = 0)

   text_input_frame = customtkinter.CTkFrame(master = Czech_gm_win, width = 500, height = 300)
   text_input_frame.grid(row = 1, column = 0)

   global text_input_box
   text_input_box = customtkinter.CTkEntry(master = text_input_frame, width = 150, height = 50)
   text_input_box.grid(row = 0, column = 0, pady = 15)

   enter_btn = customtkinter.CTkButton(master = text_input_frame, text = "Enter", 
                                       width = 10, height = 10, 
                                       command = lambda: get_input(turn))
   enter_btn.grid(row = 0, column = 1, padx = 10)

def georgia_screen(im_dict):
   global georgia_gm_win
   global turn 
   turn = 6

   
   georgia_gm_win = customtkinter.CTkToplevel(main)
   georgia_gm_win.geometry("600x600")
   georgia_gm_win.title("Classic")

   image_frame =customtkinter.CTkFrame(master = georgia_gm_win, width = 500, height = 500)
   image_frame.grid(row = 0, column = 0, padx = 150, pady = 10)

   neder_image_file =  (im_dict.get("Georgia"))

   neder_lable_image = customtkinter.CTkImage(Image.open(neder_image_file), size=(300, 300))
   neder_image_button = customtkinter.CTkLabel(master=image_frame, image=neder_lable_image, text = " ", text_color = "black")
   neder_image_button.grid(row = 0, column = 0)

   text_input_frame = customtkinter.CTkFrame(master = georgia_gm_win, width = 500, height = 300)
   text_input_frame.grid(row = 1, column = 0)

   global text_input_box
   text_input_box = customtkinter.CTkEntry(master = text_input_frame, width = 150, height = 50)
   text_input_box.grid(row = 0, column = 0, pady = 15)

   enter_btn = customtkinter.CTkButton(master = text_input_frame, text = "Enter", 
                                       width = 10, height = 10, 
                                       command = lambda: get_input(turn))
   enter_btn.grid(row = 0, column = 1, padx = 10)

def ireland_screen(im_dict):
   global ireland_gm_win
   global turn 
   turn = 7

   
   ireland_gm_win = customtkinter.CTkToplevel(main)
   ireland_gm_win.geometry("600x600")
   ireland_gm_win.title("Classic")

   image_frame =customtkinter.CTkFrame(master = ireland_gm_win, width = 500, height = 500)
   image_frame.grid(row = 0, column = 0, padx = 145, pady = 10)

   neder_image_file =  (im_dict.get("Ireland"))

   neder_lable_image = customtkinter.CTkImage(Image.open(neder_image_file), size=(300, 500))
   neder_image_button = customtkinter.CTkLabel(master=image_frame, image=neder_lable_image, text = " ", text_color = "black")
   neder_image_button.grid(row = 0, column = 0)

   text_input_frame = customtkinter.CTkFrame(master = ireland_gm_win, width = 500, height = 300)
   text_input_frame.grid(row = 1, column = 0)

   global text_input_box
   text_input_box = customtkinter.CTkEntry(master = text_input_frame, width = 150, height = 50)
   text_input_box.grid(row = 0, column = 0, pady = 15)

   enter_btn = customtkinter.CTkButton(master = text_input_frame, text = "Enter", 
                                       width = 10, height = 10, 
                                       command = lambda: get_input(turn))
   enter_btn.grid(row = 0, column = 1, padx = 10)

def lesotho_screen(im_dict):
   global lesotho_gm_win
   global turn 
   turn = 8

   
   lesotho_gm_win = customtkinter.CTkToplevel(main)
   lesotho_gm_win.geometry("600x600")
   lesotho_gm_win.title("Classic")

   image_frame =customtkinter.CTkFrame(master = lesotho_gm_win, width = 500, height = 500)
   image_frame.grid(row = 0, column = 0, padx = 150, pady = 10)

   neder_image_file =  (im_dict.get("Lesotho"))

   neder_lable_image = customtkinter.CTkImage(Image.open(neder_image_file), size=(300, 300))
   neder_image_button = customtkinter.CTkLabel(master=image_frame, image=neder_lable_image, text = " ", text_color = "black")
   neder_image_button.grid(row = 0, column = 0)

   text_input_frame = customtkinter.CTkFrame(master = lesotho_gm_win, width = 500, height = 300)
   text_input_frame.grid(row = 1, column = 0)

   global text_input_box
   text_input_box = customtkinter.CTkEntry(master = text_input_frame, width = 150, height = 50)
   text_input_box.grid(row = 0, column = 0, pady = 15)

   enter_btn = customtkinter.CTkButton(master = text_input_frame, text = "Enter", 
                                       width = 10, height = 10, 
                                       command = lambda: get_input(turn))
   enter_btn.grid(row = 0, column = 1, padx = 10)

def srilanka_screen(im_dict):
   global sri_gm_win
   global turn 
   turn = 9

   
   sri_gm_win = customtkinter.CTkToplevel(main)
   sri_gm_win.geometry("600x600")
   sri_gm_win.title("Classic")

   image_frame =customtkinter.CTkFrame(master = sri_gm_win, width = 500, height = 500)
   image_frame.grid(row = 0, column = 0, padx = 150, pady = 10)

   neder_image_file =  (im_dict.get("Srilanka"))

   neder_lable_image = customtkinter.CTkImage(Image.open(neder_image_file), size=(300, 300))
   neder_image_button = customtkinter.CTkLabel(master=image_frame, image=neder_lable_image, text = " ", text_color = "black")
   neder_image_button.grid(row = 0, column = 0)

   text_input_frame = customtkinter.CTkFrame(master = sri_gm_win, width = 500, height = 300)
   text_input_frame.grid(row = 1, column = 0)

   global text_input_box
   text_input_box = customtkinter.CTkEntry(master = text_input_frame, width = 150, height = 50)
   text_input_box.grid(row = 0, column = 0, pady = 15)

   enter_btn = customtkinter.CTkButton(master = text_input_frame, text = "Enter", 
                                       width = 10, height = 10, 
                                       command = lambda: get_input(turn))
   enter_btn.grid(row = 0, column = 1, padx = 10)

def suriname_screen(im_dict):
   global suriname_gm_win
   global turn 
   turn = 10

   
   suriname_gm_win = customtkinter.CTkToplevel(main)
   suriname_gm_win.geometry("600x600")
   suriname_gm_win.title("Classic")

   image_frame =customtkinter.CTkFrame(master = suriname_gm_win, width = 500, height = 500)
   image_frame.grid(row = 0, column = 0, padx = 150, pady = 10)

   neder_image_file =  (im_dict.get("Suriname"))

   neder_lable_image = customtkinter.CTkImage(Image.open(neder_image_file), size=(300, 300))
   neder_image_button = customtkinter.CTkLabel(master=image_frame, image=neder_lable_image, text = " ", text_color = "black")
   neder_image_button.grid(row = 0, column = 0)

   text_input_frame = customtkinter.CTkFrame(master = suriname_gm_win, width = 500, height = 300)
   text_input_frame.grid(row = 1, column = 0)

   global text_input_box
   text_input_box = customtkinter.CTkEntry(master = text_input_frame, width = 150, height = 50)
   text_input_box.grid(row = 0, column = 0, pady = 15)

   enter_btn = customtkinter.CTkButton(master = text_input_frame, text = "Enter", 
                                       width = 10, height = 10, 
                                       command = lambda: get_input(turn))
   enter_btn.grid(row = 0, column = 1, padx = 10)

# program segment under done by me 
main = customtkinter.CTk()
main.geometry("400x400")
main.title("Intro window")

# system set up 
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# seting up the intro/title screen
TopF = customtkinter.CTkFrame(master = main, height=200, width=200)
TopF.grid(row=0,column=0, pady = 10, padx = 70)

# Everything below will go in the TopF(Top Frame)
welcomeLable = customtkinter.CTkLabel(master = TopF, text = "WELCOME TO GEOSKETCH")
welcomeLable.grid(row = 0, column =0, padx = 50)

#  lambda function that calls a function named UnitedStates_screen and passes it an argument named im_dict
ply_btn = customtkinter.CTkButton(master = TopF, text = "Classic", command = lambda: UnitedStates_screen(im_dict))
ply_btn.grid(row = 1, column = 0, pady = 5)

if (__name__ == "__main__"):
   main.mainloop()

