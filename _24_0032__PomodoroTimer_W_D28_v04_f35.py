from tkinter import *
import math


#Dr. Toma, the tomato:

# ---------------------------- CONSTANTS ------------------------------- #
#Colors (in Hex code):
#in layered order from outer-most to inner-most color layers: window background > canvas background >
PINK = "#ED7B7B"
RED = "#E7305B"
GREEN = "#9BDEAC"
YELLOW = "#EBE76C"
ORANGE = "#F0B86E"
PURPLE = "#836096"

#Fonts:
FONT_NAME = "Courier"

#Integers (variable numbers):
progress_50_min_timer = 25     # 3000 = 50 min, as default
short_10_min_timer = 5     # 600 = 10 min, as default
long_20_min_timer = 20      # 1200 = 20 min, as default
# progress_timer_in_seconds_TEST_ONLY = 3   # 5 sec. FOR TESTING PURPOSES ONLY
# short_10_min_timer_TEST_ONLY = 1   # 1 sec. FOR TESTING PURPOSES ONLY
# long_20_min_timer_TEST_ONLY = 2   # 2 sec. FOR TESTING PURPOSES ONLY
reps = 0  #number of sessions we've had. If we did 4 reps, then we've had 2 progress sessions and 2 breaks.
# take total number of reps, and divide by 2 in order to get the total number of progress sessions.


#Strings:
checkmark_string = "✔"    #checkmark string version obtained from wikipedia:  https://en.wikipedia.org/wiki/Check_mark
main_timer = None   #for now, until we tap into the count > 0 and get ahold of the rest below.
timer_text = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer_text
    window.after_cancel(main_timer)    #stops the timer
    #timer_text 00:00 from canvas
    canvas.itemconfig(timer_text, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))   #this code line needs to be placed before/above we .pack() it. # the implied x and y value are the *args; text="text_here" is the keyword arguments (**kwargs)   #timer_text is the variable that we link once we get the function 'count_down' fixed
    # canvas.grid(column=1, row=1)

    # title_lable = "Timer"
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=("Arial", 36, 'bold'))  # color=GREEN)
    # timer_label.grid(column=1, row=0)

    #reset check_marks
    checkmark_label.config(text="")
    # checkmark_label.grid(column=1, row=3)
    
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer_button():    # this function is responsible for calling that function 'timer_count_down', and we drop the 'start_timer_button' part behind the command= of the Start button code block
    global reps
    progress_countdown_seconds = progress_50_min_timer * 60
    short_break_countdown_seconds = short_10_min_timer * 60
    long_break_countdown_seconds = long_20_min_timer * 60

    reps += 1

    # 20 min long break countdown:
    if reps % 4 == 0:
        count_down_function(long_break_countdown_seconds)
        timer_label.config(text="20 Minute Break", fg=RED)    # if reps == 4 or reps == 8 or reps == 12 or reps == 16:
    #     (count_down_function(long_break_countdown_seconds))


    # 10 min short break countdown:
    elif reps % 2 == 0:
        count_down_function(short_break_countdown_seconds)
        timer_label.config(text="5 Minute Break", fg=PINK)
    # elif reps == 2 or reps == 6 or reps == 10 or reps == 14:
    #     (count_down_function(short_break_countdown_seconds))

    # 50 min Progress countdown:
    else:
        count_down_function(progress_countdown_seconds)
        timer_label.config(text="Progress Mode", fg=GREEN)    # elif reps == 1 or reps == 3 or reps == 5 or reps == 7 or reps == 9 or reps == 11 or reps == 13 or reps == 15:\
    #     count_down_function(progress_countdown_seconds)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()  #either get ahold of the tkinter Module, then the Tk() Class, OR if using a lot of Classes (which we will be doing in this program), then we will just use the .Tk() Class from importing tkinter
#set the title of the window:
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)   #this ACTUALLY ADDS to the original width and height of the original 421x518 window. It won't take AWAY, or keep it the same size, it ADDS to the x and y lengths. So (padx=40, pady=40) would be a total window size of 461x558 pixels.  # https://colorhunt.co/palette/ebe76cf0b86eed7b7b836096 for bg=background_color_of_choice (without using "", because )

fg=GREEN #foreground

canvas = Canvas(width=430, height=496, bg=YELLOW, highlightthickness=0)  #variable canvas is created from the Canvas Widget  # width and height ar in pixel. # bg=background_color_for_canvas (not using "", since YELLOW is a variable name.  # highlightthickness=0 will get rid of the white line.

#Grid layout will be 3 columns wide and 5 rows down:

# Timer label:
timer_label = Label(text="This is old text", fg=GREEN, bg=YELLOW, font=("Arial", 36, 'bold')) #color=GREEN
timer_label.config(text="Timer")
timer_label.grid(column=1, row=0)

#############

tomato_img = PhotoImage(file="tomato4.png") #Also add the image=(PhotoImage datatype Class of tkinter), in order to read through a file and get ahold of a photo at a certain location.  (use Absolute File path, if in another dir). #Also will need to provide a variable name to store this image to (not the Class, but a different variable name of choice, like 'tomato_img'.), then place it after the 'image=' part of the next line:
canvas.create_image(215, 248, image=tomato_img)  #add my image to it, x and y (which are implied, inside) is needed in the (). Because we want the image to be placed right in the center of the window, we divide the dimensions in half, for both, and place those numbers in the paren(). #Also add the image=(PhotoImage datatype Class of tkinter), in order to read through a file and get ahold of a photo at a certain location. Also add the variable after the 'image=' part.
timer_text = canvas.create_text(214, 305, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))   #this code line needs to be placed before/above we .pack() it. # the implied x and y value are the *args; text="text_here" is the keyword arguments (**kwargs)   #timer_text is the variable that we link once we get the function 'count_down' fixed
canvas.grid(column=1, row=1)   #to actually put it on the screen. Pack is okay for now, til we have to add more components. (changed to grid() )

#############

# Start Button:
button = Button(text="Start", font=20, highlightthickness=0, command=start_timer_button) #command=miles_to_kilometers #ONCE the button is actually pressed, then you run the calculation from the miles and it rewrites over the km quantity converted amount and places it OVER the 0 that was written at the col=1, row=1 that was at the original spot for the km_result_label
button.grid(column=0, row=2)   #the fix was to reduce the col from 2 to 1, and row from 3 to 2.

#############

# Reset Button:
button = Button(text="Reset", font=20, highlightthickness=0, command=reset_timer)  #no () for the main_timer stop command  #ONCE the button is actually pressed, then you run the calculation from the miles and it rewrites over the km quantity converted amount and places it OVER the 0 that was written at the col=1, row=1 that was at the original spot for the km_result_label
button.grid(column=2, row=2)   #the fix was to reduce the col from 2 to 1, and row from 3 to 2.

#############

# checkmark label:
checkmark_label = Label(fg=GREEN, bg=YELLOW, font=("Arial", 24, 'bold'))  # color=GREEN   #label is a kwarg (see all key-value pairs on this line)   # was this before: text="This is old text",
checkmark_label.grid(column=1, row=3)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down_function(count):
    # count = 5    # no need to put this var here, because we will be passing 5 as the argument later into the function call.
    countdown_in_mins = math.floor(count / 60)   #rounds down to whole number
    countdown_in_secs = count % 60   #remaining seconds after we cleanly divide it by 60
    if countdown_in_secs < 10:
        countdown_in_secs = f"0{countdown_in_secs}"

    canvas.itemconfig(timer_text, text=f"{countdown_in_mins}:{countdown_in_secs}")
    if count > 0:
        global main_timer   #needs to extract this from Constants, so this must be global
        main_timer = window.after(1000, count_down_function, count - 1)   # count_down should NOT be count_down() here.   #When/if we want to cancel the timer, we have to go back to the window.after( ) line, and we have to give it a name (put it inside a variable), then window.after_cancel() in the line above where we want to cancel it at.
    else:
        start_timer_button()  #you need to place this function AFTER the if statement so the the above block will still run first # But! Dedent the function afterwards! # if it's 0, then start the timer button again
        add_an_extra_check_mark = ""
        progress_sessions = math.floor(reps/2)
        for _ in range(progress_sessions):  #warning, because reps divided by 2 or anything divided by anything, becomes a floating type number.
            # checkmark_label.config(text=checkmark_string)
            # checkmark_label.grid(column=1, row=3)
            add_an_extra_check_mark += checkmark_string
        checkmark_label.config(text=add_an_extra_check_mark)


#
# def short_break_10min_count_down(count):
#     # count = 5    # no need to put this var here, because we will be passing 5 as the argument later into the function call.
#     countdown_in_mins = math.floor(count / 60)   #rounds down to whole number
#     countdown_in_secs = count % 60   #remaining seconds after we cleanly divide it by 60
#     if countdown_in_secs < 10:
#         countdown_in_secs = f"0{countdown_in_secs}"
#
#     canvas.itemconfig(timer_text, text=f"{countdown_in_mins}:{countdown_in_secs}")
#     if count > 0:
#         window.after(1000, progress_count_down, count - 1)   # count_down should NOT be count_down() here.
#
#
# def long_break_20min_count_down(count):
#     # count = 5    # no need to put this var here, because we will be passing 5 as the argument later into the function call.
#     countdown_in_mins = math.floor(count / 60)   #rounds down to whole number
#     countdown_in_secs = count % 60   #remaining seconds after we cleanly divide it by 60
#     if countdown_in_secs < 10:
#         countdown_in_secs = f"0{countdown_in_secs}"
#
#     canvas.itemconfig(timer_text, text=f"{countdown_in_mins}:{countdown_in_secs}")
#     if count > 0:
#         window.after(1000, progress_count_down, count - 1)   # count_down should NOT be count_down() here.


window.mainloop()
