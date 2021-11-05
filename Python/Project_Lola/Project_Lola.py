import wolframalpha
import pyttsx3
import wikipedia

client = wolframalpha.Client("5RGUKH-L47W88HU97")
engine = pyttsx3.init()



# print(next(res.results).text)
import PySimpleGUI as sg                            # Part 1 - The import

# Define the window's contents
sg.theme('DarkGreen')
layout = [  [sg.Text('What Can I Do For You')],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Button('Ok')] ]

# Create the window
window = sg.Window('Hello! I am Lola', layout)      # Part 3 - Window Defintion
                                                
# Display and interact with the Window
while True:
    event, values = window.read()                       # Part 4 - Event loop or Window.read call

# Do something with the information gathered
    if event in (None, 'Cancel'):
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking("Wolfram Result: "+wolfram_res,"Wikipedia Result: "+wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say("Wolfram Result: "+wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say("Wolfram Result: "+wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say("Wikipedia Result: "+wiki_res)
        sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()


    print(values[0])

# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window