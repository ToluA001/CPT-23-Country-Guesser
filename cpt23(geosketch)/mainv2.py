# import statements
from tkinter import *
import customtkinter
from PIL import Image

global score 
score = 0 

# How to play fucnction
def how_to_ply_func():
   how_to_ply_win = customtkinter.CTkToplevel(main)

   how_to_ply_win.geometry("900x500")

   how_to_ply_win.title("How to play?")

   how_to_ply_instruc_frame = customtkinter.CTkScrollableFrame(master = how_to_ply_win, width = 850, height = 450)
   how_to_ply_instruc_frame.pack(pady = 10)

   how_to_ply_instruc = customtkinter.CTkLabel(master = how_to_ply_instruc_frame, text = "-To start the game, close this window, return to the title screen and click the 'Classic' button\nClassic gamemode- user wil be presented the outline of a country and must type in the name of the country")
   how_to_ply_instruc.grid(row = 0, column = 0)

# classic game mose func
im_dict = {
   "U.S" : "u.s_outline.png",
   "Netherland" : "Netherland.jpg",
   "Chad" : "chadd.png",
   "Suriname" : "this is where the image will go",
   "Georgia" : "this is where the image will go",
   "China" : "this is where the image will go",
   "Srilanka" : "image will go here",
   "Czech" : "image will go here",
   "Ireland" : "image will go here",
   "Lesotho" : "image will go here"
   }





def save_score():
   global score 
   global user_name_entry

   score_dict = {}

   user_name = user_name_entry.get()
   score_str = str(score)

   with open ('score.txt', 'a') as f:
      f.write(user_name + "\n" + score_str + "\n")
   
   with open ('score.txt', 'r') as f:

      contents = f.readlines()

   for i in range (len(contents)):
      if i % 2 == 0:
         key = contents[i].strip()
      else:
        value = contents[i].strip()
        score_dict[key] = value
   
   print(score_dict)



def score_win():
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

   
   save_score_btn = customtkinter.CTkButton(master = save_score_frame, width = 20, height = 20, text = "Save Score", command = save_score)
   save_score_btn.grid(row = 1, column = 1)




def Chad_screen(im_dict):
   def get_input():
      user_input = text_input_box.get()
      user_input.lower()
      if user_input == "chad":
         print("Chad is correct")
         global score 
         score += 1
      
      classic_gm_win.destroy()
      score_win()
      print(score)

   classic_gm_win = customtkinter.CTkToplevel(main)
   classic_gm_win.geometry("600x600")
   classic_gm_win.title("Classic")

   image_frame =customtkinter.CTkFrame(master = classic_gm_win, width = 500, height = 300)
   image_frame.grid(row = 0, column = 0, padx = 150, pady = 10)

   chad_image_file =  (im_dict.get("Chad"))

   chad_button_image = customtkinter.CTkImage(Image.open(chad_image_file), size=(300, 200))
   chad_image_button = customtkinter.CTkLabel(master=image_frame, image=chad_button_image, text = "Guess this country", text_color = "black")
   chad_image_button.grid(row = 0, column = 0)

   text_input_frame = customtkinter.CTkFrame(master = classic_gm_win, width = 500, height = 300)
   text_input_frame.grid(row = 1, column = 0)

   text_input_box = customtkinter.CTkEntry(master = text_input_frame, width = 150, height = 50)
   text_input_box.grid(row = 0, column = 0, pady = 15)

   enter_btn = customtkinter.CTkButton(master = text_input_frame, text = "Enter", width = 10, height = 10, command = get_input)
   enter_btn.grid(row = 0, column = 1, padx = 10)

def Neder_screen(im_dict):
   def get_input():
      user_input = text_input_box.get()
      user_input.lower()
      if user_input == "netherlands":
         print ("Netherland is Correct")
         global score 
         score += 1
      classic_gm_win.destroy()
      Chad_screen(im_dict)

   classic_gm_win = customtkinter.CTkToplevel(main)
   classic_gm_win.geometry("600x600")
   classic_gm_win.title("Classic")

   image_frame =customtkinter.CTkFrame(master = classic_gm_win, width = 500, height = 300)
   image_frame.grid(row = 0, column = 0, padx = 150, pady = 10)

   neder_image_file =  (im_dict.get("Netherland"))

   neder_lable_image = customtkinter.CTkImage(Image.open(neder_image_file), size=(300, 300))
   neder_image_button = customtkinter.CTkLabel(master=image_frame, image=neder_lable_image, text = "Guess this country", text_color = "black")
   neder_image_button.grid(row = 0, column = 0)

   text_input_frame = customtkinter.CTkFrame(master = classic_gm_win, width = 500, height = 300)
   text_input_frame.grid(row = 1, column = 0)

   text_input_box = customtkinter.CTkEntry(master = text_input_frame, width = 150, height = 50)
   text_input_box.grid(row = 0, column = 0, pady = 15)

   enter_btn = customtkinter.CTkButton(master = text_input_frame, text = "Enter", width = 10, height = 10, command = get_input)
   enter_btn.grid(row = 0, column = 1, padx = 10)

def UnitedStates_screen(im_dict):
   # This is the first screen that the main window will call when the classic button is clicked.
   def get_input():
      # This function is called the enter button is clicked 

      # Gets the input from the  
      user_input = text_input_box.get()

      # Makes the input all lower case
      user_input.lower()

      # Checks the input 
      if user_input == "u.s.a" or user_input == "united states" or user_input == "u.s" or user_input == "united states of america":
         print ("U.S is correct")
         global score 
         score += 1
      
      # Destroys the window and calls the next window 
      classic_gm_win.destroy()
      Neder_screen(im_dict)

   # Making the window 
   classic_gm_win = customtkinter.CTkToplevel(main)
   classic_gm_win.geometry("600x600")
   classic_gm_win.title("Classic")

   # An empty frame, this is where the image will go 
   image_frame =customtkinter.CTkFrame(master = classic_gm_win, width = 500, height = 300)
   image_frame.grid(row = 0, column = 0, padx = 150, pady = 10)

   # Access the dictionary and gets the value of the key 
   us_image_file =  (im_dict.get("U.S"))

   # Uses the value of the key to find the image file
   # and creates the image object that will be used in the label 
   us_image = customtkinter.CTkImage(Image.open(us_image_file), size=(300, 200))

   # Due to the fact that there is no widget that only shows the image, I'm using a label to display the image
   us_image_label = customtkinter.CTkLabel(master=image_frame, image=us_image, text = "Guess this country", text_color = "black")
   us_image_label.grid(row = 0, column = 0)

   # A frame for the input box 
   text_input_frame = customtkinter.CTkFrame(master = classic_gm_win, width = 500, height = 300)
   text_input_frame.grid(row = 1, column = 0)

   # The input box 
   text_input_box = customtkinter.CTkEntry(master = text_input_frame, width = 150, height = 50)
   text_input_box.grid(row = 0, column = 0, pady = 15)

   # The enter button
   enter_btn = customtkinter.CTkButton(master = text_input_frame, text = "Enter", width = 10, height = 10, command = get_input)
   enter_btn.grid(row = 0, column = 1, padx = 10)


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

how_to_ply_btn = customtkinter.CTkButton(master = TopF, text = "HOW TO PLAY", command = how_to_ply_func)
how_to_ply_btn.grid(row = 1, column = 0)

ply_btn = customtkinter.CTkButton(master = TopF, text = "Classic", command = lambda: UnitedStates_screen(im_dict))
ply_btn.grid(row = 2, column = 0, pady = 5)

# The following will be settings such as theme
setting_frame = customtkinter.CTkFrame(master = main, height = 100, width = 200)
setting_frame.grid(row = 3, column = 0)

main.mainloop()

