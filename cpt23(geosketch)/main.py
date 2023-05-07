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
   "Chad" : "chadd.png"
   }

def score_win():
   score_win = customtkinter.CTkToplevel(main)
   score_win.geometry("400x400")

   score_win.title("score")

   score_label = customtkinter.CTkLabel(master=score_win, text = "score will go here")
   score_label.grid(row = 0, column = 0 )


def Chad_screen(im_dict):
   def get_input():
      user_input = text_input_box.get()
      if user_input == "Chad":
         print("Chad is correct")
         global score 
         score += 1
         print(score)

   classic_gm_win = customtkinter.CTkToplevel(main)
   classic_gm_win.geometry("600x600")
   classic_gm_win.title("Classic")

   image_frame =customtkinter.CTkFrame(master = classic_gm_win, width = 500, height = 300)
   image_frame.grid(row = 0, column = 0, padx = 150, pady = 10)

   neder_image_file =  (im_dict.get("Chad"))

   us_button_image = customtkinter.CTkImage(Image.open(neder_image_file), size=(300, 200))
   us_image_button = customtkinter.CTkLabel(master=image_frame, image=us_button_image, text = "Guess this country", text_color = "black")
   us_image_button.grid(row = 0, column = 0)

   text_input_frame = customtkinter.CTkFrame(master = classic_gm_win, width = 500, height = 300)
   text_input_frame.grid(row = 1, column = 0)

   text_input_box = customtkinter.CTkEntry(master = text_input_frame, width = 150, height = 50)
   text_input_box.grid(row = 0, column = 0, pady = 15)

   enter_btn = customtkinter.CTkButton(master = text_input_frame, width = 10, height = 10, command = get_input)
   enter_btn.grid(row = 0, column = 1, padx = 10)

def Neder_screen(im_dict):
   def get_input():
      user_input = text_input_box.get()
      if user_input == "Netherland":
         print ("Netherland is Correct")
         global score 
         score += 1
         print(score)
      Chad_screen(im_dict)

   classic_gm_win = customtkinter.CTkToplevel(main)
   classic_gm_win.geometry("600x600")
   classic_gm_win.title("Classic")

   image_frame =customtkinter.CTkFrame(master = classic_gm_win, width = 500, height = 300)
   image_frame.grid(row = 0, column = 0, padx = 150, pady = 10)

   neder_image_file =  (im_dict.get("Netherland"))

   us_button_image = customtkinter.CTkImage(Image.open(neder_image_file), size=(300, 200))
   us_image_button = customtkinter.CTkLabel(master=image_frame, image=us_button_image, text = "Guess this country", text_color = "black")
   us_image_button.grid(row = 0, column = 0)

   text_input_frame = customtkinter.CTkFrame(master = classic_gm_win, width = 500, height = 300)
   text_input_frame.grid(row = 1, column = 0)

   text_input_box = customtkinter.CTkEntry(master = text_input_frame, width = 150, height = 50)
   text_input_box.grid(row = 0, column = 0, pady = 15)

   enter_btn = customtkinter.CTkButton(master = text_input_frame, width = 10, height = 10, command = get_input)
   enter_btn.grid(row = 0, column = 1, padx = 10)

def Classic_gm(im_dict):
   turn = 0 
   if turn == 0:

      def get_input():
         user_input = text_input_box.get()
         if user_input == "U.S":
            print ("U.S is correct")
            global score 
            score += 1
            print(score)
         classic_gm_win.destroy()
         Neder_screen(im_dict)

      classic_gm_win = customtkinter.CTkToplevel(main)
      classic_gm_win.geometry("600x600")
      classic_gm_win.title("Classic")

      image_frame =customtkinter.CTkFrame(master = classic_gm_win, width = 500, height = 300)
      image_frame.grid(row = 0, column = 0, padx = 150, pady = 10)

      us_image_file =  (im_dict.get("U.S"))

      us_button_image = customtkinter.CTkImage(Image.open(us_image_file), size=(300, 200))
      us_image_button = customtkinter.CTkLabel(master=image_frame, image=us_button_image, text = "Guess this country", text_color = "black")
      us_image_button.grid(row = 0, column = 0)

      text_input_frame = customtkinter.CTkFrame(master = classic_gm_win, width = 500, height = 300)
      text_input_frame.grid(row = 1, column = 0)

      text_input_box = customtkinter.CTkEntry(master = text_input_frame, width = 150, height = 50)
      text_input_box.grid(row = 0, column = 0, pady = 15)

      enter_btn = customtkinter.CTkButton(master = text_input_frame, width = 10, height = 10, command = get_input)
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

ply_btn = customtkinter.CTkButton(master = TopF, text = "Classic", command = lambda: Classic_gm(im_dict))
ply_btn.grid(row = 2, column = 0, pady = 5)

# The following will be settings such as theme
setting_frame = customtkinter.CTkFrame(master = main, height = 100, width = 200)
setting_frame.grid(row = 3, column = 0)

main.mainloop()

